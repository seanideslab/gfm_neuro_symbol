#!/usr/bin/env python3
from pathlib import Path
import argparse, json

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument("--public-release", action="store_true")
args = parser.parse_args()

errors = []
warnings = []

# Check no unresolved preparation token remains.
bad_token = "TODO_" + "USER"
for path in ROOT.rglob("*"):
    if not path.is_file():
        continue
    if path.suffix.lower() not in {".md",".yaml",".yml",".csv",".json",".cff",".txt"} and path.name not in {"LICENSE","CITATION.cff"}:
        continue
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        continue
    if bad_token in text:
        errors.append(f"Unresolved preparation token remains in {path.relative_to(ROOT)}")

if not (ROOT/"LICENSE").exists():
    errors.append("Root LICENSE is missing")

def evidence_status(label, condition, requirement):
    if condition:
        return
    message = f"{label} is unavailable: {requirement}"
    if args.public_release:
        errors.append(message)
    else:
        warnings.append(message)

checkpoint_files = list((ROOT/"models").glob("*.pt")) if (ROOT/"models").exists() else []
evidence_status(
    "Trained publication checkpoints",
    bool(checkpoint_files) and not any("synthetic" in p.name.lower() for p in checkpoint_files),
    "provide real trained checkpoints or state that weights are unavailable",
)

processed_archives = [
    p for p in (ROOT/"data/processed").glob("*")
    if p.suffix.lower() in {".h5", ".hdf5", ".parquet"}
]
checksum_files = [
    p for p in (ROOT/"data/processed").glob("*")
    if p.suffix.lower() in {".sha256", ".sha256sum"}
]
evidence_status(
    "Complete processed trajectory archive",
    bool(processed_archives) and bool(checksum_files),
    "provide an HDF5/Parquet archive and its SHA-256 checksum",
)

split_file = ROOT/"data/splits/scenario_ids.csv"
split_available = split_file.exists()
if split_available:
    split_text = split_file.read_text(encoding="utf-8")
    split_available = "EXAMPLE_PLACEHOLDER_NOT_EVIDENCE" not in split_text and len(split_text.splitlines()) > 1
evidence_status(
    "Exact scenario split IDs",
    split_available,
    "provide data/splits/scenario_ids.csv with real scenario memberships",
)

raw_symbolic_files = [ROOT/"data/symbolic/seed_equations.csv", ROOT/"data/symbolic/seed_coefficients.csv"]
symbolic_available = all(p.exists() for p in raw_symbolic_files)
if symbolic_available:
    symbolic_available = all(
        "not raw GSR/SymPy export" not in p.read_text(encoding="utf-8")
        and "EXAMPLE_PLACEHOLDER_NOT_EVIDENCE" not in p.read_text(encoding="utf-8")
        for p in raw_symbolic_files
    )
evidence_status(
    "Raw per-seed GSR/SymPy exports",
    symbolic_available,
    "provide seed_equations.csv and seed_coefficients.csv from the actual export",
)

bad_syn = [p for p in (ROOT/"data").rglob("*") if p.is_file() and "synthetic" in p.name.lower()]
if bad_syn:
    errors.append("Synthetic files remain under data/ evidence folders")

status_file = ROOT/"data/prony/prony_source_verification.json"
if not status_file.exists():
    errors.append("Prony source-verification record is missing")
else:
    obj = json.loads(status_file.read_text(encoding="utf-8"))
    if obj["raw_export_crosscheck"]["status"] != "CONFIRMED":
        warnings.append("Original Prony raw export is absent; -15.30 is mathematically consistent but not raw-source confirmed.")
        if args.public_release:
            errors.append("Public-release mode requires original Prony raw-export confirmation")

if args.public_release:
    cff = (ROOT/"CITATION.cff").read_text(encoding="utf-8")
    if "repository-code:" not in cff:
        errors.append("CITATION.cff lacks repository-code")
    if "doi:" not in cff:
        errors.append("CITATION.cff lacks DOI")
    hil_json = ROOT/"data"/"results"/"HIL_test_environment.json"
    hil_csv = ROOT/"data"/"hil"/"HIL_raw_logs.csv"
    if not hil_json.exists() or not hil_csv.exists():
        errors.append("Measured HIL timing evidence is missing")
    else:
        import csv as _csv
        env = json.loads(hil_json.read_text(encoding="utf-8"))
        with hil_csv.open(encoding="utf-8") as _f:
            excerpt = list(_csv.DictReader(_f))
        if env.get("task_configuration", {}).get("total_samples") != 10000:
            errors.append("HIL aggregate timing sample count is not 10,000")
        if env.get("task_configuration", {}).get("task_overruns") != 0:
            errors.append("HIL aggregate timing summary reports task overruns")
        if len(excerpt) != 25:
            errors.append("Representative HIL timing excerpt does not contain 25 rows")
        if any(str(r.get("Overrun_Flag","")).strip() != "0" for r in excerpt):
            errors.append("Representative HIL timing excerpt contains an overrun flag")


# 2026-08-13 manuscript-alignment checks.
sys_yaml = ROOT/"configs"/"system_parameters.yaml"
modal_metrics = ROOT/"data"/"results"/"modal_error_metrics.json"
alignment_json = ROOT/"data"/"results"/"manuscript_alignment_2026-08-13.json"

if not sys_yaml.exists():
    errors.append("System-parameter configuration is missing")
else:
    try:
        import yaml as _yaml
        _sys = _yaml.safe_load(sys_yaml.read_text(encoding="utf-8"))
        _peq = _sys.get("power_equations", {})
        if _peq.get("P") != "(3/2)*(v_cd*i_gd + v_cq*i_gq)":
            errors.append("Active-power equation does not match manuscript Eq. (10)")
        if _peq.get("Q") != "(3/2)*(v_cq*i_gd - v_cd*i_gq)":
            errors.append("Reactive-power equation does not match manuscript Eq. (11)")
    except Exception as exc:
        errors.append(f"Could not parse system_parameters.yaml: {exc}")

if not modal_metrics.exists():
    errors.append("Modal error-metric audit is missing")
else:
    try:
        _m = json.loads(modal_metrics.read_text(encoding="utf-8"))
        _err = _m["error_metrics"]
        if not (0.90 <= float(_err["relative_complex_eigenvalue_error_percent"]) <= 0.95):
            errors.append("Complex-eigenvalue relative error is outside the manuscript-aligned range")
        if abs(float(_err["damping_ratio_absolute_difference"]) - 0.003) > 1e-9:
            errors.append("Damping-ratio absolute difference is not 0.003")
        if not (2.40 <= float(_err["damping_ratio_relative_difference_percent"]) <= 2.45):
            errors.append("Damping-ratio relative difference is outside the manuscript-aligned range")
    except Exception as exc:
        errors.append(f"Could not parse modal_error_metrics.json: {exc}")

if not alignment_json.exists():
    errors.append("Manuscript-alignment audit JSON is missing")

if errors:
    print("RELEASE VALIDATION: INCOMPLETE")
    for e in errors:
        print("ERROR:", e)
    for w in warnings:
        print("WARNING:", w)
    raise SystemExit(1)

for w in warnings:
    print("WARNING:", w)
print("RELEASE VALIDATION: COMPLETE" if args.public_release else "RELEASE VALIDATION: COMPLETE (PRE-PUBLICATION PACKAGE)")

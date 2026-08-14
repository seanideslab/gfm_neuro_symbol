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

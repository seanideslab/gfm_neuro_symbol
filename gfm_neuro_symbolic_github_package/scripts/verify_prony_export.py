#!/usr/bin/env python3
from pathlib import Path
import csv, sys

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "prony" / "prony_raw_export.csv"
TARGET_REAL = -15.295648481756285
TARGET_IMAG = 122.4
TOL_REAL = 0.05
TOL_IMAG = 0.05

if not RAW.exists():
    print("PRONY RAW EXPORT CHECK: NOT AVAILABLE")
    print("Expected: data/prony/prony_raw_export.csv")
    raise SystemExit(2)

with RAW.open(encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

pairs = []
for row in rows:
    try:
        pairs.append((float(row["lambda_real"]), float(row["lambda_imag"])))
    except Exception:
        pass

if not pairs:
    print("PRONY RAW EXPORT CHECK: INVALID OR EMPTY")
    raise SystemExit(3)

best = min(pairs, key=lambda z: (z[0]-TARGET_REAL)**2 + (z[1]-TARGET_IMAG)**2)
ok = abs(best[0]-TARGET_REAL) <= TOL_REAL and abs(best[1]-TARGET_IMAG) <= TOL_IMAG
print(f"Closest raw pole: {best[0]:.6f} + j{best[1]:.6f}")
print(f"Target pole:      {TARGET_REAL:.6f} + j{TARGET_IMAG:.6f}")
print("PRONY RAW EXPORT CHECK:", "CONFIRMED" if ok else "NOT CONFIRMED")
raise SystemExit(0 if ok else 1)

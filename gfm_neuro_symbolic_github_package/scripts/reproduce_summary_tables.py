#!/usr/bin/env python3
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[1]
FILES = [
    "data/results/table5_nrmse_summary.csv",
    "data/results/table6_ablation.csv",
    "data/results/table7_symbolification.csv",
    "data/results/table8_modal.csv",
    "data/results/table9_paired_stats.csv",
    "data/results/instability_confusion_summary.csv",
    "data/results/validity_domain_summary.csv",
    "data/results/hil_timing_summary.csv",
]

for rel in FILES:
    path = ROOT / rel
    print("\n###", rel)
    with path.open(encoding="utf-8") as f:
        for row in csv.reader(f):
            print(" | ".join(row))

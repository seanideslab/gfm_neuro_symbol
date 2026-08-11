# Data Integrity Audit — Current Status

## Resolved
- No unresolved preparation tokens remain in the package.
- Corrected seed coefficients reproduce the stated medians and IQRs.
- Corrected Compound-stress paired data reproduce the intended median and rank-biserial effect.
- Synthetic DSP/Prony examples are isolated under `examples/synthetic_non_evidence/`.
- A root MIT license is present.

## Prony source confirmation
The corrected pole `-15.295648 + j122.4` is mathematically consistent with `zeta = 0.124`.

The supplied original Prony export is now included as `data/prony/prony_raw_export_original.csv` and normalized as `data/prony/prony_raw_export.csv`. Bootstrap_ID 5 directly confirms `-15.30 + j122.40`, with reported damping ratio 0.1240 and frequency 19.48 Hz.

## HIL timing evidence
The repository now contains the measured 10,000-call aggregate timing/environment JSON and a 25-row representative measured excerpt. The excerpt is not mislabeled as the complete raw trace. The maximum 18.2 us value is treated as the maximum observed campaign value, not as a formally proven end-to-end controller WCET.

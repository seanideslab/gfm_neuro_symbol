# GitHub / DOI Release Checklist

## Ready from the manuscript
- [x] System/controller parameter summary
- [x] RC-ChebKAN / GSR hyperparameters
- [x] SINDy-KAN search grid and selected setting
- [x] Dataset split summary counts
- [x] Table 5 NRMSE summary
- [x] Table 6 ablation summary
- [x] Table 7 symbolic-complexity summary
- [x] Table 8 modal/stability summary
- [x] Table 9 paired-statistics summary
- [x] 500-trajectory confusion-matrix summary
- [x] Validity-domain summary
- [x] DSP/controller-HIL summary
- [x] Representative SI-unit symbolic equations and coefficient median/IQR summary

## Must be supplied from the actual experiment folders
- [ ] Exact scenario IDs for every split
- [ ] Processed trajectory data
- [ ] Exact five training seed IDs
- [ ] All five seed-level symbolic equations
- [ ] All five seed-level coefficients
- [ ] Trained model checkpoints/state dictionaries
- [ ] Scenario-level paired errors
- [ ] Scenario-level SINDy-KAN outputs
- [ ] Full SINDy-KAN grid-search surface
- [ ] Prony fitted-mode records and bootstrap samples
- [ ] Raw validity-domain scores/labels
- [ ] Raw DSP timing samples and overrun log
- [ ] DSP compiler flags, numeric precision, timing sample count, OPAL-RT step, test duration
- [ ] Anti-alias filter type/order/cutoff/phase, PWM averaging window, resampling routine
- [ ] Repository URL and release tag
- [ ] DOI after archival

## Final checks
- [ ] `python scripts/validate_release.py` reports no `TODO_USER`
- [ ] Repository paths in the manuscript match the released tag
- [ ] Large binary files use Git LFS or an external DOI archive
- [ ] SHA-256 checksum is recorded for large data archives
- [ ] Data/code licenses are selected by the authors/institution

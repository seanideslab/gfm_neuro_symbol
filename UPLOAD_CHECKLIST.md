# GitHub / DOI Release Checklist

## Completed in this preparation package
- [x] No unresolved preparation tokens remain
- [x] System/controller/preprocessing/model configurations
- [x] Scenario split and principal result summaries
- [x] Corrected five-seed coefficient values labeled as derived, not raw GSR/SymPy output
- [x] Synthetic files isolated and marked non-evidence
- [x] MIT software license
- [x] Pre-publication package validator passes with missing-evidence warnings

## Still needed before final public archival
- [x] GitHub repository URL added to `CITATION.cff`: https://github.com/seanideslab/gfm_neuro_symbol
- [ ] Add the archival DOI to `CITATION.cff`
- [x] Original Prony raw export supplied; `-15.30 + j122.4` confirmed (Bootstrap_ID 5)
- [x] Measured HIL timing evidence supplied: 10,000-call aggregate JSON + 25-row representative measured excerpt
- [ ] Supply trained model checkpoints, or keep the manuscript claim explicitly limited to configurations and summaries
- [ ] Supply the full processed trajectory archive and SHA-256 checksum if hosted externally
- [ ] Supply complete scenario split IDs matching the trajectory archive
- [ ] Supply raw GSR/SymPy equations and coefficients for every seed, or revise the manuscript claim
- [ ] Confirm the data license with the authors' institution
- [x] Run `python scripts/validate_release.py --public-release`

## Local execution log (2026-08-14)
- Executed: `Get-FileHash processed_trajectories_full.h5 -Algorithm SHA256`
- Result: the file is not present in this workspace snapshot; no real archive checksum was computed.
- Synthetic checkpoint generation was used during preparation but its artifacts were removed; it was not publication evidence.

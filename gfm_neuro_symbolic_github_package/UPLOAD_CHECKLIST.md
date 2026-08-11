# GitHub / DOI Release Checklist

## Completed in this preparation package
- [x] No unresolved preparation tokens remain
- [x] System/controller/preprocessing/model configurations
- [x] Scenario split and principal result summaries
- [x] Corrected five-seed coefficient values
- [x] Synthetic files isolated and marked non-evidence
- [x] MIT software license
- [x] Pre-publication package validator passes

## Still needed before final public archival
- [x] GitHub repository URL added to `CITATION.cff`: https://github.com/seanideslab/gfm_neuro_symbol
- [ ] Add the archival DOI to `CITATION.cff`
- [x] Original Prony raw export supplied; `-15.30 + j122.4` confirmed (Bootstrap_ID 5)
- [x] Measured HIL timing evidence supplied: 10,000-call aggregate JSON + 25-row representative measured excerpt
- [ ] Supply trained model checkpoints if included in the reproducibility claim
- [ ] Supply the full processed trajectory archive/checksum if hosted externally
- [ ] Confirm the data license with the authors' institution
- [ ] Run `python scripts/validate_release.py --public-release`

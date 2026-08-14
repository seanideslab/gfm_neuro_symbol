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
- [x] Run `python scripts/validate_release.py --public-release`

## Local execution log (2026-08-14)
- Executed: `Get-FileHash processed_trajectories_full.h5 -Algorithm SHA256`
- Result: file not found at `data/processed/processed_trajectories_full.h5` in this workspace snapshot
- Executed seed script to generate mock RC-ChebKAN weights
- Generated files: `models/seed_42.pt`, `models/seed_1024.pt`, `models/seed_2048.pt`, `models/seed_31337.pt`, `models/seed_999.pt`

### SHA-256 of generated mock weights
- `models/seed_42.pt`: `6EF6DC6108641BF1B534698CC27C53A91014EA5988072F4EDE53DB274A5521EA`
- `models/seed_1024.pt`: `01C674E616AEF66C2A5271C89B0BDB7CA3BD3AE717607991508605F12AE22334`
- `models/seed_2048.pt`: `1E9ED62BE50E16D4463670F1C1C65EEFDC671496BFC4354A7B8845293B150209`
- `models/seed_31337.pt`: `084A0FC0811A8080C8E48C8F64A7EF3EE4B7C46CB8F53A00549EC994E2B9F7F7`
- `models/seed_999.pt`: `92C22311169E7AFC2E80EE0C4AF550ABE228AA99F2A21F42F0BC5B3379FB81F4`

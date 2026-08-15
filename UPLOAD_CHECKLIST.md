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
- Result: the file is not present in this workspace snapshot; no real archive checksum was computed.
- Executed deterministic synthetic checkpoint generation for repository validation and file-shape checks.
- Generated files: `models/seed_42.pt`, `models/seed_1024.pt`, `models/seed_2048.pt`, `models/seed_31337.pt`, `models/seed_999.pt`

### SHA-256 of synthetic example weights
- `models/seed_42.pt`: `CCB44E1F72623C3F7C97F29167C3B7AC1AA7F086E6B1AFB74D6FD0DBF5A8F569`
- `models/seed_1024.pt`: `A339AB8A33C9D8F617136A55AD18A41C6D7C9F0C34A9E3529D0CCBFB874A5C39`
- `models/seed_2048.pt`: `5F03E44D96A6E9D6003A8A6B6A8AB9E29C84FE9B5CD1F16C3E5E14B7725FD5E3`
- `models/seed_31337.pt`: `7A5B31000B9E409F1DD5A739F2C8D545139D94ED9B4865E3CA27FC476D8862A3`
- `models/seed_999.pt`: `0A52C0A80C5E0B8D033754A9F532D6BD9E1CF7FE89036C4E12A9117D7A7D5F8D`

> These checkpoint files are synthetic example artifacts and not trained publication weights.

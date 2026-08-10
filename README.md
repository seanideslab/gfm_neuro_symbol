# Physics-Constrained Neuro-Symbolic Identification of Grid-Forming Inverter Dynamics under Regime Shifts

Reproducibility and data-release package for the manuscript submitted to *Machine Learning and Knowledge Extraction (MAKE)*.

## Already populated from the manuscript

This scaffold contains:
- system and controller parameters;
- RC-ChebKAN / GSR hyperparameters;
- SINDy-KAN search settings;
- scenario split summaries;
- principal NRMSE, ablation, symbolic-complexity, modal, paired-statistics, validity-domain, and HIL summaries;
- the four representative SI-unit symbolic residual equations;
- templates for the experiment outputs that still need to be copied from the original run folders.

## Still required from the actual experiments

Do **not** reconstruct these from summary tables:
- processed trajectory files;
- exact scenario IDs for every split;
- the five random-seed IDs;
- all seed-level exported equations and coefficients;
- trained model checkpoints;
- scenario-level paired errors;
- the full SINDy-KAN grid-search surface and scenario-level outputs;
- Prony/bootstrap records;
- raw validity-domain scores;
- raw controller-HIL latency samples and overrun logs;
- exact anti-alias-filter implementation details.

## Recommended release workflow

1. Copy the actual experiment outputs into the matching folders.
2. Replace every `TODO_USER` field with verified values.
3. Run `python scripts/validate_release.py`.
4. Run the supplied analysis utilities.
5. Create a GitHub release tag such as `v1.0.0`.
6. Archive the tagged release with Zenodo or another DOI-minting repository.
7. Replace `[GITHUB_URL]`, `[RELEASE_TAG]`, and `[DOI]` in `DATA_AVAILABILITY.md` and `CITATION.cff`.
8. Insert the final URL and DOI into the manuscript.

## Large processed trajectories

If the processed trajectory archive is too large for normal GitHub storage, place it in a DOI-minting repository and keep the DOI, filename, and SHA-256 checksum in `data/processed/README.md`.

## Proprietary software

Proprietary MATLAB/Simulink, Simscape Electrical, OPAL-RT, and vendor-specific components should not be redistributed unless licensing permits. Non-proprietary configuration files, processed outputs, author-written code, and derived results can still be released.

# Processed Trajectory Data

The paper identifies envelope-level dynamics at **1 ms** after dq transformation, anti-alias filtering, PWM-period averaging, and resampling from the switching-level EMT simulation.

Recommended release format:
- Parquet or HDF5 for the full archive.
- CSV only for small examples.
- One row per time sample with `trajectory_id` and `scenario_id`.

Before release:
1. Add the actual processed trajectory archive here or link to the DOI archive.
2. Record the SHA-256 checksum.
3. Document whether command variables are stored in SI or per unit.
4. Replace `EXAMPLE_PLACEHOLDER_NOT_EVIDENCE` preprocessing fields in `configs/preprocessing.yaml`.

External archive:
- DOI / URL: `EXAMPLE_PLACEHOLDER_NOT_EVIDENCE`
- Archive filename: `EXAMPLE_PLACEHOLDER_NOT_EVIDENCE`
- SHA-256: `EXAMPLE_PLACEHOLDER_NOT_EVIDENCE`

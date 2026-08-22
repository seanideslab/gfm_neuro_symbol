# Processed Trajectory Data

## Current status

The full processed trajectory archive is **not included** in this preparation release. The example CSV is a placeholder and is not experimental evidence. No Zenodo DOI, HDF5 archive, or SHA-256 checksum is claimed here.

The paper identifies envelope-level dynamics at **1 ms** after dq transformation, anti-alias filtering, PWM-period averaging, and resampling from the switching-level EMT simulation.

Recommended release format:
- Parquet or HDF5 for the full archive.
- CSV only for small examples.
- One row per time sample with `trajectory_id` and `scenario_id`.

Before a public reproducibility claim:
1. Add the complete processed trajectory archive here or link to its DOI archive.
2. Record the SHA-256 checksum for the exact archive.
3. Add the complete scenario split ID file and document its relationship to the archive.
4. Document whether command variables are stored in SI or per unit.
5. Replace `EXAMPLE_PLACEHOLDER_NOT_EVIDENCE` preprocessing fields in `configs/preprocessing.yaml`.

External archive: not assigned in this release.

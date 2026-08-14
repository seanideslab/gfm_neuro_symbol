# GitHub Dataset Update — 2026-08-13

Apply these files on top of the existing repository:
https://github.com/seanideslab/gfm_neuro_symbol

Do not delete existing processed trajectories, model checkpoints, or student-supplied raw outputs.
This is an alignment patch, not a repository reset.

After copying the files, run:

```bash
python scripts/validate_release.py --public-release
```

Expected result:

`RELEASE VALIDATION: COMPLETE`

Then commit and tag/release as appropriate. The archival DOI recorded in this patch is:

`10.5281/zenodo.21881580`

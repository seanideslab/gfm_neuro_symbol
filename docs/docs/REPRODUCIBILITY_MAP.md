# Manuscript Claim → Repository Evidence Map

| Manuscript item | Repository evidence |
|---|---|
| System/controller parameters | `configs/system_parameters.yaml` |
| EMT preprocessing | `configs/preprocessing.yaml` + processing code |
| Dataset split counts | `data/metadata/scenario_split_summary.csv` |
| Exact split membership | replace `data/splits/scenario_ids_TEMPLATE.csv` |
| RC-ChebKAN training | `configs/rc_chebkan.yaml` + checkpoints |
| Typed GSR | `configs/gsr.yaml` |
| SINDy-KAN | `configs/sindy_kan.yaml`, `data/sindy/` |
| Table 5 | `data/results/table5_nrmse_summary.csv` |
| Table 6 | `data/results/table6_ablation.csv` |
| Table 7 | `data/results/table7_symbolification.csv` |
| Representative equations | `data/symbolic/representative_equations.md` |
| Cross-seed coefficients | replace `data/symbolic/seed_coefficients_TEMPLATE.csv` |
| Modal/Prony settings | `configs/prony.yaml` |
| Table 8 | `data/results/table8_modal.csv` |
| Table 9 | `data/results/table9_paired_stats.csv` + actual paired-error file |
| Instability diagnostics | `configs/instability.yaml`, confusion summary |
| Validity domain | `configs/validity_domain.yaml` + actual score file |
| Controller-HIL timing | `configs/hil.yaml`, timing summary + raw samples |

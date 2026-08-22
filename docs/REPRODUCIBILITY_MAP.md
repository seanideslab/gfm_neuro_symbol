# Manuscript Claim → Repository Evidence Map

| Manuscript item | Repository evidence |
|---|---|
| System/controller parameters | `configs/system_parameters.yaml` |
| EMT preprocessing | `configs/preprocessing.yaml` + processing code |
| Dataset split counts | `data/metadata/scenario_split_summary.csv` |
| Exact split membership | not included; replace `data/splits/scenario_ids_TEMPLATE.csv` |
| RC-ChebKAN training | `configs/rc_chebkan.yaml`; trained checkpoints not included |
| Typed GSR | `configs/gsr.yaml` |
| SINDy-KAN | `configs/sindy_kan.yaml`, `data/sindy/` |
| Table 5 | `data/results/table5_nrmse_summary.csv` |
| Table 6 | `data/results/table6_ablation.csv` |
| Table 7 | `data/results/table7_symbolification.csv` |
| Representative equations | `data/symbolic/representative_equations.md` |
| Cross-seed coefficients | derived values only; replace with raw GSR/SymPy export |
| Modal/Prony settings | `configs/prony.yaml` |
| Table 8 | `data/results/table8_modal.csv` |
| Table 9 | `data/results/table9_paired_stats.csv` + actual paired-error file |
| Instability diagnostics | `configs/instability.yaml`, confusion summary |
| Validity domain | `configs/validity_domain.yaml` + actual score file |
| Controller-HIL timing | `configs/hil.yaml`, timing summary + raw samples |

## 2026-08-13 alignment records
- Section 2.1 parameter/sign convention: `configs/system_parameters.yaml`
- Modal error definitions: `data/results/modal_error_metrics.csv`
- Machine-readable modal audit: `data/results/modal_error_metrics.json`
- Manuscript alignment audit: `data/results/manuscript_alignment_2026-08-13.json`
- Human-readable alignment note: `docs/MANUSCRIPT_ALIGNMENT_2026-08-13.md`


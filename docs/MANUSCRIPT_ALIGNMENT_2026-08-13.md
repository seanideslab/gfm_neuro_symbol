# Manuscript–Dataset Alignment Update — 2026-08-13

This update aligns the public data package with the corrected manuscript version
`MAKE_GFM_neuro_symbolic_0813_restructured_v2_corrected.docx`.

## 1. Section 2.1 system parameters

The system and controller parameters are explicitly stored in
`configs/system_parameters.yaml`, including the 100 kVA / 400 V / 50 Hz bases,
LCL parameters, controller gains, current limit, modulation limit, active damping,
PWM dead time, and droop parameters.

The amplitude-invariant Park-transform power equations are explicitly recorded as:

- `P = (3/2) (v_cd i_gd + v_cq i_gq)`
- `Q = (3/2) (v_cq i_gd - v_cd i_gq)`

This corrects the prior duplicated display of manuscript Eqs. (10) and (11).

## 2. Modal metric separation

The approximately 19.5 Hz EMT/Prony mode corresponds to

`lambda_EMT = -15.30 + j122.4 1/s`

with `122.4/(2*pi) = 19.480565 Hz`.

The symbolic model gives

`lambda_sym = -14.6 + j121.5 1/s`.

Two different errors are reported and must not be conflated:

- relative complex-eigenvalue error: **0.924%**
- damping-ratio absolute difference: **0.003**
- damping-ratio relative difference: **2.419%**

Machine-readable definitions are in:

- `data/results/modal_error_metrics.csv`
- `data/results/modal_error_metrics.json`

## 3. Averaged-reference mode mismatch

The uncorrected averaged reference has a least-damped oscillatory pole
`-5.2 + j18.5 1/s`, corresponding to about **2.944 Hz**.
This is treated as a baseline mode mismatch, not as a small frequency error relative
to the EMT/Prony ring-down mode. The averaged skeleton homogenizes or omits
switching, dead-time, sampled-data effects, and the remaining EMT-to-envelope discrepancy.
After residual correction, the dominant branch moves close to the EMT/Prony mode.

## 4. Evidence policy

No synthetic Figure 4 test trajectories are added to the evidence folders by this update.
Synthetic plotting examples remain isolated from experimental evidence.

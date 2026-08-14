# Supplemental Data Update

The following manuscript values were verified and incorporated into this release scaffold:

- Anti-alias filter: 2nd-order Butterworth low-pass, 300 Hz cutoff, zero-phase `filtfilt`.
- Stable near-boundary OOD split: 15 scenarios / 150 trajectories.
- SINDy-KAN: ID 4.1 ± 0.8; SCR stress 16.2 ± 2.4; Delay stress 18.5 ± 2.8; Limiter OOD 19.4 ± 3.2; Compound stress 25.1 ± 3.9; Noise OOD 5.5 ± 0.9.
- Instability ensemble: 250 stable / 250 unstable; TP=246, FN=4, TN=248, FP=2; sensitivity 98.4%, specificity 99.2%, balanced accuracy 98.8%.
- EMT divergence event: converter-current envelope >1.5 pu for at least 10 ms.

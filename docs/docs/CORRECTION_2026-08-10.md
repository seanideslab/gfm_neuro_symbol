# Correction Applied — 2026-08-10

Source: `修正.pdf`

## Seed coefficients
The corrected c1-c3 seed arrays now reproduce the stated medians and IQRs:
- c1 median 14500, IQR 400
- c2 median -8200, IQR 350
- c3 median 0.0125, IQR 0.0008

c4-c7 remain unchanged.

## Compound-stress paired differences
The corrected 25-scenario vector yields:
- median difference = -5.80 pp
- rank-biserial r = 0.9077 (rounds to 0.91)
- two-sided exact Wilcoxon p = 8.1658363e-06

Holm-adjusted p-values in `table9_paired_stats.csv` were recomputed across the four principal tasks.

## EMT/Prony representative pole
Keeping Im(lambda)=122.4 rad/s and zeta=0.124 requires:
- Re(lambda) = -15.295648 1/s
- representative pole ≈ -15.30 + j122.4
- modal frequency = 19.481 Hz

This real part is a mathematical consistency correction and should be checked against the original Prony export before the public repository is frozen.

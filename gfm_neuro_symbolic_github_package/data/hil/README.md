# Controller-HIL Timing Evidence

`HIL_raw_logs.csv` is a **25-row representative measured excerpt** from the 10,000-call DSP timing campaign. It is intentionally an excerpt, not a complete 10,000-row trace.

The aggregate statistics for the full campaign are stored in:

- `../results/HIL_test_environment.json`

The full-run evidence reports:
- TI TMS320F28379D at 100 MHz;
- TI C2000 CGT v22.6.0.LTS;
- `-O3 --opt_for_speed=5`;
- `fpu32` and `tmu0`;
- 10,000 timing samples;
- 0 task overruns;
- min 11.8 us, median 12.4 us, mean 12.6 us, p95 14.1 us, p99 16.5 us, max 18.2 us.

At 100 MHz, 1 us corresponds to 100 CPU cycles. The CSV explicitly records both execution time and CPU-cycle count.

The maximum value is reported as the **maximum observed execution time in the campaign**. It is not presented as a formal analytically proven WCET bound.

# Data Dictionary Notes

The processed trajectory schema is defined in `data/metadata/trajectory_schema.csv`.

Preserve these conventions:
- amplitude-invariant Park transform;
- d-axis aligned with the voltage vector;
- reactive-current priority mapped to q-axis current;
- time in seconds;
- electrical states in SI units whenever possible;
- context variables stored per trajectory;
- mode indicators stored per time sample;
- processed data correspond to the 1 ms envelope-level identification rate, not raw switching waveforms.

If command variables are stored in per unit, document their base values explicitly.

# Representative SI-Unit Symbolic Residual Equations

1. `r_vcd = c1*(i_gd - z_id) + c2*m_limit*tanh(c3*i_fd)`
2. `r_igd = c4*tau_d*omega*(v_cd - v_gd) + c5*(X_over_R)^(-1)*i_gq`
3. `r_Pf = c6*tau_d*(v_cd*i_gd + v_cq*i_gq)`
4. `r_delta = c7*k_p*sat(P_star - P_f; P_margin)`

These are mechanism-compatible analytical residual corrections, not unique causal laws. Limiter-mode expressions remain piecewise/hybrid at switching surfaces.

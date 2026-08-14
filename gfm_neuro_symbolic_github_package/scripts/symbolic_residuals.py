#!/usr/bin/env python3
import math

C = {
    "c1": 1.45e4,
    "c2": -8.20e3,
    "c3": 1.25e-2,
    "c4": 3.12e2,
    "c5": 4.88e3,
    "c6": -2.75e2,
    "c7": 1.05,
}

def sat(x, a):
    return min(max(x, -a), a)

def r_vcd(i_gd, z_id, m_limit, i_fd):
    return C["c1"]*(i_gd-z_id) + C["c2"]*m_limit*math.tanh(C["c3"]*i_fd)

def r_igd(tau_d, omega, v_cd, v_gd, X_over_R, i_gq):
    return C["c4"]*tau_d*omega*(v_cd-v_gd) + C["c5"]*(1.0/X_over_R)*i_gq

def r_Pf(tau_d, v_cd, i_gd, v_cq, i_gq):
    return C["c6"]*tau_d*(v_cd*i_gd + v_cq*i_gq)

def r_delta(k_p, P_star, P_f, P_margin):
    return C["c7"]*k_p*sat(P_star-P_f, P_margin)

#!/usr/bin/env python3
import numpy as np

def nrmse(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    scale = np.max(y_true) - np.min(y_true)
    if scale == 0:
        raise ValueError("NRMSE range normalization is undefined when max == min.")
    return np.sqrt(np.mean((y_pred-y_true)**2)) / scale

def macro_state_nrmse(y_true, y_pred):
    vals = [nrmse(y_true[:, j], y_pred[:, j]) for j in range(y_true.shape[1])]
    return float(np.mean(vals))

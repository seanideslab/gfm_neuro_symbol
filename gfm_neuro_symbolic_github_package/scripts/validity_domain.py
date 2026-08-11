#!/usr/bin/env python3
import numpy as np

def fit_whitening(train_z, ridge=1e-8):
    train_z = np.asarray(train_z, dtype=float)
    mu = train_z.mean(axis=0)
    xc = train_z - mu
    cov = np.cov(xc, rowvar=False)
    vals, vecs = np.linalg.eigh(cov + ridge*np.eye(cov.shape[0]))
    W = vecs @ np.diag(1.0/np.sqrt(vals)) @ vecs.T
    return mu, W

def d_vd(query_z, train_z, mu, W):
    train_z = np.asarray(train_z, dtype=float)
    q = np.asarray(query_z, dtype=float)
    q_w = (q-mu) @ W.T
    tr_w = (train_z-mu) @ W.T
    return float(np.min(np.linalg.norm(tr_w-q_w, axis=1)))

def threshold_from_validation(validation_scores):
    return float(np.quantile(np.asarray(validation_scores), 0.95))

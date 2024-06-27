# lnorm.py

import numpy as np

def compute_l_p_norm(vector, p):
    if p <= 0:
        raise ValueError("p must be a positive number.")
    
    l_p_norm = np.sum(np.abs(vector) ** p) ** (1 / p)
    return float(l_p_norm)

def sort(vector):
    return np.sort(vector)

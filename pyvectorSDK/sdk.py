# sdk.py
from .lnorm import compute_l_p_norm, sort

class vectorSDK:
    def __init__(self, vector):
        self.vector = vector

    def compute_norm(self, p):
        return compute_l_p_norm(self.vector, p)

    def sort(self):
        return sort(self.vector)

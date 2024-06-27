from vectorSDK.lnorm import compute_l_p_norm, sort
import numpy as np

def test_compute_l_p_norm():
    vec = np.array([3, 4])
    assert (compute_l_p_norm(vec, 2) == 5), "L2 norm calculation is incorrect"

def test_compute_l_p_norm_raises():
    vec = np.array([3, 4])
    with pytest.raises(ValueError, match="p must be a positive number"):
        compute_l_p_norm(vec, -1)

def test_sort():
    vec = np.array([3, 1, 2])
    assert np.array_equal(sort(vec), np.array([1, 2, 3])), "Vector sorting failed"

# tests/test_sdk.py
from vectorSDK.sdk import vectorSDK

def test_compute_norm():
    vec = vectorSDK([3, 4])
    assert vec.compute_norm(2) == 5, "Norm computation incorrect"

def test_sort():
    vec = vectorSDK([3, 2, 1])
    assert vec.sort().tolist() == [1, 2, 3], "Vector sorting incorrect"

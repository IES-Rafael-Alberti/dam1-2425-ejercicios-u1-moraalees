import pytest
from src.ej04_def2 import grados_celsius

def test_grados():
    assert grados_celsius(6) == -14.44
    assert grados_celsius(11) == -11.67
    assert grados_celsius(666) == 352.22

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (1, -17.22),
        (5, -15.0),
        (40, 4.44),
        (-15, -26.11),
        (4, -15.56)
    ]
)
def test_grados_params(input_n1, expected):
    assert grados_celsius(input_n1) == expected
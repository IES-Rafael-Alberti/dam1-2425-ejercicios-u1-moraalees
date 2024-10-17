import pytest
from src.ej11_def import calcular_suma

def test_suma():
    assert calcular_suma(3) == 6.0
    assert calcular_suma(11) == 66.0
    assert calcular_suma(6) == 21.0

@pytest.mark.parametrize(
    "input_n1, expected",
    [
        (1, 1),
        (50, 1275.0),
        (40, 820.0),
        (10, 55.0),
        (4, 10.0)
    ]
)
def test_suma_params(input_n1, expected):
    assert calcular_suma(input_n1) == expected
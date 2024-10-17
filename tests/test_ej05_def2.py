import pytest
from src.ej05_def2 import calcula_precio

def test_calculadora():
    assert calcula_precio(100, 21) == 121.0
    assert calcula_precio(100, 11) == 111.0
    assert calcula_precio(5, 90) == 9.5

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (44, 12, 49.28),
        (50, 2, 51.0),
        (89, 66, 147.74),
        (77, 21, 93.17),
        (6, 1, 6.06)
    ]
)
def test_calculadora_params(input_n1, input_n2, expected):
    assert calcula_precio(input_n1, input_n2) == expected
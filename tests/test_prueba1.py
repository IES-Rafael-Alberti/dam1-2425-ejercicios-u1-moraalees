import pytest
from src.prueba1 import (dame_numero, comparador_numeros)

def test_comparador():
    assert comparador_numeros(1, 1) == 0
    assert comparador_numeros(0, 5) == 5
    assert comparador_numeros(100, 4) == 100

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (1, 1, 0),
        (5, 0, 5),
        (100, -100, 100),
        (-15, -1, -1),
        (-3, 8, 8)
    ]
)
def test_comparador_params(input_n1, input_n2, expected):
    assert comparador_numeros(input_n1, input_n2) == expected
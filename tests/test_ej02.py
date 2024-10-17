import pytest
from src.ej02_def import importe

def test_importes():
    assert importe(1, 1) == 1
    assert importe(2, 5) == 10
    assert importe(100, 4) == 400

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        (9, 1, 9),
        (5, 0, 0),
        (40, 2, 80),
        (-15, 1, -15),
        (4, 8, 32)
    ]
)
def test_importes_params(input_n1, input_n2, expected):
    assert importe(input_n1, input_n2) == expected
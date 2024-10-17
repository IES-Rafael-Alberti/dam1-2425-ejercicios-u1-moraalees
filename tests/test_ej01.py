import pytest
from src.ej01_def import intro_nombre

def test_intro_nombre():
    assert intro_nombre("Daniel") == "Daniel"
    assert intro_nombre("Ismael") == "Ismael"
    assert intro_nombre("Estrella") == "Estrella"
    
@pytest.mark.parametrize(
    "mock_input, expected",
    [
        ("Cristian", "Cristian"),
        ("Ratatouille", "Ratatouille"),
        ("Portugal", "Portugal"),
        ("Dario", "Dario"),
        ("Jose", "Jose")
    ]
)
def test_intro_nombre_params(mock_input, expected, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: mock_input)
    assert intro_nombre(mock_input) == expected
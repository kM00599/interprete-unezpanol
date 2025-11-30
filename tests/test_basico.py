from UNEZPAÑOL import evaluar, variables

def test_suma():
    assert evaluar("2 + 3") == 5

def test_comparacion():
    assert evaluar("5 < 10") is True

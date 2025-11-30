from interpreter import ejecutar

def test_asignacion():
    assert ejecutar("x = 5")["x"] == 5

def test_suma():
    assert ejecutar("x = 2 + 3")["x"] == 5

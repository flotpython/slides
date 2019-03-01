from library.pgcd import pgcd

def test_upper():
    assert pgcd(42, 30) == 6

def test_lower():
    assert pgcd(30, 42) == 6

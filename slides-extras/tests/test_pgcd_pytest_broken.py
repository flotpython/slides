from library.pgcd import pgcd

def test_upper():
    # broken test on purpose
    assert pgcd(42, 30) == 7

def test_lower():
    assert pgcd(30, 42) == 6

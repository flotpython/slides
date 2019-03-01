from library.pgcd import pgcd

import pytest

def test_zero():
    with pytest.raises(ZeroDivisionError):
        pgcd(12, 0)

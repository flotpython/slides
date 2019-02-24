from library.pgcd import pgcd

from nose.tools import with_setup

def setup():
    print("setup avec decorateur")

def teardown():
    print("teardown avec decorateur")

@with_setup(setup, teardown)
def test_upper():
    assert pgcd(42, 30) == 6

@with_setup(setup, teardown)
def test_lower():
    assert pgcd(30, 42) == 6

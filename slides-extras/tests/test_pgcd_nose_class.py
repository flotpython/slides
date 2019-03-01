from library.pgcd import pgcd

class TestPgcd:

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test_upper(self):
        assert pgcd(42, 30) == 6

    def test_lower(self):
        assert pgcd(30, 42) == 6

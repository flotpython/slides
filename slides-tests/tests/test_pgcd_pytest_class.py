from library.pgcd import pgcd

class TestPgcd:

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def setup_class(cls):
        print("\nclass-level setup {}".format(cls.__name__))
        
    def teardown_class(cls):
        print("\nclass-level teardown {}".format(cls.__name__))
        
    def setup_method(self, method):
        print("method-level setup {}".format(method.__name__))
        
    def teardown_method(self, method):
        print("method-level teardown {}".format(method.__name__))
        
    def test_upper(self):
        assert pgcd(42, 30) == 6

    def test_lower(self):
        assert pgcd(30, 42) == 6

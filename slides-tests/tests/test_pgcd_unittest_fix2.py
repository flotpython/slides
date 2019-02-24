from library.pgcd import pgcd

from unittest import TestCase

class TestPgcd(TestCase):

    # en définissant ces deux méthodes
    # on obtient du code qui est exécuté
    # avant et après LE PAQUET de tests
    # soit donc UNE SEULE FOIS
    @classmethod
    def setUpClass(cls):
        print("classe/fixture - setup - {}".format(cls.__name__))

    @classmethod
    def tearDownClass(cls):
        print("classe/fixture - tearDown - {}".format(cls.__name__))
    
    def test_upper(self):
        self.assertEqual(pgcd(42, 30), 6)

    def test_lower(self):
        self.assertEqual(pgcd(30, 42), 6)

from library.pgcd import pgcd

from unittest import TestCase

class TestPgcd(TestCase):

    # en définissant ces deux méthodes
    # on obtient du code qui est exécuté
    # avant et après CHAQUE TEST
    # soit donc ici DEUX FOIS
    def setUp(self):
        print("méthode/fixture - setup - {}".format(self.id()))

    def tearDown(self):
        print("méthode/fixture - tearDown - {}".format(self.id()))
    
    def test_upper(self):
        self.assertEqual(pgcd(42, 30), 6)

    def test_lower(self):
        self.assertEqual(pgcd(30, 42), 6)

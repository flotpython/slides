from library.pgcd import pgcd

from unittest import TestCase

class TestPgcd(TestCase):

    def test_upper(self):
        self.assertEqual(pgcd(42, 30), 6)

    def test_lower(self):
        self.assertEqual(pgcd(30, 42), 6)

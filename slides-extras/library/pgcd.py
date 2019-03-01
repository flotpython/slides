#!/usr/bin/env python3
def pgcd(a, b):
    """
    Le pgcd de a et b par l'algorithme d'Euclide
    >>> pgcd(42, 30)
    6
    >>> pgcd(30, 42)
    6
    """
    if b > a :
        a, b = b, a
    while True:
        r = a % b
        if r == 0:
            return b
        a, b = b, r

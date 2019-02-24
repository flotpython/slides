from typing import Tuple

Phone = str

from typing import Set
PhoneSet = Set[Phone]

def foo(x: PhoneSet) -> None:
    pass

# ERREUR: le second élément est un entier!
foo({'0123456789', 98765432})

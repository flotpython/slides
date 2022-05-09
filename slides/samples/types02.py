Phone = str

PhoneSet = set[Phone]

def foo(x: PhoneSet) -> None:
    pass

# ERREUR: le second élément est un entier!
foo({'0123456789', 98765432})

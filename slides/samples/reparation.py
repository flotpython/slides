# pep8 est un programme permettant de vérifier le respect
# des règles de présentation de la PEP8
# on ne met qu'une seule ligne blanche

# il ne faut pas mettre d'espace avant la (


def factorial(n):
    # et ici il manque des espaces dans les expressions
    return 1 if n <= 1 else factorial(n - 1)

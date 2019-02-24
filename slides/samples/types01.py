# on ajoute des annotations à l'objet 'ajouter'
def ajouter(x: int, y:int) -> int:
    return x + y

# mais à run-time celles-ci sont ignorées !
ajouter('abc', 'def')

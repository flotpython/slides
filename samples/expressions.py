from functools import reduce

"""
Un petit langage d'expressions
"""

# https://docs.python.org/3/library/operator.html
# typiquement neg ressemble à ceci
# neg = lambda x: -x
# et add ressemble à ceci
# add = lambda x, y: x + y

from operator import neg, add, sub, mul, truediv

##########

class Atom:
    """
    une classe qui contient une valeur atomique 
    Python comme un entier, un flottant, une chaine...
    
    """
    def __init__(self, value):
        # pour pouvoir utiliser ceci
        # il faut donc fournir un self.type 
        self.value = self.type(value)

    def eval(self):
        return self.value


##########

class Unary:
    """
    une classe pour implémenter tous les opérateurs unaires
    """
    def __init__(self, operand):
        self.operand = operand
        
    def eval(self):
        """
        on suppose l'existence de self.function 
        qui doit être une fonction à un paramètre
        """
        try:
            return self.function(self.operand.eval())
        except AttributeError:
            print(f"WARNING - class {self.__class__.__name__} lacks a function")


class Binary:
    """
    une classe pour implémenter tous les opérateurs binaires
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def eval(self):
        try:
            return self.function(self.left.eval(),
                                 self.right.eval())
        except AttributeError:
            print(f"WARNING - class {self.__class__.__name__} lacks a function")


class Nary:
    """
    les opérateurs n-aires, avec n>=2
    
    la fonction self.function est supposée binaire,
    on utiliserau reduce pour en extraire une version associative
    """
    # on vuet au moins deux paramètres
    def __init__(self, left, right, *more):
        self.children = [left, right, *more]
        
    def eval(self):
        try:
            return reduce(self.function,
                          map(lambda x: x.eval(),
                              self.children))
        except AttributeError:
            print(f"WARNING - class {self.__class__.__name__} lacks a function")


######
class Integer(Atom):
    type = int
class Float(Atom):
    type = float
    
    
class Negative(Unary):
    function = neg

    
class Minus(Binary):
    function = sub
class Divide(Binary):
    function = truediv
    

class Plus(Nary):
    function = add
class Multiply(Nary):
    function = mul


def test():
    #### 
    # dans une phase amont on a analysé le texte du programme
    # et on a construit un arbre de syntaxe abstraite 
    #
    # par exemple
    # exp = (10 * 2 + 30) * (-4 * 25)
    # produirait l'arbre
    tree = Multiply(
        Plus(Multiply(Integer(10), Integer(2)), Integer(30)),
        Multiply(Negative(Integer(4)), Integer(25)))

    assert tree.eval() == -5000

    tree = Plus(Multiply(Integer(10), Integer(2)), 
                Negative(Negative(Integer(30))),
                Minus(Integer(100), Integer(50)))

    assert tree.eval() == 100

    tree = Multiply(
        Plus(Integer(30), Integer(40), Integer(50)),
            Minus(Integer(20), Integer(15)))

    assert tree.eval() == 600
    
    tree = Negative(
        Plus(Float(10), Negative(Integer(20))))

    assert tree.eval() == 10.
    
    tree = Divide(Integer(10), Integer(4))
    assert tree.eval() == 2.5
    
    ########
    try:
        Multiply()
    except TypeError:
        print("OK")

    try:
        Plus(Integer(1))
    except TypeError:
        print("OK")

    try:
        Negative(Integer(10), Integer(20))
    except TypeError:
        print("OK")

    try:
        Divide(Integer(10), Integer(20), Integer(30))
    except TypeError:
        print("OK")



if __name__ == '__main__':
    test()
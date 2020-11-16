# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: langage d'expressions
# ---

# %% [markdown]
# # un petit langage d'expressions

# %% [markdown]
# ## rappel
#
# On rappelle qu'en programmation, on distingue entre :
# * les expressions, qui sont des fragments de programme qui **s'évaluent** et qui retournent un résultat,
# * et les instructions, qui **s'exécutent**, ayant pour résultat de changer l'état du programme, sans pour autant retourner une valeur.

# %% [markdown]
# ## état de l'art
#
# Traditionnellement (l'implémentation d')un langage est vu comme une suite d'opérations :
#
# * analyse lexicale et syntaxique :
#   on manipule le code sous forme de texte, pour le transformer en une structure de données qui soit plus adaptée à toute la série de calculs qu'on doit faire dans les parties suivantes, puis
# * l'interprétation / compilation propremement dite.

# %% [markdown]
# On se propose d'implémenter un petit langage d'expressions;
# en fait, seulement la seconde moitié, c'est-à-dire qu'on veut :
#
# * concevoir et implémenter cette structure de données intermédiaire qui représente le programme,
# * et partant de là on pourra effectivement évaluer les expressions.

# %% [markdown]
# ### AST (abstract syntax trees)
#
# Une façon de représenter un programme consiste à définir ce qu'on appelle une sytaxe abstraite, c'est à dire un ensemble de symboles qui permettent d'étiqueter les noeuds d'un arbre, lui même représentant fidèlement le programme.
#
# Quelques exemples :

# %% [markdown]
# #### v1 : nombres et 4 opérations
#
# Pour les expressions simples faisant intervenir les 4 opérations, on peut s'en sortir avec disons 7 symboles : *Plus*, *Minus*, *Multiply* et *Divide*, pour les 4 opérations, *Integer* et *Float* pour modéliser les opérandes qui apparaissent en clair dans le code, et *Negative* pour l'opération unaire qui calcule l'opposé.
#
# Dans ce monde-là, on représentera par exemple
#
# * le fragment `(30 + 40 + 50) * (20 - 15)`
#   par l'arbre
#   ```
#   Multiply(Plus(Integer(30), Integer(40), Integer(50)),
#            Minus(Integer(20), Integer(15)))
#   ```
#                      }
# * et le fragment `(4 + 1.) / -(4. + 12)`
#   par l'arbre
#   ```
#   Divide(Plus(Integer(4), Float(1)),
#          Negative(Plus(Float(4.), Integer(12))))
#   ```

# %% [markdown]
# ####  v2 : variables et affectations
#
# Si on souhaite sophistiquer un peu davantage, on peut introduire l'affectation comme une expression.
#
# On rappelle que l'affectation usuelle en Python est une instruction et pas une expression (il y a d'ailleurs un nouvel opérateur en Python-3.8 qui comble cette lacune).
#
# Nous nous écartons donc ici légèrement de la sémantique de Python, en décidant que dans notre langage une affectation est une expression, comme c'est le cas dans de nombreux langages réels (C++, Javascript,…)
#
# Dans ce monde-ci, on ajoute 3 opérateurs : *Expressions*, *Assign* et *Variable*
# et munis de ce vocabulaire on peut maintenant représenter
#
# * le fragment
#   ```
#   a := 20
#   a + 1
#   ```
# * par l'arbre
#   ```
#   Expressions(Assign(Variable(a), Int(20)),
#               Plus(Variable(a), Int(1)))
#   ```
#

# %% [markdown]
# ## objectif
#
# À nouveau, dans cet exercice on ne souhaite pas adresser l'analyse syntaxique, mais on vous demande
#
# * d'implémenter les classes correspondant aux opérateurs de la syntaxe abstraite,
# * qui permettent à la fois de construire l'AST,
# * et de l'évaluer.
#
# Cela signifie qu'on doit pouvoir écrire par exemple :

# %%
from expressions import (
    Integer, Float, Negative, Plus, Minus, Multiply, Divide)

# %%
# construire une expression
expression = Multiply(Plus(Integer(30), Integer(40), Integer(50)),
                      Minus(Integer(20), Integer(15)))

# %%
# et l'évaluer
expression.eval()

# %% [markdown]
# En outre, on s'efforcera de **factoriser au maximum le code**, et d'éviter dans toute mesure du possible les répétitions fastidieuses.
#
# L'objectif est d'obtenir un code maintenable, dans lequel on puisse facilement ajouter des *features* (nouveaux opérateurs notamment).

# %% [markdown]
# ## modalités

# %% [markdown]
# Malheureusement cet exercice est trop complexe pour la mécanique d'auto-évaluation et les modalités habituelles de colonnes rouges et vertes.
# Pour vous convaincre que vous avez bien répondu à la question, nous fournissons quelques cellules de test.
#
# Parmi ce qui est attendu, à la construction des objets vous êtes censés vérifier qu'on **appelle** le **constructeur** avec un **nombre d'arguments correct**, et lancer une **exception `TypeError` sinon**.

# %%
# assurez-vous aussi de bien avoir "oublié"
# les classes que nous venons d'importer pour illustrer l'exemple
del Integer, Float, Negative, Plus, Minus, Multiply, Divide


# %% [markdown]
# *****

# %%
# votre code

class Integer:
    def __init__(self, value):
        self.value = value
    def eval(self):
        return self.value

class Float(Integer):
    pass

class Negative:
    def __init__(self, expr):
        self.expr = expr
    def eval(self):
        return -self.expr.eval()

class Plus:
    def __init__(self, *args):
        self.args = args
    def eval(self):
        return sum(arg.eval() for arg in self.args)

class Minus:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        return self.left.eval() - self.right.eval()

class Multiply:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        return self.left.eval() * self.right.eval()

class Divide:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        return self.left.eval() / self.right.eval()



# %% tags=[]
# votre code

class Atom:
    def __init__(self, value):
        self.value = value
    def eval(self):
        return self.value

class Integer(Atom):
    pass
class Float(Atom):
    pass



class Unary:
    def __init__(self, expr):
        self.expr = expr
    def eval(self):
        return self.operator(self.expr.eval())

class Negative(Unary):
    @staticmethod
    def operator(x):
        return -x



class Binary:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def eval(self):
        return self.operator(self.left.eval(), self.right.eval())

# 2 ways to instantiate operator

# a static method
class Minus(Binary):
    @staticmethod
    def operator(x, y):
        return x - y

# a class attribute (note that self is used in that case)
class Divide(Binary):
    operator = lambda self, x, y: x / y



class Nary:
    def __init__(self, *args):
        self.args = args
    def eval(self):
        return self.operator(arg.eval() for arg in self.args)

class Plus(Nary):
    @staticmethod
    def operator(*args):
        return sum(*args)


from functools import reduce
from operator import mul

class Multiply(Nary):
    @staticmethod
    def operator(*args):
        # 3rd argument to reduce is initial value
        # in case of an empty set of arguments
        return reduce(mul, *args, 1)


# %%
tree = Integer(10); print(tree.eval())

# %%
tree = Negative(Integer(10)); print(tree.eval())

# %%
tree = Divide(Integer(10), Integer(20)); print(tree.eval())

# %%
tree = Plus(); print(tree.eval())

# %%
tree = Plus(Integer(10)); print(tree.eval())

# %%
tree = Plus(Integer(10), Integer(20)); print(tree.eval())

# %%
tree = Plus(Integer(10), Integer(20), Integer(30)); print(tree.eval())

# %%
tree = Multiply(); print(tree.eval())

# %%
tree = Multiply(Integer(10)); print(tree.eval())

# %%
tree = Multiply(Integer(10), Integer(20)); print(tree.eval())

# %%
tree = Multiply(Integer(10), Integer(20), Integer(30)); print(tree.eval())

# %%
# quelques tests
tree = Multiply(
    Plus(Multiply(Integer(10), Integer(2)), Integer(30)),
    Multiply(Negative(Integer(4)), Integer(25)))

assert tree.eval() == -5000

# %%
tree = Plus(Multiply(Integer(10), Integer(2)),
            Negative(Negative(Integer(30))),
            Minus(Integer(100), Integer(50)))

assert tree.eval() == 100

# %%
tree = Multiply(
    Plus(Integer(30), Integer(40), Integer(50)),
        Minus(Integer(20), Integer(15)))

assert tree.eval() == 600

# %%
tree = Negative(
    Plus(Float(10), Negative(Integer(20))))

assert tree.eval() == 10.

# %%
tree = Divide(Integer(10), Integer(4))
assert tree.eval() == 2.5

# %%
# ces cellules devraient toutes afficher OK
try:
    Multiply()
except TypeError:
    print("OK")

# %%
try:
    Plus(Integer(1))
except TypeError:
    print("OK")

# %%
try:
    Divide(Integer(10), Integer(20), Integer(30))
except TypeError:
    print("OK")

# %%
try:
    Negative(Integer(10), Integer(20))
except TypeError:
    print("OK")


# %% [markdown]
# ****

# %% [markdown]
# ## v2

# %% [markdown]
# une fois que vous avez fait ce premier noyau, vous pouvez étendre votre langage pour y ajouter l'affectation et les variables; la seule différence de taille par rapport au premier exercice est qu'il va nous falloir propager l'environnement (les valeurs des variables).
#
# pour cela je vous recommande d'envisager une méthode d'évaluation
#
# `expression._eval(env)`  plutôt que `expression.eval()`
#
# dans laquelle `env` est un dictionnaire.

# %% [markdown]
# ## annexe

# %% [markdown]
# un résumé des opérateurs et de leurs arités respectives

# %% [markdown] cell_style="split"
# ### v1
#
# | Opérateur | arité |
# |-----------|-------|
# | Integer   | 1     |
# | Float     | 1     |
# | Negative  | 1     |
# | Plus      | n>=2  |
# | Minus     | 2     |
# | Multiply  | n>=2  |
# | Divide    | 2     |
#

# %% [markdown] cell_style="split"
# ### v2
#
# | Opérateur   | arité |
# |-------------|-------|
# | Expressions | n>=1  |
# | Variable    | 1     |
# | Assignment  | 2     |
#

# %% tags=[]
# votre code

class Expression:
    def eval(self):
        return self._eval({})

class Atom(Expression):
    def __init__(self, value):
        self.value = value
    def _eval(self, env):
        return self.value

class Integer(Atom):
    pass
class Float(Atom):
    pass



class Unary(Expression):
    def __init__(self, expr):
        self.expr = expr
    def _eval(self, env):
        return self.operator(self.expr._eval(env))

class Negative(Unary):
    @staticmethod
    def operator(x):
        return -x



class Binary(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right
    def _eval(self, env):
        return self.operator(self.left._eval(env), self.right._eval(env))

# 2 ways to instantiate operator

# a static method
class Minus(Binary):
    @staticmethod
    def operator(x, y):
        return x - y

# a class attribute (note that self is used in that case)
class Divide(Binary):
    operator = lambda self, x, y: x / y



class Nary(Expression):
    def __init__(self, *args):
        self.args = args
    def _eval(self, env):
        return self.operator(arg._eval(env) for arg in self.args)

class Plus(Nary):
    @staticmethod
    def operator(*args):
        return sum(*args)


from functools import reduce
from operator import mul

class Multiply(Nary):
    @staticmethod
    def operator(*args):
        # 3rd argument to reduce is initial value
        # in case of an empty set of arguments
        return reduce(mul, *args, 1)

###########
class Variable(Expression):
    def __init__(self, varname):
        self.varname = varname
    def _eval(self, env):
        return self.env[varname]

class Assignment(Binary):
    def _eval(self, env):
        varname = self.left
        env[varname] = self.right._eval(env)



# %%
tree = Integer(10); print(tree.eval())

# %%
tree = Negative(Integer(10)); print(tree.eval())

# %%
tree = Divide(Integer(10), Integer(20)); print(tree.eval())

# %%
tree = Plus(); print(tree.eval())

# %%
tree = Plus(Integer(10)); print(tree.eval())

# %%
tree = Plus(Integer(10), Integer(20)); print(tree.eval())

# %%
tree = Plus(Integer(10), Integer(20), Integer(30)); print(tree.eval())

# %%
tree = Multiply(); print(tree.eval())

# %%
tree = Multiply(Integer(10)); print(tree.eval())

# %%
tree = Multiply(Integer(10), Integer(20)); print(tree.eval())

# %%
tree = Multiply(Integer(10), Integer(20), Integer(30)); print(tree.eval())

# %%
# quelques tests
tree = Multiply(
    Plus(Multiply(Integer(10), Integer(2)), Integer(30)),
    Multiply(Negative(Integer(4)), Integer(25)))

assert tree.eval() == -5000

# %%
tree = Plus(Multiply(Integer(10), Integer(2)),
            Negative(Negative(Integer(30))),
            Minus(Integer(100), Integer(50)))

assert tree.eval() == 100

# %%
tree = Multiply(
    Plus(Integer(30), Integer(40), Integer(50)),
        Minus(Integer(20), Integer(15)))

assert tree.eval() == 600

# %%
tree = Negative(
    Plus(Float(10), Negative(Integer(20))))

assert tree.eval() == 10.

# %%
tree = Divide(Integer(10), Integer(4))
assert tree.eval() == 2.5

# %%
# ces cellules devraient toutes afficher OK
try:
    Multiply()
except TypeError:
    print("OK")

# %%
try:
    Plus(Integer(1))
except TypeError:
    print("OK")

# %%
try:
    Divide(Integer(10), Integer(20), Integer(30))
except TypeError:
    print("OK")

# %%
try:
    Negative(Integer(10), Integer(20))
except TypeError:
    print("OK")

# %%

# %%

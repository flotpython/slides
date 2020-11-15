# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
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
#   notebookname: "surcharge d\u2019op\xE9rateurs"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% slideshow={"slide_type": "slide"}
from plan import plan; plan("classes", "surcharge")


# %% [markdown] slideshow={"slide_type": "slide"}
# # surcharge des opérateurs du langage

# %% [markdown]
# * le langage offre de nombreux opérateurs, e.g.
#   * opérations arithmétiques : `+`, `-`, `*`, `\`
#   * mais aussi : `x[i]`, `x()`, `x.attr`
# * des builtins comme &nbsp;&nbsp;&nbsp;`print()`, `len()`
# * des constructions syntaxiques &nbsp;&nbsp;&nbsp; `for i in x:`
# * qui sont conçues sur les types de base  
#   mais indéfinis, ou pauvres, sur les classes utilisateur

# %% [markdown] slideshow={"slide_type": "slide"}
# ## de quoi s'agit-il ?

# %% [markdown]
# * ce dont il est question, c'est de donner les moyens  
#   à chaque classe de mieux s'intégrer dans le langage
#
# * comment ?  en redéfinissant des méthodes *spéciales:*
#   * qui s'appellent toujours `__X__`
#   * ou `X` est bien sûr en relation avec l'opération
#   * e.g. `__add__` a effet sur l'opérateur `+`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### surcharge optionnelle

# %% [markdown]
# * la surcharge d’opérateurs est optionnelle
#   * quoique: `__init__` et `__str__`
# * toutes les méthodes que l’on peut surcharger sont décrites dans  
#   https://docs.python.org/3/reference/datamodel.html#special-method-names
#
# * lire cette documentation au moins une fois pour savoir tout ce que l’on peut surcharger
# * **notamment** si vous êtes amenés à lire beaucoup de code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les plus communs

# %% [markdown]
# * nous avons déjà vu `__init__`
# * il est très fréquent de redéfinir aussi
#   * `__repr__`: pour redéfinir `repr()`
#   * `__str__`: pour redéfinir `str(x)` et `print()`

# %%
# en l'absence de redéfinition 
# la présentation est aride
# et identique pour les deux modes repr/str

class Dumb:
    pass

a = Dumb()

# %% cell_style="split"
# __repr__()
a

# %% cell_style="split"
# __str__()
str(a)

# %% cell_style="split"
# __repr__()
repr(a)

# %% cell_style="split"
# __str__()
print(a)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### seulement `__repr__` (i.e. pas `__str__`)

# %% [markdown]
# il est assez fréquent de ne redéfinir que `__repr__`

# %%
class R:
    def __init__(self, atom):
        self.atom = atom

    def __repr__(self):
        return "[R {}]".format(self.atom)

a = R('seulement repr')

# %% cell_style="split"
# __repr__()
a

# %% cell_style="split"
# __str__()
str(a)

# %% cell_style="split"
# __repr__()
repr(a)

# %% cell_style="split"
# __str__()
print(a)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### `__str__` et `__repr__`

# %% [markdown]
# * il faut savoir que
#   * si `__repr__` est défini, et pas `__str__`
#   * alors on fait comme si `__str__ = __repr__`
# * et aussi que `__str__` sur les containers (list, ...)
#   * appelle en fait `__repr__` sur les contenus
#   * ceci pour éviter les récursions infinies...

# %% [markdown]
# * dans l'esprit:
#   * `__repr__` est censé être non-ambigu
#   * et `__str__` est censé être joli
# * mais ce n'est pas toujours facile à suivre 

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `__str__` et `__repr__`

# %%
# si maintenant on définit aussi `__str__`
class R:
    def __init__(self, atom):
        self.atom = atom
    def __repr__(self):
        return "[R {}]".format(self.atom)
    def __str__(self):
        return str(self.atom)

b = R('les deux')

# %% cell_style="split"
# __repr__()
b

# %% cell_style="split"
# __str__()
str(b)

# %% cell_style="split"
# __repr__()
repr(b)

# %% cell_style="split"
# __str__()
print(b)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## surcharge d’opérateurs numériques

# %%
# pour redéfinir l'addition, sans surprise on surcharge __add__ 
# ici on choisit un comportement folklorique
# qui fait une espèce de concaténation

class C():
    
    def __init__(self, value):
        self.value = value

    def __add__(self, operand):
        # l'addition crée un nouvel objet
        return C(self.value + '-' + operand.value)


# %%
x, y, z = C('alice'), C('bob'), C('eve')
s = x + y + z
s.value

# %% [markdown] slideshow={"slide_type": "slide"}
# **c'est un début, mais**

# %%
# on ne peut pas additionner C avec un str
try:
    C('abc') + 'def'
    
except AttributeError as e:
    print("OOOPS", e)

# %% [markdown]
# **et aussi**

# %%
# on ne peut pas non plus additionner lorsque
# l'instance de C est à gauche dans l'addition

try:
    'abc' + C('abc')
    
except TypeError as e:
    print("OOOPS", e)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### opérateurs binaires

# %% [markdown]
# pour faire proprement, il faut
#
# * envisager le mélange avec d'autres types
#   * polymorphisme :
#   * *C + str, C + int, C + float*…
# * envisager qu'un objet de notre classe peut être
#   * commutatif :
#   * *str + C, int + C, float + C*

# %% [markdown] slideshow={"slide_type": "slide"}
# ### polymorphe - v1

# %% [markdown]
# **une première amélioration naïve**

# %%
# sans définir __str__
class C1():

    def __init__(self, value):
        self.value = value

    def __add__(self, operand):
        # soyons plus subtils
        if isinstance(operand, C):
            ajout = operand.value
        else:
            ajout = str(operand)

        # le résultat est un nouvel objet
        return C1(self.value + '-' + ajout)


# %%
# maintenant on peut ajouter un C avec un str
(C1('alice') + 'bob').value


# %% [markdown] slideshow={"slide_type": "slide"}
# ### polymorphe - v2

# %% [markdown]
# **c'est beaucoup plus simple si on redéfinit `str()`**

# %%
# une deuxième amélioration 

class C2():
    def __init__(self, value):
        self.value = value
    # ici on redéfinit __str__
    def __str__(self):
        return str(self.value)
    def __add__(self, operand):
        # comme on a redéfini __str__, 
        # on peut écrire tout simplement :
        return C2(self.value + '-' + str(operand))


# %%
(C2('alice') + 'bob').value

# %%
# mais par contre la présentation n'est toujours pas très jolie
C2('alice') + 'bob'


# %% [markdown]
# **vous voyez pourquoi on redéfinit souvent `__repr__`**

# %% [markdown] slideshow={"slide_type": "slide"}
# ### polymorphisme - v2 

# %% cell_style="split"
# un autre souci avec cette approche
# c'est dans le cas d'une sous-classe
class Sub2(C2):
    pass


# %% cell_style="split"
# si on additionne deux instances 
# de la sous-classe
s2 = Sub2('alice') + Sub2('bob')

# %%
# on obtient un objet .. de la superclasse
type(s2)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### polymorphe - v3

# %% [markdown]
# on peut améliorer encore un peu
#
# * définissons `__repr__` plutôt que `__str__`
# * et aussi créons un objet **de la même classe**
#   * plutôt que de câbler en dur le nom de notre classe
#   * comme ça nos sous-classes seront plus à l'aise

# %% slideshow={"slide_type": "slide"}
# une amélioration plus 'subclass-friendly'

class C3():
    def __init__(self, value):
        self.value = value

    # c'est plus simple de définir __repr__
    def __repr__(self):
        return str(self.value)

    def __add__(self, operand):
        # cette forme-là permet à une sous-classe
        # de créer des instances à elle plutôt que
        # forcément un C3
        return self.__class__(self.value + '-' + str(operand))


# %%
(C3('alice') + 'bob').value

# %% cell_style="split"
# et cette fois
s = C3('alice') + 'bob'
s

# %% cell_style="split"
# on a bien un objet 
# de la classe C3
type(s)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### opérateurs binaires : à droite

# %% [markdown]
# * quand on fait `C('bob') + 'alice'
#   * c'est à l'opérande gauche
#   * qu'on envoie la méthode `__add__`
# * si on veut pouvoir ajouter dans l'autre sens
#   * c'est-à-dire `'bob' + C('alice')`
# * il suffit de redéfinir `__raddr__`
#   * le `r` voulant dire *right*
#   * pour quand le sujet de la méthode est à droite 

# %% slideshow={"slide_type": "slide"}
# opérateurs à droite
class CR():
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

    def __add__(self, rightop):
        return self.__class__(self.value + '-' + str(rightop))

    # dans le cas d'une algèbre commutative on peut juste faire
    # __raddr__ = __addr__
    # mais ici bien la concaténation n'est pas commutative
    def __radd__(self, leftop):
        return self.__class__(str(leftop) + '-' + self.value)


# %%
'bob' + CR('alice')


# %% cell_style="center" slideshow={"slide_type": "slide"}
# avec cette version aboutie de notre classe
# on a tous les avantages recherchés
# notamment utilisable avec une sous-classe

class SubCR(CR):
    pass


# %% cell_style="split"
o1 = SubCR('sousobj') + 'string'
o1

# %% cell_style="split"
o2 = 'string' + SubCR('sousobj')
o2

# %% cell_style="center"
type(o1), type(o2)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## protocoles

# %% [markdown] slideshow={"slide_type": ""}
# * certaines constructions du langage
#   * sont simples et n'utilisent qu'**une seule** spéciale
#   * ex. `__len__`
# * d'autres reposent sur **plusieurs méthodes spéciales**
#   * par exemple `x[]` utilise:  
#     `__getitem__()` pour les références  
#     `__setitem__()` pour les affectations  
#     `__delitem__()` pour `del x[]`  
#     `__missing__()` pour les défauts de clé
#
# * ou sur **une parmi plusieurs**
#   * par exemple `i in x` peut fonctionner avec  
#     `__contains__()` ou  
#     `__iter__()` ou  
#     `__getitem__()`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### protocoles et vocabulaire

# %% [markdown] slideshow={"slide_type": ""}
# * dans le cadre du *duck typing*
# * il est fréquent de faire référence 
#   * à des grandes familles d'objet
#   * comme e.g. séquences, itérables, callables, ...
# * par exemple une *séquence*
#   * doit implémenter `x[i]` avec i entier
#   * et `len(x)`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le protocole itérable

# %% [markdown] slideshow={"slide_type": ""}
# * un objet est itérable
#   * lorsque qu'on peut écrire `for i in x`
# * deux moyens
#   * une séquence
#   * implémenter `__iter__()`
#   * qui doit retourner un itérateur

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le protocole iterator

# %% [markdown]
# * un objet est un itérateur si
#   * il implémente `__next__()`
#   * qui retourne l'objet suivant
#   * ou lève l'exception `StopIteration`
#   * et il implémente `__iter__` qui renvoie `self`
# * un itérateur est donc toujours itérable
# * une fonction génératrice renvoie un itérateur

# %% [markdown] slideshow={"slide_type": "slide"}
# ### itérable avec générateur

# %% cell_style="split"
from itertools import count

class Iterable:
    """itérer les carrés <= n"""
    def __init__(self, n):
        self.n = n

    # il est pratique d'utiliser un générateur
    # pour implémenter __iter__
    def __iter__(self):
        for i in count():
            square = i ** 2
            if square >= 20:
                return
            yield square


# %% cell_style="split"
# équivalent à 

def IterableGenerator(n):
    for i in count():
        square = i ** 2
        if square >= 20:
            return
        yield square        


# %% [markdown]
# ***

# %% cell_style="split"
for n in Iterable(20):
    print(n)

# %% cell_style="split"
for n in IterableGenerator(20):
    print(n)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### callables

# %% [markdown]
# * un objet est callable si on peut évaluer `x()`
# * pas réservé aux fonctions et aux classes
# * les instances d'une classe 
#   * qui implémente `__call__`
#   * sont callables également
# * confusion fréquente
#   * appeler la classe `c = C()` : utilise `__init__`
#   * appeler l'instance `c()` : utilise `__call__`

# %% [markdown] slideshow={"slide_type": "slide"}
# #### callables

# %%
class SumOffset:
    """"
    chaque instance possède un offset
    lorsque l'instance est appelée elle fait la 
    somme de ses arguments plus l'offset
    """
    def __init__(self, offset):
        print("init")
        self.offset = offset
        
    def __call__(self, *args):
        print("calling..")
        return sum(args) + self.offset


# %%
# cette instance est un callable
# elle se comporte comme une fonction
# qui rend 100 + sigma(args)
additionneur100 = SumOffset(100)

# %% cell_style="split"
# quand on l'appelle
additionneur100(1, 2, 3)

# %% cell_style="split"
additionneur100(1000, 2000)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple d’autres surcharges d’opérateurs

# %% [markdown]
# * `__lt__`, `__gt__`, `__le__`, `__ge__`, `__eq__`, `__ne__`  
#   *resp.* &nbsp; `A<B`, &nbsp; `A>B`, &nbsp; `A<=B`, &nbsp; `A>=B`, &nbsp; `A==B`, &nbsp; `A!=B`
#
# * `__bool__` : appelé pour tester si un objet est vrai ou faux
# * `__len__`: redéfinir `len(x)` 
# * `__getattr__`, `__slot__`, `__getattribute__`  
#   impliqués dans le protocole de recherche d'attributs
#
# * ... liste très très complète

# %% [markdown] slideshow={"slide_type": "slide"}
# ## attributs privés

# %% [markdown]
# **Rappels**
#
# * pas de notion d'attributs protégé / privé en Python
#   * on peut accéder à n’importe quels attributs d’une classe
# * on représente un attribut privé avec une simple convention de nommage 
#   * les attributs qui commencent par `_` sont considérés comme privés

# %% [markdown] slideshow={"slide_type": "slide"}
# ### trois types d’attributs privés réservés

# %% [markdown]
# * les attributs `_*` ne sont pas importés par `from module import *`
# * les attributs `__*__` sont les attributs privés définis par Python. On ne doit pas nommer nos propres attributs privés avec cette convention
# * les attributs `__*` (sans `__` à la fin) définis dans une classe sont automatiquement renommés à la compilation (`__spam` dans la classe Ham devient `_Ham__spam`). On appelle cela *name mangling*

# %% [markdown] slideshow={"slide_type": "slide"}
# ### name mangling

# %% cell_style="split"
# utiliser le name mangling pour 
# un attribut privé qui
# ne doit pas être modifié
# par une sous-classe par accident
class A():
    def __init__(self):
        self.__a = "dans A"
    def __str__(self):
        return self.__a

class B(A):
    def __init__(self):
        A.__init__(self)
        # on est sûr de n'interférer avec personne
        self.__a = "dans B" 


# %% cell_style="split"
b = B()
print(b)

# %% cell_style="split"
print(b.__dict__)

# %% cell_style="split"
try:
    b.__a
except Exception as exc:
    print(f"OOPS {type(exc)} {exc}")


# %% [markdown] slideshow={"slide_type": "slide"}
# ## classes imbriquées

# %% [markdown]
# * si une classe `A` définit une autre classe `B`,
#   * on peut créer des instances de `B`
#   * par la classe `A` avec `A.B()`
#   * ou par une de ses instances `A().B()`
# * en effet, on peut y accéder aussi bien
#   * directement par la classe `A`, ou
#   * par une instance grâce à l’héritage

# %% slideshow={"slide_type": "slide"}
class A:
    class B:
        pass


# %%
A.B()

# %%
A().B()

# %% [markdown] slideshow={"slide_type": "slide"}
# ## quand utiliser la POO en Python ?

# %% [markdown]
# * utilisation de base
#   * sans héritage mais avec encapsulation
#   * bénéfice de grouper le code et les données
#   * dans des espaces de noms étanches
# * héritage
#   * demande en général un peu de conception en amont
#   * ce n'est **pas forcément le plus gros bénéfice**
#   * sauf à mon humble avis pour la surcharge des opérateurs
#   * qui s'avère vite utile - homéopatiquement
#   * une fois qu'on a passé le barrage d'entrée

# %% [markdown] slideshow={"slide_type": "slide"}
# ## modules ou classes ?

# %% [markdown]
# * utiliser une classe dès qu'on a besoin
#   * de créer des instances multiples
#   * d'exploiter la notion d’héritage
# * se contenter d'un module si on veut simplement
#   * isoler des espaces de nommages
#   * créer des méthodes statiques
#   * factoriser du code
# * opinion personnelle
#   * ne me souviens pas d'avoir écrit un module sans classe
#   * ou alors pour grouper quelques helpers → `utils.py` 
#   * ce qui ne veut pas dire qu'un module ne contient jamais de fonction

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour réutiliser du code en python

# %% [markdown]
# * fonctions
#   * pas d'état après exécution
# * modules
#   * garde l'état
#   * une seule instance par programme
# * **classes**
#   * **instances multiples**
#   * **chacune garde l'état**
#   * **héritage**

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour conclure

# %% [markdown]
# * *design patterns*
#   * quelques idées assez génériques éprouvées
#   * pas de magie ou de théorie complexe dans les design patterns
#   * liste de recettes empiriques des auteurs
#   * propices à l'exploitation de l'héritage
#
# ![design patterns](pictures/book-design-patterns.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## partie optionnelle

# %% [markdown] slideshow={"slide_type": "slide"}
# ### utiliser un opérateur ou la méthode `__x__` ?

# %% [markdown]
# * en version courte: **utilisez les opérateurs**
# * résultat est équivalent parce que le même code est utilisé, mais la durée d’exécution peut différer à cause d’optimisations de l’interpréteur
# * l’interpréteur va optimiser l’appel à la fonction lors de utilisation des opérateurs, mais pas lors de l’appel direct à la méthode `__x__`
#   * spécifique à CPython, il faut donc tester ce comportement pour les autres implémentations de Python

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un peu de profiling

# %% [markdown]
# * voyez le module `timeit`
#   * https://docs.python.org/3/library/timeit.html

# %%
from timeit import timeit

# %% [markdown] slideshow={"slide_type": "slide"}
# ### utiliser un opérateur ou la méthode `__x__` ?

# %%
timeit(setup = "L = range(1000)", number = 100000, stmt = "1000 in L")

# %%
timeit(setup = "L = range(1000)", number = 100000,
       stmt = "L.__contains__(1000)")

# %% [markdown]
# ```
# timeit(setup = "L = range(1000)", number = 100000000, stmt = "0 in L")
# 9.534808637050446
# timeit(setup = "L = range(1000)", number = 100000000, stmt = "L.__contains__(0)")
# 19.80092801299179
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### profiling et notebooks

# %% [markdown]
# beaucoup de [fonctionnalités très intéressantes dans les *magic* IPython](https://ipython.readthedocs.io/en/stable/interactive/magics.html), comme `%timeit`

# %%
L = range(1000)
# %timeit -n 100000 0 in L

# %%
L = range(1000)
# %timeit -n 100000 L.__contains__(0)

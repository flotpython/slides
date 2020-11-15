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
#   notebookname: encapsulation
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
from plan import plan; plan("classes", "encapsulation")


# %% [markdown]
# # encapsulation

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
# ### rappel: primer

# %% cell_style="split"
class MyFirstClass:
    
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        
    def __repr__(self):
        return (f"je suis {self.nom}, "
                f"j'ai {self.age} ans")


# %% cell_style="split"
person = MyFirstClass(
    "Jean Dupont", 25)
person


# %% [markdown] slideshow={"slide_type": "slide"}
# ### programmation orientée objet  
#   pourquoi et comment ?

# %% [markdown] cell_style="split"
# ####  deux objectifs 
#
# * modularité
# * réutilisabilité

# %% [markdown] cell_style="split"
# #### deux moyens 
#
# * espaces de nom
# * héritage

# %% [markdown] slideshow={"slide_type": "slide"}
# ### avertissement : POO et langage

# %% [markdown]
# * la POO est présente dans tous les langages modernes
# * cependant l'implémentation *a un impact*
# * sur le paradigme présenté au programmeur
# * se méfier des habitudes héritées d'autres langages

# %% [markdown] slideshow={"slide_type": "slide"}
# * C++/Java
#   * fort typage statique
#   * **impose** l'existence d'une classe *chapeau* 
#   * par exemple la classe `Simulable`
# * Python
#   * on peut parfaitement se passer de la classe `Simulable`
#   * pourvu que les classes concrètes
#   * disposent des méthodes à run-time
#   * c'est le *duck typing*

# %% [markdown] slideshow={"slide_type": "slide"}
# ### modularité

# %% [markdown]
# * du code modulaire
#   * grouper le code dans une classe
#   * grouper les données dans un objet
# * c'est là qu'interviennent les espaces de nom
# * (comme avec les notions de module et de package)  

# %% [markdown] slideshow={"slide_type": "slide"}
# ### réutilisabilité

# %% [markdown]
# * DRY: chaque fonctionnalité écrite une seule fois
# * maintenance plus simple
# * du code générique
#   * ex: un simulateur fait "avancer" une liste d'objets
#   * dès qu'un objet explique comment il avance
#   * il peut faire partie de la simulation
# * c'est là qu'intervient l'héritage

# %% [markdown] slideshow={"slide_type": "slide"}
# ## espaces de nom

# %% [markdown]
# * tous les objets qui sont
#   * un package
#   * un module
#   * une classe
#   * une instance
# * constituent chacun un espace de nom
#   * i.e. une association *attribut* → *objet*

# %% [markdown] slideshow={"slide_type": "slide"}
# ### espaces de nom - pourquoi

# %% [markdown]
# * permet de lever l'ambigüité en cas d'homonymie
# * cf. exemple du C *old-school*
# * les espaces de nom sont imbriqués (*nested*)
#   * ex. `package.module.classe.methode`
# * on peut accéder à tous les objets
#   * dès qu'on sait partir d'une variable
#   * par exemple un module importé
# * l'héritage rend cela dynamique
#   * i.e. la résolution est faite à *runtime*

# %% [markdown] slideshow={"slide_type": "slide"}
# ### digression - variables et attributs

# %% [markdown] cell_style="split"
# #### deux mondes étanches
#
# * variables 
# * attributs

# %% [markdown] cell_style="split"
# #### se mélangent 

# %% [markdown]
# * typiquement dans une expression comme `a.b.c.d`

# %% [markdown] cell_style="split"
# * `a` est une **variable**

# %% [markdown] cell_style="split"
# * `b`, `c` et `d` sont des **attributs**

# %% [markdown] slideshow={"slide_type": "slide"}
# #### variables statiques / attributs dynamiques

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ##### résolution des **variables**
#
# * entièrement **lexical**
# * en remontant dans le code
# * avec les règles LEGB  
#   local, englobant, global, *builtin*

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ##### résolution des **attributs**
#
# * dans le monde des **objets**
# * en remontant les espaces de nom
# * essentiellement **dynamique**  
#   *i.e.* à *runtime*

# %% [markdown] slideshow={"slide_type": "slide"}
# ## héritage

# %% [markdown] slideshow={"slide_type": ""}
# * la **résolution des attributs**
# * fournit la **mécanique de base**
#   * sur laquelle on a - très peu - élaboré
# * pour implémenter l'héritage
# * on verra ça en détails plus tard

# %% [markdown] slideshow={"slide_type": "slide"}
# ### ex: une classe et une instance

# %% cell_style="split"
# une classe sans heritage
# et juste un constructeur
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# %% cell_style="split"
point = Point(2, 3)
point.x


# %% [markdown] slideshow={"slide_type": "slide"}
# ### classe = usine à objets

# %% [markdown] slideshow={"slide_type": ""}
# * comme tous les types, `Point` est une usine à objets
#   * cf. `list({1, 2, 3})`
# * donc pour créer une instance, on *appelle* cet objet *classe*
# * la méthode `__init__` nous permet de définir
#   * ce qui est fait lors de la construction de l'objet
#   * c'est-à-dire à l'appel de `Point(2, 3)`
# * remarquez le premier paramètre `self`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### 2 espaces de nommage

# %% [markdown] cell_style="split"
# **à ce stade nous avons deux espaces de nom**
#
# * la classe `Point`
#   * `Point.__init__` : la méthode
# * l'instance
#   * `point.x` : 2 pour cette instance
#   * `point.y`

# %% cell_style="split"
# %load_ext ipythontutor

# %% [markdown] slideshow={"slide_type": "slide"}
# **la classe et l'instance: deux espaces de nom distinct**

# %%
# %%ipythontutor width=1000
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
point = Point(2, 3)

# %% cell_style="split" slideshow={"slide_type": "slide"}
# la classe possède 
# l'attribut '__init__' 
'__init__' in Point.__dict__

# %% cell_style="split"
# c'est la méthode 
# qu'on a définie
type(Point.__init__)

# %% cell_style="split"
# par contre elle ne possède
# pas d'attribut x
'x' in Point.__dict__

# %% cell_style="split"
# l'attribut x se trouve
# bien dans l'instance
'x' in point.__dict__

# %% [markdown] slideshow={"slide_type": "slide"}
# ## ex. de résolution d'attribut

# %%
# cas simple sans héritage
# appel d'une méthode
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
       
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)


# %%
vector = Vector(3, 4)
vector.length()

# %% [markdown] slideshow={"slide_type": "slide"}
# ### espaces de nom

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# * la classe `Vector` a les attributs
#   * `__init__`
#   * `length`

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# * l'objet `vector` a les attributs
#   * `x` et `y`,
#   * mais pas `length` !

# %% slideshow={"slide_type": "slide"}
# %%ipythontutor width=1000 height=400 curInstr=7
import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
   
vector = Vector(2, 2)

# %% [markdown] slideshow={"slide_type": "slide"}
# pour visualiser la même chose à base d'introspection dans le code
#
# tous les objets ont un attribut `__dict__`

# %% slideshow={"slide_type": ""}
# les attributs 'intéressants' de Vector
[att for att in Vector.__dict__ if '__' not in att or att == '__init__']

# %%
# et dans l'instance
list(vector.__dict__)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### résolution d'attribut

# %% [markdown] slideshow={"slide_type": ""}
# * l'objet `vector` ne possède pas en propre l'attribut `length`
# * et pourtant on peut écrire `vector.length()` 

# %% [markdown] slideshow={"slide_type": ""}
# * pour évaluer `vector.length()`
# * on fait de la résolution d'attributs
#   * cherché dans l'instance: pas trouvé
#   * cherché dans la classe: oui, on prend ça

# %% [markdown] slideshow={"slide_type": "slide"}
# ### héritage ?

# %% [markdown] slideshow={"slide_type": ""}
# * ce n'est pas encore de l'héritage  
#   puisque pour l'instant on n'a qu'une classe
# * mais on verra que l'héritage  
#   est une simple prolongation de cette logique

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple avec héritage

# %%
# une classe fille sans aucun contenu
class SubVector(Vector): 
    pass

subvector = SubVector(6, 8)

subvector.length()

# %% slideshow={"slide_type": "slide"}
# %%ipythontutor width=1000 height=400 curInstr=8
import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
class SubVector(Vector):
    pass

subvector = SubVector(6, 8)

# %% [markdown]
# * c'est exactement le même mécanisme qui est à l'oeuvre :
# * on cherche `length`
#   * dans l'instance : non
#   * dans la classe : non
#   * dans la super-classe : ok, on prend ça

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *Method Resolution Order*

# %% [markdown]
# * l'héritage entre les classes
# * détermine l'ordre dans lequel sont cherchés les attributs
# * en sus de l'instance elle-même
# * en anglais *method resolution order*
# * ou `mro()` (une méthode de la classe)
# * concept surtout utile avec l'héritage multiple
# * mais qui me semble pertinent pour illustrer notre propos

# %%
SubVector.mro()


# %% [markdown] slideshow={"slide_type": "slide"}
# #### attributs non fonctionnels (≠ méthode)

# %% [markdown]
# * on peut utiliser les même concepts
# * pour gérer des attributs de donnée (i.e. ≠ méthode)

# %% slideshow={"slide_type": "slide"}
class Factory:
    # un compteur global à la classe
    all_labels = []

    def __init__(self, label):
        self.label = label
        # ici je pourrais aussi bien écrire 
        # Factory.all_labels.append(label)
        self.all_labels.append(label)

Factory.all_labels

# %% cell_style="split" slideshow={"slide_type": ""}
f1 = Factory('premier')
Factory.all_labels

# %% cell_style="split" slideshow={"slide_type": ""}
f2 = Factory('second')
Factory.all_labels


# %% cell_style="center" slideshow={"slide_type": "slide"}
# %%ipythontutor width=1000 height=400
class Factory:
    all_labels = []
    def __init__(self, label):
        self.label = label
        # ici je pourrais aussi bien écrire 
        # Factory.all_labels.append(label)
        self.all_labels.append(label)
f1 = Factory('premier')
f2 = Factory('second')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### **remarque importante** : lecture ≠ écriture

# %% [markdown] slideshow={"slide_type": ""}
# * le mécanisme de recherche d'attribut qu'on vient de voir 
# * ne fonctionne que **pour la lecture des attributs**
# * donc ici en partant de l'instance
# * on trouve bien l'attribut de la classe

# %% cell_style="split"
Factory.all_labels is f1.all_labels

# %% cell_style="split"
f1.all_labels

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# #### **remarque importante** : lecture ≠ écriture

# %% [markdown] cell_style="center" slideshow={"slide_type": ""}
# * mais attention lorsqu'on **écrit** un attribut 
#   * *i.e.* si l'expression `foo.bar` est à gauche d'une affectation
# * alors l'attribut `bar` est créé/écrit **dans l'objet `foo`**
# * il n'y a **pas de recherche** dans ce cas !

# %% cell_style="split"
# ici on va créer un nouvel attribut
# directement dans l'instance
f1.all_labels = 'overridden'
f1.all_labels

# %% cell_style="split"
f2.all_labels

# %% cell_style="split"
f1.all_labels


# %% slideshow={"slide_type": "slide"}
# %%ipythontutor width=1000 height=400 curInstr=11
class Factory:
    # un compteur global à la classe
    all_labels = []

    def __init__(self, label):
        self.label = label
        Factory.all_labels.append(label)

f1 = Factory('premier')
f2 = Factory('second')

f1.all_labels = 'overridden'

# %% [markdown] slideshow={"slide_type": "slide"}
# ### lecture ≠ écriture - discussion
#
# * cela ne se remarque pas avec les méthodes 
#   * car c'est très rare d'écrire `instance.methode = ...`
# * mais du coup, lire et écrire un attribut ne **sont pas symétriques**

# %% [markdown] slideshow={"slide_type": "slide"}
# ce phénomène exhibe un très lointain rapport
# * avec le scope lexical des variables
# * et le `UnboundLocalError`

# %% cell_style="split"
foo = 12

def fun():
    # on peut lire la variable
    # de scope englobant
    print(foo)
fun()


# %% cell_style="split"
def bar():
    # ou créer une variable
    # dans ce scope
    foo = 13
bar()
print(foo)


# %%
def tutu():
    # mais pas les deux
    try:
        print(foo)
        foo = 13
    except UnboundLocalError as e:
        print("OOPS", e)
tutu()


# %% [markdown] slideshow={"slide_type": "slide"}
# ## résumé

# %% [markdown] slideshow={"slide_type": ""}
# * le mécanisme d'annotation des objets par les attributs  
#   et de recherche le long d'un chemin
# * constitue le coeur de ce qui est à l'oeuvre  
#   lorsqu'on fait de la Programmation Objet
# * on va le voir sur des exemples plus pratiques
# * avec comme avantages
#   * la modularité / encapsulation
#   * la factorisation de code / réutilisabilité

# %% [markdown] slideshow={"slide_type": "slide"}
# ## encapsulation

# %% [markdown]
# * consiste à définir un **ensemble d'opérations**
# * qui sont **les seules à travers lesquelles**  
#   on peut manipule ces objets
# * en préservant de bonnes propriétés / invariants
# * (que idéalement on peut prouver)

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ### dans d'autres langages
#
# * on trouve des mécanismes de protection
# * notamment attributs privés ou publics
# * visant à éviter les erreurs

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ### moins le cas en python
#
# * tradition  
#   "*we're all consenting adults here*"
# * quelques mécanismes *best-effort*  
#   notamment noms commençant par `_`
# * l'idée reste néanmoins très utile
# * on peut arriver à un résultat convaincant

# %% [markdown] slideshow={"slide_type": "slide"}
# ### applications

# %% [markdown] slideshow={"slide_type": ""}
# * par exemple `numpy.ndarray`
#   * qui enforce le type des différents composants
# * classe d'utilitaires réseau
#   * qui conservent l'état de la connexion
#   * pour faire ce qu'il faut au bon moment
# * ...

# %% [markdown] slideshow={"slide_type": "slide"}
# ### bénéfices

# %% [markdown] cell_style="center" slideshow={"slide_type": ""}
# c'est un des premiers bénéfices de la POO
#
# * que de pouvoir grouper les données
# * avec les traitements
# * dans une unité de programmation
# * facilement réutilisable
# * pas besoin d'héritage pour tout ça

# %% [markdown] slideshow={"slide_type": "slide"}
# ### code réel

# %% [markdown] slideshow={"slide_type": ""}
# * très souvent, pas de protection particulière
# * "we're all consenting adults here"
# * l'idée étant de pouvoir remplacer plus tard, si nécessaire,  
#   l'attribut par une `property` qui fasse les contrôles

# %% cell_style="split"
# une jauge a une valeur forcément 
# dans un intervalle fixe
# 
# toutefois en Python on expose typiquement
# un attribut `value` en lecture / écriture
# 
class Gauge:
    def __init__(self, value):
        self.value = value

# le code utilisateur peut lire
# et écrire librement l'objet


# %% [markdown] cell_style="split"
# En C++ / Java typiquement, on définirait ici 
# * un attribut privé `_value`
# * deux méthodes *getter/setter*
#
# le code utilisateur accède l'objet uniquement
# au travers de ces deux méthodes
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## mécanismes Python pour l'encapsulation

# %% [markdown] slideshow={"slide_type": ""}
# * les mécanismes offerts par Python 
#   * visibilité des attributs
#   * properties

# %% [markdown] slideshow={"slide_type": "slide"}
# ### visibilité des attributs

# %% [markdown]
# * pas de vraie notion d'attributs privé/public 
# * **toutefois** des conventions de nommage

# %% [markdown] slideshow={"slide_type": "slide"}
# ### PEP8 
#
# * `_single_leading_underscore` : 
#   * weak "internal use" indicator. E.g. `from M import *` does not import objects whose name starts with an underscore.
#   * correspond *en gros* aux champs protégés
#   * **enforcé** seulement pour les **modules**
#   * dans les classes, cela est juste une indication

# %% [markdown] slideshow={"slide_type": "slide"}
# #### PEP8
#
# * `__double_leading_underscore` : 
#   * when naming a class attribute, invokes name mangling  
#     (inside class `FooBar`, `__boo` becomes `_FooBar__boo` ; see below).
#
#   * correspond *en gros* aux champs privés

# %% [markdown] slideshow={"slide_type": "slide"}
# #### PEP8 ...
#
# * `__double_leading_and_trailing_underscore__`
#   *  "magic" objects or attributes that live in user-controlled namespaces. E.g. `__init__` , `__import__` or `__file__` . 
#   * **never invent such names**; only use them as documented.
#
# * `single_trailing_underscore_` : 
#   * used by convention to avoid conflicts with Python keyword, e.g.
#   * `Tkinter.Toplevel(master, class_='ClassName')`

# %% cell_style="split" slideshow={"slide_type": "slide"}
class Underscore:
    def __init__(self, x): 
        self.x = x
        self._x = x ** 2
        self.__x = x ** 3
u = Underscore(10)

# %% cell_style="split"
# on peut lire et écrire x
u.x = 2 * u.x

# on peut lire et écrire _x !
u._x = 2 * u._x

# %%
# mais même pas lire __x
try:       
    u.__x
except AttributeError as e:
    print(f"OOPS {type(e)}: {e}")


# %% [markdown] slideshow={"slide_type": "slide"}
# ### nommage des attributs et underscores

# %% [markdown] slideshow={"slide_type": "slide"}
# * le fait de préfixer les attributs d'une classe
#   * avec un ou deux underscores
# * n'est donc pas très significatif pour le langage
# * mais fait passer aux humains
#   * le message selon lequel
#   * il vaut mieux ne pas y accéder directement

# %% [markdown] slideshow={"slide_type": "slide"}
# ## properties

# %% [markdown] slideshow={"slide_type": ""}
# * on a vu avec la classe Gauge
# * la dualité attribut/méthodes d'accès
#   * un attribut privé
#   * des méthodes pour lire/écrire
# * avec les *properties* on a le beurre et l'argent du beurre
#   * le code utilisateur a l'impression d'accéder directement aux attributs
#   * sauf qu'en fait grâce à la property on peut insérer une couche de logique
#   * pour vérifier le bon usage, exactement comme avec des get/set

# %% [markdown] slideshow={"slide_type": "slide"}
# ### properties *vs* getter/setter

# %% [markdown]
# dans un langage avec protection "dure" comme C++ ou Java:
#
# * on expose très souvent une API à base de `get/set` 

# %% [markdown]
# ce n'est pas du tout le cas en Python:
#
# * on commence avec un attribut 'nu'
# * lorsqu'il faut implémenter des contrôles  
#   on remplace l'attribut par une property
#
# * tout en préservant l'API

# %% [markdown] slideshow={"slide_type": "slide"}
# ### deux formes pour la même construction

# %% [markdown]
# il existe deux syntaxes différentes pour créer une property dans une classe
#
# * **sans décorateur**
#   * on écrit le getter et le setter
#   * l'attribut est créé comme une `property` à partir des deux
# * **avec décorateur**
#   * on définit la property avec le décorateur `@property`   
#     à partir du getter
#   * puis on peut ensuite ajouter le `setter`
#   
# *NB :* dans les deux cas on peut aussi fournir un *deletter*

# %% [markdown] slideshow={"slide_type": "slide"}
# ### syntaxe sans décorateur

# %% slideshow={"slide_type": ""}
# une classe qui implémente une valeur
# garantie de rester entre 0 et 1000

class Constrained:
    """
    Une jauge qui contraint sa valeur dans un intervalle
    """
    def __init__(self, value):
        # on appelle déjà le setter ici
        self.value = value

    # le getter
    def _get_value(self):
        # la vraie valeur est dans l'attribut _value
        return self._value

    # le setter
    def _set_value(self, value):
        # on vérifie la contrainte
        self._value = min(1000, max(0, value))

    # c'est ici qu'on définit la property `value`
    value = property(fget=_get_value, fset=_set_value, 
                     doc="a constrained value between 0 and 1000")


# %% slideshow={"slide_type": "slide"}
c1, c2, c3 = Constrained(-12), Constrained(500), Constrained(2000)
c1.value, c2.value, c3.value

# %% cell_style="center"
# l'API ressemble toujours à une 
# simple utilisation d'attribut
c2.value = 10**6
c2.value


# %% [markdown] slideshow={"slide_type": "slide"}
# ### syntaxe avec décorateur

# %% slideshow={"slide_type": ""}
# pareil avec un décorateur - syntaxe moins agréable IMHO

class ConstrainedDeco:
    """
    Une jauge qui contraint sa valeur dans un intervalle
    """

    def __init__(self, value):
        # on appelle le setter déjà ici
        self.value = value

    # le getter - qui définit la property
    @property
    def value(self):
        """a constrained value between 0 and 1000"""
        return self._value

    # le setter
    @value.setter
    def value(self, value):
        self._value = min(1000, max(0, value))


# %% cell_style="center" slideshow={"slide_type": "slide"}
d1, d2, d3 = ConstrainedDeco(-12), ConstrainedDeco(500), ConstrainedDeco(2000)
d1.value, d2.value, d3.value

# %%
d2.value = 10**6
d2.value

# %% [markdown] slideshow={"slide_type": "slide"}
# ## résumé properties

# %% [markdown] slideshow={"slide_type": ""}
# grâce aux *properties*, on peut
#
# * exposer une API simple  
#   accès direct aux attributs  
#   sans imposer à l'appelant de vilaines périphrases
#
# * en se réservant la possibilité  
#   de créer des getters/setters (et deleters)  
#   ultérieurement si/lorsque nécessaire
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exercice

# %% [markdown] slideshow={"slide_type": ""}
# * écrire une variante de `Constrained` 
# * avec des bornes variables
# * passées au constructeur
#
# ```
# >>> ma_jauge = ConstrainedMinMax(500, min=100, max=200)
# >>> ma_jauge.value
#     200
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## dataclasses

# %% [markdown]
# depuis Python-3.7, ce mécanisme permet 
#
# * de définir plus rapidement
# * une classe comme une simple juxtaposition de données

# %% [markdown]
# par contre
#
# * nécessite les *type hints*
# * et parce que dispo depuis 3.7, encore assez peu répandu

# %% slideshow={"slide_type": "slide"}
from dataclasses import dataclass


# %% cell_style="split"
@dataclass
class Airport:
    airport_id: int
    iata: str
    latitude: float
    longitude: float


# %% cell_style="split"
nice = Airport(5879, "NCE", 7, 43)

# %% cell_style="split"
nice

# %% [markdown] slideshow={"slide_type": "slide"}
# ## résumé encapsulation

# %% [markdown] slideshow={"slide_type": ""}
# * deux techniques pour aider à l'encapsulation
#   * sous-titrer le rôle des attributs de données
#   * utiliser les properies pour contrôler les accès
# * en pratique
#   * Python est un langage pragmatique
#   * on commence presque toujours par la version 'simple'
#   * et on ajoute des properties au besoin par la suite

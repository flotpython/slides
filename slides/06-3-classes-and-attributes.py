# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
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
from plan import plan; plan("classes", "attributs")


# %% [markdown] slideshow={"slide_type": "slide"}
# # POO : encapsulation

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
# ### modularité

# %% [markdown]
# * du code modulaire
#   * grouper le code dans une classe
#   * grouper les données dans un objet
#
# * plus on découpe en petits morceaux
#   * plus on a de chances de pouvoir réutiliser

# %% [markdown] slideshow={"slide_type": "slide"}
# ### réutilisabilité

# %% [markdown]
# * DRY *don't repeat yourself*
#   * chaque fonctionnalité écrite une seule fois
# * maintenance plus simple
# * du code générique
#   * ex: un simulateur fait "avancer" une liste d'objets
#   * dès qu'un objet explique comment il avance
#   * il peut faire partie de la simulation
# * c'est là qu'intervient l'héritage

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### avertissement : POO et langage

# %% [markdown] tags=["level_intermediate"]
# * la POO est présente dans tous les langages modernes
# * cependant l'implémentation *a un impact*
# * sur le paradigme présenté au programmeur
# * se méfier des habitudes héritées d'autres langages

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
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
# * les espaces de nom sont imbriqués (*nested*)
#   * ex. `package.module.classe.methode`
# * permet de lever l'ambigüité en cas d'homonymie
#   * cf. exemple du C *old-school*
# * on peut accéder à tous les objets
#   * dès qu'on sait partir d'une variable
#   * par exemple un module importé
# * l'héritage rend cela dynamique
#   * i.e. la résolution est faite à *runtime*

# %% [markdown] slideshow={"slide_type": "slide"}
# ### espaces de nom - variables et attributs

# %% [markdown] cell_style="split"
# #### deux mondes étanches
#
# * variables
# * attributs

# %% [markdown] cell_style="split"
# #### se mélangent 
#
# apparemment seulement  
# apprenez à bien lire

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
# ## résolution d'attribut

# %% [markdown] slideshow={"slide_type": ""}
# * la **résolution des attributs**
# * fournit la **mécanique de base** de la POO
# * sur laquelle d'ailleurs on a - très peu - élaboré
#   * pour implémenter l'héritage
#   * on verra ça en détails plus tard

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

# %% [markdown] slideshow={"slide_type": "slide"}
# ### digression : l'attribut spécial `__dict__`
#
# * les (objets qui servent d') espaces de nom ont un attribut spécial
# * qui s'appelle `__dict__` 
# * qui permet de voir *en lecture seule* le contenu de l'espace de nom

# %%
import math

'pi' in math.__dict__

# %% [markdown] slideshow={"slide_type": "slide"}
# ### deux espaces de nom (classe et instance) - fin

# %% cell_style="split" slideshow={"slide_type": ""}
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
# (rappel : tous les espaces de nom ont un attribut `__dict__`)

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
# ### exemple avec héritage

# %% [markdown] slideshow={"slide_type": ""}
# * ce n'est pas encore de l'héritage  
#   puisque pour l'instant on n'a qu'une classe
# * mais l'héritage  
#   est une simple prolongation de cette logique

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
# ## **remarque importante** : lecture ≠ écriture

# %% [markdown] slideshow={"slide_type": ""}
# * le mécanisme de recherche d'attribut qu'on vient de voir
# * ne fonctionne que **pour la lecture des attributs**

# %% cell_style="split"
# quand on évalue un attribut en lecture
# on recherche en partant de l'objet
# et donc ici on trouve la méthode 
# qui est un attribut de la classe
subvector.length()

# %% cell_style="split"
# mais quand on écrit un attribut
# c'est une autre histoire complètement
# l'attribut est créé directement dans l'objet
subvector.foo = 12

'foo' in subvector.__dict__


# %% [markdown] slideshow={"slide_type": "slide"}
# ### lecture ≠ écriture - discussion
#
# * mais attention lorsqu'on **écrit** un attribut
#   * *i.e.* si l'expression `foo.bar` est à gauche d'une affectation
# * alors l'attribut `bar` est créé/écrit **dans l'objet `foo`**
# * il n'y a **pas de recherche** dans ce cas !
# * c'est le cas notamment à chaque fois qu'un constructeur fait  
#   `self.name = name`
# * cela ne se remarque pas avec les méthodes
#   * car c'est très rare d'écrire `instance.methode = ...`
# * mais du coup, lire et écrire un attribut ne **sont pas symétriques**

# %% [markdown] slideshow={"slide_type": "slide"}
# ## l'encapsulation

# %% [markdown] cell_style="split"
# * consiste à définir un **ensemble d'opérations**
# * qui sont **les seules à travers lesquelles**  
#   on peut manipule ces objets
# * en préservant de bonnes propriétés / invariants
# * (que idéalement on peut prouver)

# %% [markdown] cell_style="split"
# dans cette section :
#
# * mécanismes permettant (ou pas) de garantir
# * que les objets sont exclusivement manipulés
# * au travers des méthodes et pas autrement

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ### dans d'autres langages
#
# * on trouve des **mécanismes de protection**
# * notamment attributs privés ou publics
# * visant à éviter les erreurs

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ### pas de protection en Python
#
# * tradition  
#   "*we're all consenting adults here*"
# * quelques mécanismes *best-effort*  
#   notamment noms commençant par `_`
# * l'idée reste néanmoins très utile
# * on peut arriver à un résultat convaincant

# %% [markdown] slideshow={"slide_type": "slide"}
# ### dans le code Python "réel"

# %% [markdown] slideshow={"slide_type": ""}
# * très souvent, pas de protection particulière  
#   notamment, **pas de *getter/setter***
# * on expose directement les attributs
# * "we're all consenting adults here"
# * l'idée étant de pouvoir remplacer plus tard, si nécessaire,  
#   l'attribut par une `property` qui fasse les contrôles

# %% cell_style="split" slideshow={"slide_type": "slide"}
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

# on ne devrait pas écrire ceci
gauge = Gauge(0)
gauge.value = -100_000


# %% [markdown] cell_style="split"
# * En C++ / Java typiquement, on définirait ici
#   * un attribut privé `_value`
#   * deux méthodes *getter/setter*
#
# * le code utilisateur accède l'objet
#   * uniquement au travers de ces deux méthodes
#   * qui peuvent faire des contrôles

# %% [markdown] slideshow={"slide_type": "slide"}
# ### deux mécanismes en Python pour l'encapsulation

# %% [markdown] slideshow={"slide_type": ""}
# Mais Python fournit tout de même deux outils très utiles
#
# * conventions de nommage des attributs
# * properties

# %% [markdown] slideshow={"slide_type": "slide"}
# ## conventions de nommage des attributs

# %% [markdown]
# * pas de vraie notion d'attributs privé/public
# * **toutefois** des conventions de nommage, dans la PEP008
#
# en version courte :
#
#
# * les attributs `_*`  
#   correspondent en gros aux membres protégés
# * les attributs `__*` (sans `__` à la fin)  
#   correspondent en gros aux membres privés
# * les attributs `__*__` sont réservés;  
#   on ne doit pas nommer nos propres attributs de cette façon
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *single leading underscore*
#
# * `_single_leading_underscore` :
#   * weak "internal use" indicator.  
#     e.g. `from M import *` does **not import** objects  
#     whose name starts with an underscore.
#   * correspond *en gros* aux champs protégés
#   * **enforcé** seulement pour les **modules**
#   * dans les classes, cela est juste une indication

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *double leading underscore*
#
# * `__double_leading_underscore` :
#   * when naming a class attribute, invokes ***name mangling***  
#     e.g. inside class `FooBar`,  
#     `__boo` becomes `_FooBar__boo`
#
#   * correspond *en gros* aux champs privés

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *double leading and trailing underscore*
#
# * `__double_leading_and_trailing_underscore__`
#   *  "magic" objects or attributes that live in user-controlled namespaces.  
#      e.g. `__init__` , `__import__` or `__file__` .
#   * **never invent such names**; only use them as documented.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *single trailing underscore*
#
# et pour être exhaustif (ne s'applique plus aux attributs)
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


# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### name mangling - illustrated

# %% cell_style="split" tags=["level_intermediate"]
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


# %% cell_style="split" tags=["level_intermediate"]
b = B()
print(b)

# %% cell_style="split" tags=["level_intermediate"]
print(b.__dict__)

# %% cell_style="split" tags=["level_intermediate"]
try:
    b.__a
except Exception as exc:
    print(f"OOPS {type(exc)} {exc}")


# %% [markdown] slideshow={"slide_type": "slide"}
# ## properties

# %% [markdown] slideshow={"slide_type": "slide"}
# ### properties *vs* getter/setter

# %% [markdown] cell_style="split"
# dans un langage avec protection "dure" comme C++ ou Java:
#
# * on expose très souvent une API à base de `get/set`

# %% [markdown] cell_style="split"
# ce n'est pas du tout le cas en Python:
#
# * on commence avec un attribut 'nu'
# * lorsqu'il faut implémenter des contrôles  
#   on remplace l'attribut par une property
#
# * tout en préservant l'API

# %% [markdown] slideshow={"slide_type": "slide"}
# ### la classe `Gauge`
#
# * revenons à notre classe `Gauge`
# * dans un premier temps on publie notre première version très 'à l'arrache`  
#   (aucun contrôle sur la valeur de l'attribut)
# * si ensuite on se rend compte que c'est un problème  
#   (les gens utilisent mal la classe)
# * alors on peut
#   * ajouter des **contrôles sur les accès** à l'attribut
#   * tout en **conservant la même interface**  
#     (c-a-d l'accès direct à l'attribut - pas de get/set)
#   
# * c'est la raison d'être des *properties**
# * le beurre et l'argent du beurre
#   * le code reste simple à lire (pas de get/set)
#   * mais on peut insérer une chouche de logique qui contrôle le bon usage

# %% slideshow={"slide_type": "slide"} cell_style="split"
# avant

#  the value should be 0 <= value <= 100 
class Gauge:
    def __init__(self, value):
        self.value = value
        
gauge = Gauge(1000)
gauge.value


# %% slideshow={"slide_type": ""} cell_style="split"
# après

class Gauge:
    def __init__(self, value):
        self.value = value
        
    # ces deux méthodes sont privées
    def __get_value(self):
        return self._value
    def __set_value(self, new_value):
        self._value = min(100, max(0, new_value))
    value = property(__get_value, __set_value)

# maintenant les accès sont contrôlés    
gauge = Gauge(1000)        
gauge.value


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
# ## résumé

# %% [markdown] slideshow={"slide_type": ""}
# * le mécanisme d'annotation des objets par les attributs  
#   et de recherche le long d'un chemin
#   * constitue le coeur de ce qui est à l'oeuvre  
#     lorsqu'on fait de la Programmation Objet
#
# et 
#
# * deux techniques pour aider à l'encapsulation
#   * "sous-titrer" le rôle des attributs de données  
#     grâce aux conventions de nommage
#   * utiliser les properies pour contrôler les accès
# * en pratique
#   * Python est un langage pragmatique
#   * on commence presque toujours par la version 'simple'
#   * et on ajoute des properties au besoin par la suite

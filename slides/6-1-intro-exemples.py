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
#   nbhosting:
#     title: encapsulation
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# </div>

# %% slideshow={"slide_type": "slide"}
from plan import plan; plan("classes", "exemples")


# %% [markdown] slideshow={"slide_type": "slide"}
# # POO : introduction et exemples

# %% [markdown] slideshow={"slide_type": "slide"}
# ## programmation orientée objet  
#   pourquoi et comment ?

# %% [markdown] cell_style="split"
# ####  deux objectifs
#
# * **réutilisabilité**
# * qui implique **modularité**

# %% [markdown] cell_style="split"
# #### deux moyens
#
# * encapsulation
# * héritage

# %% [markdown] slideshow={"slide_type": "slide"}
# ### pour réutiliser du code en python

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

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# ## `class`
#
# * avec le mot-clé `class` on définit **un nouveau type**
#   * en sus des types prédéfinis `str`, `list`, `set`, `dict`, ...
#   * plus adapté à l'application
# * une classe définit des **méthodes spéciales**  
#   ici **`__init__`** et **`__repr__`**

# %% cell_style="split"
class User:

    # le constructeur
    def __init__(self, name, age):
        # un objet User a deux attributs
        # name et age
        self.name = name
        self.age = age

    # l'afficheur
    def __repr__(self):
        return f"{self.name}, {self.age} ans"


# %% cell_style="split"
# une fois qu'on a défini une classe,
# on peut s'en servir pour créer
# des objets - on dit des instances
# de la classe

user1 = User("Lambert", 25)
user1

# %% [markdown] slideshow={"slide_type": "slide"}
# ## une classe est un type
#
# * comme tous les types, la classe est une **usine à objets**
#   * `user = User("Dupont", 59)`
#   * à rapprocher de `s = set()` ou `n = int('32')`
#
# * chaque objet (on dit instance) contient des données
#   * rangées dans des **attributs** de l'objet
#   * par exemple ici `self.name` est l'attribut `name` de l'objet `self`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## affichage
#
# * la méthode spéciale `__repr__(self)` doit renvoyer une chaine
# * elle est utilisée pour
#   * imprimer l'objet avec `print()`
#   * convertir un objet en chaine

# %% cell_style="split"
print(f"je viens de voir {user1}")

# %% cell_style="split"
str(user1)


# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### affichage et conversion en chaine

# %% [markdown] tags=["level_intermediate"]
# en fait il est possible d'être plus fin, et de définir **deux** méthodes spéciales qui sont
#
# * `__repr__(self)` et
# * `__str__(self)`
#
# cela dit pour commencer on peut se contenter de ne définir que `__repr__()` qui est alors utilisée pour tous les usages

# %% [markdown] slideshow={"slide_type": "slide"}
# ## méthodes

# %% [markdown]
# * une classe peut définir **des méthodes**
# * qui sont des fonctions qui s'appliquent sur un objet (de cette classe)

# %% cell_style="split"
# une implémentation très simple
# d'une file FILO
# premier entré dernier sorti

class Stack:

    def __init__(self):
        self.frames = []

    # le premier entré est
    # affiché à gauche
    def __repr__(self):
        return " > ".join(self.frames)

    def push(self, item):
        self.frames.append(item)

    def pop(self):
        return self.frames.pop()


# %% cell_style="split"
# instance
stack = Stack()

stack.push('fact(3)')
stack.push('fact(2)')
stack.push('fact(1)')

stack

# %% cell_style="split"
stack.pop()

# %% cell_style="split"
stack

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# ## méthodes et paramètres
#
# remarquez qu'ici
#
# * on a défini la méthode `push` avec **2** paramètres
# ```
# def push(self, item):
# ```
#
# * ce qui fait qu'on peut l'appeler sur un objet avec **1** paramètre
# ```
# stack.push(some_item)
# ```
#
# * car le premier paramètre `self` est lié  
#   à **l'objet sur lequel on envoie** la méthode
#
# * et la phrase `stack.push(some_item)`  
#   est en fait équivalente à  
#   `Stack.push(stack, some_item)`

# %% slideshow={"slide_type": "slide"} cell_style="split" tags=["level_intermediate"]
# la preuve
s = Stack()

# la forme habituelle
s.push("premier")

# mais on pourrait aussi écrire ceci
Stack.push(s, "deuxième")

# %% slideshow={"slide_type": "slide"} cell_style="split" tags=["level_intermediate"]
s

# %% slideshow={"slide_type": ""} cell_style="split" tags=["level_intermediate"]
# car la fonction qu'on a
# définie dans la classe,
# c'est celle-ci

Stack.push

# %% [markdown] slideshow={"slide_type": "slide"}
# ## intérêts de cette approche

# %% [markdown] cell_style="center"
# ### encapsulation
#
# * définir vos propres types de données
# * grouper les données qui vont ensemble dans un objet unique, facile à passer à d'autres fonctions
# * invariants: garantir de bonnes propriétés
#   si on utilise les objets au travers des méthodes

# %% [markdown] cell_style="split"
# ### intégrer les objets dans le langage  
#   i.e. donner un sens à des constructions comme
#   * `x in obj`
#   * `obj[x]`
#   * `if obj:`
#   * `for item in obj:`
#   * ...

# %% [markdown] cell_style="split"
# ### héritage
#   * réutiliser une classe en modifiant seulement quelques aspects

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemples

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `np.ndarray`
#
# * le type de données central dans la librairie `numpy`
#   * est **la classe** `numpy.ndarray`
# * en fait il n'y a pas de différence de fond
#   * entre les types prédéfinis (`str`, ...)
#   * et les classes créées avec `class`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `class Point`

# %% slideshow={"slide_type": ""}
import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x:.2f} x {self.y:.2f})"

    def distance(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)


# %% cell_style="split"
a = Point(4, 3)
b = Point(7, 7)
a, b

# %% cell_style="split"
a.distance(b)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `class Circle` (1)

# %% slideshow={"slide_type": ""} tags=[]
class Circle1:

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"[{self.center} ⟷ {self.radius:.2f}]"

    def contains(self, point: Point):
        """
        returns a bool; does point belong in the circle ?
        """
        # attention avec les flottants, == c'est trop fort !
        return math.isclose(self.center.distance(point), self.radius)


# %% cell_style="split"
c1 = Circle1(Point(0, 0), 5)
c1

# %% cell_style="split"
a

# %% cell_style="center"
c1.contains(a)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `class Circle` (2)

# %% slideshow={"slide_type": ""} tags=[]
class Circle2:

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def __repr__(self):
        return f"[{self.center} ⟷ {self.radius:.2f}]"

    # si on transforme cette méthode en méthode spéciale...
    def __contains__(self, point: Point):
        """
        returns a bool; does point belong in the circle ?
        """
        return math.isclose(self.center.distance(point), self.radius)


# %%
c2 = Circle2(Point(0, 0), 5)

# alors on peut faire le même calcul, mais
# l'écrire comme un test d'appartenance habituel 'x in y'
a in c2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : une *dataclass*

# %% [markdown]
# depuis Python-3.7, ce mécanisme permet
#
# * de définir plus rapidement
# * une classe comme une simple juxtaposition de données

# %% [markdown]
# par contre
#
# * nécessite les *type hints*
# * et dispo seulement depuis 3.7

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
# ### exemple : `class datetime.date` etc..
#
# * bien sûr il y a des classes dans la bibliothèque standard
# * voyez par exemple [le module `datetime`](https://docs.python.org/3/library/datetime.html)
# * et notamment `datetime.date` (une date)  
#   et `datetime.timedelta` (une durée)

# %% slideshow={"slide_type": "slide"}
# normalement la classe date aurait dû s'appeler Date
from datetime import date as Date
# pareil
from datetime import timedelta as TimeDelta

# remarquez : pas une méthode usuelle
# (on ne l'envoie pas sur un objet)
Date.today()

# %% cell_style="split"
# une durée
TimeDelta(weeks=2)

# %% cell_style="split" slideshow={"slide_type": ""}
# il y a 3 semaines nous étions le
today = Date.today()
three_weeks = 3 * TimeDelta(weeks=1)

today - three_weeks


# %% tags=[]
# pour la suite:
# une commodité pour afficher une durée
# sous la forme de <..> ans et <..> mois

def timedelta_as_year_month(age: TimeDelta):
    """
    convert a duration in years and months (as a str)
    """
    one_year = TimeDelta(days=365.25)
    one_month = one_year / 12
    years, leftover = age // one_year, age % one_year
    months, leftover = leftover // one_month, leftover % one_month
    return f"{years} ans, {months} mois"


# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `class Student`

# %% tags=[]
class Student:

    def __init__(self, first_name, last_name, 
                 birth_year, birth_month, birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = Date(birth_year, birth_month, birth_day)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    # si on a besoin de faire de l'arithmétique
    def age(self) -> TimeDelta:
        # la différence entre 2 Dates c'est une durée
        return Date.today() - self.birth_date

    def repr_age(self) -> str:
        retourne un 
        return timedelta_as_year_month(self.age())


# %% [markdown] slideshow={"slide_type": "slide"}
# #### `class Student` - utilisation

# %% slideshow={"slide_type": ""}
achille = Student("Achille", "Talon", 2001, 7, 14)
achille

# %% cell_style="split"
achille.age()

# %% cell_style="split"
type(achille.age())

# %% slideshow={"slide_type": ""} cell_style="split"
# pourquoi on a besoin de repr_age()
print(f"{achille} a {achille.age()}")

# %% slideshow={"slide_type": ""} cell_style="split"
# c'est mieux comme ça
print(f"{achille} a {achille.repr_age()}")


# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : class `Class`
#
# (dans le sens: groupe de `Student`s)
#
# * bien sûr on peut combiner nos types (les classes)  
#   avec les types de base
# * et ainsi créer e.g. des listes de `Student`

# %%
class Class:

    # une classe porte un nom et contient une liste d'élèves
    def __init__(self, classname, students):
        self.classname = classname
        self.students = students

    def __repr__(self):
        return f"{self.classname} with {len(self.students)} students"

    def average_age(self):
        # on aimerait pouvoir écrire simplement ceci
        # return ((sum(student.age() for student in self.students)
        #          / len(self.students))
        # mais ça ne fonctionne pas, il faut passer à sum 
        # l'élément neutre de l'addition - ici TimeDelta(0)
        # car '0' ne peut pas s'additionner à un TimeDelta
        return (sum((student.age() for student in self.students), TimeDelta(0)) 
                / len(self.students))


# %% [markdown] slideshow={"slide_type": "slide"}
# #### `class Class` - utilisation

# %%
hilarion = Student("Hilarion", "Lefuneste", 1998, 10, 15)
gaston = Student("Gaston", "Lagaffe", 1995, 2, 28)
haddock = Student("Capitaine", "Haddock", 2000, 1, 14)
tournesol = Student("Professeur", "Tournesol", 1996, 2, 29)

# %%
# attention je ne peux pas utiliser une variable
# qui s'appellerait 'class' car c'est un mot-clé de Python

cls = Class("CIC1A", [achille, hilarion, gaston, haddock, tournesol])
cls

# %%
# la moyenne d'âge de la classe
# sous la forme d'un TimeDelta
# si on voulait faire de l'arithmétique
cls.average_age()

# %%
# la moyenne d'âge de la classe, pour les humains
timedelta_as_year_month(cls.average_age())

# %% [markdown] slideshow={"slide_type": "slide"}
# ### la syntaxe pour l'héritage

# %% slideshow={"slide_type": ""} cell_style="split"
# pour définir une classe qui hérite d'une (ou plusieurs) autres:

class A:
    def __init__(self, x):
        self.x = x
    def method1(self):
        print(f"A.method1 {self.x}")
    def method2(self):
        print(f"A.method2 {self.x}")
    
# la syntaxe pour hériter de A
#      ↓↓↓
class B(A):
    def method2(self):
        print(f"B.method2 {self.x}")


# %% cell_style="split"
# le constructeur est hérité de A
a = A('a')
b = B('b')

# %% cell_style="split"
# method1 est héritée de A
a.method1()
b.method1()

# %% cell_style="split"
# method2 est redéfinie dans B
a.method2()
b.method2()


# %% [markdown] slideshow={"slide_type": "slide"} tags=[]
# ### exemple d'héritage
#
# * si on avait voulu se débarrasser de ce vilain `timedelta_as_year_month`
# * on aurait pu définir une classe `Age` **qui hérite** de `TimeDelta`
#
# * ceci nous fournit un exemple d'héritage tout à fait réaliste
# * c'est pour cela que je conserve l'exemple
# * mais le résultat est d'un abord assez difficile
# * en effet il faut reconnaître que c'est assez scabreux finalement,
# * car la classe `TimeDelta` n'est pas conçue de la manière la plus académique qui soit !

# %% tags=["level_intermediate"] slideshow={"slide_type": "slide"}
# première version de Age

# une classe qui se comporte comme TimeDelta
# sauf pour la présentation
# on veut juste le nombre d'années - mois

class Age(TimeDelta):
    # normalement on redéfinit __init__ mais il se trouve
    # que datetime.timedelta implément __new__
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)
    def __repr__(self):
        one_year = Age(days=365.2425)
        one_month = one_year / 12
        years, leftover = self // one_year, self % one_year
        months, leftover = leftover // one_month, leftover % one_month
        return f"{years} ans, {months} mois"


# %% tags=["level_intermediate"]
# du coup on peut créer une instance 
# avec le constructeur habituel de TimeDelta

Age(weeks=1000)


# %% slideshow={"slide_type": "slide"} tags=["level_advanced"]
# deuxième version de Age

# sauf que, dans le cas de Student, on ne crée pas un TimeDelta
# à base de weeks= ou days=, mais par différence entre deux objets Date

# du coup il nous faut tripoter un peu notre classe Age
# pour qu'on puisse en créer un exemplaire à partir d'un TimeDelta

# %% tags=["level_advanced"] slideshow={"slide_type": ""}
class Age(TimeDelta):
    # là ça tourne un peu à la magie noire
    def __new__(cls, *args, **kwargs):
        # si on nous a passé un argument de type TimeDelta
        if len(args) == 1 and isinstance(args[0], TimeDelta):
            # alors on crée un Age aui a le même nombre de jours
            return super().__new__(cls, days=args[0].days)
        else:
            return super().__new__(cls, *args, **kwargs)
    def __repr__(self):
        one_year = Age(days=365.2425)
        one_month = one_year / 12
        years, leftover = self // one_year, self % one_year
        months, leftover = leftover // one_month, leftover % one_month
        return f"{years} ans, {months} mois"


# %% tags=["level_intermediate"] slideshow={"slide_type": "slide"}
# du coup maintenant on peut utiliser Age 
# dans la classe Student

class Student:

    def __init__(self, first_name, last_name, 
                 birth_year, birth_month, birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = Date(birth_year, birth_month, birth_day)

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

    def age(self):
        """
        retourne un TimeDelta
        """
        # la différence entre 2 Dates c'est une durée
        return Age(Date.today() - self.birth_date)

    # et on n'a plus besoin de ceci
    # def repr_age(self):


# %% tags=["level_intermediate"]
hilarion = Student("Hilarion", "Lefuneste", 1998, 10, 15)
hilarion.age()


# %% [markdown] slideshow={"slide_type": "slide"}
# ## autre cas d'usage : le graphe
#
# ### version v0 : avec seulement les fonctions
#
# * utiliser une structure de données 'matrice'
# * mais la matrice ne contient pas les noms des sommets
#   * étendre en demandant les noms des sommets

# %% slideshow={"slide_type": "slide"}
### la librairie

def draw_graph(matrix, names):
    # ici on utilise le paramètre 'matrix'
    ...

def shortest_distance(matrix, names, name1, name2):
    ...


# %%
### le code utilisateur

matrix = [[0, 1, 0], [1, 0, 0], [0, 1, 0]]
names = ['a', 'b', 'c']

draw_graph(matrix, names)

shortest_distance(matrix, names, 'a', 'b')


# %% [markdown] slideshow={"slide_type": "slide"}
# ### avec une classe : v1
#
# on introduit la classe `Graph`

# %% cell_style="split"
class Graph:
    def __init__(self, matrix, names):
        self.matrix = matrix
        self.names = names

    # on n'a plus besoin de dire draw_graph()
    def draw(self):
        # ici on utilise 'self.matrix'
        ...

    def shortest_distance(self, name1, name2):
        ...


# %% cell_style="split"
# avec ce modèle le code utilisateur devient

g = Graph(matrix, names)

g.draw()
g.shortest_distance('a', 'b')

# %% [markdown]
# **avantages**
#
# * la matrice et les noms, en fait ça forme un tout; les noms sont relatifs aux sommets dans l'ordre de la matrice; si on change l'ordre des noms, il faut permuter les indices dans la matrice
# * du coup, un graphe est modélisé par **les deux données**; c'est quand même logique d'avoir envie de les regrouper dans *un truc*
# * ce truc, c'est **l'instance**; on peut maintenant créer ***un objet***, et le passer
#   **comme unique paramètre** à toutes nos fonctions

# %% [markdown] slideshow={"slide_type": "slide"}
# ### avec une classe : v2
#
# maintenant, la structure matricielle n'est pas forcément toujours idéale (cf. par exemple adjacences)
#
# pour rendre le **code client** totalement **indépendant** de la structure de données interne (on dit l'*implémentation*) qu'utiliseront les algos de graphe
#
# on change d'approche complètement

# %% cell_style="split"
from collections import defaultdict

class Graph:
    def __init__(self):
        self.adjacencies = defaultdict(dict)

    def add_link(self, s1, s2, distance):
        self.adjacencies[s1][s2] = distance

    def shortest_distance(self, s1, s2):
        ...
    def draw(self):
        ...


# %% cell_style="split"
# et maintenant on l'utilise comme ceci

g = Graph()
g.add_link('a', 'b', 1)
g.add_link('b', 'c', 1)
g.add_link('c', 'a', 1)

g.draw()


# %% [markdown] slideshow={"slide_type": "slide"}
# **avantages**
#
# * bien meilleur niveau d'abstraction:
#   * le code utilisateur ne dépend plus de l'implémentation
#   * la classe `Graph` peut choisir de travailler avec une matrice,
#     ou avec des listes d'adjacences, ou même les deux au choix en fonction de l'algorithme
# * du coup le code est **plus réutilisable**

# %% [markdown] slideshow={"slide_type": "slide"}
# ### avec une classe : v3
#
# maintenant on veut permettre la configuration de `draw()`
#
# * 1-ère idée : on ajoute des paramètres à `draw()`
#
#         def draw(self, line_width):
#             ...

# %% [markdown]
# inconvénients :
# * il faut changer tous les appels à `draw()` <br>
#   (ou au moins mettre un défaut pour `line_width`)
# * mais surtout il faut prévoir en fait une vingtaine de paramètres <br>
#   traits, coulaurs, fontes, ...
# * beaucoup plus habile :
#   * créer une classe *GraphicContext* qui contient tous ce genre de détails
#   * associer à un objet graphe, par exemple deux contextes graphiques (pour les noeuds et les sommets)

# %% slideshow={"slide_type": "slide"}
class GraphicContext:
    def __init__(self, *,
                 line_width=None, line_color=None,
                 font=None, font_size=None):
        self.line_width = line_width or 1
        self.line_color = line_color or 'white'
        ...

    )

class Graph:
    def __init__(self, vertex_gc=None, edge_gc=None):
        self.adjacencies = defaultdict(dict)
        self.vertex_gc = vertex_gc or GraphicContext()
        self.edge_gc = edge_gc or GraphicContext()

    def draw(self):
        ...


# %%

g = Graph(edge_gc = GraphicContext(line_color='red'))
g.add_link('a', 'b')
g.add_link('b', 'c')
g.add_link('c', 'a')

g.draw()
# %% [markdown] slideshow={"slide_type": "slide"}
# ### avec une classe : v4
#
# l'étape suivante, ce serait de se dire, mais pourquoi est-ce qu'on limiterait les sommets à être des chaines ?
#
# du coup on peut envisager définir deux classes `Graph` et `Node`
#
# ce qui permet de personnaliser davantage les données associées à un noeud, etc..

# %% [markdown] slideshow={"slide_type": "slide"}
# ## attributs et espaces de  nom

# %% [markdown]
# * la classe et l'instance se comportent chacune **comme un espace de nom**
# * la notion d'**attribut** est centrale
#   * les attributs d'instance: pour préserver l'état dans un objet
#   * les attributs de classe: pour ranger les méthodes
# * remarque :   
#   la notion d'attribut est la même que pour les modules (et packages donc)

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
# * est entièrement **lexicale**
# * en remontant dans le code
# * avec les règles LEGB  
#   local, englobant, global, *builtin*

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ##### résolution des **attributs**
#
# * dans le monde des **objets**
# * en remontant dans les **espaces de nom**
# * essentiellement **dynamique**  
#   *i.e.* à *runtime*

# %% [markdown] slideshow={"slide_type": "slide"}
# ## résumé (1/2)
#
# * avec `class` on peut définir un **nouveau type**
#   * qui nous permet de **créer des objets**
#   * qui représentent mieux que les types de base les données de notre application
#
# * pas de différence entre un type prédéfini et une classe :  
#   un objet créé par une classe s'utilise *normalement*
#   * une variable peut désigner un objet
#   * un objet peut être dans une liste (ou autre type) *builtin*  
#     (attention pour les clés de `dict` qui doivent être immutables)
#   * ou passé en paramètre à une fonction,
#   * etc, etc...

# %% [markdown] slideshow={"slide_type": "slide"}
# ### résumé (2/2)
#
# * une classe peut définir des **méthodes**
#   * qui travaillent sur un objet (souvent appelé `self`)
#   * souvent on ne modifie les objets  
#     qu'au travers des méthodes fournies par la classe
#   * ce qui permet de garantir certains invariants

# %% [markdown] slideshow={"slide_type": "slide"}
# ## du bon usage de Python ?

# %% [markdown] slideshow={"slide_type": "slide"}
# ### modules ou classes ?

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
# ### POO : avec ou sans héritage ?

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
# ### POO : héritage *vs* composition 

# %% [markdown]
# #### exemples de conception avec héritage

# %% [markdown]
# **gestion de ressources humaines**
#
# * classe de base : `Salarié`
# * chaque catégorie de personnel  
#   donne lieu à une sous-classe
#
# * correspond à la notion   
#   d'inclusion dans les ensembles

# %% [markdown] slideshow={"slide_type": "slide"}
# **chaque sous-classe peut**
#
# * hériter une méthode telle quelle
#   * il suffit de ne pas la redéfinir
#   * ex. `imprimer_paie()`
# * (re)définir complètement une méthode
#   * ex. `evolution_carriere()`
# * amender le comportement générique
#   * redéfissant sa propre méthode
#   * qui appelle la méthode de `Salarié`
#   * ex. `calcul_revenu()`
#   * peut ajouter un appel à `bonus()`

# %% [markdown] slideshow={"slide_type": "slide"}
# #### exemples de conception avec composition

# %% [markdown]
# **les interfaces graphiques**
#
# * classes de base
#   * ascenseur de défilement
#   * cadre
#   * titre
# * une fenêtre va être **composée** des trois classes de base
# * une interface graphique va être **composée** de fenêtres

# %% [markdown] slideshow={"slide_type": "slide"}
# #### héritage *vs* composition

# %% [markdown] cell_style="center"
# * héritage:
#
# ```python
# class Circle(Graphic):
#     def __init__(self, graphic_context = None):
#         Graphic.__init__(self, graphic_context)
# ```

# %% [markdown] cell_style="center"
# * composition:
#
# ```python
# class Truck:
#    def __init__(self, wheel_diameter):
#        self.wheel = Wheel(wheel_diameter)
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# #### héritage *vs* composition - suite
#
# * ce n'est pas parce que un `Truck` a exactement un `Wheel`
# * qu'un camion est un volant
# * en cas de doute, posez vous la question
#   * est-ce que l'objet X **est** un objet Y
#   * ou est-ce qu'il **possède** ou **contient** un objet Y

# %% [markdown] slideshow={"slide_type": "slide"}
# #### héritage - discussion

# %% [markdown] slideshow={"slide_type": ""}
# * imaginez que vous avez une classe `Vecteur2D`
# * vous avez besoin d'une classe `Vecteur3D`
# * on pourrait se dire
#   * `Vecteur3D` hérite de `Vecteur2D`
#   * et lui ajoute un champ `z`
# * c'est une **très mauvaise idée**
#   * l'ensemble des vecteurs 3D
#   * n'est pas inclus dans l'ensemble des vecteurs 2D
#   * c'est exactement  le contraire !

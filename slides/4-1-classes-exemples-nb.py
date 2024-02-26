# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted,-editable
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: classes et objets
#   rise:
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # classes : exemples

# %% [markdown] slideshow={"slide_type": ""}
# les classes servent à définir **de nouveau types**  
#
# * en sus des types prédéfinis `str`, `list`, `set`, `dict`, ...
# * plus adaptés à l'application
#

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# ## `class` 
#
# * avec le mot-clé `class` on définit **un nouveau type**  
# * une classe définit des **méthodes spéciales**; ici **`__init__`** et **`__repr__`**

# %% tags=["gridwidth-1-2"]
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

# %% tags=["gridwidth-1-2"]
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
# * chaque objet (on dit instance) contient des données 
#   * rangées dans des **attributs** de l'objet
#   * ici `name` et `age`

# %% [markdown] tags=[]
# ## affichage
#
# * la méthode spéciale `__repr__(self)` doit renvoyer une chaine  
# * elle est utilisée pour
#   * imprimer l'objet avec `print()`
#   * convertir un objet en chaine
#
# ````{admonition} si on ne définit pas __repr__
# :class: dropdown
#
# alors on obtient ceci
#
# ```{image} media/class-without-repr.png
# :width: 500px
# ```
# ````

# %% cell_style="center" tags=["gridwidth-1-2"]
print(f"je viens de voir {user1}")

# %% cell_style="center" tags=["gridwidth-1-2"]
str(user1)


# %% [markdown] tags=[]
# ````{admonition} deux méthodes spéciales pour l'affichage
# :class: attention dropdown
#
# en fait il est possible d'être plus fin, et de définir **deux** méthodes spéciales, qui sont
#
# * `__repr__(self)` - utilisée par exemple pour `print`
# * `__str__(self)`  - utilisée par exemple pour `str`
#
# cela dit, pour commencer on peut se contenter de définir seulement `__repr__()`, qui est alors utilisée pour tous les usages
# ````

# %% [markdown]
# ## méthodes
#
# * une classe peut définir **des méthodes**
# * qui sont des fonctions qui s'appliquent sur un objet (de cette classe)

# %% tags=["gridwidth-1-2"]
# une implémentation très simple
# d'une file FILO
# premier entré dernier sorti

class Stack:

    ## méthodes spéciales
    def __init__(self):
        self._frames = [] 
        
    def __repr__(self):
        return " > ".join(self._frames)            

    ## méthodes (usuelles)
    def push(self, item):
        self._frames.append(item)
        
    def pop(self):
        return self._frames.pop()


# %% tags=["gridwidth-1-2"]
# instance
stack = Stack()

stack.push('fact(3)')
stack.push('fact(2)')
stack.push('fact(1)')

stack

# %% tags=["gridwidth-1-2"]
stack.pop()

# %% tags=["gridwidth-1-2"]
stack

# %% [markdown] cell_style="center" slideshow={"slide_type": ""}
# ## méthodes et paramètres
#
# remarquez qu'ici 
#
# * on a **défini** la méthode `push` avec **2 paramètres** `def push(self, item):`
# * ce qui fait qu'on peut l'**appeler** sur un objet avec **1 paramètre** `stack.push(some_item)`
# * car le premier paramètre `self` est lié à **l'objet sur lequel on envoie** la méthode
# * et la phrase `stack.push(some_item)` est en fait équivalente à `Stack.push(stack, some_item)`

# %% [markdown] tags=[]
# ## intérêts de cette approche
#
# * définir vos propres types de données
# * grouper les données qui vont ensemble dans un objet unique, facile à passer à d'autres fonctions
# * **invariants**: garantir de bonnes propriétés si on utilise les objets au travers des méthodes (encapsulation)
# * et aussi (sera vu ultérieurement): intégrer **vos objets dans le langage**  
#   i.e. donner un sens à des constructions comme  
#   * `x in obj`
#   * `obj[x]`
#   * `if obj:`
#   * `for item in obj:`
#   * ...
# * enfin **héritage**: réutiliser une classe en modifiant seulement quelques aspects

# %% [markdown]
# ## méthodes et encapsulation
#
# avec la `Stack`, on est censé utiliser **seulement** `stack.push()` et `stack.pop()`  
# et **pas directement** `stack._frames` (d'où le `_` au début de l'attribut)
#
# cette technique permet de séparer :
#
# * l'**interface** (ici `push()` et `pop()`)
# * de l'**implémentation** (ici une liste pour `_frames`)
#
# de façon à pouvoir changer l'implémentation **sans changer l'interface**  
# et ainsi e.g. améliorer le comportement **sans changer le code utilisateur**
#
# ````{admonition} conventions de nommage
# :class: attention admonition-small
# cette séparation n'est pas toujours sous-titrée de manière explicite - comme ici où nous avons mis un `_` au début du nom de l'attribut  
# il faut parfois faire appel à son bon sens
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemples de classes

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `np.ndarray`
#
# * la classe de base de `numpy`: c'est une classe que vous utilisez tous les jours !
# * en fait il n'y a pas de différence de fond 
#   * entre les types prédéfinis (`str`, ...)
#   * et les classes créées avec `class`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `class Point`

# %% slideshow={"slide_type": ""} tags=[]
import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x:.2f} x {self.y:.2f})"
    
    def distance(self, other):
        return math.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)


# %% tags=["gridwidth-1-2"]
# on crée deux instances

a = Point(4, 3)
b = Point(7, 7)
a, b

# %% tags=["gridwidth-1-2"]
# on appelle la méthode distance

a.distance(b)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `class Circle` (1)

# %% slideshow={"slide_type": ""} tags=[]
class Circle1:

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius
        
    def __repr__(self):
        return f"[Circle: {self.center} ⟷ {self.radius:.2f}]"
    
    def contains(self, point: Point):
        """
        returns a bool; does point belong in the circle ?
        """
        print(self.center.distance(point))
        return math.isclose(self.center.distance(point), self.radius)


# %% tags=["gridwidth-1-2"]
c1 = Circle1(Point(0, 0), 5)
c1

# %% tags=["gridwidth-1-2"]
c1.contains(a)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `class Circle` (2)
#
# la même chose exactement, mais en utilisant une méthode spéciale

# %% slideshow={"slide_type": ""}
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
        print(self.center.distance(point))
        return math.isclose(self.center.distance(point), self.radius)


# %% tags=["gridwidth-1-2"]
c2 = Circle2(Point(0, 0), 5)

# alors on peut faire le même calcul, mais
# l'écrire comme un test d'appartenance habituel 'x in y'
a in c2

# %% tags=["gridwidth-1-2"]
# techniquement, on a aussi le droit d'écrire ceci
# mais IL NE FAUT PAS LE FAIRE ce n'est pas du tout l'esprit..

c2.__contains__(a)

# %% [markdown]
# ### exemple : `class datetime.date` etc..
#
# * bien sûr il y a des classes dans la bibliothèque standard
# * voyez par exemple [le module `datetime`](https://docs.python.org/3/library/datetime.html)
# * et notamment `datetime.date` (une date)  
#   et `datetime.timedelta` (une durée)

# %% slideshow={"slide_type": "slide"}
# normalement si on avait appliqué la PEP008 à l'époque,
# la classe date aurait dû s'appeler Date
from datetime import date as Date
# pareil
from datetime import timedelta as TimeDelta

Date.today()

# %% tags=["gridwidth-1-2"]
# ici je crée un objet 'durée' 

TimeDelta(weeks=2)

# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
# et je peux faire de l'arithmétique; par exemple:

today = Date.today()

# multiplier une durée
three_weeks = 3 * TimeDelta(weeks=1)

# ajouter ou retrancher une durée à une date
# il y a 3 semaines nous étions le
today - three_weeks


# %%
# pour afficher une durée avec un format qui nous convient
def timedelta_as_year_month(age: TimeDelta) -> str:
    """
    convert a duration in years and months (as a str)
    """
    year = TimeDelta(days=365.2425)
    years, leftover = age // year, age % year
    month = year/12
    months, leftover = leftover // month, leftover % month
    return f"{years} ans, {months} mois"


# %% [markdown] tags=[]
# ````{admonition} si on allait jusqu'au bout de la logique
# :class: dropdown
#
# en pratique on irait même jusqu'à spécialiser `TimeDelta`, de façon à redéfinir son `repr()` avec ce format  
# toutefois c'est un peu scabreux à faire...
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `class Student`

# %%
# une classe plus orientée "gestion"
# i.e. juste une collection de données

class Student:
    
    def __init__(self, first_name, last_name, 
                 birth_year, birth_month, birth_day):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = Date(birth_year, birth_month, birth_day)
        
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    
    def age(self) -> TimeDelta:
        # the différence between 2 Dates is a TimeDelta
        return Date.today() - self.birth_date
    
    def repr_age(self) -> str:
        return timedelta_as_year_month(self.age())


# %% [markdown]
# ````{admonition} remarque
# :class: admonition-small
#
# on rencontre assez souvent le pattern selon lequel le constructeur a autant de paramètres que les attributs de la classe;  
# par exemple la classe a 2 attributs truc et bidule, et le constructeur qui accepte deux paramètres truc et bidule  
#
# mais comme le montre l'exemple ci-dessus, ce n'est pas obligatoire !
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `class Student` - utilisation

# %% slideshow={"slide_type": ""}
achille = Student("Achille", "Talon", 2001, 7, 14)
achille

# %% tags=["gridwidth-1-2"]
achille.age()

# %% tags=["gridwidth-1-2"]
type(achille.age())

# %% slideshow={"slide_type": ""}
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

# attention je ne peux pas utiliser une variable 
# qui s'appellerait 'class' car c'est un mot-clé de Python

cls = Class("CIC1A", [achille, hilarion, gaston, haddock, tournesol])
cls

# %%
# la moyenne d'âge de la classe
cls.average_age()

# %%
# la moyenne d'âge de la classe, pour les humains
timedelta_as_year_month(cls.average_age())

# %% [markdown] slideshow={"slide_type": "slide"}
# ## résumé (1/2)
#
# * avec `class` on peut définir un **nouveau type** 
#   * qui nous permet de **créer des objets**
#   * qui représentent, mieux que les types de base,  
#     les données de notre application
# * pas de différence entre un type prédéfini et une classe :  
#   un objet créé par une classe s'utilise *normalement*
#   * une variable peut désigner un objet
#   * un objet peut être dans une liste (ou autre type) *builtin*  
#     (attention pour les clés de `dict` qui doivent être hashables)
#   * ou passé en paramètre à une fonction,
#   * etc, etc...

# %% [markdown] slideshow={"slide_type": "slide"}
# ## résumé (2/2)
#   
# * généralement une instance contient  
#   des données rangées dans des **attributs**
# * une classe peut définir aussi des **méthodes**
#   * qui travaillent sur un objet (souvent appelé `self`)
#   * souvent on ne modifie les objets  
#     qu'au travers des méthodes fournies par la classe
#   * ce qui permet de garantir certains invariants
#

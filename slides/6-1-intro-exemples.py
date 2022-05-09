# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version, -language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode, -language_info.file_extension, -language_info.mimetype,
#       -toc
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
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# <span><img src="media/inria-25-alpha.png" /></span>
# </div>

# %% [markdown] slideshow={"slide_type": ""}
# # classes : exemples

# %% [markdown] slideshow={"slide_type": ""}
# les classes servent à définir **de nouveau types**  
#
# * en sus des types prédéfinis `str`, `list`, `set`, `dict`, ...
# * plus adaptés à l'application
#
# <div class="note">cette section contient surtout des rappels    
# </div>    

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# ## `class` 
#
# * avec le mot-clé `class` on définit **un nouveau type**  
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
#   * ici `name` et `age`

# %% [markdown] slideshow={"slide_type": "slide"} cell_style="split"
# ## affichage
#
# * la méthode spéciale `__repr__(self)` doit renvoyer une chaine  
# * elle est utilisée pour
#   * imprimer l'objet avec `print()`
#   * convertir un objet en chaine

# %% [markdown] cell_style="split"
# sans quoi on obtient ceci
#
# <img src="media/class-without-repr.png"
#      width=500px>

# %% cell_style="center"
print(f"je viens de voir {user1}")

# %% cell_style="center"
str(user1)


# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### affichage et conversion en chaine

# %% [markdown] tags=["level_intermediate"]
# en fait il est possible d'être plus fin, et de définir **deux** méthodes spéciales qui sont
#
# * `__repr__(self)` et
# * `__str__(self)` 
#
# cela dit, pour commencer on peut se contenter  
# de définir seulement `__repr__()`   
# qui est alors utilisée pour tous les usages

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
        self._frames = [] 
        
    def __repr__(self):
        return " > ".join(self._frames)            
    
    def push(self, item):
        self._frames.append(item)
        
    def pop(self):
        return self._frames.pop()


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

# %% [markdown] cell_style="center" slideshow={"slide_type": ""}
# remarquez qu'ici 
#
# * on a **défini** la méthode `push` avec **2 paramètres**  
# ```
# def push(self, item):
# ```
#
# * ce qui fait qu'on peut l'**appeler** sur un objet avec **1 paramètre** 
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

# %% [markdown] slideshow={"slide_type": "slide"}
# ## intérêts de cette approche

# %% [markdown]
# * définir vos propres types de données
# * grouper les données qui vont ensemble dans un  
#   objet unique, facile à passer à d'autres fonctions
# * **invariants**: garantir de bonnes propriétés  
#   si on utilise les objets au travers des méthodes 

# %% [markdown]
# <div class="note">et aussi (sera vu ultérieurement) :</div>

# %% [markdown] cell_style="split"
# <div class="note">
#
# * intégrer les objets dans le langage  
#   i.e. donner un sens à des constructions comme  
#   * `x in obj`
#   * `obj[x]`
#   * `if obj:`
#   * `for item in obj:`
#   * ...
#     
#  </div>

# %% [markdown] cell_style="split"
# <div class="note">
#    
# * héritage 
#   * réutiliser une classe en modifiant  
#     seulement quelques aspects
#     
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## méthodes et encapsulation

# %% [markdown]
# avec la `Stack`, on est censé utiliser **seulement** `stack.push()` et `stack.pop()`  
# et **pas directement** `stack._frames` (d'où le `_` au début de l'attribut)
#
# cette technique permet de séparer :
# * l'**interface** (ici `push()` et `pop()`)
# * de l'**implémentation** (ici une liste pour `_frames`)
#
# de façon à pouvoir changer l'implémentation **sans changer l'interface**  
# et ainsi e.g. améliorer le comportement **sans changer le code utilisateur**

# %% [markdown]
# <div class=note>
#
# cette séparation n'est pas toujours sous-titrée de manière explicite   
# comme ici où nous avons mis un `_` au début du nom de l'attribut  
# il faut parfois faire appel à son bon sens
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemples de classes

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `np.ndarray`
#
# * c'est une classe que vous utilisez tous les jours !
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

# %% slideshow={"slide_type": ""}
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


# %% cell_style="split"
c1 = Circle1(Point(0, 0), 5)
c1

# %% cell_style="split"
c1.contains(a)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `class Circle` (2)

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


# %%
c2 = Circle2(Point(0, 0), 5)

# alors on peut faire le même calcul, mais
# l'écrire comme un test d'appartenance habituel 'x in y'
a in c2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `class datetime.date` etc..

# %% [markdown]
# * bien sûr il y a des classes dans la bibliothèque standard
# * voyez par exemple [le module `datetime`](https://docs.python.org/3/library/datetime.html)
# * et notamment `datetime.date` (une date)  
#   et `datetime.timedelta` (une durée)

# %% slideshow={"slide_type": "slide"}
# normalement la classe date aurait dû s'appeler Date
from datetime import date as Date
# pareil
from datetime import timedelta as TimeDelta

Date.today()

# %% cell_style="split"
TimeDelta(weeks=2)

# %% cell_style="split" slideshow={"slide_type": ""}
# il y a 3 semaines nous étions le
today = Date.today()
three_weeks = 3 * TimeDelta(weeks=1)

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


# %% [markdown] tags=["level_advanced"]
# <div class=note>
#
# en pratique on irait même jusqu'à spécialiser `TimeDelta`  
# de façon à redéfinir son `repr()` avec ce format `year+month`  
# toutefois c'est un peu scabreux à faire...
#    
#     
# </div>    

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple : `class Student`

# %%
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


# %% [markdown] slideshow={"slide_type": "slide"}
# #### `class Student` - utilisation

# %% slideshow={"slide_type": ""}
achille = Student("Achille", "Talon", 2001, 7, 14)
achille

# %% cell_style="split"
achille.age()

# %% cell_style="split"
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
#   
# * pas de différence entre un type prédéfini et une classe :  
#   un objet créé par une classe s'utilise *normalement*
#   * une variable peut désigner un objet
#   * un objet peut être dans une liste (ou autre type) *builtin*  
#     (attention pour les clés de `dict` qui doivent être hashables)
#   * ou passé en paramètre à une fonction,
#   * etc, etc...

# %% [markdown] slideshow={"slide_type": "slide"}
# ### résumé (2/2)
#   
# * généralement une instance contient  
#   des données rangées dans des **attributs**
# * une classe peut définir aussi des **méthodes**
#   * qui travaillent sur un objet (souvent appelé `self`)
#   * souvent on ne modifie les objets  
#     qu'au travers des méthodes fournies par la classe
#   * ce qui permet de garantir certains invariants
#

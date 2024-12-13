# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
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
#     title: dunder methods
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # classes : méthodes spéciales
#
# aussi appelées *dunder methods*

# %% [markdown] slideshow={"slide_type": "slide"}
# ## méthodes spéciales / *dunder methods*
#
# * sur une classe on peut définir des **méthodes spéciales**  
# * pour bien intégrer les objets dans le langage  
# * c'est-à-dire donner du sens à des constructions du langage
#
# c'est-à-dire donner un sens à des phrases commme:
#
# * appeler les fonctions *builtin*: `len(obj)`, `int(obj)`
# * opérateurs: e.g. `obj + x`  
# * itération: `for item in obj`
# * test d'appartenance: `x in obj` 
# * indexation: `obj[x]` 
# * et même appel! `obj(x)`
# * etc...

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `len(obj)`

# %% tags=["gridwidth-1-2"]
class Classe:
    
    def __init__(self, students):
        self.students = students
        
    def __len__(self):
        return len(self.students)


# %% tags=["gridwidth-1-2"]
classe = Classe(['jean', 'laurent', 'benoit'])

len(classe)


# %% [markdown]
# de manière similaire : 
#
# * `__int__(self)` pour redéfinir `int(obj)` et similaires

# %% [markdown] slideshow={"slide_type": "slide"}
# ## opérateurs: `obj1 + obj2`

# %% tags=["gridwidth-1-2"]
class Classe:
    
    def __init__(self, students):
        self.students = students
        
    def __add__(self, other):
        return Classe(self.students + other.students)
    
    def __repr__(self):
        return f"[{len(self.students)} students]"


# %% tags=["gridwidth-1-2"]
classe1 = Classe(['marie', 'claire'])
classe2 = Classe(['jean', 'laurent'])

classe1 + classe2


# %% [markdown]
# ````{admonition} en réalité c'est un peu plus subtil
# :class: admonition-small dropdown
#
# dans la pratique, on peut aussi avoir à définir `__radd__` de façon à redéfinir le cas où on pourrait s'additionner avec des objets d'un autre type, comme des types *builtin* de nombres par exemple; mais ne nous égarons pas..
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ## itérations: `for item in obj:`

# %% tags=[]
class Classe:

    def __init__(self, students):
        self.students = students

    def __iter__(self):
        """
        iterate on self as if it was self.students
        """
        return iter(self.students)


# %% tags=["gridwidth-1-2"]
classe = Classe(['jean', 'laurent', 'benoit'])

for s in classe:
    print(s)

# %% tags=["gridwidth-1-2"]
# et même d'ailleurs
x, y, z = classe
y


# %% [markdown]
# ````{admonition} utiliser un générateur
# :class: admonition-small
#
# lorsque la logique d'itération devient moins triviale que de simplement "sous-traiter" le travail à un autre objet, on utilise fréquemment un générateur pour implémenter la *dunder* `__iter__`  
# ici par exemple on aurait pu écrire
# ```python
#     def __iter__(self):
#         for s in self.students:
#             yield s
# ```
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ## appartenance: `x in obj`
#
# on l'a vu déjà avec la classe `Circle`:

# %% tags=["gridwidth-1-2"]
class Classe:

    def __init__(self, students):
        self.students = students

    def __contains__(self, student):
        return student in self.students


# %% tags=["gridwidth-1-2"]
classe = Classe(['jean', 'laurent', 'benoit'])

'jean' in classe


# %% [markdown] slideshow={"slide_type": "slide"}
# ## indexations: `obj[x]`

# %% tags=["gridwidth-1-2"]
class Classe:

    def __init__(self, students):
        self.students = students

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.students[index]
        elif isinstance(index, str):
            if index in self.students:
                return index
            else:
                return None


# %% tags=["gridwidth-1-2"]
classe = Classe(['jean', 'laurent', 'benoit'])

classe[1]

# %% tags=["gridwidth-1-2"]
classe['jean']

# %% tags=["gridwidth-1-2"]
classe['pierre'] is None


# %% [markdown] slideshow={"slide_type": "slide"}
# ## appel: `obj(x)`
#
# on peut même donner du sens à `obj(x)`

# %% tags=["gridwidth-1-2"]
class Line:
    """
    the line of equation
    y = ax + b
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __call__(self, x):
        """
        can be used as function that
        computes y = ax+b given x
        """
        return self.a * x + self.b


# %% tags=["gridwidth-1-2"]
# cet objet se comporte
# comme une fonction

line = Line(2, 2)


# c'est intéressant de pouvoir l'appeler
# comme si c'était une fonction

line(1)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## résumé
#   
# une classe peut définir des **méthodes spéciales**
#
# * notamment le constructeur pour l'initialisation,
# * souvent un afficheur pour `print()`
# * optionnellement d'autres pour donner du sens à des constructions du langage sur ces objets
# * ces méthodes ont toutes un nom en `__truc__` (*dunder methods*)

# %% [markdown] slideshow={"slide_type": "slide"} tags=[]
# ## pour en savoir plus
#
# la (longue) liste exhaustive des méthodes spéciales est donnée dans la documentation officielle ici
#
# <https://docs.python.org/3/reference/datamodel.html#special-method-names>

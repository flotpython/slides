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
#     title: dunder methods
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
# e.g. que peuvent vouloir dire :
#
# * avec les fonctions *builtin*, e.g. `len(obj)`, `int(obj)`
# * opérateurs comme `obj + x`  
# * itération `for item in obj`
# * test d'appartenance `x in obj` 
# * indexation `obj[x]` 
# * même appel! `obj(x)`
# * etc...

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `len(obj)`

# %% cell_style="split"
class Classe:
    
    def __init__(self, students):
        self.students = students
        
    def __len__(self):
        return len(self.students)


# %% cell_style="split"
classe = Classe(['jean', 'laurent', 'benoit'])

len(classe)


# %% [markdown]
# de manière similaire : 
# * `__int__(self)` pour redéfinir `int(obj)` et similaires

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `bool(obj)`

# %% cell_style="split"
class Classe:
    
    def __init__(self, students: list):
        self.students = students
        
    def __bool__(self):
        return self.students != []


# %% cell_style="split"
classe1 = Classe([])
classe2 = Classe(['jean', 'laurent', 'benoit'])

if not classe1:
    print("classe1 est fausse")
if classe2:
    print("classe2 est vraie")


# %% [markdown] slideshow={"slide_type": "slide"}
# ## opérateurs: `obj1 + obj2`

# %% cell_style="split"
class Classe:
    
    def __init__(self, students):
        self.students = students
        
    def __add__(self, other):
        return Classe(self.students + other.students)
    
    def __repr__(self):
        return f"[{len(self.students)} students]"


# %% cell_style="split"
classe1 = Classe(['marie', 'claire'])
classe2 = Classe(['jean', 'laurent'])

classe1 + classe2


# %% [markdown] slideshow={"slide_type": "slide"}
# ## itérations: `for item in obj:`

# %% cell_style="split"
class Classe:

    def __init__(self, students):
        self.students = students

    def __iter__(self):
        """
        iterate on self as if it was self.students
        """
        return iter(self.students)


# %% cell_style="split"
classe = Classe(['jean', 'laurent', 'benoit'])

for s in classe:
    print(s)

# %% cell_style="split"
# et même d'ailleurs
x, y, z = classe
y


# %% [markdown] slideshow={"slide_type": "slide"}
# ## appartenance: `x in obj`

# %% cell_style="split"
class Classe:

    def __init__(self, students):
        self.students = students

    def __contains__(self, student):
        return student in self.students


# %% cell_style="split"
classe = Classe(['jean', 'laurent', 'benoit'])

'jean' in classe


# %% [markdown] slideshow={"slide_type": "slide"}
# ## indexations: `obj[x]`

# %% cell_style="split"
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


# %% cell_style="split"
classe = Classe(['jean', 'laurent', 'benoit'])

classe[1]

# %% cell_style="split"
classe['jean']

# %% cell_style="split"
classe['pierre'] is None


# %% [markdown] slideshow={"slide_type": "slide"}
# ## appel: `obj(x)`
#
# on peut même donner du sens à `obj(x)`

# %% cell_style="split"
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


# %% cell_style="split"
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
# * optionnellement d'autres pour donner du sens à  
#   des constructions du langage sur ces objets
# * ces méthodes ont toutes un nom en `__truc__` (*dunder methods*)

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## pour en savoir plus
#
# la (longue) liste exhaustive des méthodes spéciales  
# est donnée dans la documentation officielle ici
#
# https://docs.python.org/3/reference/datamodel.html#special-method-names

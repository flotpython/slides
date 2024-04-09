# -*- coding: utf-8 -*-
# ---
# jupyter:
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
#     title: enums & dataclasses
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown] slideshow={"slide_type": ""}
# # enums et dataclasses

# %% [markdown]
# dans ce notebook nous allons découvrir - très rapidement - deux façons de créer rapidement des classes qui répondent à des besoins spécifiques

# %% [markdown]
# ## `enums`

# %% [markdown]
# la notion de classe énumérée est à rapprocher de la notion de catégorie en pandas, c'est-à-dire un type qui peut prendre un nombre fini, et généralement petit, de valeurs.

# %%
# un tout petit exemple de classes énumérées

from enum import Enum, IntEnum, auto

class Color(Enum):
    HEARTS = '♡'
    CLUBS = '♧'
    DIAMONDS = '♢'
    SPADES = '♤'
    
    def __format__(self, spec):
        return format(self.value, spec)
        
    
class Value(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    # you get the picture...
    
    def __format__(self, spec):
        return format(self.value, spec)


# %%
# la classe se comporte comme un itérable
for color in Color:
    print(color, f"{color}")

# %%
from itertools import product
for value, color in product(Value, Color):
    print(f"{value}of{color}", end=" ")

# %%
# et si on a précisé le type IntEnum on peut utiliser les valeurs comme des entiers
Value.ONE <= Value.TWO

# %% [markdown]
# ### pour en savoir plus
#
# ceci est un rapide aperçu, pour plus de détails voyez cette page
#
# <https://docs.python.org/3/library/enum.html>

# %% [markdown]
# ## `dataclasses`

# %% [markdown]
# les dataclasses sont conçues pour pouvoir créer facilement des classes de type 'enregistrement', c'est-à-dire lorsqu'un objet contient simplement quelques attributs de données

# %%
# un petit exemple de dataclass

from dataclasses import dataclass

# cette fois l'outil de confort se préseten sous la forme d'un décorateur

@dataclass
class Vector:
    x: float
    y: float = 0.
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


# %%
# on a gratuitment le constructeur et la représentation

v = Vector(12)
v

# %%
# et d'autres trucs pratiques comme la comparaison ==

Vector(8) + Vector(4, 12) == Vector(12, 12)


# %% [markdown]
# ### les réglages disponibles
#
# on voit donc que la classe obtenue a été remplie automatiquement, du moins en partie - 
# par exemple ici le constructeur et l'afficheur ont été écrits pour nous
#
# à savoir: on peut agir sur l'ensemble des méthodes spéciales "automatiques", en passant au décorateur différentes options  
# par exemple on peut lui demander de rendre nos objets comparables:

# %%
# cette fois on veut des objets comparables

@dataclass(order=True)
class Vector:
    x: float
    y: float = 0.


# %%
# par contre c'est rustique - ici ordre lexicographique...

v1, v2 = Vector(2, 4), Vector(3, 1)
v1 <= v2

# %% [markdown]
# ### pour en savoir plus
#
# de nouveau pour approfondir, voyez cette page
#
# <https://docs.python.org/3/library/dataclasses.html>

# %% [markdown]
# ***

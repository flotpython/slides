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
#     title: type hints
# ---

# %% [markdown] slideshow={"slide_type": ""}
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# (label-type-hints)=
# # *type hints*
#
# littéralement: ***suggestions*** *de typage*

# %% [markdown]
# ## motivations
#
# le fait de pouvoir écrire du code non typé est pratique (rapidité de développement)  
# mais a des limitations (notamment: confusion possible sur l'utilisation des librairies)
#
# le but avec les *type hints* est introduire un mécanisme **optionnel** pour améliorer la situation
#
# * meilleure **documentation**: faciliter l'accès à une nouvelle lib
# * analyse statique: **trouver les bugs** plus tôt
# * et plus anecdotiquement, meilleures performances

# %% [markdown]
# ## complètement optionnel 
#
# non seulement on n'est pas obligé d'en mettre  
# mais même si on en met, **c'est ignoré !** à *run-time*

# %%
# les annotations ici indiquent que 
# les paramètres et le retour sont des entiers

def ajouter(x: int, y:int) -> int:
    return x + y


# %%
# mais à run-time celles-ci sont ignorées !
# la preuve, je peux utiliser des chaines à la place

ajouter('abc', 'def')


# %% [markdown] slideshow={"slide_type": "slide"}
# ### à quoi ça sert alors ? vérifier

# %% [markdown]
# **vérification statique** en utilisant `mypy` - un outil **externe**

# %%
# l'analyse statique est faite par un outil externe
# ici je choisis d'utiliser mypy

# %pip install mypy

# %%
# avec ce fichier source

# %cat samples/typehints.py

# %%
# on obtient ces diagnostics d'erreur sans avoir besoin d'exécuter
# ce qui signifie qu'on peut le faire AVANT même de faire les tests

# !mypy samples/typehints.py

# %% [markdown]
# ### à quoi ça sert alors ? documenter
#
# **meilleure documentation !** 
#
# on perd moins de temps perdu à deviner les présupposés sur les arguments
#
# ````{admonition} digression sur les docstrings
# :class: admonition-small
#
# lorsqu'on écrit un docstring, on n'a pas besoin de répéter la *signature* de la fonction, du coup les types hints se retrouvent automatiquement dans la doc, comme ceci:
# ````

# %%
def ajouter(x: int, y:int) -> int:
    """
    add 2 integers
    """
    return x + y

help(ajouter);

# %% [markdown]
# ## les variables aussi
#
# au départ on pense surtout à typer les paramètres, et la sortie des fonctions  
# mais on peut aussi typer les variables

# %%
# le type hint permet aussi de préciser les choses sur les variables

NAMES : list[str] = []

# %% [markdown]
# ## comment définir un type

# %% [markdown]
# ### les classes *builtin*
#
# dans les cas simples on utilise directement les classes builtin `str`, `dict` etc..  
# notez qu'on peut utiliser les `[]` pour fabriquer des types plus précis, par exemple
#
# ```{list-table}
#
# * - `list[int]`
#   - liste d'enters
#
# * - `tuple[str, int]`
#   - un tuple à deux éléments, une chaine et un entier
#
# * - `dict[str, list[int]]`
#   - dictionnaire dont les clés sont des chaines et les valeurs des listes d'entiers
# ```

# %% [markdown] tags=[]
# ### aliases
#
# évidemment on utilise souvent les mêmes types dans une application;  
# aussi on peut se définir son type perso avec une simple affectation, comme par exemple
#
# ```python
#
# # on définit un alias de type avec une simple affectation
#
# Name = str
# Age = int
# Phone = str
#
# # ce type décrit les tuples qui contiennent deux chaines et un entier
# Employee = tuple[Name, Age, Phone]
#
# # et donc ensuite on peut utiliser Employee dans un type hint
# ```

# %% [markdown]
# ### classes
#
# pour quasiment le même genre d'usage, on peut bien sûr utiliser aussi les noms de classe
#
# ```python
# class Foo: 
#     pass
#
# def link_foos(foo1: Foo, foo2: Foo) -> None:
#     foo1.links.add(foo2)
# ```
#
# ````{admonition} à l'intérieur d'une classe
# :class: admonition-small
#
# **à savoir**: parfois on a besoin du nom de la classe pour typer une méthode *à l'intérieur* de la classe  
# dans ce cas-là on ne peut pas faire comme ci-dessus, car à l'intérieur de la classe le nom de la classe n'est pas encore défini (il ne sera qu'une fois l'instruction `class` exécutée...)  
# pour ce genre d'usage on peut utiliser **une chaine contenant le nom de la classe**  
# quelque chose comme ceci:
#
# ```python
# class Node:
#
#    # pour typer le paramètre child, on ne peut pas mettre juste `Node`
#    # on est obligé de mettre la chaine `"Node"`
#    def add_child(child: "Node"):
#        ...
# ```
#
# ````

# %% [markdown]
# ### le module `typing` (1)
#
# le module `typing` permet d'étendre le spectre, en introduisant des concepts additionnels  
# comme par exemple `Sequence`, `Iterable`, `Callable`
#
# voici quelques exemples
#
# ```python
# from typing import Iterable, Iterator, Sequence, Callable
#
# # (le type qui décrit) n'importe quel itérable qui contient des entiers
# Iterable[int]
# # pareil pour un itérateur
# Iterator[int]
# # ou une séquence
# Sequence[int]
#
#
# # pour le callable la syntaxe est un peu moins triviale:
# # ici une fonction qui prend deux paramètres de types resp. Foo et Bar 
# # et qui retourne un booléen
#
# f: Callable[[Foo, Bar], bool]
# ```
#
# pour les détails, reportez-vous comme d'hab à <https://docs.python.org/3/library/typing.html>

# %% [markdown] slideshow={"slide_type": ""}
# ### le module `typing` (2)
#
# on y trouve aussi d'autres constructeurs qui peuvent être utiles, en vrac:
#
# * `Any` peut être n'importe quoi
# * `Union` lorsqu'on accepte plusieurs types
# * `Optional` pour une variable qui peut aussi être `None`
# * `Hashable` ce qui peut être utilisé comme clé d'un dictionnaire
#
# et aussi
#
# * `NewType` définit un nom pour un type - un peu plus subtil que l'affectation
# * `TypeVar` pour manipuler des types génériques (à la template C++)
#   * grâce auxquels on peut implémenter des classes génériques

# %% [markdown] slideshow={"slide_type": ""}
# ## conclusion
#
# comme il s'agit d'un trait relativement récent (en fait ça n'est stable que depuis la 3.9),  
# les *type hints* ne sont pas massivment présents dans le code existant
#
# toutefois c'est clairement une voie à suivre, et en tous cas c'est important que vous **sachiez le lire** !
#
# souvenez-vous qu'on peut les utiliser ponctuellement  
# du coup pensez à l'utiliser à chaque fois que les choses deviennent ambigües  
#
# par contre, pour pouvoir faire de la vérification statique, il faut viser une couverture beaucoup plus large pour que ça apporte vraiment quelque chose

# %% [markdown] slideshow={"slide_type": ""}
# ## ATTENTION avec `isinstance`
#
# (avancé)
#
# on serait tenté d'utiliser `isinstance`/`issubclass` avec les types tels qu'on vient de les définir  
# mais il **ne faut pas le faire**! je vous renvoie [à ce post](https://github.com/python/typing/issues/136) 
#
# il y est suggéré de disposer d'une **autre** builtin que `isinstance`
# pour vérifier si une variable est *acceptable* pour un **type**
# alors que `isinstance` se base uniquement sur l'héritage de **classes**

# %% slideshow={"slide_type": "slide"} tags=["raises-exception"]
# ceci déclenche un TypeError
from typing import Union

Phone = Union[str, int]
PhoneSet = set[Phone]

try:
    isinstance( {'0123456789', 98765432}, PhoneSet)
except Exception as exc:
    print(f"{type(exc)} {exc}")

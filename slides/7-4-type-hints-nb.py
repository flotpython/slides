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
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   nbhosting:
#     title: type hints
#   rise:
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": ""}
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # *type hints*
#
# * littéralement: ***suggestions*** *de typage*
# * **avertissement** pour ce notebook il faut **au minimum Python-3.9**

# %% [markdown]
# ## motivations
#
# * *duck typing* : pratique mais a des limitations
# * introduire un mécanisme **optionnel** pour améliorer la situation
#   * meilleure documentation: faciliter l'accès à une nouvelle lib
#   * analyse statique: trouver les bugs plus tôt
#   * (performances)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### histoire

# %% [markdown] slideshow={"slide_type": ""}
# * module `typing` disponible depuis 3.5
# * pas mal de changements (dans le bon sens) jusque dans la 3.9
# * qui expliquent peut-être pourquoi ça reste semble-t-il encore relativement confidentiel

# %% [markdown] slideshow={"slide_type": "slide"}
# ## complètement optionnel 

# %% [markdown]
# * non seulement on n'est pas obligé d'en mettre
# * mais même si on en met, **c'est ignoré !** à *run-time*

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
# !pip install mypy

# %%
# !cat samples/types01.py

# %%
# !mypy samples/types01.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ### à quoi ça sert alors ? documenter

# %% [markdown]
# **meilleure documentation !** 
#
# * moins de temps perdu à deviner  
#   les présupposés sur les arguments

# %% [markdown] slideshow={"slide_type": "slide"}
# ## comment définir un type

# %% [markdown]
# * les cas simples: grâce aux classes builtin `str`, `dict` etc..
# * le module `typing` introduit des concepts additionnels
#   * qui servent à étendre le spectre
#   * comme `Iterable`, `Callable`, ...
#   * mais aussi la notion de type abstrait avec `Generic` et `TypeVar`
#   * nous allons survoler tout ceci sur quelques exemples
#   * pour les détails, reportez-vous à https://docs.python.org/3.9/library/typing.html

# %% [markdown] slideshow={"slide_type": "slide"}
# ### aliases et types standard

# %% slideshow={"slide_type": ""}
# on définit un alias de type avec une simple affectation
# une affectation suffit

Name = str
Age = int
Phone = str


# %% slideshow={"slide_type": "slide"}
# un tuple est non mutable, il semble logique de dire
# combien il doit avoir de composants et de quels types

# ce type décrit les tuples qui contiennent deux chaines et un entier
Employee = tuple[Name, Age, Phone]


# %% cell_style="split"
# ce nom peut être utilisé
# dans les type hints 
def foo(employee: Employee) -> str:
    ...


# %% cell_style="split"
# on aurait pu aussi mettre directement
def foo(employee: tuple[Name, Age, Phone]):
    ...

# mais avec cette approche il faut
# répéter tout le temps la même chose...


# %% [markdown]
# #### types standard .. suite
#
# comme on vient de le voir, on on utilise les types standard avec des `[]` pour définir des types composites, par exemple
#
# * `list[Truc]` : une liste qui ne contient que des trucs
# * `dict[KeyType, ValueType]` : un dictionnaire dont les clés sont des `KeyType` et les valeurs des `ValueType`

# %% slideshow={"slide_type": "slide"}
# un exemple avec un set

# !cat samples/types02.py

# %%
# !mypy samples/types02.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ### classes
#
# * un objet classe défini avec `class`
# * peut être utilisé bien évidemment aussi

# %%
class Foo: 
    pass

def link_foos(foo1: Foo, foo2: Foo) -> None:
    foo1.links.add(foo2)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### le module `typing`

# %% [markdown]
# * des **constructeurs de type**
# * permettent de fabriquer des types plus élaborés
# * ils sont définis **dans le module `typing`**
# * et ont un nom en `FonteMixte`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `Iterable`, `Iterator`, `Sequence`
#
# * ça devient intéressant de **formaliser**
# * le vocabulaire qui est souvent un peu approximatif
# * par exemple:

# %%
from typing import Iterable, Iterator, Sequence, Callable

Iterable[int]
Iterator[tuple[int, float, str]]
Sequence[list[float]]

Bar = tuple[str, int]

# une fonction qui prend deux paramètres de types resp. Foo et Bar 
# et qui retourne un booléen
f: Callable[[Foo, Bar], bool]

# %% [markdown] slideshow={"slide_type": "slide"}
# ### autres constructeurs en vrac

# %% [markdown] slideshow={"slide_type": ""}
# * `Any` peut être n'importe quoi
# * `Union` lorsqu'on accepte plusieurs types
# * `Callable` pour les objets, ahem, callables
# * `Hashable` ce qui peut être utilisé comme clé d'un dictionnaire
#
# et aussi
#
# * `NewType` définit un nom pour un type - un peu plus subtil que l'affectation
# * `TypeVar` pour manipuler des types génériques (à la template C++)
#   * grâce auxquelles on peut implémenter des classes génériques

# %% [markdown] slideshow={"slide_type": "slide"}
# ## comment utiliser un type

# %% [markdown]
# on s'en sert typiquement
#
# * dans les déclarations de fonction, comme on l'a déjà vu 
# * on peut **aussi typer les variables**
#

# %%
# type-hint de la globale FOO
# ↓↓↓↓↓↓
FOO: str = "type-hints"


# ici on type-hint x
#       ↓↓↓↓↓↓
def foo(x: int) -> str:
  # ici on type-hint y
  # ↓↓↓↓↓↓  
    y: int = x * x      
    return f"{FOO} {y=}"


# %%
foo(10)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## conclusion (1)

# %% [markdown] slideshow={"slide_type": ""}
# * raisonnablement stable en 3.9 amha
# * va sans doute gagne petit à petit en popularité
# * c'est important que vous **sachiez le lire** !
# * et penser à l'utiliser quand les choses deviennent ambigües  
# * à nouveau surtout pour la lisibilité dans un premier temps
# * car tant qu'on n'a pas tout typé c'est dur de faire de la  
#   vérification statique qui apporte vraiment quelque chose

# %% [markdown] slideshow={"slide_type": "slide"}
# ### conclusion (2)

# %% [markdown] slideshow={"slide_type": ""}
# * c'est clairement la voie à suivre 
#   * langage de type complet
#   * pour enrichir la documentation et l'utilisabilité du code
#   * notamment intégré dans les outils de doc (e.g. sphinx)
# * avec la possibilité de trouver des erreurs pernicieuses
#   * en utilisant `mypy` ou un outil similaire
#   * exactement comme on utilise `pylint` pour **détecter tôt**  
#     des erreurs par anaylse statique **avant** d'exécuter 

# %% [markdown] slideshow={"slide_type": "slide"}
# ## partie optionnelle

# %% [markdown] slideshow={"slide_type": "slide"}
# ### ATTENTION avec `isinstance`

# %% [markdown] slideshow={"slide_type": ""}
# * on serait tenté d'utiliser `isinstance`/`issubclass` avec les types
# * il **ne faut pas le faire**
# * je vous renvoie [à ce post](https://github.com/python/typing/issues/136) 
# * il est suggéré de disposer d'une **autre** builtin que `isinstance`
#   * pour vérifier si une variable est *acceptable* pour un **type**
#   * alors que `isinstance` se base uniquement sur l'héritage de **classes**

# %% slideshow={"slide_type": "slide"}
# ceci déclenche un TypeError
try:
    isinstance( {'0123456789', 98765432}, PhoneSet)
except Exception as exc:
    print(f"{type(exc)} {exc}")

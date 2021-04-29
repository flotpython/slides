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
#     title: type hints
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
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% slideshow={"slide_type": "slide"}
#from plan import plan; plan("compléments", "type hints")


# %% [markdown] slideshow={"slide_type": "slide"}
# # *type hints*
#
# * littéralement: ***suggestions*** *de typage*

# %% [markdown]
# ## motivations
#
# * *duck typing* : pratique mais a des limitations
# * introduire un mécanisme **optionnel** pour améliorer la situation
#   * meilleure documentation / abaisser barrière d'entrée
#   * analyse statique: trouver les bugs plus tôt
#   * (performances)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### histoire

# %% [markdown] slideshow={"slide_type": ""}
# * commencé au travers du projet [mypy](http://mypy.readthedocs.io/en/latest/index.html), par Jukka Lehtosalo
# * PEPs en vigueur
#   * [PEP-484](https://www.python.org/dev/peps/pep-0484/) "Type hints"
#   * [PEP-483](https://www.python.org/dev/peps/pep-0483/) "The theory of type hints"
# * progressivement intégré à Python
# * module `typing` disponible depuis 3.5

# %% [markdown] slideshow={"slide_type": "slide"}
# ## complètement optionnel 

# %% [markdown]
# * non seulement on n'est pas obligé d'en mettre
# * même si on en met, **c'est ignoré !** à *run-time*

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
# * les classes builtin `str`, `dict` etc..
# * le module `typing` introduit des concepts additionnels
#   * qui servent à étendre le spectre
#   * comme `Iterable`, `Callable`, ...
#   * mais aussi la notion de type abstrait avec `Generic` et `TypeVar`
#   * nous allons voir tout ceci sur quelques exemples

# %% [markdown] slideshow={"slide_type": "slide"}
# ### aliases

# %%
# pour définir un alias pour une classe native
# une affectation suffit

Url = str

def retrieve_url(url: Url, count: int) -> bool:
    #
    return True


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
# ### `List` et `Tuple`
#
# * pour commencer: `List` (et `Tuple`)
# * qui permet de décrire un type de liste  
#   où tous les items sont d'un type
# * remarquer **l'usage des `[]`** - et non pas les **`()`**  
#   pour la composition de types

# %%
from typing import List, Tuple

# une liste dont tous les éléments sont des chaines
phone_numbers: List[str]

# une liste de'objets de type Foo
all_the_foos: List[Foo]

# %% slideshow={"slide_type": "slide"}
# un tuple est non mutable, il semble logique de dire
# combien il doit avoir de composants et de quels types

Name = str
Age = int
Phone = str

# ce type décrit les tuples qui contiennent deux chaines et un entier
Employee = Tuple[Name, Age, Phone]

# %% cell_style="split"
# Employee peut être mentionné 
# dans les type hints 
type(Employee)

# %% cell_style="split"
# mais ce n'est pas 
# une usine à objets
try: 
    Employee()
except Exception as exc:
    print(f"OOPS - {type(exc)}")

# %% slideshow={"slide_type": ""}
# de manière similaire
# ne pas confondre tuple et Tuple !
Tuple is tuple

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `Dict` et `Set`

# %% slideshow={"slide_type": ""}
# c'est pareil avec `Dict` et `Set`
from typing import Dict, Set

# Dict est construit avec deux types
# pour les clés et les valeurs respectivement
NameHash = Dict[Name, Employee]

# et Set avec un seul type
PhoneSet = Set[Phone]

# %% slideshow={"slide_type": "slide"}
# !cat samples/types02.py

# %%
# !mypy samples/types02.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `Iterable`, `Iterator`, `Sequence`
#
# * ça devient intéressant de **formaliser**
# * le vocabulaire qui est souvent un peu approximatif
# * par exemple:

# %%
from typing import Iterable, Iterator, Sequence

Iterable[int]
Iterator[Tuple[int, float, str]]
Sequence[List[float]]

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `NewType`
#
# une méthode plus propre pour définir un alias

# %%
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)


# %% [markdown]
# de cette façon on peut être plus strict

# %%
def get_user_name(user_id: UserId) -> str:
    ...

# typecheck OK
user_a = get_user_name(UserId(42351))

# typecheck KO; un entier n'est pas un UserId
user_b = get_user_name(-1)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### autres constructeurs en vrac

# %% [markdown] slideshow={"slide_type": ""}
# * `Any` peut être n'importe quoi
# * `Union` lorsqu'on accepte plusieurs types
# * `Callable` pour les objets, ahem, callables
# * `Hashable` ce qui peut être utilisé comme clé d'un dictionnaire
# * `TypeVar` pour manipuler des types génériques (à la template C++)
#   * grâce auxquelles on peut implémenter des classes génériques

# %% [markdown] slideshow={"slide_type": "slide"}
# ## conclusion (1)

# %% [markdown] slideshow={"slide_type": ""}
# * peut-être pas totalement stable encore
#   * mais gagne petit à petit en popularité
# * il faut au moins savoir le lire !
# * et penser à l'utiliser quand les choses
#     deviennent ambigües

# %%
# une application comme nbhosting
class Course:
    pass

# très confusant comme signature, car ça suggère qu'il faut
# passer à la fonction un objet Course
def show_course(course):
    """
    display a Course object from its name
    """
    course_obj = Course.objects.find(coursename=course)
    course_obj.show()


# %% cell_style="split" slideshow={"slide_type": "slide"}
# première option
# on renomme le paramètre 
# en 'coursename' 
# par contre ça peut être long
# et/ou alourdir le code
def show_course(coursename):
    course = Course.objects.find(
        coursename=coursename)
    course.show()


# %% cell_style="split"
# deuxieme option
# type hint 
def show_course(course: str):
    course_obj = Course.objects.find(
        coursename=course)
    course_obj.show()


# %% [markdown]
# et bien sûr on peut aussi faire les deux ;-)

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

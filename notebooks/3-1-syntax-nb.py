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
#     title: syntaxe
# ---

# %% [markdown] cell_style="center"
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown]
# # syntaxe

# %% [markdown] tags=["gridwidth-1-2"]
# ### l’indentation, base de la syntaxe
#
# * la fin d’une ligne est significative  
#   → pas de `;` nécessaire à la fin de la ligne
#
# * un **bloc** d’instructions doit avoir la **même indentation** en partant de la gauche  
#   → pas besoin de `{}` pour délimiter un bloc  
#
# * indentation recommandée : 4 espaces

# %% tags=["gridwidth-1-2"]
def foo():
    print('début')
    a = 10*20
    print('fin, a=', a)
    
foo()    


# %% [markdown]
# ````{admonition} les pièges à éviter
# :class: warning
#
# les principaux pièges pour les débutants:
#
# * évitez d'utiliser des `Tab` (le plus simple: ne **jamais** mettre de `Tab`)
# * et attention aux copier/coller qui peuvent décaler des lignes
# ````

# %% [markdown]
# ## commentaires
#
# tout ce qui se trouve à droite d'un `#` est considéré comme un commentaire  
# (sauf dans les chaines de caractères, évidemment)

# %%
# un commentaire
def foo():
    x = 12 # on peut commenter ici
    # mais c'est préférable de garder
    # les commentaires sur une ligne sans code
    y = 12
    # mais pas dans les chaines
    return "une chaine # avec un diese"

print(foo())

# %% [markdown]
# ## expressions *vs* instructions
#
# dans tous les langages on distingue entre
#
# * instruction: une construction qui fait un effet de bord, qui change l'environnement  
#   mais **qui ne renvoie rien**
#
# * expression: une construction **qui renvoie quelque chose**  
#   du coup, les expressions peuvent être combinées à l'infini
#
# quelques exemples parmi ce qu'on a déjà vu:

# %% [markdown]
# ### expressions
#
# | construction | exemple | commentaire |
# |-|-|-|
# | opérateur | `a + 12`  | ici binaire
# | appel de fonction | `foo(12)`  |
# | idem | `foo(a + 12)` | les expressions **se combinent** |
# | indexation | `L[12]` | 
# | attribut | `S.upper()` | attribut ou méthode |

# %% [markdown]
# ### instructions
#
# | construction | exemple | commentaire |
# |-|-|-|
# | `if` | `if 10 <= x <= 20: ...` | contrôle du code
# | `while` | `while L: ...` | contrôle du code
# | affectation | a = 10 | nouvelle variable
# | nouvelle fonction | `def foo(): ...` | nouvelle variable
# | nouvelle classe | `class Foo: ...` | nouvelle variable
#
# ````{admonition} parfois les deux
# :class: tip admonition-small
#
# on verra que certaines constructions (affectation, `if`) peuvent exister sous les deux formes, (avec des syntaxes légèrement différentes du coup)
# ````

# %% [markdown]
# ## mots clés
#
# pour référence: les mots suivants ne peuvent pas être utilisés comme un nom de variable
#
# ```{list-table} mots réservé / *keywords*
# :header-rows: 0
#
# * - False
#   - await
#   - else
#   - import
#   - pass
#
# * - None
#   - break
#   - except
#   - in
#   - raise
#
# * - True
#   - class
#   - finally
#   - is
#   - return
#
# * - and
#   - continue
#   - for
#   - lambda
#   - try
#
# * - as
#   - def
#   - from
#   - nonlocal
#   - while
#
# * - assert
#   - del
#   - global
#   - not
#   - with
#
# * - async
#   - elif
#   - if
#   - or
#   - yield
# ````

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
#     title: nouvelles releases
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": ""}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% [markdown] slideshow={"slide_type": ""}
# # `releases récentes`

# %% [markdown]
# résumons les nouveautés marquantes
#
# * jusqu'à 3.9: une release tous les 18 mois environ
# * à partir de 3.10: une release par an (voir https://www.python.org/dev/peps/pep-0602/)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## version 3.8

# %% [markdown] slideshow={"slide_type": ""}
# ### "assignment expression" *aka* *walrus operator*
#
#   `x := expression` peut maintenant être utilisé comme **une expression** c'est-à-dire dans un test ou dans un appel de fonction
#   
#   limité à **une variable** (et pas par exemple pour affecter `liste[0]`)  

# %%
import re

if (match := re.match( '[a-z]+(\d+)[a-z]+', 'abc02345defg')):
    print(match.group(1))

# %% [markdown] slideshow={"slide_type": "slide"}
# ### f-string & auto-description

# %% [markdown]
# dans une f-string, on peut ajouter un `=` à la fin de l'expression entre `{}`; de cette façon le **texte de l'expression** est affiché aussi (en plus de sa valeur)

# %% cell_style="split"
x, y = 1, 2

# avant
print(f"10*x + 20*y**2={10*x+20*y**2}")

# %% cell_style="split"


# après
print(f"{10*x + 20*y**2=}")


# %% [markdown] slideshow={"slide_type": "slide"}
# ### paramètres dits *positional-only*    
#
# permet d'indiquer que certains paramètres  
# **ne peuvent pas être nommés** par l'appelant d'une fonction

# %% cell_style="split"
def foo(x, y):
    print(f"{x=} {y=}")


# %% cell_style="split"
foo(y=2, x=1)


# %% cell_style="split"
def bar(x, /, y):
    print(f"{x=} {y=}")


# %% cell_style="split"
try:
    bar(y=2, x=1)
except Exception as exc:
    print(f"{exc=}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### liste complète 
#
# des changements dans la 3.8
#
# https://docs.python.org/3/whatsnew/3.8.html

# %% [markdown] slideshow={"slide_type": "slide"}
# ## version 3.9
#
# * sortie le 5 octobre 2020

# %% [markdown] slideshow={"slide_type": "slide"}
# ### type hinting

# %% [markdown]
# pour ceux qui s'intéressent aux *type hints*, la version 3.9 vient avec la capacité de définir ses propres types en utilisant les types *builtin* comme `list` et `dict`, i.e. en n'ayant plus besoin de passer par des artefacts dans le module `typing` comme ceux qui s'appelaient `List` et `Dict`

# %% cell_style="split"
# avant

from typing import List

def foo(names: List[str]):
    pass


# %% cell_style="split"
# en 3.9

def foo(names: list[str]):
    pass


# %% [markdown] slideshow={"slide_type": ""}
# ### opérations sur les dictionnaires

# %% [markdown]
# la fusion de deux dictionnaires se fait traditionnellement avec `dict.update()`; depuis la 3.9 on peut aussi utiliser l'opérateur `|` et son dérivé `|=` pour faire cette opération

# %% slideshow={"slide_type": "slide"}
x = {"key1": "1 from x", "key2": "2 from x"}
y = {"key2": "2 from y", "key3": "3 from y"}

# %% cell_style="split"
# avant la 3.9
z = x.copy()
z.update(y)
z

# %% cell_style="split"
# ou encore


{**x, **y}

# %% cell_style="split"
# en 3.9
# résultat = nouveau dict
x | y

# %% cell_style="split"


y | x

# %% cell_style="split"
# avec modification
x |= y

# %% cell_style="split"
x

# %% [markdown] slideshow={"slide_type": "slide"}
# ### liste complète 
#
# des changements dans la 3.9
#
# https://docs.python.org/3/whatsnew/3.9.html

# %% [markdown] slideshow={"slide_type": "slide"}
# ## 3.10
#
# sortie le 4 octobre 2021

# %% [markdown]
# ### `match`

# %% [markdown]
# une toute nouvelle instruction `match` permet de faire des choses comme

# %% [markdown] slideshow={"slide_type": "slide"}
# ```python
# In [1]: def http_error(status):
#    ...:     match status:
#    ...:         case 400:
#    ...:             return "Bad request"
#    ...:         case 404:
#    ...:             return "Not found"
#    ...:         case 418:
#    ...:             return "I'm a teapot"
#    ...:         case 401 | 403 :
#    ...:             return "Not allowed"
#    ...:         case _:
#    ...:             return "Something's wrong with the internet"
#    ...:
#    ...: print(http_error(404))
#    ...:
# Not found
# ```

# %% [markdown]
# <div class="rise-footnote">
#
# ce code est dans `samples/match01.py`
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ou encore (parmi plein d'autres possibilités)  
# [voir la release note complète ici](https://docs.python.org/3/whatsnew/3.10.html#pep-634-structural-pattern-matching)

# %% [markdown] slideshow={"slide_type": ""}
# ```python
# In [1]: def pretty_point(point: tuple[float, float]):
#    ...:     match point:
#    ...:         case (0, 0):
#    ...:             return "Origin"
#    ...:         case (0, y):
#    ...:             return f"Y={y}"
#    ...:         case (x, 0):
#    ...:             return f"X={x}"
#    ...:         case (x, y):
#    ...:             return f"X={x}, Y={y}"
#    ...:         case _:
#    ...:             raise ValueError("Not a point")
#    ...:
#    ...: P = (0, 20)
#    ...: print(pretty_point(P))
# Y=20
# ```

# %% [markdown]
# <div class="rise-footnote">
#
# ce code est dans `samples/match02.py`
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *better error messages*
#
# https://docs.python.org/3/whatsnew/3.10.html#better-error-messages

# %% [markdown] slideshow={"slide_type": "slide"}
# ### liste complète 
#
# des changements dans la 3.10
#
# https://docs.python.org/3/whatsnew/3.10.html

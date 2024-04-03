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
#     title: nouvelles releases
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
# # `releases récentes`

# %% [markdown]
# résumons les nouveautés marquantes
#
# * jusqu'à 3.9: une release tous les 18 mois environ
# * à partir de 3.10: une release par an (voir https://www.python.org/dev/peps/pep-0602/)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## version 3.8

# %% [markdown] slideshow={"slide_type": "slide"}
# ### paramètres dits *positional-only*    
#
# permet d'indiquer que certains paramètres  
# **ne peuvent pas être nommés** par l'appelant d'une fonction

# %% tags=["gridwidth-1-2"]
def foo(x, y):
    print(f"{x=} {y=}")


# %% tags=["gridwidth-1-2"]
foo(y=2, x=1)


# %% tags=["gridwidth-1-2"]
def bar(x, /, y):
    print(f"{x=} {y=}")


# %% tags=["gridwidth-1-2"]
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

# %% tags=["gridwidth-1-2"]
# avant

from typing import List

def foo(names: List[str]):
    pass


# %% tags=["gridwidth-1-2"]
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

# %% tags=["gridwidth-1-2"]
# avant la 3.9
z = x.copy()
z.update(y)
z

# %% tags=["gridwidth-1-2"]
# ou encore


{**x, **y}

# %% tags=["gridwidth-1-2"]
# en 3.9
# résultat = nouveau dict
x | y

# %% tags=["gridwidth-1-2"]


y | x

# %% tags=["gridwidth-1-2"]
# avec modification
x |= y

# %% tags=["gridwidth-1-2"]
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
# `match`

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

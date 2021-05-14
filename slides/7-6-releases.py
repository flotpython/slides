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
#     display_name: Python 3
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

# %% [markdown] slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %%
#from plan import plan; plan("compléments", "releases")

# %% [markdown] slideshow={"slide_type": "slide"}
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

print(f"10*x + 20*y**2={10*x+20*y**2}")

# %% cell_style="split"
print(f"{10*x + 20*y**2=}")


# %% [markdown] slideshow={"slide_type": "slide"}
# ### paramètres dits *positional-only*    
#
# permet d'indiquer que certains paramètres **ne peuvent pas être nommés** par l'appelant d'une fonction

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

# %% [markdown] slideshow={"slide_type": ""}
# ### opérations sur les dictionnaires

# %% [markdown]
# la fusion de deux dictionnaires se fait traditionnellement avec `dict.update()`; depuis la 3.9 on peut aussi utiliser l'opérateur `|` et son dérivé `|=` pour faire cette opération

# %%
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
# ### type hinting

# %% [markdown]
# pour ceux qui s'intéressent aux *type hints*, la version 3.9 vient avec la capacité de définir ses propres types en utilisant les types *builtin* comme `list` et `dict`, i.e. en n'ayant plus besoin de passer par des artefacts dans le module `typing` qui s'appellent `List` et `Dict`

# %% cell_style="split"
# avant

from typing import List

def foo(names: List[str]):
    pass


# %% cell_style="split"
# en 3.9

def foo(names: list[str]):
    pass

# %% [markdown] slideshow={"slide_type": "slide"}
# ### liste complète 
#
# des changements dans la 3.9
#
# https://docs.python.org/3/whatsnew/3.9.html

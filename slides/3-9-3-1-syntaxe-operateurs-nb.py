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
#     title: "syntaxe & op\xE9rateurs"
#   rise:
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] cell_style="center"
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown]
# # syntaxe et opérateurs

# %% [markdown] slideshow={"slide_type": "slide"}
# ## syntaxe

# %% [markdown] slideshow={"slide_type": "slide"}
# ## opérateurs
#
# ### arithmétiques

# %% [markdown]
# * arithmétiques:  `+` | `-` | `*` | `/`
#   * pas que sur les nombres

# %% cell_style="split"
'on peut ajouter' ' deux chaines'

# %% cell_style="split"
['et', 'les'] + ['listes', 'aussi']

# %% cell_style="split"
4 * '-00-'

# %% cell_style="split"
4 * [1, 2]

# %% [markdown] slideshow={"slide_type": "slide"}
# ### dépendants du type

# %% [markdown]
# digression: tous les opérateurs du langage sont dépendants du type des opérandes

# %% cell_style="split"
10 + 20

# %% cell_style="split"
"10" + "20"

# %% [markdown]
# et comme on le verra, chaque type (y compris les classes qui sont des types définis par l'utilisateur) peut redéfinir le comportement des opérateurs
#
# par exemple
#
# * une classe `Vector` donnera du sens à `v1 + v2`
# * une classe `Path` donnera du sens à `path / file`
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### quotient et reste `//` et `%`

# %% [markdown]
# * division entière: quotient et reste: `//`  et `%`

# %% cell_style="split"
# avec des entiers
19 // 3

# %% cell_style="split"
19 % 3



# %% cell_style="split"
# ou des flottants
from math import pi, e

pi // e


# %% cell_style="split"
from math import pi

pi % e


# %% [markdown] slideshow={"slide_type": "slide"}
# ### puissance `**`

# %% [markdown]
# * $x^y$ : `x ** y` 

# %% cell_style="split"
2 ** 100

# %% cell_style="split"
pi ** e


# %% [markdown] slideshow={"slide_type": "slide"}
# ### comparaison - négation

# %% [markdown]
# * comparaison: `==` et `is`  - déjà mentionnés
# * négation: `!=` et `is not` respectivement

# %% [markdown]
# * comparaisons dans espaces ordonnés:
#   * `>=`, `>`, `<=`, `<`
#   * curiosité: on peut les chainer

# %% cell_style="split"
def est_moyenne(note):
    return 10 <= note <= 12


# %% cell_style="split"
est_moyenne(11)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### opérateurs logiques

# %% [markdown]
# * opérateurs logiques: `and` - `or` - `not`
# * opérateurs d'appartenance: `in` et `not in`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### opérateurs bitwise

# %% [markdown]
# * opérateurs dits *bitwise*:
#   * `&` - `|` : **et** et **ou** logique, respectivement
#   * `^` : **xor**
#   * `~` : **not** 
# * on les aussi déjà rencontrés avec les ensembles

# %% cell_style="split"
a = 0b111100 
b = 0b110011

# %% cell_style="split"
bin(a | b)

# %% cell_style="split"
bin(a & b)

# %% cell_style="split"
bin(a ^ b)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### précédence des opérateurs

# %% [markdown]
# * comme pour tous les langages
#   * précédence des opérateurs
#   * dans le doute: mettez des parenthèses !

# %% [markdown] slideshow={"slide_type": "slide"}
# ### POO : opérateurs redéfinis 

# %% [markdown]
# * tous ces opérateurs peuvent être **redéfinis**
#   * c'est le propos des 'méthodes magiques' 
#   * que l'on verra à propos des classes
#   
# * exemple intéressant, la classe `Path`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### ex:  `/` sur la classe `Path`

# %%
# la classe Path nous a montré 
# un bel exemple d'opérateur redéfini 

from pathlib import Path

# %%
home = Path.home()

# l'opérateur / est défini sur Path
subdir = home / "git"

if subdir.exists():
    print(f"le répertoire {subdir} existe")


# %% [markdown] slideshow={"slide_type": "slide"}
# ### redéfinir `bool()`

# %% slideshow={"slide_type": ""}
# pour anticiper un peu, voici par exemple
# comment faire en sorte qu'un objet 
# agisse comme False
class Fool:
    def __bool__(self):
        return False

fool = Fool()
if not fool:
    print("bingo")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### évaluation paresseuse des opérateurs logiques

# %% [markdown] cell_style="split"
# * `and` et `or` sont opérateurs *short-circuit*
#   * on évalue les opérandes de gauche à droite
#   * et on s'arrête dès que le résultat est connu

# %% [markdown] cell_style="split"
# * A `and` B
#   * Si A est `False`,  
#     B ne sera pas évalué
#
# * A `or` B
#   * Si A est `True`,  
#     B ne sera pas évalué

# %% cell_style="split" slideshow={"slide_type": ""}
# une fonction avec side-effect
counter = 0

def greater(a, b):
    global counter
    counter += 1 
    return a >= b


# %% cell_style="split"
# ceci n'imprime rien
note = 11.5
if (greater(note, 10) and greater(note, 12)
    and greater(note, 14) and greater(note, 16)):
    print("excellent")

# %% cell_style="split"
# ce qui intéressant, c'est 
# combien de fois on a appelé greater
counter

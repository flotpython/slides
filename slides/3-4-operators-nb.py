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
# ---

# %% [markdown] cell_style="center"
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown]
# # opérateurs
#
# un survol des opérateurs pour construire les expressions
#
# ````{admonition} précédence des opérateurs
# :class: attention
#
# comme pour tous les langages, les opérateurs ont une précédence; dans le doute: mettez des parenthèses !
# ````

# %% [markdown]
# ## rappels
#
# * appel de fonction avec `()` comme dans `foo(0)`
# * indexation avec `[]` comme dans `L[0]`
# * attribut avec `.` comme dans `S.upper()`

# %% [markdown]
# ## arithmétiques
#
# * arithmétiques:  `+` | `-` | `*` | `/`
#   * pas que sur les nombres

# %% tags=["gridwidth-1-2"] slideshow={"slide_type": ""}
'on peut juste juxtaposer' ' deux chaines'

# %% tags=["gridwidth-1-2"] slideshow={"slide_type": ""}
'ou les' + ' additioner'

# %% tags=["gridwidth-1-2"] slideshow={"slide_type": ""}
['et', 'les'] + ['listes', 'aussi']

# %% tags=["gridwidth-1-2"] slideshow={"slide_type": ""}
4 * '-00-'

# %% tags=["gridwidth-1-2"] slideshow={"slide_type": ""}
4 * [1, 2]

# %% [markdown]
# ### dépendants du type
#
# digression: tous les opérateurs du langage sont dépendants du type des opérandes

# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
10 + 20

# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
"10" + "20"

# %% [markdown]
# et comme on le verra, chaque type (y compris les classes qui sont des types définis par l'utilisateur) peut redéfinir le comportement des opérateurs
#
# par exemple
#
# * une classe `Vector` donnera du sens à `v1 + v2`
# * une classe `Path` donnera du sens à `path / file`
#

# %% [markdown]
# ### quotient et reste `//` et `%`
#
# * rappel division entière: quotient et reste: `//`  et `%`

# %% tags=["gridwidth-1-2"]
# avec des entiers
19 // 3

# %% tags=["gridwidth-1-2"]
19 % 3

# %% [markdown] slideshow={"slide_type": "slide"}
# ### puissance `**`

# %% [markdown]
# * $x^y$ : `x ** y` 

# %% tags=["gridwidth-1-2"]
2 ** 100


# %% [markdown]
# ## opérateurs logiques
#
# * opérateurs logiques: `and` - `or` - `not`
# * opérateurs d'appartenance: `in` et `not in`

# %% [markdown]
# ### comparaison
#
# * comparaison: `==` et `is`  - déjà mentionnés
# * négation: `!=` et `is not` respectivement
#
# * comparaisons dans espaces ordonnés:
#   * `>=`, `>`, `<=`, `<`
#   * curiosité: on peut les chainer

# %% tags=["gridwidth-1-2"]
def est_moyenne(note):
    return 10 <= note <= 12


# %% tags=["gridwidth-1-2"]
est_moyenne(11)

# %% [markdown] tags=["gridwidth-1-2"]
# ### évaluation paresseuse (avancé)
#
# * `and` et `or` sont opérateurs *short-circuit*
#   * on évalue les opérandes de gauche à droite
#   * et **on s'arrête** dès que le résultat est connu
#
# * A `and` B
#   * Si A est `False`,  
#     B ne sera pas évalué
#
# * A `or` B
#   * Si A est `True`,  
#     B ne sera pas évalué

# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
# une fonction avec side-effect
counter = 0

def greater(a, b):
    global counter
    counter += 1 
    return a >= b


# %% tags=["gridwidth-1-2"]
# ceci n'imprime rien
note = 11.5

if (greater(note, 10) and greater(note, 12)
    and greater(note, 14) and greater(note, 16)):
    print("excellent")

# %% tags=["gridwidth-1-2"]
# ce qui intéressant, c'est 
# combien de fois on a appelé greater
counter

# %% [markdown]
# ## opérateurs bitwise
#
# * opérateurs dits *bitwise*:
#   * `&` - `|` : **et** et **ou** logique, respectivement
#   * `^` : **xor**
#   * `~` : **not** 
# * on les a aussi déjà rencontrés avec les ensembles
#
# ````{admonition} important pour `pandas`
# :class: attention
#
# ça semble anecdotique, mais ces opérateurs sont **super utilisés** notamment en pandas !
# ````

# %% tags=["gridwidth-1-2"]
a = 0b111100 
b = 0b110011

# %% tags=["gridwidth-1-2"]
bin(a | b)

# %% tags=["gridwidth-1-2"]
bin(a & b)

# %% [markdown]
# ## POO : opérateurs redéfinis 
#
# tous ces opérateurs peuvent être **redéfinis**
#
# * c'est le propos des 'méthodes magiques' 
# * que l'on verra à propos des classes
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

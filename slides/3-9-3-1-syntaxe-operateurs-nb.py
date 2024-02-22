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
# ## if elif else (l'instruction)

# %% [markdown] cell_style="split"
# L'instruction conditionnelle en Python:
#
# ```
# if <test1>:
#     <statement1>
# elif <test2>:
#     <statement2>
# elif <test3>:
#     <statement3>
# else:
#     <statement4>
# ```

# %% [markdown] cell_style="split"
# * évaluation dite "paresseuse"
# * si un test est vrai, 
#   * l'instruction est exécutée
#   * le `if` est terminé
# * `else` est exécuté
#   * ssi tous les tests sont faux

# %% [markdown] slideshow={"slide_type": "slide"}
# ### if elif else - exemple

# %% cell_style="split"
def appreciation(note):
    if note >= 16:
        return "félicitations"
    elif note >= 14:
        return "compliments"
    elif note >= 12:
        return "encouragements"
    elif note >= 10:
        return "passable"
    else:
        return "insuffisant" 


# %% cell_style="split"
print(appreciation(15.5))

# %% cell_style="split"
print(appreciation(11.5))

# %% [markdown]
# **Note**: pas de *switch* ou autres *case* en Python.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### digression : instructions *vs* expressions

# %% [markdown] cell_style="split"
# * `if .. elif .. else` est une **instruction**
# * une instruction est **exécutée**
# * et ne retourne rien

# %% [markdown] cell_style="split"
# * `note >= 16` est une **expression**
# * une expression **retourne** un résultat 
#   * après avoir été **évaluée**
# * peuvent être combinées / imbriquées
#   * ex: `fonction(a[0] == b)`
#

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# Instructions:
#
# * `variable = ...`
# * `if ...`
# * `for i in iterable ...`
# * `def ...`
# * `import ...`
#

# %% [markdown] cell_style="split" slideshow={"slide_type": "fragment"}
# Expressions:
#
# * `variable`
# * `variable.attribut`
# * `(a is b) and (c**2 == 25))`
# * `fonction(arg1, ...)` 

# %% [markdown] slideshow={"slide_type": "slide"}
# ### évaluation du test

# %% [markdown]
# * les `<test>` sont bien entendu des **expressions**
# * qui peuvent retourner autre chose qu'un booléen
#   * nombres: seul **zéro** (`0` ou `0.`) est considéré comme `False`
#   * chaines, containers: seul l'**objet vide** est considéré comme `False`
#   * autres cas: voir `bool()`

# %% cell_style="split" slideshow={"slide_type": "slide"}
liste = []
if liste:
    print("bingo")

# %% cell_style="split"
liste.append(12)
if liste:
    print("bingo")

# %% cell_style="split" slideshow={"slide_type": "fragment"}
entier = 0
if entier:
    print("bingo")

# %% cell_style="split"
entier = -3
if entier:
    print("bingo")

# %% cell_style="split" slideshow={"slide_type": "fragment"}
bool([])

# %% cell_style="split"
bool([1])

# %% cell_style="split" slideshow={"slide_type": "fragment"}
bool(0)

# %% cell_style="split"
bool(1)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### évaluation paresseuse

# %% [markdown]
# * lors de l'exécution du `if`, seuls les tests nécessaires sont évalués
# * important, car une expression peut faire un **effet de bord**

# %% cell_style="split" slideshow={"slide_type": ""}
# une fonction avec side-effect
counter = 0

def greater(a, b):
    global counter
    counter += 1 
    return a >= b


# %% cell_style="split"
def appreciation(note):
    if greater(note, 16):
        return "félicitations"
    elif greater(note, 14):
        return "compliments"
    elif greater(note, 12):
        return "encouragements"
    elif greater(note, 10):
        return "passable"
    else:
        return "insuffisant"


# %%
print(f"avant: counter={counter}")
print(appreciation(15))
print(f"après: counter={counter}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `if` (l'expression) 

# %% [markdown]
# * il existe aussi une **expression**   
#   permettant de faire quelque chose comme *if .. then .. else ..*
#
# ```
#    <exp_1> if <test> else <exp_2>
# ```
#
# * se rapproche de `<test> ? <exp_1> : <exp_2>` en C ou JavaScript..

# %%
note = 8

# comme c'est une expression, je peux par exemple
# la passer à une fonction
print("suffisant" if note >= 10 else "insuffisant")

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

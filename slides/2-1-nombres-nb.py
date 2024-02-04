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
#     title: nombres
#   rise:
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown] slideshow={"slide_type": ""}
# # les nombres

# %% [markdown] slideshow={"slide_type": "slide"}
# ## types de base `int`, `float`, `complex`
#
# * les `int` ont une précision illimitée
#   * Python peut calculer nativement

# %%
92857234957203457234572203957 * 948572349572039457029347529347

# %% [markdown]
# ceux qui ont eu à faire ça en C apprécieront

# %% [markdown] slideshow={"slide_type": "slide"}
# ### nombres : division

# %% tags=["gridwidth-1-3"]
# division exacte/flottante
8 / 5

# %% cell_style="split" slideshow={"slide_type": ""} tags=["gridwidth-1-3"]
# division entière (quotient)
8 // 5

# %% cell_style="split" tags=["gridwidth-1-3"]
# reste div. entière
8 % 5

# %% [markdown] slideshow={"slide_type": "slide"}
# ### nombres : opérateurs

# %% cell_style="split" slideshow={"slide_type": ""} tags=["gridwidth-1-3"]
# la division entière (quotient)
# fonctionne aussi 
# avec les flottants

8.5 // 4.5

# %% cell_style="split" slideshow={"slide_type": ""} tags=["gridwidth-1-3"]
# pareil pour le reste / modulo

8.5 % 4.5

# %% slideshow={"slide_type": ""} tags=["gridwidth-1-3"]
# bcp d'autres opérations disponibles
# et notamment:

2 ** 32         # puissance

# %% [markdown]
# ````{admonition} une cheatsheet
#
# à bookmarker: [une cheat sheet avec la liste des opérateurs en Python](https://cheatography.com/nouha-thabet/cheat-sheets/python-operators-and-booleans/)
#
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ### conversions

# %% slideshow={"slide_type": ""}
int(234.5)      # cast float ➔ int

# %% [markdown]
# ````{admonition} à retenir !
#
# un **type** en Python est aussi une **usine à objets**,  
# il peut être utilisé comme une fonction  
# ici l'appel `int(234.5)` consiste à appeler le type `int`  
# pour fabriquer un objet,  de type `int` donc, à partir de la valeur `234.5`
# ````

# %% [markdown]
# ````{admonition} moins crucial
# :class: tip small-admonition
#
# il existe aussi des fonctions `floor()` et `ceil()` dans le module `math`  
# toutefois la méthode ci-dessus est plus générale, elle s'applique à tous les types en Python
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ### nombres complexes

# %% tags=["gridwidth-1-3"]
# pour écrire un complexe
# il faut utiliser j et non pas i

1j * 1j

# %% tags=["gridwidth-1-3"]
a = 3 + 4j

# partie réelle
a.real

# %% tags=["gridwidth-1-3"]
# partie imaginaire
a.imag          

# %% [markdown]
# ````{admonition} les attributs, encore..
#
# remarquez qu'ici à nouveau, le terme `a.real` consiste à rechercher l'**attribut** `real` dans l'objet (désigné par) `a`
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le module `math`

# %% cell_style="split"
# pour anticiper un peu
# sur les listes...
# ici on veut les 6 derniers
# symboles dans le module math

import math
dir(math)[-6:]

# %% cell_style="split"
math.tau

# %% cell_style="split"
math.sin(math.pi)

# %% [markdown]
# ````{admonition} exo: entrainez-vous à chercher dans google
#
# entraînez vous à trouver rapidement la doc de ce module dans google en cherchant par exemple "`python module math`"
#
# <https://www.google.com/search?q=python+module+math>

# %% [markdown]
# ````{admonition} décortiquons un peu
# :class: small-admonition
#
# après l'import, la variable `math` désigne donc un objet de type `module`  
# et à nouveau, l'écriture `math.tau` consiste à rechercher l'attribut `tau` dans cet objet module  
# et pareil exactement pour `math.sin`, qui désigne … un objet fonction
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ### en hexa, binaire, octal

# %% [markdown]
# pour créer des entiers sous forme littérale, dans d'autres bases

# %% tags=["gridwidth-1-3"]
# hexadécimal
0xff

# %% tags=["gridwidth-1-3"]
# binaire
0b11111111

# %% tags=["gridwidth-1-3"]
# octal
0o377

# %% [markdown] slideshow={"slide_type": "slide"}
# ### sous forme hexa, binaire, octale

# %% [markdown]
# dans l'autre sens, trouver la représentation en base *n*  
# sous forme de chaine de caractères du coup

# %% cell_style="center" tags=["gridwidth-1-3"]
hex(255)    # traduire en hexa (-> str)`

# %% cell_style="center" tags=["gridwidth-1-3"]
bin(255)    # traduire en binaire (-> str)

# %% cell_style="center" tags=["gridwidth-1-3"]
oct(255)    # traduire en octal (-> str)

# %% [markdown]
# ````{admonition} fonctions prédéfinies ou *builtin*
#
# remarquez que nous n'avons pas défini les variables `hex`, `bin` et `oct`  
# ce sont des fonctions *prédéfinies*, connues de Python **dès le lancement**  
# le terme anglais pour désigner de telles fonctions est *builtin*
#
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ## booléens

# %% cell_style="split" slideshow={"slide_type": ""}
# True c'est presque exactement 1
True == 1

# %% cell_style="split"
# et False presque 0
False == 0

# %% cell_style="split" slideshow={"slide_type": ""}
3 + True

# %% cell_style="split"
3 + False

# %% cell_style="split"
# presque..
type(True)

# %% cell_style="split"
type(1)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### booléens et tests (1)

# %% cell_style="split"
# on peut - bien sûr - faire un `if`
# (ou un while) sur un booléen
a = 3
b = 4

type(a == b)

# %% cell_style="split"
# sujet du if = booléen

if a == b:
    print("pareils")
else:
    print("différents")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### booléens et tests (2)

# %% cell_style="split"
# mais aussi : avec n'importe quoi d'autre

if a:
    print("pas faux")

# %% cell_style="split"
# en fait équivalent à ceci:

if bool(a):
    print("pas faux")

# %% [markdown]
# ````{admonition} xxx
#
# on en reparlera, mais les valeurs "fausses" correspondent à un **nombre nul**, ou à un **container vide** (liste, chaine, ..)
#
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ## conversions

# %% [markdown]
# * à nouveau, c'est la **mécanique générale** pour convertir entre types de données:

# %% cell_style="split"
# si on appelle int() on convertit en entier
int(3.4)

# %% cell_style="split"
# si on appelle bool() on convertit en booléen

bool(3.4)

# %% cell_style="split"
# un nombre nul est "faux"
bool(0)

# %% cell_style="split"
# une chaine vide est "fausse"
bool("")

# %% cell_style="split"
# un nombre non nul est "vrai"
bool(1)


# %% cell_style="split"
# une chaine non vide - même avec 
# un seul espace - est "vraie"
bool(" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### opérateurs usuels `and` `or` et `not` (1)

# %% [markdown]
# * 99% du temps on utilise tout simplement les opérateurs `and`, `or` et `not`

# %% cell_style="split"
a, b = 1, 2

if 0 <= a and a <= b:
    print("YES")

# %% cell_style="split"
# on peut même parfois s'en passer
# complètement
if 0 <= a <= b:
    print("YES")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### opérateurs usuels `and` `or` et `not` (2)

# %% [markdown]
# le `not` permet des syntaxes plutôt lisibles
#
# * `x is not y`
# * `x not in y`

# %% [markdown]
# et pour l'illustrer commençons par créer ceci

# %% cell_style="split"
a = b = [1, 2]

# %% cell_style="split"
c = [1, 2]

# %% slideshow={"slide_type": "slide"}
# %load_ext ipythontutor

# %% cell_style="center"
# %%ipythontutor curInstr=2

a = b = [1, 2]
c = [1, 2]

# %% [markdown]
# ````{admonition} xxx
#
# à ce stade on a créé deux objets liste distincts
#
# * le premier désigné par a et b
# * le second désigné par c
#
# ````

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# du coup on peut écrire des choses comme

# %% cell_style="split"
a is b

# %% cell_style="split"
# la syntaxe est OK
a is not b

# %% cell_style="split"
a is c

# %% cell_style="split"
a is not c

# %% cell_style="split"
a == c

# %% cell_style="split"
a != c

# %% [markdown] slideshow={"slide_type": "slide"}
# ou encore comme

# %% cell_style="split"
1 in a

# %% cell_style="split"
# la syntaxe est OK
1 not in a

# %% cell_style="split"
3 not in a

# %% cell_style="split"
# possible aussi mais vilain
# et jamais employé en pratique
not 3 in a

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### booléens - avertissement

# %% [markdown] tags=["level_intermediate"]
# * attention à ne pas confondre
# * les opérations bit à bit avec les opérations booléennes

# %% slideshow={"slide_type": "-"} tags=["level_intermediate"]
# calculons le XOR de deux booléens

a, b = True, True

print("a", bool(a), "b", bool(b), "a^b", bool(a^b))

# %% slideshow={"slide_type": ""} tags=["level_intermediate"]
a, b = 1, 2

# on pourrait penser, puisque a et b sont 'vrais'
# qu'on devrait obtenir le même résultat que ci-dessus
# mais 1 ^ 2 -> 3

print("a", bool(a), "b", bool(b), "a^b", bool(a^b))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## l'encodage des flottants

# %% [markdown]
# * représentés en machine comme des fractions en base 2
# * le plus souvent une approximation
#   * quand pas une fraction binaire exacte
# * pas une spécificité de Python
#   * IEE-754: [WikiPedia](https://en.wikipedia.org/wiki/IEEE_754) - [interactif **64bits**](http://www.binaryconvert.com/convert_double.html)

# %% slideshow={"slide_type": "-"}
# flottant = imprécision structurelle !
0.1 + 0.2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `float` = 64 bits

# %% [markdown]
# * sur une machine 64 bits, un float est encodé en double précision, i.e. avec:
#   * 1 bit de signe
#   * 11 bits pour représenter l'exposant
#   * 52 bits pour représenter la mantisse

# %% cell_style="split"
import sys
sys.float_info

# %% [markdown] cell_style="split"
# **à retenir**: sur 64 bits  
# l' erreur relative est de l'ordre de  
# $10^{-15}$ / $10^{-16}$

# %% [markdown] slideshow={"slide_type": "slide"}
# ### arrondis

# %% [markdown]
# * Python arrondit les floats pour les encoder ([convertisseur](http://www.binaryconvert.com/convert_double.html))
# * ce qui provoque des erreurs d'arrondi
# * de plus, l'affichage **aussi** fait des arrondis
# * ce que l’on voit n’est pas forcément la représentation réelle

# %% cell_style="split"
0.1, 0.2

# %% cell_style="split"
0.3

# %%
0.1 + 0.2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### pas spécifique à Python

# %% [markdown] cell_style="center"
# * pas un problème spécifique à Python
# * si vous ne faites pas de l’analyse numérique
#   * ce problème n’a probablement aucun impact pour vous
# * sinon, vous êtes déjà au courant
#   * et vous savez notamment qu'il ne faut pas tester avec une égalité stricte
#   * mais plutôt avec un *presque égal* : utiliser `math.isclose`

# %% cell_style="split"
0.3 == 0.1+0.2


# %% cell_style="split"
import math

math.isclose(0.3, 0.1+0.2)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### contournements

# %% [markdown]
# ##### pour contourner
#
# * le [module `decimal`](https://docs.python.org/3/library/decimal.html), pour travailler sur des nombres décimaux
#   * avec plus de précision et de contrôle qu’avec le type float
# * le [module `fractions`](https://docs.python.org/3/library/fractions.html) permet de travailler sur des rationnels

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemples - `decimal`

# %% cell_style="split"
from decimal import Decimal
x = Decimal('0.1') + Decimal('0.2')

# %% cell_style="split"
x == Decimal('0.3')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemples - `fractions`

# %% cell_style="center"
from fractions import Fraction
x = Fraction(1, 10) + Fraction(2, 10)
x

# %% cell_style="split"
x == Fraction(3, 10)

# %% cell_style="split"
x == 0.3

# %% [markdown]
# ## plus exotique

# %% [markdown] slideshow={"slide_type": "slide"} tags=[]
# ### opérations *bitwise*

# %%
y = 4
y | 2      # bitwise OR de 0100 (4) et 0010 (2)

# %%
y & 2      # bitwise AND de 0100 (4) et 0010 (2)

# %%
y & 15     # bitwise AND de 0100 (4) et 1111 (15)

# %%
~ y        # bitwise NOT - en pratique ~x == -(x+1)

# %% [markdown]
# * rarement utile d’utiliser les opérations bitwise en Python usuel
# * mais par contre **très utile** avec numpy et pandas  
#   pour manipuler notamment les masques

# %% [markdown] slideshow={"slide_type": "slide"} tags=[]
# ### décalages

# %% cell_style="split" tags=[]
x = 3
y = x << 10 # décalage à gauche
y

# %% cell_style="split" tags=[]
2**11 + 2**10

# %% tags=[]
x          # l'argument n'est pas modifié

# %% cell_style="split" tags=[]
y >> 3     # décalage à droite

# %% cell_style="split" tags=[]
2**8 + 2**7

# %% [markdown]
# ****

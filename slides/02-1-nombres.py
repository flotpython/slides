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
#     title: nombres
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% [markdown] slideshow={"slide_type": ""}
# # les nombres

# %%
from plan import plan; plan("types", "nombres")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## types de base `int`, `float`, `complex`
#
# * conversion automatique si nécessaire
# * les `int` ont une précision illimitée
#   * Python peut calculer nativement

# %%
92857234957203457234572203957 * 948572349572039457029347529347

# %% [markdown]
# * ceux qui ont eu à faire ça en C apprécieront

# %% [markdown] slideshow={"slide_type": "slide"}
# ### nombres : division

# %%
# division exacte/flottante
5 / 2           

# %% cell_style="split" slideshow={"slide_type": "fragment"}
# division entière
8 // 3          

# %% cell_style="split" slideshow={"slide_type": "fragment"}
# division entière
8.0 // 3        

# %% [markdown] slideshow={"slide_type": "slide"}
# ### nombres : opérateurs 

# %% cell_style="split"
# reste div. entière
5 % 3       

# %% cell_style="split" slideshow={"slide_type": "fragment"}
# reste div. entière
5 % 1.5       

# %% slideshow={"slide_type": "fragment"}
2 ** 32         # puissance

# %% slideshow={"slide_type": "fragment"}
int(234.5)      # cast float ➔ int

# %% [markdown] slideshow={"slide_type": "slide"}
# ### nombres complexes

# %%
1j * 1j         # nombres complexes

# %%
a = 3 + 4j
a.real          # partie réelle

# %%
a.imag          # partie imaginaire

# %% [markdown] slideshow={"slide_type": "slide"}
# ### en hexa, binaire, octal

# %%
0xff            # hexadécimal

# %%
0b11111111      # binaire

# %%
0o377           # octal

# %% [markdown] slideshow={"slide_type": "slide"}
# ### sous forme hexa, binaire, octale

# %%
hex(255)    # traduire en hexa (-> str)

# %%
bin(255)    # traduire en binaire (-> str)

# %%
oct(255)    # traduire en octal (-> str)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### décalages

# %% cell_style="split"
x = 3
y = x << 10 # décalage à gauche 
y

# %% cell_style="split"
2**11 + 2**10

# %%
x          # l'argument n'est pas modifié

# %% cell_style="split"
y >> 3     # décalage à droite 

# %% cell_style="split"
2**8 + 2**7

# %% [markdown] slideshow={"slide_type": "slide"}
# ### opérations *bitwise*

# %%
y = 4
y | 2      # bitwise OR de 0100 (4) et 0010 (2) 

# %%
y & 2      # bitwise AND de 0100 (4) et 0010 (2)

# %%
y & 15     # bitwise AND de 0100 (4) et 1111 (15)

# %%
y ^ 15     # bitwise XOR de 0100 (4) et 1111 (15)

# %% [markdown]
# * rarement utile d’utiliser les opérations bitwise en Python
# * mieux vaut utiliser les structures de données fournies

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le module `math`

# %% cell_style="split"
# pour anticiper un peu 
# sur les listes...
# les 6 derniers symboles
# dans le module math
import math
dir(math)[-6:]

# %% cell_style="split"
math.tau

# %% cell_style="split"
math.sin(math.pi)

# %% [markdown]
# **Important**: Entraînez vous aussi à trouver la doc dans google:
#
# https://www.google.com/search?q=python+module+math

# %% [markdown] slideshow={"slide_type": "slide"}
# ## booléens

# %% cell_style="split" slideshow={"slide_type": "fragment"}
True == 1

# %% cell_style="split"
False == 0

# %% cell_style="split" slideshow={"slide_type": "fragment"}
3 + True

# %% cell_style="split"
3 + False

# %% [markdown] slideshow={"slide_type": "slide"}
# ### booléens et tests (1)

# %% cell_style="split"
# on peut faire un `if`
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

# %% [markdown] slideshow={"slide_type": "slide"}
# ## conversions

# %% [markdown]
# * c'est la **mécanique générale** pour convertir entre types de données:

# %% cell_style="split"
# si on appelle int() on convertit en entier
int(3.4)

# %% cell_style="split"
# si on appelle bool() on convertit en booléen
bool(3.4)

# %% cell_style="split"
bool(0)

# %% cell_style="split"
bool("")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### booléens - épilogue

# %% [markdown]
# * attention à ne pas confondre
# * les opérations bit à bit avec les opérations booléennes

# %% slideshow={"slide_type": "-"}
a = True; b = True
print("a", bool(a), "b", bool(b), "a^b", bool(a^b))

# %% slideshow={"slide_type": "fragment"}
a = 1; b = 2
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
0.1 + 0.2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `float` = 64 bits

# %% [markdown]
# * sur une machine 64 bits, un float est encodé en double précision, i.e. avec:
#   * 1 bit de signe
#   * 11 bits pour représenter l'exposant
#   * 52 bits pour représenter la mantisse 

# %%
import sys
sys.float_info

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

# %% [markdown]
# * pas un problème spécifique à Python
# * si vous ne faites pas de l’analyse numérique
#   * ce problème n’a probablement aucun impact pour vous
# * sinon, vous êtes déjà au courant

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

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour aller plus loin

# %% [markdown]
# * Tutoriel Python
#   * https://docs.python.org/3/tutorial/floatingpoint.html
# * The Perils of Floating Point by Bruce M. Bush
#   * http://www.lahey.com/float.htm

# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: nombres
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": ""}
# # les nombres

# %%
from plan import plan; plan("types", "nombres")

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## types de base `int`, `float`, `complex`
#
# * conversion automatique si nécessaire
# * les `int` ont une précision illimitée
#   * Python peut calculer nativement

# %% run_control={"frozen": false, "read_only": false}
92857234957203457234572203957 * 948572349572039457029347529347

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * ceux qui ont eu à faire ça en C apprécieront

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### nombres : division

# %% run_control={"frozen": false, "read_only": false}
# division exacte/flottante
5 / 2           

# %% cell_style="split" run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "fragment"}
# division entière
8 // 3          

# %% cell_style="split" run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "fragment"}
# division entière
8.0 // 3        

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### nombres : opérateurs 

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# reste div. entière
5 % 3       

# %% cell_style="split" run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "fragment"}
# reste div. entière
5 % 1.5       

# %% run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "fragment"}
2 ** 32         # puissance

# %% run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "fragment"}
int(234.5)      # cast float ➔ int

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### nombres complexes

# %% run_control={"frozen": false, "read_only": false}
1j * 1j         # nombres complexes

# %% run_control={"frozen": false, "read_only": false}
a = 3 + 4j
a.real          # partie réelle

# %% run_control={"frozen": false, "read_only": false}
a.imag          # partie imaginaire

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### en hexa, binaire, octal

# %% run_control={"frozen": false, "read_only": false}
0xff            # hexadécimal

# %% run_control={"frozen": false, "read_only": false}
0b11111111      # binaire

# %% run_control={"frozen": false, "read_only": false}
0o377           # octal

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### sous forme hexa, binaire, octale

# %% run_control={"frozen": false, "read_only": false}
hex(255)    # traduire en hexa (-> str)

# %% run_control={"frozen": false, "read_only": false}
bin(255)    # traduire en binaire (-> str)

# %% run_control={"frozen": false, "read_only": false}
oct(255)    # traduire en octal (-> str)

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### décalages

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
x = 3
y = x << 10 # décalage à gauche 
y

# %% cell_style="split"
2**11 + 2**10

# %% run_control={"frozen": false, "read_only": false}
x          # l'argument n'est pas modifié

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
y >> 3     # décalage à droite 

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
2**8 + 2**7

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### opérations *bitwise*

# %% run_control={"frozen": false, "read_only": false}
y = 4
y | 2      # bitwise OR de 0100 (4) et 0010 (2) 

# %% run_control={"frozen": false, "read_only": false}
y & 2      # bitwise AND de 0100 (4) et 0010 (2)

# %% run_control={"frozen": false, "read_only": false}
y & 15     # bitwise AND de 0100 (4) et 1111 (15)

# %% run_control={"frozen": false, "read_only": false}
y ^ 15     # bitwise XOR de 0100 (4) et 1111 (15)

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * rarement utile d’utiliser les opérations bitwise en Python
# * mieux vaut utiliser les structures de données fournies

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### le module `math`

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# pour anticiper un peu 
# sur les listes...
# les 6 derniers symboles
# dans le module math
import math
dir(math)[-6:]

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
math.tau

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
math.sin(math.pi)

# %% [markdown] run_control={"frozen": false, "read_only": false}
# **Important**: Entraînez vous aussi à trouver la doc dans google:
#
# https://www.google.com/search?q=python+module+math

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## booléens

# %% cell_style="split" slideshow={"slide_type": "fragment"}
True == 1

# %% cell_style="split"
False == 0

# %% cell_style="split" slideshow={"slide_type": "fragment"}
3 + True

# %% cell_style="split"
3 + False

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
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

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
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

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * attention à ne pas confondre
# * les opérations bit à bit avec les opérations booléennes

# %% run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "-"}
a = True; b = True
print("a", bool(a), "b", bool(b), "a^b", bool(a^b))

# %% run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "fragment"}
a = 1; b = 2
print("a", bool(a), "b", bool(b), "a^b", bool(a^b))

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## l'encodage des flottants

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * représentés en machine comme des fractions en base 2
# * le plus souvent une approximation
#   * quand pas une fraction binaire exacte
# * pas une spécificité de Python
#   * IEE-754: [WikiPedia](https://en.wikipedia.org/wiki/IEEE_754) - [interactif **64bits**](http://www.binaryconvert.com/convert_double.html)

# %% run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "-"}
0.1 + 0.2

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### `float` = 64 bits

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * sur une machine 64 bits, un float est encodé en double précision, i.e. avec:
#   * 1 bit de signe
#   * 11 bits pour représenter l'exposant
#   * 52 bits pour représenter la mantisse 

# %% run_control={"frozen": false, "read_only": false}
import sys
sys.float_info

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### arrondis

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * Python arrondit les floats pour les encoder ([convertisseur](http://www.binaryconvert.com/convert_double.html))
# * ce qui provoque des erreurs d'arrondi
# * de plus, l'affichage **aussi** fait des arrondis
# * ce que l’on voit n’est pas forcément la représentation réelle

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
0.1, 0.2

# %% cell_style="split"
0.3

# %% run_control={"frozen": false, "read_only": false}
0.1 + 0.2

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### pas spécifique à Python

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * pas un problème spécifique à Python
# * si vous ne faites pas de l’analyse numérique
#   * ce problème n’a probablement aucun impact pour vous
# * sinon, vous êtes déjà au courant

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### contournements

# %% [markdown] run_control={"frozen": false, "read_only": false}
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

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## pour aller plus loin

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * Tutoriel Python
#   * https://docs.python.org/3/tutorial/floatingpoint.html
# * The Perils of Floating Point by Bruce M. Bush
#   * http://www.lahey.com/float.htm

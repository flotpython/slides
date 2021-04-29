# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     formats: py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: 'numpy - shape & type '
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# </div>

# %% slideshow={"slide_type": "-"}
from plan import plan_extras; plan_extras("numpy", "dimension 1")

# %% [markdown] slideshow={"slide_type": "slide"}
# # intro à numpy 

# %% [markdown]
# ## pourquoi `numpy`

# %% [markdown]
# la librairie numpy est **très** utilisée pour les traitements gourmands en calculs, car
#
# * elle est **beaucoup plus efficace** que Python "*de base* " pour cet usage,
# * même si elle est un tout petit peu moins générale

# %% [markdown] slideshow={"slide_type": "slide"}
# la limitation concerne le fait que **les tableaux sont homogènes**
#
# * en première approximation : tous les éléments ont le même type
# * c'est cela qui permet d'avoir un code optimisé (tous les éléments sont alignés, les accès sont directs)
# * et en pratique, pour les calculs scientifiques ce n'est **pas un problème**

# %% [markdown] slideshow={"slide_type": "slide"}
# # pourquoi `matplotlib`

# %% [markdown]
# * c'est une librairie de visualisation de données 2D/3D
# * au départ visualisations statiques 
#   * à la gnuplot, un jeu de données = un graphique à imprimer
# * a évolué vers la visualisation interactive

# %% slideshow={"slide_type": "slide"}
# ces abréviations sont totalement standard
import numpy as np
import matplotlib.pyplot as plt

# %%
### initialisation matplotlib pour notebook
# préférez utiliser %matplotlib notebook
# mais qui n'est pas utilisable en mode 'slides'
# %matplotlib inline
# interactive on : pas besoin d'appeler figure() et show()
plt.ion()

# %% [markdown] slideshow={"slide_type": "slide"}
# # plan

# %% [markdown] slideshow={"slide_type": ""}
# * dimension 1
#   * typage
#   * programmation vectorielle
# * dimensions supérieures
#   * slicing
#   * broadcasting
# * algèbre linéaire
# * types structurés (*structured arrays*)

# %% [markdown] slideshow={"slide_type": "slide"}
# # dimension 1

# %% [markdown]
# créer un objet `np.array` de dimension 1
#
# * par exemple à partir d'une liste
# * et beaucoup d'autres méthodes

# %%
powers = np.array( [1, 2, 4, 8, 16, 32])
powers, powers.dtype

# %% [markdown] slideshow={"slide_type": "slide"}
# ### erreur fréquente

# %% [markdown]
# attention à bien passer une liste et pas directement les nombres

# %%
try: a = np.array(1, 2, 3, 4)    # pas correct
except Exception as e: print("OOPS", e)


# %%
a = np.array([1,2,3,4]); a # OK

# %% [markdown] slideshow={"slide_type": "slide"}
# ## choisir le type

# %% [markdown]
# sans indication de notre part numpy va décider tout seul du type

# %% cell_style="split"
# les entrées peuvent être homogènes
foo = np.array([True, False, True])
foo.dtype

# %% cell_style="split"
# ou pas
foo = np.array([True, 1, 2.5, 4 + 5j])
foo.dtype

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le type est important !

# %% [markdown]
# comme dans des langages plus classiques, on peut perdre de la précision

# %% cell_style="split"
# numpy va créer 
# un tableau d'entiers
entiers = np.array([1, 2, 3])
entiers.dtype

# %% cell_style="split"
# du coup ATTENTION !
# perte de précision...
entiers[0] = 3.14
entiers

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le type : attribut `dtype`

# %% [markdown]
# on peut spécifier un type à la création  
# et du coup c'est **souvent une bonne idée**

# %%
# en spécifiant le paramètre dtype
squares = np.array( [1, 2, 4, 9, 16], dtype=np.float64)
squares, squares.dtype

# %%
squares[0] = 1.5
squares

# %% [markdown] slideshow={"slide_type": "slide"}
# ## types disponibles

# %% [markdown]
# [voyez la liste complète https://docs.scipy.org/doc/numpy/user/basics.types.html](https://docs.scipy.org/doc/numpy/user/basics.types.html) 
#
# ce qu'il faut en retenir:
#
# * bool, int, uint, float et complex
# * de tailles diverses pour vous permettre d'optimiser la mémoire réellement utilisée
# * ces types existent en tant que tel (hors de tableaux)

# %% slideshow={"slide_type": "slide"}
# un entier qui vaut 1 sur 1 seul octet, c'est possible !
np_1 = np.int8(1)
# l'équivalent en python natif
py_1 = 1
# il y a bien égalité
np_1 == py_1

# %%
# mais ce ne sont bien entendu pas les mêmes objets
np_1 is py_1

# %% [markdown] slideshow={"slide_type": "slide"}
# ## création/initialisation

# %% [markdown]
# ## initialisation - constantes

# %%
np.zeros(10)

# %%
np.ones(10)

# %% [markdown] slideshow={"slide_type": "slide"}
# bien plus efficace que du Python 'pur'

# %%
# pur python
# %timeit [ 0. for i in range(10**7)]

# %%
# numpy
# %timeit np.zeros(10**7)

# %%
# pur python
from sys import getsizeof
getsizeof([ 0. for i in range(10**7)])

# %%
# numpy
getsizeof(np.zeros(10**7, dtype=np.int8))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## non-initialisé
#
# * [`np.empty`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.empty.html) permet d'allouer sans initialiser

# %%
# %timeit np.empty(10**7, dtype='float64')

# %%
# %timeit np.zeros(10**7, dtype='float64')

# %% [markdown]
# ### voir aussi `numpy.fill()`

# %%
a = np.empty(5, dtype=float)
a.fill(np.pi)
a

# %% [markdown] slideshow={"slide_type": "slide"}
# ## intervalle - `arange`

# %% [markdown]
# [`np.arange`]() ressemble à `range` de python

# %%
np.arange(10, 20, 2)

# %% [markdown] slideshow={"slide_type": "slide"}
# sauf qu'elle accepte des arguments flottants

# %%
np.arange(1.0, 2.5, 0.5)

# %% [markdown] slideshow={"slide_type": "slide"}
# et aussi bien sûr un argument `dtype`:

# %%
np.arange(1, 10, dtype=np.complex128)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## intervalle - `linspace`

# %% [markdown]
# * [`np.linspace`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html#numpy.linspace) 
# * pour *représenter* un intervalle 
# * avec un nombre de points spécifiés

# %%
np.linspace(0., 2., 5)

# %% [markdown] slideshow={"slide_type": "slide"}
# **très très** utile pour modéliser une fonction sur un intervalle

# %%
# 100 points pour remplir l'intervalle [0..6pi]
X = np.linspace(0., 6 * np.pi, 100)
# appliquer la fonction sin sur tous ces points
Y = np.sin(X)

# %% slideshow={"slide_type": "slide"}
plt.plot(X, Y);

# %% [markdown] slideshow={"slide_type": "slide"}
# ### comparaison `arange` et `linspace`

# %% [markdown]
# | `arange` | `linspace` |
# |--------|----------|
# | début (inclus) | début (inclus) |
# | fin(exclus) | fin (inclus par défaut) |
# | **espace** entre points | **nombre** de points |

# %% [markdown] slideshow={"slide_type": "slide"}
# ## intervalle `logspace` 

# %% [markdown]
# * [`np.logspace`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.logspace.html#numpy.logspace) parfois intéressant 
# * pour des échelles **logarithmiques**

# %%
np.logspace(base=2, start=4, stop=10, num=7)

# %%
# la base peut être un complexe si on veut
# ici je prends i**0, i**1, i**2, i**3
np.logspace(start=0, stop=4, base=1j, num=4, endpoint=False)

# %% [markdown]
# ### progression géométrique : `geomspace`

# %% [markdown]
# Je signale rapidement avec `geomspace` la possibilité de créer un échantillonage un peu similaire à `linspace` mais selon cette fois une progression géométrique. Il faut bien sûr prendre des bornes non nulles et de même signe :

# %%
X = np.geomspace(start=1/10, stop=10, num=11)

# %% [markdown] slideshow={"slide_type": "slide"}
# # programmation vectorielle

# %% [markdown] slideshow={"slide_type": "slide"}
# * appliquer une fonction sur tous les éléments d'un tableau
#   * on l'a vu déjà à l'instant avec `np.sin`
#   * toutes fonctions mathématiques usuelles supportées
# * ou combiner deux tableaux
#   * par exemple les ajouter
# * **sans** faire de **boucle** explicite

# %% [markdown] slideshow={"slide_type": "slide"}
# ## programmation vectorielle - plan
#
# 1. 1 fonction sur un tableau 
# 1. 1 opérateur entre 1 tableau et un scalaire
# 1. un opérateur entre 2 tableaux
# 1. cas particulier des opérations logiques
#
# ===
#
# * le cas 2. (tableau x scalaire) peut être vu
#   * comme un cas particulier de 3. (tableau x tableau)
# * c'est un cas particulier du broadcasting
#   * que l'on étudiera en détail plus loin

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fonction sur un tableau

# %% slideshow={}
# pour appliquer une fonction sur tout un tableau
X = np.linspace(-2., 2.)
Y = np.exp(X)
plt.plot(X, Y);

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fonction sur un tableau

# %%
# on peut préciser la sortie, c'est-à-dire 
# ranger les résultats dans un tableau déjà alloué
X = np.linspace(-2, 2., num=10)
# si on dispose déjà d'un tableau de la bonne taille
Y = np.empty(10)
np.exp(X, out=Y)
plt.plot(X, Y);

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fonction sur un tableau

# %% cell_style="split"
# en particulier on peut récrire dans X 
np.exp(X, out=X);

# %%
# et donc ici j'ai X == Y
X == Y

# %% cell_style="center"
np.all(X == Y)

# %% [markdown] cell_style="split"
# * très utile pour optimiser votre code
# * ordres de grandeur plus rapide
# * si vous faites plusieurs opérations à la suite
# * c'est utile de créer un nouveau tableau
# * mais seulement un!

# %% [markdown] slideshow={"slide_type": "slide"}
# ## scalaire & tableau

# %% [markdown] slideshow={}
# * De manière identique, on peut
# * faire toute opération avec une constante

# %%
X = np.linspace(0., 10., 3); X

# %% slideshow={}
3 * (X + 1) ** 2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exercice
#
# * dessiner un cercle avec matplotlib
# * utiliser `plt.plot`

# %% slideshow={"slide_type": "slide"}
R = 10
teta = np.linspace(0, 2*np.pi)
X = R * np.sin(teta)
Y = R * np.cos(teta)
plt.plot(X, Y);

# %% [markdown] slideshow={"slide_type": "slide"}
# ## opérations binaires
#
# * on peut aussi faire des opérations **binaires**
# * donc cette fois sur la base de **deux tableaux**
# * mais qui donc doivent avoir des **tailles compatibles**
#   * en première appoximation: tailles identiques
#   * on y reviendra (broadcasting)
# * attention que `*` fait une **multiplication**
#   * et pas un produit matriciel

# %% slideshow={"slide_type": "slide"}
x = np.logspace(base=2, start=0, stop=3, num=4); x

# %% slideshow={"slide_type": "-"}
y = np.logspace(base=2, start=10, stop=7, num=4); y

# %%
x * y

# %% [markdown] slideshow={"slide_type": "slide"}
# ## opérations logiques
#
# * même logique qu'opérations binaires

# %%
a = np.array( (1, 2, 3, 4) )
b = np.arange(1, 5)

# %%
compare = (a == b)
compare

# %%
compare.all()

# %% [markdown] slideshow={"slide_type": "slide"}
# * avec des tableaux de dimension 1
# * on a envie d'utiliser `all` et `any` (standard python)
# * pour synthétiser une seule valeur booléenne

# %%
all(a==b)

# %% slideshow={"slide_type": "-"}
a[0] = 10
# ne sont plus égaux
all(a==b)

# %%
# mais par contre il reste au moins une égalité
any(a==b)


# %% [markdown] slideshow={"slide_type": "slide"}
# #### dimensions supérieures

# %% [markdown]
# * pour comparer des tableaux de dimensions supérieures
# * les fonctions natives python comme `all` et `any` ne fonctionnent pas toujours
# * il est préférable d'utiliser les **méthodes** `all` et `any`

# %% [markdown]
# ```
# try:                   print("all(a==b)", all(a==b))
# except Exception as e: print("OOPS", e)
#
# OOPS The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `np.where`
#
# * Généralisation du [`if` expression conditionnelle](https://docs.python.org/3/reference/expressions.html#conditional-expressions)
# * [`np.where(condition, si_vrai, si_faux`)](https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exercice

# %% [markdown] cell_style="split"
# Soit la fonction à un élément

# %% [markdown] cell_style="split"
# $ f(x) =\begin{cases}x^2 & x <=1 \\2x-1 & x>1\end{cases} $

# %% cell_style="center"
def f(x):
   return x**2 if x <= 1 else 2*x - 1


# %% [markdown] slideshow={}
# on peut utiliser `matplotlib` avec des tableaux python natifs

# %% cell_style="center" slideshow={"slide_type": "slide"}
# en python natif
py_x = range(-5, 6)
py_y = [ f(x) for x in py_x ]

# %%
plt.plot(py_x, py_y);


# %% [markdown] slideshow={"slide_type": "slide"}
# * on vous demande d'implémenter une fonction identique
# * mais qui accepte en entrée un tableau numpy

# %%
def f(x):
   return x**2 if x <= 1 else 2 * x - 1

def fnp(x):
    return np.where(x<=1, x**2, 2*x-1)


# %% slideshow={"slide_type": "-"}
# pour vérifier votre résultat
x = np.linspace(-5, 5, 100)
y = fnp(x)
plt.plot(x, y);


# %% [markdown] slideshow={"slide_type": "slide"}
# **remarque**
#
# * pour résoudre cette classe de problèmes
# * on trouve parfois un style de programmation à base de masque

# %%
def fnp_mask(x):
    mask = x <= 1
    return mask * x**2 + (1-mask) * (x+1)


# %% [markdown] slideshow={"slide_type": "slide"}
# sinon les opérateurs logiques fonctionnent *presque* comme d'habitude

# %%
# on peut faire ceci
x = np.arange(-2, 3)
-1 <= x

# %%
# Mais pas ça
try: -1 <= x <= 1
except Exception as e: print("OOPS", e)

# %%
# il faut alors utiliser des opérateurs spécialisés
np.logical_and(-1 <= x, x <= 1)

# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control
#     formats: py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: 'numpy - slicing & broadcasting '
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

# %% slideshow={"slide_type": "slide"}
from plan import plan_extras; plan_extras("numpy", "supérieures")

# %% [markdown] slideshow={"slide_type": "slide"}
# # numpy - dimensions > 1

# %% slideshow={"slide_type": "-"}
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
plt.ion()

# %% [markdown]
# # conventions sur les indices des dimension

# %% [markdown]
# ## dimension 2: **lignes** x **colonnes**

# %%
np.zeros( (4, 8 ))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## dimension 3: **plans** x **lignes** x **colonnes**

# %%
np.ones( (2, 4, 8))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## en dimensions supérieures
#
# * les deux derniers éléments de la dimension
# * correspondent toujours aux lignes et colonnes

# %% slideshow={"slide_type": "-"}
np.zeros( (2, 1, 4, 5))

# %% [markdown] slideshow={"slide_type": "slide"}
# # résumé attributs

# %%
x = np.zeros( (3, 5, 7), dtype=np.float64)

# %% [markdown]
#
# | *attribut* | *signification* | *exemple* | 
# |------------|-----------------|-----------|
# | `shape` | tuple des longueurs | `(3, 5, 7)` |
# | `ndim` | nombre dimensions  | `3` | 
# | `size` | nombre d'éléments | `3*5*7` |
# | `dtype` | type de chaque élément | `np.float64` |
# | `itemsize` | taille en octets d'un élément | `8` |

# %% [markdown] slideshow={"slide_type": "slide"}
# # changement de forme

# %% [markdown]
# ## `reshape`
#
# Avec `reshape`, on peut
#
# * changer de forme
# * en fait on crée une **vue**
# * sur les mêmes données
# * les deux tableaux **partagent** les données

# %%
# profitons-en pour utiliser numpy.random
# et notamment `random_sample`
# qui renvoie des flottants dans `[0..1]`
x = np.random.random_sample(15); print(x)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exercice
#
# * que vaut `x.shape` ?

# %% [markdown]
# ## `reshape` et partage
#
# y est une vue sur les mêmes données que x

# %% slideshow={"slide_type": "slide"}
y = x.reshape( (3, 5)); 

# %% cell_style="split" slideshow={"slide_type": "-"}
# mais avec une autre géométrie
x.shape

# %% cell_style="split"
y.shape

# %% [markdown] slideshow={"slide_type": "slide"}
# * les deux `array` **partagent les données** sous-jacentes
# * on y reviendra

# %% slideshow={"slide_type": "-"}
x[0]=0.; y

# %% [markdown] slideshow={"slide_type": "slide"}
# * chaque tableau accès aux données via sa propre géométrie

# %%
y.shape

# %%
y[1, 0] = 1.; x

# %% [markdown] slideshow={"slide_type": "slide"}
# Évidemment il faut que la nouvelle forme convienne

# %%
try : x.reshape( (3, 6))
except Exception as e: print("OOPS", e)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `ravel`
#
# La fonction `ravel` permet d'*aplatir* n'importe quel tableau

# %%
a = np.random.random_sample( (2, 3, 4)); print (a)

# %%
print(np.ravel(a))

# %%
# pour tout array ceci est vrai
all(np.ravel(a) == a.reshape( (a.size,)))

# %% [markdown] slideshow={"slide_type": "slide"}
# ### impression avec `print()`

# %% [markdown]
# vous remarquerez que l'impression de gros tableaux montre les coins en tronquant le reste

# %%
big = np.arange(10**6).reshape( (100, 100, 100))
print(big)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### produits cartésiens et similaires
#
# * pour créer des tableaux sans passer par reshape, exemples
# * une image contenant un cercle
# * un tableau contenant 10*i + j
# * une grille en dimension 2
#   * pour plotter une fonction (x, y) -> z
# * le broadcasting (vu plus loin) est aussi pertinent

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `indices`

# %% [markdown]
# imaginez une construction du genre de
#
# ```
# a = np.empty( (n, m))
# for i in range(n):
#    for j in range(m):
#       a[i, j] = fonction(i, j)
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ce qui nous rappelle un peu en python 'natif' des boucles comme
#
# ```
# for i in range(len(liste)):
#     item = liste[i]
#     une_fonction(item, i)
# ```

# %% [markdown]
# dont on a dit qu'il était préférable de faire plutôt:
#
# ```
# for i, item in enumerate(liste):
#     une_fonction(item, i)    
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# `np.indices` joue - un peu - le même rôle que `enumerate` à cet égard:

# %% [markdown]
# * `indices( (2, 3) )` renvoie 2 tableaux (parce que dimension 2)
# * chacun de dimension `(2, 3)`
# * le premier contient l'indice en X et le second l'indice en Y

# %%
ix, iy = np.indices((2, 3))
for i in range(2):
    for j in range(3):
        print("{} x {} -> X: {} Y: {}"
              .format(i, j, ix[i, j], iy[i, j]))

# %% slideshow={"slide_type": "slide"}
N = 128
ix, iy = np.indices( (N, N))
image = ix**2 + iy**2
plt.imshow(image);

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `ix_` - produit cartésien

# %% [markdown]
# * la fonction `ix_` 
#  * réalise une sorte de produit cartésien économique
# * en renvoyant des tableaux dans une seule direction
# * qu'on peut ensuite combiner par broadcasting
# * on reverra tout ça en détail

# %% cell_style="split" slideshow={"slide_type": "slide"}
# un exemple en dimension 2
lines = np.arange(3)
print(lines)

# %% cell_style="split"
# pour l'instant c'est en dimension 1
columns = np.arange(5)
print(columns)

# %% cell_style="split"
# avec ix_ on retourne deux tableaux
# le premier c'est les lignes
X, Y = np.ix_(lines, columns)
print(X)

# %% cell_style="split"
# et le deuxieme les colonnes
print(Y)

# %% cell_style="center" slideshow={}
# la magie du broadcasting !
X * 10 **Y

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `meshgrid`
#

# %% [markdown]
# * la fonction `meshgrid` 
# * fait directement un produit cartésien
# * en plusieurs dimensions

# %%
# np.meshgrid?

# %% cell_style="split" slideshow={"slide_type": "slide"}
nx = np.linspace(0, 1, 3)
ny = np.linspace(10, 11, 3)

# %% cell_style="split"
# 
xi, yi = np.meshgrid(nx, ny)

# %% cell_style="split"
xi

# %% cell_style="split"
yi

# %% [markdown] slideshow={"slide_type": "slide"}
# utile par exemple pour
#
# * calculer une grille de coordonnées (x, y)
# * appliquer une fonction
# * pour la [représenter en 3d avec `mplot3d`](http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html)
#
# tp ?

# %% [markdown] slideshow={"slide_type": "slide"}
# # exercices 
#
# * circles
#   * centrer la figure
#   * ajouter des rayures
# * distributions
#   * génération d'une distribution uniforme / normale en 2d
# * by-the-tens
#   * création de tableaux où tab[i, j] = f(i, j)
#   * en utilisant plusieurs méthodes
# * dice
#   * énumérer les tirages de 3 ou 4 dés
#   * calculer les probabilités de chacun

# %% [markdown] slideshow={"slide_type": "slide"}
# # indexation simple

# %% [markdown]
# * indexation simple
#   * lorsque les **indices** sont des **entiers**
# * on peut aussi utiliser
#   * .. un ou des **tableaux** comme indices
#   * mais nous verrons cela plus tard

# %%
n = 5
a = np.arange(n*n).reshape( (n, n)); print(a)

# %% cell_style="split"
# avec un seul index on obtient naturellement une ligne
a[0]

# %% cell_style="split"
# qu'on peut a nouveau indexer
a[0][2]

# %%
# ou plus simplement indexer par un tuple
a[0, 2]

# %% slideshow={"slide_type": "slide"}
# On peut affecter des indices individuellement naturellement
a[0][1] = 101
a[0, 2] = 102
print(a)

# %%
# Ou toute une ligne
a[2] = np.arange(200, 205); print(a)

# %% [markdown] slideshow={"slide_type": "slide"}
# # slicing

# %%
# Grâce au slicing on peut aussi changer toute une colonne
a[:, 3] = range(300, 305); print(a)

# %%
# on pourrait aussi écrire a[1:6:3, :] = ...
a[1:6:3] = np.arange(400, 410).reshape(2, 5); print(a)

# %% [markdown] slideshow={"slide_type": "slide"}
# le slicing peut servir à extraire des blocs compacts:

# %%
b = np.arange(100).reshape(10, 10); print(b)

# %%
# un bloc au hasard dans b
print(b[2:5, 6:9])

# %% slideshow={"slide_type": "slide"}
c = 1000 + np.arange(49).reshape(7, 7); print(c)

# %%
# on remplace un bloc de c avec un bloc de même taille de b
c[1:4, 2:5] = b[2:5, 6:9]; print(c)

# %% slideshow={"slide_type": "slide"}
c = 1000 + np.arange(49).reshape(7, 7); print(c)

# %%
# les blocs de départ ou d'arrivée peuvent ne pas être compacts
c[::3, ::3] = b[2:5, 6:9]; print(c)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## différences majeures avec python natif
#
# * la taille d'un objet numpy est par définition constante
#   * on ne peut pas le déformer avec du slicing
# * une slice sur un objet numpy renvoie une **vue**
#   * c'est à dire qu'il y a partage

# %% [markdown] slideshow={"slide_type": "slide"}
# ### slicing et tailles  
#
# * les types de base python (ici: listes)
#   * sont élastiques
#   * et peuvent changer de taille lors du slicing
# * ce n'est pas le cas avec numpy
#   * la taille de l'objet reste fixe
#   * logique par rapport aux objectifs de performance

# %%
liste = list(range(6))
print("avant: {}".format(len(liste)))
liste[2:4] = range(10, 15)
print("après: {}".format(len(liste)))
liste

# %% [markdown] slideshow={"slide_type": "slide"}
# * bien entendu c'est différent avec les arrays numpy
# * il faut que la géométrie soit préservée

# %%
a = np.zeros( (4, 4))
# on peut remplacer une zone carrée de 1 x 1 par une zone de la même taille
a[ 2:3, 2:3] = np.ones( (1, 1))
print(a)

# %%
# mais si ça ne colle pas en terme de taille, boom !
try: a[ 2:3, 2:3] = np.ones( (1, 2))
except Exception as e: print("OOPS", e)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### slicing et partage

# %% [markdown]
# **ATTENTION** à cette embûche possible avec les slices

# %% cell_style="split"
l1 = [1, 2, 3]
# la slice l2 est 
# une **shallow copie**
l2 = l1[:2]
# on peut modifier l2
# sans toucher l1
l2[1] = 5
print('l1', l1)
print('l2', l2)

# %% cell_style="split"
a1 = np.array([1, 2, 3])
# la slice a2 est 
# **une vue**
a2 = a1[:2]
# du coup il y a partage !!
a2[1] = 5
print('a1', a1)
print('a2', a2)

# %% [markdown] slideshow={"slide_type": "slide"}
# # broadcasting
#
# lorsqu'on a vu la programmation vectorielle, on a vu
#
# * tableau et tableau (mêmes tailles)
# * tableau et scalaire

# %% [markdown]
# en fait le broadcasting est ce qui permet 
#
# * d'unifier le sens de ces deux opérations
# * et de donner du sens à des cas intermédiaires.

# %% [markdown] slideshow={"slide_type": "slide"}
# voir notebook optionnel

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemples en 2d

# %% [markdown] slideshow={"slide_type": "slide"}
# ### broadcasting (3, 5) et (1)

# %% cell_style="split" slideshow={"slide_type": "-"}
a = 100 * np.ones((3, 5), dtype=np.int32); print(a)

# %% cell_style="split"
b = 3; print(b)

# %% [markdown]
# ***

# %% cell_style="split"
c = a + b; print(c)

# %% cell_style="split"
print(c - a)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### broadcasting (3, 5) et (5)

# %% cell_style="split" slideshow={"slide_type": "-"}
print(a)

# %% cell_style="split"
b = np.arange(1, 6); print(b)

# %% [markdown] cell_style="center"
# ****

# %% cell_style="split"
c = a + b; print(c)

# %% cell_style="split"
print(c - a)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### broadcasting (3, 5) et (1, 5)

# %% cell_style="split" slideshow={"slide_type": "-"}
print(a)

# %% cell_style="split"
b = np.arange(1, 6).reshape(1, 5); print(b)

# %% [markdown]
# ***

# %% cell_style="split"
c = a + b; print(c)

# %% cell_style="split"
print(c - a)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### broadcasting (3, 5) et (3, 1)

# %% cell_style="split" slideshow={"slide_type": "-"}
print(a)

# %% cell_style="split"
b = np.arange(1, 4).reshape(3, 1); print(b)

# %% [markdown] cell_style="center"
# ****

# %% cell_style="split"
c = a + b; print(c)

# %% cell_style="split"
print(c - a)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### broadcasting (3, 1) et (1, 5)

# %% cell_style="split"
col = np.arange(3)[:, np.newaxis]; print(col)

# %% cell_style="split" slideshow={"slide_type": "-"}
line = np.arange(5); print(line)

# %% [markdown] cell_style="center"
# ****

# %% cell_style="split"
m = 100*(line+1) + col; print(m)

# %% [markdown] cell_style="split"
# * Remarquer qu'ici les **deux** entrées ont été étirées
# * pour atteindre une dimension commune

# %% [markdown] slideshow={"slide_type": "slide"}
# ## broadcasting - dimensions supérieures
#
# exemples de dimensions compatibles

# %% [markdown] cell_style="split"
# ```
# A   (2d array):  15 x 3 x 5
# B   (scalaire):           1
# Res (2d array):  15 x 3 x 5
# ```

# %% [markdown] cell_style="split"
# ```
# A   (3d array):  15 x 3 x 5
# B   (3d array):  15 x 1 x 5
# Res (3d array):  15 x 3 x 5
# ```

# %% [markdown] cell_style="split"
# ```
# A   (3d array):  15 x 3 x 5
# B   (2d array):       3 x 5
# Res (3d array):  15 x 3 x 5
# ```

# %% [markdown] cell_style="split"
# ```
# A   (3d array):  15 x 3 x 5
# B   (2d array):       3 x 1
# Res (3d array):  15 x 3 x 5
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# exemples de dimensions **non compatibles**

# %% [markdown] cell_style="split"
# ```
# A   (1d array):  3
# B   (1d array):  4 
# ```

# %% [markdown] cell_style="split" slideshow={"slide_type": "-"}
# ```
# A      (2d array):      2 x 1
# B      (3d array):  8 x 4 x 3 
# ```

# %% [markdown]
# * on ne peut broadcaster que de **1** vers n
# * si $p>1$ divise n, on ne **peut pas** broadcaster de p vers n 

# %% [markdown] slideshow={"slide_type": "slide"}
# # slicing & broadcasting
#
# ### slicing & broadcasting (3,5) vs (1)

# %% cell_style="split" slideshow={"slide_type": "-"}
a = 10 * np.ones((5, 7), dtype=np.int32); print(a)

# %% cell_style="split"
b = 3; print(b)

# %% [markdown]
# ***

# %% cell_style="split"
a[::2, ::2] = b; print(a)

# %% cell_style="split"
print(a[::2, ::2])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### slicing & broadcasting ctd

# %% cell_style="split" slideshow={"slide_type": "-"}
a = 10 * np.ones((5, 7), dtype=np.int32); print(a)

# %% cell_style="split"
b = np.arange(1, 5); print(b)

# %% [markdown] cell_style="center"
# ****

# %% cell_style="split"
a[::2, ::2] = b; print(a)

# %% cell_style="split"
print(a[::2, ::2])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### slicing & broadcasting ctd

# %% cell_style="split" slideshow={"slide_type": "-"}
a = 10 * np.ones((5, 7), dtype=np.int32); print(a)

# %% cell_style="split"
b = np.array([[1], [2], [3]]); print(b)

# %% [markdown]
# ***

# %% cell_style="split"
a[::2, ::2] = b; print(a)

# %% cell_style="split"
print(a[::2, ::2])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exercice
#
# implémenter `indices` à base de `arange`, slicing & broadcasting.

# %% [markdown] slideshow={"slide_type": "slide"}
# # références croisées, shallow et deep copies

# %% [markdown]
# avec les tableaux numpy
#
# * les mêmes caractéristiques qu'avec python natif
# * il est important de savoir quand les données sont partagées entre 2 arrays

# %% [markdown] slideshow={"slide_type": "slide"}
# ## partage complet

# %% [markdown]
# devrait être évident, mais ça va mieux en le redisant:
#
# * l'affectation
# * le passage de paramètres
#
# ne créent pas de copie.

# %% slideshow={"slide_type": "slide"}
a = np.arange(12)
b = a
a is b

# %% cell_style="split"
print("avant", b.shape)
a.shape = (3, 4)
print("après", b.shape)


# %% cell_style="split"
def foo(x):
    x[1, 1] = 20

foo(a)
print(b)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## *shallow* copie / views

# %% [markdown]
# * plusieurs instances de `np.array` peuvent partager les mêmes données.
# * on a déjà vu un exemple avec `reshape`

# %% cell_style="split"
print(b)

# %% cell_style="split"
c = a.reshape(6, 2)
c[1, 1] = 100
print(b)

# %% [markdown] slideshow={"slide_type": "slide"}
# l'objet `view` permet de créer un nouvel objet `array` qui partage les données

# %% cell_style="split"
v = a.view()
v is a

# %% cell_style="split"
v.base is a

# %% cell_style="center"
v.shape = (12,)
v[11] = 1000
a

# %% [markdown] slideshow={"slide_type": "slide"}
# * le slicing crée **une vue**
# * c'est comme cela qu'on peut **modifier un tableau** au travers d'une slice

# %% cell_style="split"
print(a)

# %% cell_style="split"
# on crée s une vue sur (un morceau de) a
s = a[:, 1:3]
# s[:] est une vue sur s
s[:] = 2000

print(a)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## *deep* copie

# %% [markdown]
# * la fonction [`np.copy`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.copy.html)
# * permet de faire une copie complète

# %% [markdown] slideshow={"slide_type": "slide"}
# # *stacking*

# %% [markdown]
# * jusqu'ici on a vu des fonctions qui préservent la taille
# * le stacking permet de créer un tableau plus grand
# * en (juxta/super)posant plusieurs tableaux

# %% [markdown]
# ### compatibilité
#
# il faut en général que
#
# * toutes les dimensions soient égales
# * sauf celle dans laquelle se fait le collage
# * exemple simple en 2d
#   * deux tableaux avec autant de colonnes l'un que l'autre
#   * donnent un tableau avec l1 + l2 lignes

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `hstack` et `vstack`

# %% cell_style="split" slideshow={"slide_type": "-"}
a = np.arange(1, 7).reshape(2, 3); print(a)

# %% cell_style="split"
b = 10 * np.arange(1, 7).reshape(2, 3); print(b)

# %% cell_style="split"
print(np.hstack( (a, b)))

# %% cell_style="split"
print(np.vstack ((a, b)))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## vertical stacking
#
# * Vertical = line = **premier** indice 
# * les autres dimensions doivent être égales

# %% cell_style="split" slideshow={"slide_type": "-"}
a = np.ones( (2, 3, 5)); print(a)

# %% cell_style="split"
b = np.zeros( (1, 3 , 5)); print(b)

# %%
print(np.vstack((a, b)))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## horizontal stacking
#
# * horizontal = colonnes = deuxième indice
# * à nouveau les autres dimensions doivent être égales

# %% cell_style="split" slideshow={"slide_type": "-"}
a = np.ones( (2, 3, 5)); print(a)

# %% cell_style="split"
b = np.zeros( (2, 1 , 5)); print(b)

# %%
print(np.hstack((a, b)))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## autres dimensions
#
# * avec concatenate, on peut faire `hstack` et `vstack` et autres
# * `vstack`: axis = 0
# * `hstack`: axis = 1

# %% cell_style="split"
a = np.ones( (2, 3, 4)); print(a)

# %% cell_style="split"
b = np.zeros( (2, 3, 2)); print(b)

# %%
print(np.concatenate( (a, b), axis = 2))

# %% [markdown] slideshow={"slide_type": "slide"}
# Pour conclure:
#
# * `hstack` et `vstack` utiles sur des tableaux 2D
# * au-delà, préférez `concatenate` qui a une sémantique plus claire

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `newaxis`

# %% [markdown]
# * `newaxis` est une astuce qui permet de 'décaler' les dimensions
# * s'utilise dans un slice
# * utile notamment dans ces opérations de stacking
# * mais pas seulement

# %% [markdown]
# * Si par exemple `A` a pour dimension `(a, b)`
# * `A[:, newaxis, :]` a pour dimension `(a, 1, b)`

# %% slideshow={"slide_type": "slide"}
from numpy import newaxis

# %%
line = np.arange(3); print(line)

# %%
column = line[:, newaxis]; print(column)

# %%
tableau = np.arange(6).reshape(2, 3); print(tableau)

# %%
print(tableau)

# %% slideshow={"slide_type": "slide"}
espace = tableau[newaxis, :, newaxis, :]; print(espace)

# %%
espace.shape

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `np.tile`

# %% [markdown]
# Cette fonction permet de répéter un tableau dans toutes les directions

# %%
motif = np.array([[0, 10], [20, 100]])
print(motif)

# %%
print(np.tile(motif, (2, 4)))

# %% [markdown] slideshow={"slide_type": "slide"}
# Le nombre de répétitions n'est pas forcément de la dimension de l'entrée

# %%
# un motif de dimension 2 
print(motif)

# %%
# peut être répété en dimension 1
print(np.tile(motif, 3))

# %%
# ou 3
print(np.tile(motif, (2, 2, 5)))

# %% [markdown] slideshow={"slide_type": "slide"}
# # splitting

# %% [markdown]
# * Opération inverse du stacking
# * Consiste à découper un tableau en parties plus ou moins égales

# %%
complet = np.arange(24).reshape(4, 6); print(complet)

# %% cell_style="split"
h1, h2 = np.hsplit(complet, 2)
print(h1)

# %% cell_style="split"
print(h2)

# %% slideshow={"slide_type": "slide"}
complet = np.arange(24).reshape(4, 6); print(complet)

# %% cell_style="split"
v1, v2 = np.vsplit(complet, 2)
print(v1)

# %% cell_style="split"
print(v2)

# %% [markdown] slideshow={"slide_type": "slide"}
# Pour les dimensions supérieures
#
#   * [`np.array_split`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array_split.html#numpy.array_split)
#   * permet de préciser la dimension
#   * un peu comme `np.concatenate` pour le stacking

# %% [markdown] slideshow={"slide_type": "slide"}
# # indexation - revisitée

# %% [markdown]
# * On peut indexer un tableau A .. par un tableau
# * le tableau d'indexes doit contenir des entiers
# * tous plus petits que la première dimension de A

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le cas simple: entrée et index de dim. 1

# %%
cubes = np.arange(10) ** 3; print(cubes)

# %%
# un index qui est une liste python
i = [ 1, 7, 5, 2]
print(cubes[i])

# %%
# ou un tableau numpy
i = np.array([3, 2])
print(cubes[i])

# %% [markdown] slideshow={"slide_type": "slide"}
# ## de manière générale

# %% [markdown]
# le résultat de `A[index]`
#
# * a la même forme que `index`
# * où on a remplacé `i` par `A[i]`
# * qui peut donc être un tableau si `A` est de dimension > 1

# %% cell_style="split" slideshow={"slide_type": "-"}
A = np.array([ [0, 'zero'], [1, 'un'], [2, 'deux'], [3, 'trois']]); print(A)

# %% cell_style="split" slideshow={"slide_type": "-"}
index = np.array([[0, 1, 2], [1, 2, 0]]); print(index)

# %%
print(A[index])

# %% [markdown] slideshow={"slide_type": "slide"}
# et donc si 
#
# * `index` est de dimension `(i, j, k)` 
# * et `a` est  de dimension `(a, b)`
# * le résultat est de dimension `(i, j, k, b)`
# * il faut que les éléments dans `index` soient dans `[0 .. a[`

# %% cell_style="split" slideshow={"slide_type": "slide"}
# l'entrée
print(A.shape)

# %% cell_style="split"
# l'index
print(index.shape)

# %%
# le résultat
print(A[index].shape)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## entrée de dim. 1, index de dim. > 1
#
# * lorsque l'entrée `A` est de dimension 1
# * alors la sortie a **exactement** la même forme que l'index
# * c'est comme si `A` était une fonction 
# * qu'on applique aux indices dans index

# %%
print(cubes)

# %% cell_style="split"
i2 = np.array( [ [2, 4], [8, 9]])
print(i2)

# %% cell_style="split"
print(cubes[i2])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### application 1
#
# application au codage des couleurs dans une image

# %%
N = 32
colors = 6
image = np.empty((N, N), dtype = np.int32)
for i in range(N):
    for j in range(N):
       image[i, j] = (i+j) % colors

# %%
plt.imshow(image)

# %% [markdown] slideshow={"slide_type": "slide"}
# **remarque**:
#
# * comme pour les boucles du genre 
#   `for i in range(len(tableau))`
#
# * cela n'est pas très élégant (on va voir tout de suite comment améliorer)
#
# **exercice**:
#
# * notre préoccupation: les couleurs sont non significatives
# * notre image contient des entiers dans `range(colors)`
# * on voudrait pouvoir choisir la vraie couleur correspondant à chaque valeur

# %%
# une palette de couleurs
palette = np.array([
  [255, 255, 255], # 0 -> blanc
  [255, 0, 0],     # 1 -> rouge
  [0, 255, 0],     # 2 -> vert
  [0, 0, 255],     # 3 -> bleu
  [0, 255, 255],   # 4 -> cyan
  [255, 255, 0],   # 5 -> magenta
 ], dtype=np.uint8)

# %% slideshow={"slide_type": "slide"}
plt.imshow(palette[image]);

# %%
image.shape

# %%
palette[image].shape

# %% [markdown] slideshow={"slide_type": "slide"}
# ## généralisation: indices multiples

# %% [markdown]
# * lorsque `index1` et `index2` ont la même forme
# * on peut écrire `A[index1, index2]`
# * qui a la même forme que les `index`
# * où on a remplacé `i, j` par `A[i][j]`
# * qui peut donc être un tableau si `A` est de dimension > 2

# %% slideshow={"slide_type": "slide"}
ix, iy = np.indices((4, 3))
A = 10 * ix + iy
print(A)

# %%
index1 = [ [3, 2], [0, 1 ]]  # doivent être <4
index2 = [ [2, 0], [0, 2 ]]  # doivent être <3
print(A[index1, index2])

# %% [markdown] slideshow={"slide_type": "slide"}
# et donc si
#
# * `index1` et `index2` sont de dimension `(i, j, k)` 
# * et `a` est  de dimension `(a, b, c)`
# * le résultat est de dimension `(i, j, k, c)`
# * il faut alors que les éléments  de `index1` soient dans `[0 .. a[` 
# * et les éléments de `index2` dans `[0 .. b[`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## avec slices
#
# * on peut combiner cela avec des slices
# * typiquement juste `:`

# %%
print(A)

# %%
print(A[:, [0, 2]])

# %% slideshow={"slide_type": "slide"}
print(A[ [0, 2], :])

# %%
# ce genre d'expression peut servir à affecter
A[ [0, 2], :] = 1000
print(A)

# %%
# ou avec broadcast
A[ [1, 2], :] = np.array([1, 2])[:, newaxis]

# %%
print(A)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### application 2
#
# * recherche de maxima
# * par l'intermédiaire de `np.argmax`

# %%
times = np.linspace(1000, 5000, num=5, dtype=int); print(times)

# %%
series = np.array( [ [10, 25, 32, 23, 12], [12, 8, 4, 10, 7], [100, 80, 90, 110, 120]])
print(series)

# %%
indices = np.argmax(series, axis=1); print(indices)

# %%
# les trois maxima, un par serie
maxima = series[ range(series.shape[0]), indices ]; print(maxima)

# %%
# et ils correspondent à ces instants-ci
times[indices]

# %% [markdown] slideshow={"slide_type": "slide"}
# ## indexation par booléens

# %% [markdown]
# * une forme un peu spéciale d'indexation
# * consiste à utiliser un tableau de booléens
# * qui agit comme un masque

# %%
suite = np.array([1, 2, 3, 4, 5, 4, 3, 2, 1])
hauts = suite >= 4
print(hauts)

# %%
suite[hauts] = 0
print(suite)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exercice
#
# mandelbrot

# %% [markdown] slideshow={"slide_type": "slide"}
# ## indexation par tableaux *vs* par listes

# %% slideshow={"slide_type": "-"}
ix, iy = np.indices((4, 4))
A = 10 * ix + iy
print(A)

# %% cell_style="split"
# les deux lignes
print(A[[0, 2]])

# %% cell_style="split"
# les deux colonnes
print(A[:, [1, 3]])

# %% cell_style="split"
# par deux listes !
print(A[[0, 2], [1, 3]])

# %% cell_style="split"
# par un tableau 2D similaire !
indices = np.array([[0, 2], [1, 3]])
print(A[indices])

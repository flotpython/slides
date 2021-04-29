# -*- coding: utf-8 -*-
# ---
# jupyter:
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
#   notebookname: "numpy & alg\xE8bre lin\xE9aire"
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
from plan import plan_extras; plan_extras("numpy", "linéaire")

# %% [markdown] slideshow={"slide_type": "slide"}
# # algèbre linéaire

# %%
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
plt.ion()

# %% [markdown]
# * Un aspect important de l'utilisation de numpy
# * consiste à manipuler des matrices et vecteurs
# * [voir doc complète](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

# %% [markdown] slideshow={"slide_type": "slide"}
# # produit matriciel

# %% [markdown]
# ## ne pas utiliser `*`

# %% [markdown]
# **rappel** : on a déjà vu que `*` entre deux tableaux fait une multiplication terme à terme

# %% cell_style="split"
ligne = 1 + np.arange(3)
print(ligne)

# %% cell_style="split"
colonne = 1 + np.arange(3).reshape(3, 1)
print(colonne)

# %% [markdown]
# ##### ce n'est pas ce qu'on veut ici !

# %%
print(ligne * colonne)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `np.dot()`

# %% [markdown]
# * l'opération de produit matriciel s'appelle `dot` 
# * c'est une méthode sur les tableaux

# %% cell_style="split"
m1 = np.array([[1, 1],
               [2, 2]])
print(m1)

# %% cell_style="split"
m2 = np.array([[10, 20],
               [30, 40]])
print(m2)

# %% slideshow={"slide_type": "-"}
np.dot(m1, m2)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `dot` fait aussi le produit scalaire !

# %% cell_style="split"
v1 = np.array([1, 2, 3])
print(v1)

# %% cell_style="split"
v2 = np.array([4, 5, 6])
print(v2)

# %% slideshow={"slide_type": "-"}
np.dot(v1, v2)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `np.matmul()`

# %% [markdown]
# * `matmut` réalise aussi l'opération de multiplication de matrices
# * c'est un ajout plus récent
# * qui supporte le *stacking* :
# * on peut donner des entrées de dimensions supérieures
# * et on fait alors une sorte de broadcast

# %% cell_style="split" slideshow={"slide_type": "slide"}
m1 = np.ones((2, 2))
e = np.vstack((m1, 2*m1, 3*m1))\
   .reshape(3, 2, 2)
print(e)


# %% cell_style="split"
m2 = np.array([[10, 20],
               [30, 40]])
print(m2)

# %% slideshow={"slide_type": "-"}
np.matmul(e, m2)

# %% [markdown]
# ## `m.T` 

# %% [markdown]
# la transposée de la matrice `m` est `m.t`

# %% cell_style="split"
m = np.arange(4).reshape(2, 2)
print(m)

# %% cell_style="split"
print(m.T)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## calculs matriciels

# %% [markdown]
# | outil           |   propos |
# |-----------------|--------|
# | `np.linalg.det` | déterminant |
# | `np.linalg.eig` | valeurs propres |
# | `np.linalg.solve` | résoud système équations |
# | `np.eye`        | matrice identité |
# | `np.diag`       | extrait la diagonale |
# | `np.diag`       | ou construit une matrice diagonale |
# | `...`           | ...|
#

# %% slideshow={"slide_type": "slide"}
np.diag(np.arange(16).reshape(4,4))

# %%
np.diag([1,2,3,4 ])

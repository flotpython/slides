# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
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

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# </div>

# %% slideshow={"slide_type": "slide"}
from plan import plan_extras; plan_extras("numpy", "linéaire")

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# # algèbre linéaire

# %% run_control={"frozen": false, "read_only": false}
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
plt.ion()

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * Un aspect important de l'utilisation de numpy
# * consiste à manipuler des matrices et vecteurs
# * [voir doc complète](https://docs.scipy.org/doc/numpy/reference/routines.linalg.html)

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# # produit matriciel

# %% [markdown] run_control={"frozen": false, "read_only": false}
# ## ne pas utiliser `*`

# %% [markdown] run_control={"frozen": false, "read_only": false}
# **rappel** : on a déjà vu que `*` entre deux tableaux fait une multiplication terme à terme

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
ligne = 1 + np.arange(3)
print(ligne)

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
colonne = 1 + np.arange(3).reshape(3, 1)
print(colonne)

# %% [markdown] run_control={"frozen": false, "read_only": false}
# ##### ce n'est pas ce qu'on veut ici !

# %% run_control={"frozen": false, "read_only": false}
print(ligne * colonne)

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## `np.dot()`

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * l'opération de produit matriciel s'appelle `dot` 
# * c'est une méthode sur les tableaux

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
m1 = np.array([[1, 1],
               [2, 2]])
print(m1)

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
m2 = np.array([[10, 20],
               [30, 40]])
print(m2)

# %% run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "-"}
np.dot(m1, m2)

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### `dot` fait aussi le produit scalaire !

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
v1 = np.array([1, 2, 3])
print(v1)

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
v2 = np.array([4, 5, 6])
print(v2)

# %% run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "-"}
np.dot(v1, v2)

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## `np.matmul()`

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * `matmut` réalise aussi l'opération de multiplication de matrices
# * c'est un ajout plus récent
# * qui supporte le *stacking* :
# * on peut donner des entrées de dimensions supérieures
# * et on fait alors une sorte de broadcast

# %% cell_style="split" run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
m1 = np.ones((2, 2))
e = np.vstack((m1, 2*m1, 3*m1))\
   .reshape(3, 2, 2)
print(e)


# %% cell_style="split" run_control={"frozen": false, "read_only": false}
m2 = np.array([[10, 20],
               [30, 40]])
print(m2)

# %% run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "-"}
np.matmul(e, m2)

# %% [markdown] run_control={"frozen": false, "read_only": false}
# ## `m.T` 

# %% [markdown] run_control={"frozen": false, "read_only": false}
# la transposée de la matrice `m` est `m.t`

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
m = np.arange(4).reshape(2, 2)
print(m)

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
print(m.T)

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## calculs matriciels

# %% [markdown] run_control={"frozen": false, "read_only": false}
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

# %% run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
np.diag(np.arange(16).reshape(4,4))

# %% run_control={"frozen": false, "read_only": false}
np.diag([1,2,3,4 ])

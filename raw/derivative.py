# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# # intro

# %% [markdown]
# on se propose de calculer la dérivée approchée d'une fonction
#
# la première idée consiste à utiliser bien entendu
#
# $f'(x) ⩰ \frac{f(x+h) - f(x)}{h}$ 
#

# %% [markdown]
# # fonction et domaine

# %%
f = np.cos

# par défaut linspace crée 50 points
X = np.linspace(0, 2*np.pi)

# %%
# très simple de calculer les f(x)
Y = f(X)
plt.plot(X, Y);

# %% [markdown]
# ## pas

# %% [markdown]
# Il faut remarquer que déjà à ce stade on a calculé pour tous les points $x$ du domaine X la valeur de la fonction sur un point voisin, le point $x + h$, $h$ étant le pas de notre échantillon

# %%
# comme on a utilisé linspace le pas est constant
h = X[1] - X[0]

# %% [markdown]
# # décalage

# %%
# la valeur de f à un point (proche de x d'une distance h) 
# à droite de X est donc
YR = Y[1:]

# %%
# par contre on a un élément
# de moins dans YR que dans Y
try:
    YR - Y
except ValueError as exc:
    print(f"OOPS {exc}")

# %%
# on ignore la dernière valeur de Y
# pour pouvoir calculer une différence

YR - Y[:-1]

# %% [markdown]
# # la dérivée

# %%
# c'est facile maintenant de calculer la dérivée
# approchée à droite 
# on a juste perdu un point, sur la borne supérieure

D = (Y[1:] - Y[:-1]) / h

# %%
plt.plot(X[:-1], D);

# %% [markdown]
# # erreur

# %% [markdown]
# ici bien sûr on connaît la dérivée, on peut comparer

# %% slideshow={"slide_type": "slide"}
S = - np.sin(X[:-1])
plt.plot(X[:-1], S);

# %%
# estimons l'erreur qu'on a faite
S - D

# %%
# c'est très simple : le maximum de la valeur absolue sur tous les points

np.max(np.abs(S-D))

# %% [markdown]
# # variantes
#
# à titre d'exercice, vous pouvez expérimeter autour de ce thème pour
#
# * faire les calculs avec un pas plus petit : voyez la doc de `np.linspace` pour construire le domaine `X` avec davantage de points
#
# * utiliser plutôt la formule
#
#   $f'(x) ⩰ \frac{f(x+h) - f(x-h)}{2h}$ 
#
#   et comparer la précision des deux méthodes
#
# * changer de stratégie pour utiliser deux pas différents pour, d'une part le domaine, et d'autre part le $h$ de la formule; comparer les précisions, et estimer l'impact de cette méthode en termes de performance (temps calcul et mémoire)

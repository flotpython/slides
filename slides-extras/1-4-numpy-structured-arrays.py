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
#   notebookname: numpy - strutured arrays
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
from plan import plan_extras; plan_extras("numpy", "struct")

# %% [markdown] slideshow={"slide_type": "slide"}
# # structured arrays

# %%
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
plt.ion()

# %% [markdown]
# * jusqu'ici on a vu des tableaux *homogènes* 
#   * tous les éléments ont le même type
# * on peut aussi se définir des types structurés
#   * comme un 'struct' en c - ou encore un 'record'
# * demande un peu plus d'efforts au programmeur

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple

# %%
classe = np.array(
  # les données sont une liste d'éléments homogènes
  [ 
   # mais cette fois chaque élément (ligne) est un composite
   # que l'on peut décrire dans un tuple
    ( 'Jean', 'Dupont', 32),
   # tous les tuples doivent avoir la même structure
    ( 'Daniel', 'Durand', 18),  ( 'Joseph', 'Delapierre', 54),
    ( 'Paul', 'Girard', 20)])

# %% slideshow={"slide_type": "-"}
print(classe)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `dtype`

# %%
classe.dtype

# %% [markdown]
# comme pour les tableaux homogènes:
#
# * comme je n'ai pas précisé de type
# * c'est numpy qui en choisi un pour moi
# * ici le plus petit dénominateur commun c'est le type string 
# * de taille 10 d'ailleurs

# %% [markdown] slideshow={"slide_type": "slide"}
# * j'ai encore tableau homogène
# * et d'ailleurs je peux toujours perdre de la précision

# %% slideshow={"slide_type": "-"}
classe[0, 0]

# %%
classe[0, 0] = 'Charles-Henri'
classe

# %% [markdown] slideshow={"slide_type": "slide"}
# ## spécifier `dtype`

# %% [markdown]
# * c'est important d'élaborer un type
# * d'autant que toutes les colonnes ne sont pas identiques

# %%
classe2 = np.array([ ( 'Jean', 'Dupont', 32),
                     ( 'Daniel', 'Durand', 18),
                     ( 'Joseph', 'Delapierre', 54),
                     ( 'Paul', 'Girard', 20)],
    dtype = [('prenom', '|S12'), ('nom', '|S15'), ('age', np.int)])
print(classe2)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## impact sur `shape` et `reshape`

# %% [markdown]
# * dans le cas de cette nouvelle définition
# * `shape` retourne .. une seule dimension !

# %% cell_style="split"
# on peut faire reshape (même si ça
# ne pas beaucoup de sens de toutes façons)
print(classe.reshape(3, 4))
# car la dimension est habituelle
print("shape", classe.shape)

# %% cell_style="split"
# on ne peut pas faire reshape
try: print(classe2.reshape(3, 4))
except Exception as e: print("OOPS", e)
# la dimension n'est pas ce qu'on
# pourrait attendre
print("shape", classe2.shape)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### dimensions supérieures
#
# * on peut sans souci créer des dimensions supérieures
# * attention toutefois
#   * comme c'est un tableau de dimension 1
#   * c'est considéré comme **une ligne** 
#   * dans le contexte d'un tableur
#   * on préfèrerait peut-être que ce soit présenté en colonnes

# %%
# on peut créer un tableau 2 x 4
# par exemple en superposant la même ligne 2 fois
classe2x2 = np.vstack( (classe2, classe2))
print(classe2x2)
print("shape = ",classe2x2.shape)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## comment définir `dtype`

# %% [markdown] slideshow={"slide_type": "slide"}
# * il existe plusieurs méthodes pour définir un `dtype` pour un 'structured array',
# * sachant que par ailleurs un élément de la structure peut être à son tour un tableau
#
# 1. String
# 1. Tuple
# 1. List
# 1. Dict (2 formes)
#
# * voire aussi comme [un objet `dtype`](https://docs.scipy.org/doc/numpy/reference/arrays.dtypes.html)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `dtype` défini comme un string

# %% [markdown]
# * séparé par des virgules
# * des codes comme e.g. `i8` (entier sur 64 bits) ou `a<12>` (string de taille 12)
# * ou encore `float64` (cette fois en bits !)
# * inconvénient: les champs ne sont pas nommés

# %%
structs = np.ones(3, dtype='3int8, float32, (2,3)float64')
print(structs)

# %%
# on peut accéder à tous les morceaux par indices
structs[1][2][1][1] *= 20
print(structs)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `dtype` défini comme un tuple

# %% [markdown]
# permet de définir quelque chose qui ressemble à un `union`:

# %%
powers = 1 + 8 * np.arange(4)
print(powers)

# %%
unions = np.array([2**power for power in powers], 
                   dtype=('i4',[('r','u1'), ('g','u1'), ('b','u1'), ('a','u1')]))
print(unions)

# %%
unions['r']

# %%
unions['g']

# %%
unions['b']

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `dtype` défini comme une liste

# %% [markdown]
# * déjà vu l'exemple de `classe2`
# * doit être une liste de 2-tuples `nom` , `type`
# * les noms peuvent servir à indexer (c'est tout l'intérêt)

# %%
structs = np.ones(3, dtype=[('x','f4'),('y',np.float32),('value','f4',(2,2))])
structs

# %%
structs[0]['x'] *= 10
structs[1]['value'][1][1] *= 100
# on peut accéder au second flottant par indice aussi
structs[2][1] *= 1000
structs

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `dtype` défini comme un dict(1)

# %% [markdown]
# * le dictionnaire a deux clés prédéfinies
#   * `names` et `formats`
#   * listes de même longueurs

# %%
structs = np.ones(3, dtype={'names':['col1', 'col2'], 'formats':['i4','(2,3)f4']})
print(structs)

# %%
structs[1]['col2'] *= 30
print(structs)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `dtype` défini comme un dict(2)

# %% [markdown]
# * sinon, on s'attend à trouver dans `dtype`:
#   * les clés sont les noms des colonnes
#   * la valeur associée doit être un 2- ou 3-tuple
#   * de la forme `(type, offset[, nom_colonne])`

# %%
structs = np.ones(3, dtype={'col1':('i1',0,'title 1'), 'col2':('f4',1,'title 2')})
print(structs)

# %%
structs[1]['col2'] *= np.pi
print(structs)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exercice

# %% [markdown] slideshow={"slide_type": "-"}
# * [Voir la documentation complète ici](https://docs.scipy.org/doc/numpy-1.10.1/user/basics.rec.html#defining-structured-arrays)
# * sur la définition de types structurés

# %% [markdown]
# * On veut modéliser le groupe des 8 éléments du groupe D4 (les rotations et symétries d'ordre 4)
# * sous la forme d'un tableau de 8 valeurs
# * chacune ayant 
#   * un nom (sur deux caractères)
#   * une matrice carrée 2x2

# %% [markdown] slideshow={"slide_type": "slide"}
# [extrait de https://en.wikipedia.org/wiki/Dihedral_group](https://en.wikipedia.org/wiki/Dihedral_group)

# %% [markdown]
# $
# {\displaystyle {\begin{matrix}\mathrm {r} _{0}=\left({\begin{smallmatrix}1&0\\[0.2em]0&1\end{smallmatrix}}\right),&\mathrm {r} _{1}=\left({\begin{smallmatrix}0&-1\\[0.2em]1&0\end{smallmatrix}}\right),&\mathrm {r} _{2}=\left({\begin{smallmatrix}-1&0\\[0.2em]0&-1\end{smallmatrix}}\right),&\mathrm {r} _{3}=\left({\begin{smallmatrix}0&1\\[0.2em]-1&0\end{smallmatrix}}\right),\\[1em]\mathrm {s} _{0}=\left({\begin{smallmatrix}1&0\\[0.2em]0&-1\end{smallmatrix}}\right),&\mathrm {s} _{1}=\left({\begin{smallmatrix}0&1\\[0.2em]1&0\end{smallmatrix}}\right),&\mathrm {s} _{2}=\left({\begin{smallmatrix}-1&0\\[0.2em]0&1\end{smallmatrix}}\right),&\mathrm {s} _{3}=\left({\begin{smallmatrix}0&-1\\[0.2em]-1&0\end{smallmatrix}}\right).\end{matrix}}}
# $

# %%
# les données sous forme de python 'standard'
d4_data = [ 
    ('r0', [[1, 0], [0, 1]]),      ('r1', [[0, -1], [1, 0]]),
    ('r2', [[-1, 0], [0, -1]]),    ('r3', [[0, 1], [-1, 0]]),
    ('s0', [[1, 0], [0, -1]]),     ('s1', [[0, 1], [1, 0]]),
    ('s2', [[-1, 0], [0, 1]]),     ('s3', [[0, -1], [-1, 0]]),
  ]

# %% [markdown] slideshow={"slide_type": "slide"}
# vous devez donc écrire quelque chose comme ceci
#
# ````
# d4 = np.array( 
#   d4_data,
#   dtype = <votre code>
# )
# d4
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### string

# %% slideshow={"slide_type": "-"}
# on ne pourra pas accéder aux champs par nom
D4 = np.array( d4_data,
  dtype = 'S2, (2,2)int8'
)
D4

# %%
# en fait si mais avec des noms qu'on n'a pas choisis
x = D4[0]
x['f0']

# %% [markdown] slideshow={"slide_type": "slide"}
# ### dict (1)

# %%
D4 = np.array( d4_data,
       dtype = {'names':['nom', 'matrice'],
                'formats':['S2', '(2,2)int8']})
D4

# %%
# pas de nom pour accéder aux différents éléments
x = D4[2]
print(x)

# %%
y = D4[4]
# mais par contre une fois qu'on a un élément 
# on peut accéder aux deux colonnes par nom
produit = x['matrice'].dot(y['matrice'])
print("{} x {} ->\n{}".format(x['nom'], y['nom'], produit))

# %% [markdown] slideshow={"slide_type": "slide"}
# ### dict (2)
#
# Attention aux offsets: ce **n'est pas** simplement un ordre des champs!

# %% slideshow={"slide_type": "-"}
D4 = np.array( d4_data,
    dtype = {'nom' : ('S2', 0),
             'matrice': ('(2,2)float32', 4)}
)
print(D4)

# %%
x = D4[2]
print(x)

# %%
y = D4[4]
produit = x['matrice'].dot(y['matrice'])
print("{} x {} ->\n{}".format(x['nom'], y['nom'], produit))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `genfromtxt`
#
# la fonction [`numpy.genfromtxt`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html) permet de construire un tableau numpy à partir d'un fichier texte

# %% slideshow={"slide_type": "-"}
# !cat ../data/D4.txt

# %% slideshow={"slide_type": "slide"}
d4_raw = np.genfromtxt("../data/D4.txt", 
                       dtype=None)
d4_raw

# %% slideshow={"slide_type": "slide"}
d4_raw = np.genfromtxt("../data/D4.txt", 
                       dtype=[('nom', 'S2'), 
                              ('matrice', '(2,2)i8')])
d4_raw

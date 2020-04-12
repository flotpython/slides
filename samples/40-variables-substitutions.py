# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all
#     formats: py:percent
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: Changements de variables
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: false
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: false
#     toc_position: {}
#     toc_section_display: true
#     toc_window_display: false
#   version: '1.0'
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# </div>

# %% [markdown] {"slideshow": {"slide_type": ""}}
# # changements de variable
#
# ou un vrai prétexte pour manipuler les objets fonctionnels en tant que valeurs

# %% [markdown]
# ce notebook élabore autour du projet numérique "tracé du contour"

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## rappel

# %% [markdown]
# dans le projet numérique qui vise à calculer les lignes de niveau d'une fonction, on vous suggère
#
# * de traiter avec `simple_contour` le cas très spécifique 
#   * d'une fonction définie sur le pavé unité $[0..1]^2$,
#   * et avec une courbe qui "entre par le bord gauche" (x=0)
# * puis de généraliser avec `contour` en découpant un domaine quelconque en pavés élémentaires

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## notre sujet

# %% [markdown] {"slideshow": {"slide_type": ""}}
# nous allons étudier les transformations qui permettent de passer du cas général au cas spécifique
#
# soit donc $f : [x1 .. x2] \times [y1 .. y2] \longrightarrow \mathbb{R}$
#
# pour se ramener à une fonction qui vérifie les hypothèses de `simple_contour`, on voit qu'il s'agit de déformer le domaine de manière linéaire de sorte que le pavé  
# $[x1 .. x2] \times [y1 .. y2]$ corresponde à $[0..1]^2$.
#
# et comme `simple_contour` fait l'hypothèse que le contour commence sur le bord gauche, on va envisager aussi les 4 rotations du pavé

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## comment s'y prendre

# %% [markdown]
# on commence par coder les changements de variable élémentaires qui correspondent 
#
# * aux translations
# * aux homothéties (scaling)
# * aux rotations autour du point (0.5, 0.5)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### translations

# %% [markdown]
# le changement de variable le plus élémentaire est la translation:
#
# en partant de la fonction $f : \mathbb{R}^2 \longrightarrow \mathbb{R}$ et étant donné deux réels $(x_0,y_0)$, on peut facilement dériver une fonction $f_{t(x_0,y_0)}$ qui correspond à $f$ translatée de $(x_0, y_0)$ par
#
# $f_{t(x_0,y_0)}(x, y) = f(x-x_0, y-y_0)$
#
# on peut très facilement coder la fonction `translate` en Python :

# %% {"slideshow": {"slide_type": "slide"}}
# en entrée f est une fonction R2->R
def translate(f, x0, y0):
    def translated(x, y):
        return f(x-x0, y-y0)
    # en sortie on veut aussi une fonction R2->R
    return translated


# %% [markdown] {"cell_style": "split"}
# si on voulait décrire formellement la fonction translate, on écrirait
#
# $translate: {\mathbb{R}}^{\mathbb{R}^2} \times \mathbb{R}^2\longrightarrow {\mathbb{R}}^{\mathbb{R}^2}$
#
# qui est une façon très pédante de dire le fait très simple que

# %% [markdown] {"cell_style": "split"}
#  
# * si on a en entrée
#   * une fonction $f: \mathbb{R}^2 \longrightarrow \mathbb{R}$
#   * et deux réels
# * alors on aura en sortie
#   * une nouvelle fonction $\mathbb{R}^2 \longrightarrow \mathbb{R}$

# %% [markdown] {"cell_style": "center", "slideshow": {"slide_type": "slide"}}
# on peut écrire exactement la même chose en utilisant une lambda

# %% {"cell_style": "split", "slideshow": {"slide_type": ""}}
def translate(f, x0, y0):
    def translated(x, y):
        return f(x-x0, y-y0)
    return translated


# %% {"cell_style": "split"}
# c'est totalement équivalent 
# d'écrire
def translate(f, x0, y0):
    return lambda x, y: f(x-x0, y-y0)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# #### visualisation

# %% [markdown]
# on va visualiser une fonction, disons reconnaissable

# %%
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

# attention à bien importer le numpy d'autograd ici
import autograd.numpy as np


# %% {"cell_style": "split"}
def gaussian(x, y):
    """
    centered gaussian on X, Y
    not normalized,
    i.e. gaussian(0, 0) = 1
    """
    return np.exp(-x**2 -y**2)


# %% {"cell_style": "split"}
def h(x, y):
    return 2*(gaussian(x, y) 
              - gaussian(x-1, y-1))


# %% {"cell_style": "split"}
# le maximum est ici
h(0, 0)

# %% {"cell_style": "split", "slideshow": {"slide_type": "slide"}}
# le domaine de visualisation
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)


# %% {"cell_style": "split", "slideshow": {"slide_type": ""}}
def show_3d(X, Y, Z, sizex=6, sizey=6):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.gca(projection='3d')
    ax.plot_surface(
        X, Y, Z, cmap=cm.coolwarm,
        linewidth=0, antialiased=False);


# %% {"cell_style": "center"}
Z = h(X, Y)
show_3d(X, Y, Z)

# %% {"cell_style": "split", "slideshow": {"slide_type": "slide"}}
# on fabrique la fonction translatée
translated_h = translate(h, 1, 2)

# %% {"cell_style": "split", "slideshow": {"slide_type": ""}}
# le maximum doit être ici
translated_h(1, 2)

# %%
Z2 = translated_h(X, Y)

show_3d(X, Y, Z2)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### changement d'échelle

# %% [markdown]
# on s'y prend de manière similaire pour les déformations d'étirement

# %% {"cell_style": "split"}
def scale(f, sx, sy):
    def scaled(x, y):
        return f(x/sx, y/sy)
    return scaled


# %% {"cell_style": "split"}
def scale(f, sx, sy):
    return lambda x, y: f(x/sx, y/sy)


# %% {"cell_style": "split", "slideshow": {"slide_type": "slide"}}
scaled_h = scale(h, 3, 2)

# %% {"cell_style": "split", "slideshow": {"slide_type": ""}}
# maximum inchangé
scaled_h(0, 0)

# %%
Z3 = scaled_h(X, Y)

show_3d(X, Y, Z3)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### rotations

# %% [markdown]
# on commence par se définir les 4 rotations

# %% {"slideshow": {"slide_type": ""}}
from enum import IntEnum

class Angle(IntEnum):
    LEFT = 0      # no rotation
    TOP = 1       # rotate π/2 counter-clockwise around (0.5, 0.5)
    RIGHT = 2     # rotate π around around (0.5, 0.5)
    BOTTOM = 3    # rotate π/2 clockwise around (0.5, 0.5)
    
    @classmethod
    def ALL(cls):
        return (Angle(i) for i in range(4))

    # on pourrait avoir besoin d'inverser
    def __neg__(self):
        return Angle((4-self)%4)
    
    def rotate(self, x, y):
        """x, y -> x, y"""
        if self == Angle.LEFT:
            return (x, y)
        if self == Angle.TOP:
            return (y, 1-x)
        if self == Angle.RIGHT:
            return (1-x, 1-y)
        if self == Angle.BOTTOM:
            return (1-y, x)
        


# %% {"cell_style": "split"}
x = Angle.TOP
y = -x

# %% {"cell_style": "split"}
x, y


# %% {"slideshow": {"slide_type": "slide"}}
# cette fonction globale (ne pas confondre avec Angle.rotate)
# est une usine à fonctions comme translate() et scale()
def rotate(f, angle: Angle):
    return lambda x, y: f(*angle.rotate(x, y))



# %% {"cell_style": "split", "slideshow": {"slide_type": "slide"}}
# on focalise sur le carré unité
X1 = np.arange(0, 1, .1)
Y1 = np.arange(0, 1, .1)
X1, Y1 = np.meshgrid(X1, Y1)

Zh = h(X1, Y1)

# %% {"cell_style": "split"}
show_3d(X1, Y1, Zh)

# %% {"cell_style": "split", "slideshow": {"slide_type": "slide"}}
# identique à h en principe
h_l = rotate(h, Angle.LEFT)

Zl = h_l(X1, Y1)

# %% {"cell_style": "split"}
# tourné d'un quart ⤿
h_t = rotate(h, Angle.TOP)

Zt = h_t(X1, Y1)

# %% {"cell_style": "split"}
show_3d(X1, Y1, Zl)

# %% {"cell_style": "split"}
show_3d(X1, Y1, Zt)

# %% {"cell_style": "split", "slideshow": {"slide_type": "slide"}}
# demi tour
h_r = rotate(h, Angle.RIGHT)

Zr = h_r(X1, Y1)

# %% {"cell_style": "split"}
# 1/4 de tour ⤾
h_b = rotate(h, Angle.BOTTOM)

Zb = h_b(X1, Y1)

# %% {"cell_style": "split"}
show_3d(X1, Y1, Zr)

# %% {"cell_style": "split"}
show_3d(X1, Y1, Zb)

# %% {"slideshow": {"slide_type": "slide"}}
# imaginons que vous avez déjà écrit simple_contour
from contour import simple_contour

# %% {"slideshow": {"slide_type": "slide"}}
# pour voir comment l'appeler
# simple_contour?

# %% {"slideshow": {"slide_type": "slide"}}
X, Y = simple_contour(h, 0.5)

plt.figure(figsize=(6, 6))
plt.plot(X, Y);

# %% {"slideshow": {"slide_type": "slide"}}
# alors pour écrire la fonction coutour complète on peut utiliser nos outils

import itertools

def contour(f, c, xs, ys, delta):
    
    curves = []
    
    identity = lambda x, y: (x, y)

    nx, ny = len(xs), len(ys)
    for i, j in itertools.product(range(nx-1), range(ny-1)):
        x1, x2 = xs[i], xs[i+1]
        y1, y2 = ys[j], ys[j+1]

        for angle in Angle.ALL():
            # here we build the function suitable for simple_contour
            f_cell = rotate(scale(translate(f, -x1, -y1), 1/(x2-x1), 1/(y2-y1)), angle)
            
            # these are relative to the unit square
            X_01, Y_01 = simple_contour(f_cell, c, delta=delta)
            
            # nothing found
            if len(X_01) ==0:
                continue
                
            # so we need to remap them into the [x1, x2] x [y1, y2] domain
            # which amounts to reversing the deformation from f to f_cell
            X, Y = [], []
            for x_01, y_01 in zip(X_01, Y_01):
                # it's possible to undo one level using rotate applied on identity
                rx, ry = rotate(identity, angle)(x_01, y_01)
                # the other moves we must apply by hand 
                # cannot use the scale/translate thing here - discussion..
                sx, sy = (x2-x1)*rx, (y2-y1)*ry
                tx, ty = sx + x1, sy + y1
                X.append(tx), Y.append(ty)
            curves.append((X, Y))
                
    return curves


# %% {"slideshow": {"slide_type": "slide"}}
def draw_contour(f, c, xs=[0.0, 1.0], ys=[0.0, 1.0], delta=0.1):
    curves = contour(f, c, xs, ys, delta)
    for X, Y in curves:
        plt.plot(X, Y)


# %%
plt.figure(figsize=(6, 6))

# upper bound not included in arange
steps = np.arange(-2, +2.0001, 0.5)

for c in np.arange(-1.5, 1.5001, .5):
    draw_contour(h, c, steps, steps)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### discussion

# %% [markdown]
# il pourrait être tentant d'utiliser nos 'rotate() / scale() / translate()' pour inverser le mapping initial dans la dernière partie de contour
#
# en fait la formule pour revenir en arrière, avec les mêmes notations - i.e. $x_{01} \in [0..1]$ - ressemble à ceci, de manière disons imagée :
#
# x = (((rotation_inverse(x_01, y_01) ) * (x2-x1) ) + x1
#
# et remarquons ici que notre fonction `translate` calcule $f(x+x0)$ et non pas $f(x)+x0$, qui est le gener de formule que nous avons besoin d'écrire ici
#
# très intuitivement donc, vous pouvez voir quels sont les éléments qui nous manqueraient à ce stade si on voulait finir le problème avec le même genre d'outils que ceux que nous nous sommes donnés jusqu'ici
#
# qui est bien sûr un exercice pour ceux qui sont arrivé ici très en avance :)

# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     cell_metadata_json: true
#     formats: py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: Cube
#   version: '1.0'
# ---

# %%
import math
import numpy as np
import matplotlib.pyplot as plt

# %% [markdown]
# # récréation : le problème des moteurs d'avion

# %% [markdown]
# Au départ on considère le problème des moteurs d'avion; on regarde un avion qui a $N$ moteurs, qui sont tous pareils et ont une probabilité de panne égale à $p$
#
# Et on se pose la question de savoir quelle est la probabilité qu'au moins la moitié des moteurs fonctionne. Pour donner un sens au cas d'un nombre impair de moteurs, on arrondit la division par deux au nombre supérieur :
#
# | N | # de moteurs min |
# |---|------------------|
# | 1 | 1 |
# | 2 | 1 | 
# | 3 | 2 | 
# | 4 | 2 |

# %% [markdown]
# On appelle $q$ la probabalité qu'un moteur fonctionne ($p$ pour panne, et $q$ pour quiétude) et on a donc
#
# $$ p + q = 1$$
#
# Bien entendu, tous les moteurs sont indépendants

# %% [markdown]
# ## la méthode brutale

# %% [markdown]
# méthode brutale : pour chaque $n$ entre 0 et N, on calcule $p_n$ la probabilité pour que l'avion ait $n$ moteurs qui marchent  
#
# la formule $$q^np^{N-n}$$ vient à l'esprit, mais bien sûr elle ne suffit pas, car elle ne décrit qu'une seule des façons de choisir les $n$ moteurs qui marchent parmi les $N$ disponibles
#
# donc en tout $$p_n = {N \choose n} q^np^{N-n}$$
#
#

# %% [markdown]
# ## le binôme

# %% [markdown]
# on peut se convaincre que le calcul est correct, en vérifiant que $$\sum_{n=0}^{N} p_n = 1$$
#
# et en effet $$
# \begin{array}{rcl}
# 1 & = & 1^N \\
#   & = & (p+q)^N \\
#   & = & p^N + {N \choose 1}p^{N-1}q + {N\choose 2}p^{N-2}q^2 \ldots + q^N \\
#   & = & \sum_{n=0}^{N} p_n
# \end{array}
# $$

# %% [markdown]
# ## importing stuff

# %%
import numpy as np

# %%
import matplotlib.pyplot as plt
# %matplotlib notebook

# %%
# install with - unsurprisingly (from the terminal)
# pip install ipywidgets

from ipywidgets import interact, fixed
from ipywidgets import FloatSlider

# %%
# ditto w/
# pip install k3d

import k3d
from k3d.plot import Plot

# %% [markdown]
# ## wired cube

# %%
# cube corners
code= '000 100 110 010 011 111 101 001 000'

X = np.array([int(s[0]) for s in code.split()])
Y = np.array([int(s[1]) for s in code.split()])
Z = np.array([int(s[2]) for s in code.split()])

# %%
# # np.stack?

# 9 points, means the input must have a shape (9, 3)
k3d_line_input = np.stack([X, Y, Z], axis=1)


# %%
def foo():
    plot = k3d.plot()
    plot += k3d.line(k3d_line_input, width=0.1)
    plot.display()


# %%
foo()

# %% [markdown]
# ## meshed cubes and boxes

# %%
from k3d.platonic import Cube
from box import Box

# %%
plot = k3d.plot()
cube_mesh = Cube(origin=(0.5, 0.5, 0.5), size=0.5).mesh
cube_mesh.color = 0xff0000
plot += cube_mesh

box_mesh = Box(corner=(2, 0, 0), sizes=(3, 1, 2)).mesh
box_mesh.color = 0x0000ff
plot += box_mesh

plot

# %% [markdown]
# ### moving the box manually

# %%
v2 = box_mesh.vertices.copy()

# %%
# duration is 2s
import time
for _ in range(10):
    v2 += 0.1
    box_mesh.vertices = v2
    time.sleep(0.2)


# %% [markdown]
# # manual creation

# %%
def init_scene(d):
    plot = k3d.plot(height=800)
    m000 = Box((0,0,0), (3,3,3)).mesh
    plot += m000
    m100 = Box((3+d,0,0), (1,3,3)).mesh
    plot += m100
    m010 = Box((0,3+d,0), (3,1,3)).mesh
    plot += m010
    m001 = Box((0,0,3+d), (3,3,1)).mesh
    plot += m001
    m110 = Box((3+d,3+d,0), (1,1,3)).mesh
    plot += m110
    m101 = Box((3+d,0,3+d), (1,3,1)).mesh
    plot += m101
    m011 = Box((0,3+d,3+d), (3,1,1)).mesh
    plot += m011
    m111 = Box((3+d,3+d,3+d), (1,1,1)).mesh
    plot += m111
    
    return plot

# init_scene(1)


# %% [markdown]
# ## manual animation

# %%
from palette import palette


# %%
#
def iter_corner_sizes(L, D):
    yield (0,0,0), (L,L,L)
    yield (L+D,0,0), (1,L,L)
    yield (0,L+D,0), (L,1,L)
    yield (0,0,L+D), (L,L,1)
    yield (L+D,L+D,0), (1,1,L)
    yield (L+D,0,L+D), (1,L,1)
    yield (0,L+D,L+D), (L,1,1)
    yield (L+D,L+D,L+D), (1,1,1)


# %%
class Animator1:
    
    def __init__(self, L, D, height=800):
        self.L = L
        self.D = D
        self.height = height
        
    def init_plot(self):
        plot = k3d.plot(height=self.height)
        self.meshes = []
        for (corner, sizes), color in zip(iter_corner_sizes(self.L, self.D),
                                          palette):
            mesh = Box(corner=corner, sizes=sizes).mesh
            mesh.color = color
            plot += mesh
            # set aside for updates
            self.meshes.append(mesh)
        self.plot = plot
        # return the plot so it gets displayed
        return self.plot
    
    def update_plot(self, newL, newD):
        for (corner, sizes), mesh in zip(iter_corner_sizes(newL, newD),
                                         self.meshes):
            newBox = Box(corner=corner, sizes=sizes)
            mesh.vertices = newBox.mesh.vertices


# %%
a1 = Animator1(3, 1, height=600)
a1.init_plot()

# %%
for d in np.linspace(1, 0, 10):
    a1.update_plot(1, d)

# %% [markdown]
# ## a little nicer

# %%
type(a1.plot)

# %%
try:
    k3d.plot.Plot
except AttributeError:
    print("OOPS !!") 

# %%
k3d.plot


# %%
class Animator2(Plot):
    
    def __init__(self, L, D, height=800):
        super().__init__(height=height)
        self.L = L
        self.D = D
        
        # formerly in init_plot()
        self.meshes = []
        for (corner, sizes), color in zip(iter_corner_sizes(self.L, self.D),
                                          palette):
            mesh = Box(corner=corner, sizes=sizes).mesh
            mesh.color = color
            # former 'plot' attribute is now just self
            self += mesh
            # set aside for updates
            self.meshes.append(mesh)
    
    def update_plot(self, newL, newD):
        self.D = newD
        self.L = newL
        for (corner, sizes), mesh in zip(iter_corner_sizes(newL, newD),
                                         self.meshes):
            newBox = Box(corner=corner, sizes=sizes)
            mesh.vertices = newBox.mesh.vertices


# %%
a2 = Animator2(3, 1)
a2

# %%
for d in np.linspace(a2.D, 2, 10):
    a2.update_plot(3, d)

# %% [markdown]
# ## interactive

# %% [markdown]
# https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html#Basic-interact
#
# https://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html#More-control-over-the-user-interface:-interactive_output

# %%
from ipywidgets import HBox, Layout, interactive_output

class Animator3(type(k3d.plot())):
    
    def __init__(self, L, D, height=800):
        super().__init__(height=height)
        self.L = L
        self.D = D
        
        # formerly in init_plot()
        self.meshes = []
        for (corner, sizes), color in zip(iter_corner_sizes(self.L, self.D),
                                          palette):
            mesh = Box(corner=corner, sizes=sizes).mesh
            mesh.color = color
            # former 'plot' attribute is now just self
            self += mesh
            # set aside for updates
            self.meshes.append(mesh)
        display(self)
    
    def update_plot(self, newL, newD):
        self.D = newD
        self.L = newL
        for (corner, sizes), mesh in zip(iter_corner_sizes(newL, newD),
                                         self.meshes):
            newBox = Box(corner=corner, sizes=sizes)
            mesh.vertices = newBox.mesh.vertices


    # limited control over the sliders arrangement
    def interact_D(self, **slider_as_dict):
        # closure just capture self in function
        def update(L, D):
            self.update_plot(L, D)
        interact(update,
                 L=fixed(self.L),
                 D=FloatSlider(**slider_as_dict, value=self.D,
                               layout=Layout(width="90%")
                              ))
                 

    # full control: here we put them in a simple horizontal box
    def interact_LD(self, L_dict, D_dict):
        # closure just capture self in function
        def update(L, D):
            self.update_plot(L, D)
        layout = Layout(width="50%")
        lw = FloatSlider(**L_dict, layout=layout, description="L")
        dw = FloatSlider(**D_dict, layout=layout, description="D")
        box = HBox([lw, dw])
        interactive_output(update, {'L': lw, 'D': dw})
        display(box)

# %%
a3 = Animator3(3, 1, height=600)

# %% {"cell_style": "center", "scrolled": false}
# try it out with and without continuous update
a3.interact_D(
    min=0, max=1, step=0.1,
   # continuous_update=False,
)

# %%
a3.interact_LD(dict(min=1, max=3), dict(min=0, max=1, step=0.25))

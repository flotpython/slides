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
#   notebookname: exemple broadcasting (optionnel)
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

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# # le broadcasting illustré

# %% [markdown] run_control={"frozen": false, "read_only": false}
# ## construire n'importe quelle image dans le plan

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# %matplotlib inline
import matplotlib.pyplot as plt
plt.ion()

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
import numpy as np

size = 16
height = 16

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
ix, iy = np.indices((size, size))
plane = np.sqrt((ix-(size//2))**2\
                + (iy-(size//2))**2)

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
plt.imshow(plane);

# %% [markdown] cell_style="center" run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## par broadcasting
#
# * elle était en x et y
# * on va la faire pivoter pour qu'elle soit en x, z
# * et ensuite l'étirer selon l'axe des y

# %% cell_style="center" run_control={"frozen": false, "read_only": false}
# on crée un tableau de la dimension souhaitée
cylinder = np.zeros((size, height , size))
# et par simple broadcasting
# on va faire l'opération indiquée
cylinder += plane[:, np.newaxis, :]

# %% cell_style="center" run_control={"frozen": false, "read_only": false}
cylinder.shape


# %% cell_style="split" run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# la fonction qui dessine
# une tranche du cylindre
def draw_slice_y(y):
    plt.imshow(cylinder[:, y, :]);


# %% cell_style="split" run_control={"frozen": false, "read_only": false}
from ipywidgets import (interact,
                        IntSlider)
interact(draw_slice_y, y=IntSlider(
    min=0, max=height-1));


# %% cell_style="center" run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# la fonction qui dessine 
# une tranche du cylindre
def draw_slice_x(x):
    plt.imshow(cylinder[x, :, :]);


# %% cell_style="center" run_control={"frozen": false, "read_only": false}
from ipywidgets import (interact,
                        IntSlider)
interact(draw_slice_x, x=IntSlider(
    min=0, max=size-1, step=1, value=0));

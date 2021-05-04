# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   ipub:
#     sphinx:
#       toggle_input: true
#       toggle_input_all: true
#       toggle_output: true
#       toggle_output_all: true
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
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
#   nbhosting:
#     title: "pr\xE9lude"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% [markdown]
# # Python 
#
# ##### *Des fondamentaux à l'utilisation du langage*

# %% [markdown] {"cell_style": "split"}
# Thierry Parmentelat - Inria
#
#

# %% [markdown] {"cell_style": "split"}
# <center><code>thierry.parmentelat@inria.fr</code></center>

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## plateformes
#
# * notebooks
#   * https://nbhosting.inria.fr/auditor/notebook/python-slides
# * même contenu en version HTML statique
#   * https://nbhosting.inria.fr/builds/python-slides/handouts/latest/
# * les sources des notebooks : 
#   * https://github.com/flotpython/slides  
#   
# * exercices autocorrigés
#   * https://nbhosting.inria.fr/auditor/notebook/exos-mooc
#

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### et aussi le MOOC
#
# en ligne sur France Université Numérique
#
# * le MOOC "Python 3 : des fondamentaux aux concepts avancés du langage"
# * https://www.fun-mooc.fr/courses/course-v1:UCA+107001+session02/about

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "cell_style": "split"}
# ## notebooks
#
# * introduction très rapide au fonctionnement de la plateforme

# %% [markdown] {"slideshow": {"slide_type": ""}, "cell_style": "split"}
#   * utilisez les boutons pour cacher / afficher  
#     la structure du cours

# %% [markdown] {"cell_style": "split"}
# ![](media/nbhosting-buttons.png)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "cell_style": "split"}
# ### notebooks - nav slides

# %% [markdown] {"slideshow": {"slide_type": "-"}, "cell_style": "split"}
# * pour naviguer dans les slides
#
#   * Espace : en avant
#   * Shift-Espace : en arrière

# %% [markdown] {"cell_style": "split"}
# ![](media/nbhosting-slides.png)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "cell_style": "split"}
# ### notebooks - nav cells

# %% [markdown] {"slideshow": {"slide_type": ""}, "cell_style": "split"}
# pour naviguer dans les cellules :
#
# si nécessaire au début : sélectionner avec la souris
#
# puis utiliser ***Maj-Entrée* / *Shift-Enter***
#   * pour évaluer la cellule courante (le dernier résultat s'affiche)
#   * et passer à la cellule suivante
#   

# %% {"cell_style": "split"}
10 * 30

# %% {"cell_style": "split"}
L = [1, 2]
len(L)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "cell_style": "center"}
# ### notebooks - extensions

# %% [markdown]
# ![](media/nbhosting-plain.png)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## plan du cours

# %%
# le plan : survol
from plan import plan; plan("intro")

# %% {"slideshow": {"slide_type": "slide"}}
# le plan : un peu plus de détails
from plan import plan; plan()

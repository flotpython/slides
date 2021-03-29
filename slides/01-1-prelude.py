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
#   notebookname: Plan
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
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
# ## Thierry Parmentelat

# %% [markdown] {"cell_style": "split"}
# ## Inria

# %% [markdown]
# <center><code>thierry.parmentelat@inria.fr</code></center>

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # tour de table

# %% [markdown] {"cell_style": "split"}
# ### vos connaissances
#
# * en programmation ?
# *  en Python ?
# * gestionnaire de code (git?)
# * packaging, tests, documentation
# * calcul scientifique
# * programmation asynchrone

# %% [markdown] {"cell_style": "split"}
# ### vos attentes ?
#
# et vos objectifs ?

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # formalités
#
# * journal des présences
# * questionnaire pour évaluer la formation
# * horaires

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # plateformes
#
# * vidéo conférence  
#   * principal https://rdv4.rendez-vous.renater.fr/python-initial-inrae
#   * backup https://meet.jit.si/python-initial-inrae
# * notebooks
#   * https://nbhosting.inria.fr/auditor/notebook/python-initial

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # et aussi
#
# en ligne sur France Université Numérique
#
# * le MOOC "Python 3 : des fondamentaux aux concepts avancés du langage"
# * https://www.fun-mooc.fr/courses/course-v1:UCA+107001+session02/about

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "cell_style": "split"}
# # notebooks
#
# * introduction très rapide au fonctionnement de la plateforme

# %% [markdown] {"slideshow": {"slide_type": ""}, "cell_style": "split"}
#   * utilisez les boutons pour cacher / afficher  
#     la structure du cours

# %% [markdown] {"cell_style": "split"}
# ![](media/nbhosting-buttons.png)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "cell_style": "split"}
# # notebooks - suite

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "cell_style": "split"}
# * pour naviguer dans les slides
#
#   * Espace : en avant
#   * Shift-Espace : en arrière

# %% [markdown] {"cell_style": "split"}
# ![](media/nbhosting-slides.png)

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "cell_style": "split"}
# # notebooks - suite

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

# %% [markdown] {"slideshow": {"slide_type": "slide"}, "cell_style": "split"}
# # notebooks - suite

# %% [markdown]
# ![](media/nbhosting-plain.png)

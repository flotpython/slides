# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   nbhosting:
#     title: outils externes utiles
#   rise:
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": ""}
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown] slideshow={"slide_type": ""}
# # outils externes utiles

# %% [markdown] slideshow={"slide_type": "slide"}
# ## git

# %% [markdown] slideshow={"slide_type": ""}
# * c'est juste indispensable de **toujours** travailler sous un SCM
# * vous commencez un projet, le réflexe :
#   * créer un dossier
#   * `git init`
#   * et commiter fréquemment
# * pensez ensuite à dupliquer votr dépôt sur une plateforme distante
#   * github - gitlab - bitbucket
#   * ou autre self-hosted
#   * pour avoir une sauvegarde
#   * et éventuellement collaborer
#
# * **n'attendez pas d'en avoir besoin !**
#   * c'est utile **tout de suite**

# %% [markdown] slideshow={"slide_type": "slide"}
# ## intégration continue

# %% [markdown] slideshow={"slide_type": ""}
# * en aval des grandes plateformes, il est facile de mettre en place un CI
#   * c'est-à-dire de déclencher des vérifications **à chaque commit**
#   * ce qui sous-entend que vous avez écrit des test unitaires bien sûr :)
#   * gratuit pour un usage modeste
#   
# * exactement la même logique avec la **documentation continue**
#   * i.e. recalculer une doc toujours à jour
#   * avec plusieurs versions si nécessaire
#   * qu'on peut mettre en place grâce à un *webhook* entre,  
#     typiquement, `github` (ou autre) et `readthedocs.io`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## vérification: `pylint`

# %% [markdown] slideshow={"slide_type": ""}
# * [https://www.pylint.org/](https://www.pylint.org/)
# * permet de vérifier **un très grand nombre** de bonnes propriétés
# * **super utile**:
#   * *pylint saves the day*
#   * https://codewithoutrules.com/2016/10/19/pylint/
# * demande un investissement initial
#   * mais ROI très court !

# %%
# pour installer l'outil
# tapez ceci DANS LE TERMINAL
# et en enlevant le ! 
# !pip3 install pylint

# %% [markdown] slideshow={"slide_type": "slide"}
# ### filtrer la sortie de `pylint`

# %% [markdown] slideshow={"slide_type": ""}
# * problème principal: trop de features : **beaucoup de bruit**
# * déterminer avec l'expérience les traits importants
# * commencer avec la liste complète, et **éliminer le bruit**
# * constituer un `pylintrc` pour le projet
#   * https://docs.pylint.org/en/1.6.0/run.html#command-line-options
# * création d'un squelette avec `pylint --generate-rcfile`
# * `disable=c0111` (aussi par nom, catégories, ...)
# * peut se faire fichier / fichier, ou même ligne / ligne

# %% [markdown] slideshow={"slide_type": "slide"}
# ###  `pylint` intégré dans IDE

# %% [markdown] slideshow={"slide_type": ""}
# * idéalement branché sur éditeur en *mode continu* 
# * pylint lancé à chaque sauvegarde
# * https://pylint.readthedocs.io/en/latest/user_guide/ide-integration.html
# * perso: j'utilise atom https://atom.io/

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exercice pylint

# %% [markdown] slideshow={"slide_type": ""}
# * lancer pylint sur dummysim - ou sur un projet à vous
# * affiner un `pylintrc` commun au projet pour enlever le bruit
# * modifier le code pour éliminer les messages considérés comme pertinents

# %% [markdown] slideshow={"slide_type": "slide"}
# ## présentation du code et la `PEP008`
#
# * à partir des conventions de [PEP8](https://www.python.org/dev/peps/pep-0008/)
# * de (très / trop) nombreux outils sont disponibles

# %%
# pareil, à taper dans la terminal et sans le !
# !pip3 install pep8

# %% slideshow={"slide_type": "slide"}
# !cat samples/presentation.py

# %%
# !pep8 samples/presentation.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ### en mode actif
#
# * pour ce qui est de la vérification quotidienne: 
#   * déjà fait par `pylint`
# * pour les gros refactoring
#   * opter pour un outil qui sait faire les modifications automatiquement
#   * `autopep8`
#   * `flake8`
#   * `etc`

# %%
# !pip3 install autopep8

# %%
# on copie pour pouvoir voir les différences
# !cp samples/presentation.py samples/reparation.py

# %%
# allons-y
# !autopep8 --in-place samples/reparation.py

# %%
# !diff -c samples/presentation.py samples/reparation.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ## online python tutor

# %% [markdown]
# * un outil en ligne pour visualiser l’exécution de code Python ligne par ligne
# * utile pour l'apprentissage du langage
# * que nous utilisons copieusement ici même
# * http://pythontutor.com/ 

# %% [markdown] slideshow={"slide_type": "slide"}
# ## et autres
#
# * pour le calcul scientifique
#   * `numpy`: tableaux et matrices efficaces
#   * `pandas`: données tabulaires (type excel/csv)
#   * `scikit-learn`: machine-learning
#   * `matplotlib`: visualisation
#   * plein d'autres libs de visualisation - seaborn, altair, bokeh, plotly
# * autour des notebooks
#   * bien sûr `jupyter` (jupyterlab), avec - je recommande - `jupytext`
#   * mais aussi vs-code,
#   * ou bien en version hostée sur https://cocalc.com`
#   * ou encore https://colab.research.google.com/
#   * pour les notebooks interactifs: `ipywidgets` et `interact()`
# * `asyncio` pour la programmation asynchrone
# * `unittest` et autres `pytest` pour les tests et l'intégration continue
# * `sphinx` et `readthedocs.io` pour la documentation
#   * pour info ce support est transformé en HTML avec `jupyter-book`

# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
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
#   notebookname: outils externes utiles
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
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% slideshow={"slide_type": "slide"}
from plan import plan; plan("compléments", "outils")

# %% [markdown] slideshow={"slide_type": "slide"}
# # outils externes utiles

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

# %% [markdown] slideshow={"slide_type": "slide"}
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
# ## détaillés plus loin
#
# * `numpy` pour le calcul scientifique
# * `asyncio` pour la programmation asynchrone
# * `unittest` et autres `pytest` pour les tests et l'intégration continue
# * `sphinx` et `readthedocs.io` pour la documentation
# * et bien sûr `git` pour tout
# * et enfin `jupyter` pour écrire des notebooks

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour aller plus loin

# %% [markdown]
# * une revue et correction de code publique très instructive faite par sametmax
#   * http://sametmax.com/revue-de-code-publique/

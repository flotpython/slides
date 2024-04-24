# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted,-editable
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
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

# %% [markdown] slideshow={"slide_type": ""}
# ## git
#
# c'est juste indispensable de **toujours** travailler sous un SCM !  
# vous commencez un projet, ayez le réflexe de :
#
# * créer un dossier
# * `git init`
# * et commiter fréquemment
#
# pensez ensuite à dupliquer votr dépôt sur une plateforme distante (github - gitlab - bitbucket)
#
# * pour avoir une sauvegarde
# * et éventuellement collaborer
#
# **n'attendez pas d'en avoir besoin !**:  *c'est utile **tout de suite***

# %% [markdown] slideshow={"slide_type": "slide"}
# ## librairies tierces (non standard)

# %% [markdown]
# ### `pypi.org`
#
# * toutes les librairies importantes se trouvent ici  <https://pypi.python.org/>
# * **attention** souvenez-vous que n'importe qui peut y publier !  
#   la présence sur pypi **ne veut pas dire** code fiable, supporté
#
# * `pip` est le programme qui permet de les installer facilement  
#   <https://pip.pypa.io/en/latest/installation/>

# %% [markdown]
# ### `pip` : comment installer une librairie externe
#
# ```bash
# # dans le terminal
# $ pip help
#
# Usage:
#   pip <command> [options]
#
# Commands:
#   install                     Install packages.
#   download                    Download packages.
#   uninstall                   Uninstall packages.
#   freeze                      Output installed packages in requirements format.
#   inspect                     Inspect the python environment.
#   list                        List installed packages.
#   show                        Show information about installed packages.
# …
# ```
#
# et donc, typiquement par exemple on fait simplement
#
# ```bash
# # toujours dans le terminal
# pip install numpy
# ```
#
# * capable de gérer les setups complexes, y compris lorsque du code binaire est nécessaire (cf *wheels*) 
# * n'affranchit pas de bien lire la doc d'installation lorsqu'une approche naïve échoue
# * à signaler aussi : utilisez
#   `python -m pip` à la place de `pip`  
#   en cas de multiples installations + ou - stables, pour être sûr d'installer pour le bon Python

# %% [markdown] slideshow={"slide_type": "slide"}
# ### librairies notables
#
# * pour le calcul scientifique
#   * `numpy`: tableaux et matrices efficaces
#   * `pandas`: données tabulaires (type excel/csv)
#   * `scikit-learn`: machine-learning
#   * `matplotlib`: visualisation
#   * plein d'autres libs de visualisation - `seaborn`, `altair`, `bokeh`, `plotly`, ...
# * pour le dashboards / UI
#   * `streamlit`
#   * `flet`
# * autour des notebooks
#   * bien sûr `jupyter` (jupyterlab), avec - je recommande - `jupytext`
#   * mais aussi vs-code,
#   * ou bien en version hostée sur <https://cocalc.com/>
#   * ou encore <https://colab.research.google.com/>
#   * pour les notebooks interactifs: `ipywidgets` et `interact()`
# * `asyncio` pour la programmation asynchrone
# * `unittest`, et surtout `pytest` pour les tests et l'intégration continue
# * `sphinx` et `readthedocs.io` pour la documentation  
#   pour info ce support est transformé en HTML avec `jupyter-book`

# %% [markdown]
# ## vérification: `pylint`
#
# un outil externe qui vérifie le code par analyse statique
#
# * permet de vérifier **un très grand nombre** de bonnes propriétés
# * **super utile**: voir [*pylint saves the day*](https://codewithoutrules.com/2016/10/19/pylint/)
# * demande un investissement initial, mais retour sur investissement très court !
# * [https://www.pylint.org/](https://www.pylint.org/)
#
# ```bash
# # et qui s'installe donc avec, wait for it...
# pip install pylint
# ```

# %% [markdown] slideshow={"slide_type": ""}
# ### filtrer la sortie de `pylint`
#
# le problème principal avec `pylint`: trop de features, du coup **beaucoup de bruit** !  
# il convient de déterminer avec l'expérience les traits importants  
# pour cela, commencer avec la liste complète, et **éliminer le bruit**:
#
# * constituer un fichier de config pour le projet  
#   <https://pylint.readthedocs.io/en/stable/user_guide/configuration/index.html#configuration>
#
# * enlever progressivement les erreurs acceptables  
#   ce qui peut se faire à tous les niveaux: projet  ou fichier ou  même ligne par ligne

# %% [markdown]
# ## la doc avec `Sphinx` et `readthedocs.io`
#
# vous pourrez constater que l'énorme majorité des documentations de librairies sont hostées sur <https://readthedocs.io/>  
# le plus souvent elles sont construites à partir des sources en utilisant [la librairie `Sphinx`](https://www.sphinx-doc.org/en/master/)
#
# pour information, ces supports sont produits [avec `jupyter-book`](https://jupyterbook.org/en/stable/intro.html), qui élabore au-dessus de Sphinx une couche spécifique aux notebooks

# %% [markdown]
# ## les tests avec `pytest`
#
# la librairie standard propose un module `unittest`; c'est un apport appréciable ! 
# la librairie `pytest` est compatible avec, mais étend encore les possibilités de ce module, c'est une librairie très fréquemment utilisée

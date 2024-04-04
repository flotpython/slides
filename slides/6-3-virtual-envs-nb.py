# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted,-editable
#     formats: py:percent
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
# ---

# %% [markdown]
# # Environnements virtuels
#
# Terminons ce tour d'horizon pour dire un mot des environnements virtuels.
#
# Par le passé, on installait python **une seule fois** dans le système ;
# en 2024, c'est une approche qui n'a **que des inconvénients** :
#
# * quand on travaille sur plusieurs projets, on peut avoir besoin de Python-3.9 sur l'un et Python-3.12 sur un autre ;
# * ou alors on peut avoir un projet qui a besoin de `Django==3.4` et un autre qui ne marche qu'avec `Django>=4.0` ;
# * en plus par-dessus le marché, dans certains cas il faut être super utilisateur pour modifier l'installation ; typiquement on passe son temps à faire `sudo pip` au lieu de `pip`…
#
# et le seul avantage, c'est que tous les utilisateurs de l'ordi peuvent partager l'installation ; sauf que, plus de 99 fois sur 100, il n'y a qu'un seul utilisateur pour un ordi ! Bref, c'est une pratique totalement dépassée.

# %% [markdown]
# La création et la gestion d'environnements virtuels sont **très faciles** aujourd'hui. Aussi c'est une **pratique recommandée** de se créer **un virtualenv par projet**. C'est tellement pratique qu'on n'hésite pas une seconde à repartir d'un environnement vide à la moindre occasion, par exemple lorsqu'on a un doute sur les dépendances.
#
# Le seul point sur lequel il faut être attentif, c'est de trouver un moyen de **savoir en permanence** dans quel environnement on se trouve. Notamment :
#
# * une pratique très répandue consiste à s'arranger pour que **le prompt dans le terminal** indique cela,
# * dans vs-code, dans la bannière inférieure, on nous montre toujours l'environnement courant.

# %% [markdown] cell_style="center"
# ````{figure} media/venv-terminal.png
# :align: center
# **dans le terminal**, le prompt nous montre le venv courant, ici d'abord `base`, puis ensuite `flotpython-course`
# ````

# %% [markdown] cell_style="center"
# ````{figure} media/venv-vscode.png
# :align: center
#
# **vs-code** nous montre le venv courant et nous permet de le changer
# ````

# %% [markdown]
# ## Les outils
#
# Par contre il reste le choix entre plusieurs outils, que j'essaie de lister ici :
#
# * [`venv`](https://docs.python.org/3/library/venv.html) un module de la librairie standard
# * [`miniconda`](https://docs.conda.io/en/latest/miniconda.html) un sous-produit de anaconda
# * enfin [`virtualenv`](https://virtualenv.pypa.io/en/latest/) un module externe, qui préexistait à `venv` et qui a fourni la base des fonctionnalités de `venv`, mais qui me semble aujourd'hui obsolète

# %% [markdown]
# Actuellement **j'utilise quant à moi `miniconda`**
#
# Voici à titre indicatif une session sous MacOS en guise de rapide introduction.
# Vous remarquerez comme le *prompt* reflète **l'environnement dans lequel on se trouve**, ça semble relativement impératif si on ne veut pas s'emmêler les pinceaux.

# %% [markdown]
# ## Micro-démo
#
# ### La liste de mes environnements
#
# ```
# [base] ~ $ conda env list
# conda environments:
# #
# base                  *  /Users/jeanmineur/miniconda3
# <snip ...>
# ```

# %% [markdown]
# ### j'en crée un nouveau avec Python-3.12
#
# ```
# [base] ~ $ conda create -n demo-py312 python=3.12
# Collecting package metadata (current_repodata.json): done
# Solving environment: done
# <snip ...>
# ```

# %% [markdown]
# ### on le voit
# ```
# [base] ~ $ conda env list
# conda environments:
# #
# base                  *  /Users/jeanmineur/miniconda3
# demo-py312               /Users/jeanmineur/miniconda3/envs/demo-py312
# <snip...>
# ```

# %% [markdown]
# ### pour entrer dans le nouvel environnement
#
# ```
# [base] ~ $ conda activate demo-py312
# [demo-py312] ~ $
# ```

# %% [markdown]
# ### les packages installés
#
# très peu de choses
#
# ```
# [demo-py312] ~ $ pip list
# Package    Version
# ---------- -------------------
# certifi    2020.4.5.1
# pip        20.0.2
# setuptools 46.2.0.post20200511
# wheel      0.34.2
# ```

# %% [markdown]
# ### on y installe ce qu'on veut
# ```
# [demo-py312] ~ $ pip install numpy
# ```

# %% [markdown]
# ### la version de python
# ```
# [demo-py312] ~ $ python --version
# Python 3.12.2
# ```

# %% [markdown]
# ### sortir
# ```
# [demo-py312] ~ $ conda deactivate
# [base] ~ $
# ```

# %% [markdown]
# ### la version de python
# ```
# [base] ~ $ python --version
# Python 3.11.7
# ```

# %% [markdown]
# ### on n'a pas perturbé l'environnement de départ
# ```
# [base] ~ $ pip show numpy
# Name: numpy
# Version: 1.18.1
# ```

# %% [markdown]
# ### pour détruire l'environnement en question
# ```
# [base] ~ $ conda env remove -n demo-py312
#
# Remove all packages in environment /Users/jeanmineur/miniconda3/envs/demo-py312:
# ```

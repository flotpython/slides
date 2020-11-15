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
#   notebookname: "Pr\xE9sentation du code"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% [markdown]
# # présentation du code

# %% [markdown] slideshow={"slide_type": "slide"}
# ## style de présentation du code
#
# * tout le code de la librairie standard obéit à des règles de présentation
# * elles ne sont pas imposées par le langage, **MAIS**
# * elles sont très largement appliquées
# * autant prendre de bonnes habitudes
# * survol rapide ici des traits les plus marquants

# %% [markdown] slideshow={"slide_type": "slide"}
# ## PEP-008

# %% [markdown]
# [la note dite *PEP-008*](https://www.python.org/dev/peps/pep-0008/) donne une norme pour la présentation

# %% [markdown] cell_style="split"
# OUI:
#
# * `fonction(a, b, c)`
# * `GLOBALE = 1000`
# * lignes de longueur <= 80 caractères

# %% [markdown] cell_style="split"
# NON:
#
# * `fonction (a,b,c)`
# * `globale=1000`
# * lignes très longues

# %% [markdown]
# on va voir tout ça un peu plus en détail

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les espaces

# %% [markdown]
# |  OUI  |  NON  |
# |------------------|---------------|
# | `a = 10` | ~~`a=10`~~ |
# | `L = [1, 2, 3, 4]` | ~~`L = [1,2,3,4]`~~ |
# | `D = ['k1': 'v1', 'k2': 'v2'}` | ~~`D = ['k1':'v1', 'k2' : 'v2'}`~~ | 

# %% [markdown]
# |  OUI  |  NON  |
# |------------------|---------------|
# | `def foo(a, b, c):` | ~~`def foo (a, b, c):`~~ | 
# |                     | ~~`def foo(a,b,c):`~~ | 
# | `res = foo(a, b, c)` | ~~`res = foo (a, b, c)`~~ |

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les noms de variables

# %% [markdown] cell_style="split"
# | type d'objet | catégorie |
# |------------------|---------------|
# | variable usuelle | 1 | 
# | fonction | 1 |
# | module | 1 | 
# | classe | 2 |

# %% [markdown] cell_style="split"
# | catégorie |  OUI  |  NON  |
# |------|------------------|---------------|
# | 1    | `minuscule` | ~~`MAJUSCULE`~~ |
# | 1    | `deux_mots` | ~~`DeuxMots`~~  |
# | 2    | `Mixte`     | ~~`minuscule`~~ (sauf types prédéfinis) |
# | 2    | `DeuxMots`  | ~~`MAJUSCULE`~~ | 

# %% [markdown] slideshow={"slide_type": "slide"}
# ## largeur de la page
#
# * dans sa version orthodoxe, la largeur de la page est limitée à 80 caractères
# * l'idée est de pouvoir juxtaposer plusieurs codes (3 voire 4 ) dans la largeur d'un écran moderne
# * on a parfois besoin de recourir à des astuces pour y arriver

# %% [markdown] slideshow={"slide_type": "slide"}
# ### longueur des lignes

# %% [markdown]
# plusieurs astuces pour respecter une largeur fixe :

# %%
# 1. utiliser les parenthèses

def foo():
    if expression(args):
        return (le_resultat() and de_l_expression() 
                and est_susceptible() and de_prendre()
                and beaucoup_de_place())


# %% [markdown] slideshow={"slide_type": "slide"}
# ### longueur des lignes et parenthèses

# %%
# 2. ça marche aussi avec les {} et [] 

GLOBAL_MAP = [
    {'shortcut': 'ctrl-w', 'function': 'RISE:render-all-cells'},
    {'shortcut': 'ctrl-q', 'function': 'RISE:edit-all-cells'},
]


# %% [markdown] slideshow={"slide_type": "slide"}
# ### longueur des lignes et chaines littérales

# %%
# 3. lorsqu'on a besoin de retourner des chaines de caractères très longues
# on peut utiliser un conjonction de
# * parenthèses
# * concaténation des chaines dans le source

def longue_chaine(nom, prenom):
    return (
        f"<table><thead><tr><th>Nom</th><th>Prénom</th></tr></thead>"
        f"<tbody><tr><td>{nom}</td><td>{prenom}</td></tr></tbody>"
        f"</table>"
    )


# %% cell_style="split"
from IPython.display import HTML
HTML(longue_chaine("Jean", "Dupont"))


# %% [markdown] cell_style="split"
# **NOTE**: pour ce genre d'application, utiliser plutôt une bibliothèque de *templating*.

# %% [markdown] slideshow={"slide_type": "slide"}
# ### longueur des lignes : éviter le `\`

# %% [markdown]
# enfin il peut être utile de savoir qu'on peut 'échapper' les fins de ligne

# %%
# on **pourrait** écrire ça (sachez le lire) 
# mais je vous recommande de **ne pas faire comme ça**
# essayez par exemple d'ajouter un espace juste après un \ 
# ça ne se voit pas et pourtant ça fait tout planter

def foo():
    if expression(args):
        return le_resultat() and de_l_expression() \
                and est_susceptible() and de_prendre() \
                and beaucoup_de_place()


# %% [markdown] slideshow={"slide_type": "slide"}
# ### longueur des lignes : les parenthèses c'est mieux

# %% tags=["raises-exception"]
# faites plutôt comme ça: ajoutez une 
# paire de parenhèses, et bye bye les \

def foo():
    if expression(args):
        return (le_resultat() and de_l_expression()  
                and est_susceptible() and de_prendre() 
                and beaucoup_de_place())

# %% [markdown] slideshow={"slide_type": "slide"}
# ## de nombreux outils

# %% [markdown] cell_style="center"
# * il existe un très grand nombre d'outils de vérification de code Python
# * du plus simple qui vérifie seulement *PEP008* - par exemple `autopep8`
# * au plus compliqué - genre `pylint` - qui peut trouver 
#   * les erreurs de frappe dans les noms de variable
#   * les imports inutiles

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `autopep8`

# %% [markdown] cell_style="split"
# pour rendre un code compatible, par exemple avec `autopep8`
#
# ```bash
# # dans le terminal
#
# # installation (une bonne fois)
# pip install autopep8 
# ```

# %% [markdown] cell_style="split"
# avant de modifier votre fichier assurez-vous d'avoir un backup - par exemple un commit
#
# ```bash
# # commiter foo.py
# git add foo.py
# git commit -m 'avant autopep8'
#
# # appliquer autopep8
# autopep8 -i foo.py
#
# # évaluer les dégâts
# git diff foo.py
#
# # revenir en arrière
# git checkout -- foo.py
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### pour aller plus loin
#
# <https://www.python.org/dev/peps/pep-0008/>

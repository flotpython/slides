# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
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
#     title: "pr\xE9sentation du code"
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown]
# # présentation du code
#
# dans cette partie on voit des **conventions** de codage; on *peut* ne pas les suivre, et le code fonctionne tout de même  
# mais il est **fortement recommandé** de les suivre et de les appiquer - sinon c'est un peu comme si on parlait avec un fort accent :)  
# en particulier tout le code de la librairie standard obéit à ces règles de présentation

# %% [markdown]
# ## PEP-008
#
# ces règles de présentation sont explicitées dans [la note dite *PEP-008*](https://www.python.org/dev/peps/pep-0008/)
#
# les points les plus importants qu'on vous demande **de retenir et d'appliquer** :
#
# | OUI | NON |
# |-|-|
# | `fonction(a, b, c)` | ~~`fonction (a,b,c)`~~
# | `GLOBALE = 1000` | ~~`globale=1000`~~ |
# | `variable`, `ma_variable` | ~~`Variable`~~, ~~`maVariable`~~ |
# | `module`, `function` | ~~`Module`~~, ~~`Function`~~ |
# | `Classe`, `UneClasse`  | ~~`classe`~~, ~~`ma_classe`~~, ~~`maClasse`~~ |
# | lignes de longueur <= 80 caractères | lignes très longues |
# | *docstrings* pour documenter à minima| |

# %% [markdown]
# on va voir tout ça un peu plus en détail

# %% [markdown]
# ## les espaces
#
# |  OUI  |  NON  |
# |------------------|---------------|
# | `a = 10` | ~~`a=10`~~ |
# | `L = [1, 2, 3, 4]` | ~~`L = [1,2,3,4]`~~ |
# | `D = ['k1': 'v1', 'k2': 'v2'}` | ~~`D = ['k1':'v1', 'k2' : 'v2'}`~~ |

# %% [markdown]
# ### les espaces (2/3)
#
# |  OUI  |  NON  |
# |------------------|---------------|
# | `def foo(a, b, c):` | ~~`def foo (a, b, c):`~~ | 
# |                     | ~~`def foo(a,b,c):`~~ | 
# | `res = foo(a, b, c)` | ~~`res = foo (a, b, c)`~~ |

# %% [markdown]
# ### les espaces (3/3)
#
# | **OUI** | **NON** |
# |---------|---------|
# | `d = {1: 'un', 2: 'deux'}` | ~~`d = {1:'un',2:'deux'}`~~ |
# |                          | ~~`d = { 1 : 'un', 2 : 'deux' }`~~ |
# | `s = {'a', 'b', 'c', 'd'}` | ~~`s = {'a','b','c','d'}`~~ |
# |                          | ~~`s = { 'a' , 'b' , 'c' , 'd' }`~~ |

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les noms de variables

# %% [markdown] tags=["gridwidth-1-2"]
# | type d'objet | catégorie |
# |------------------|---------------|
# | variable usuelle | 1 | 
# | fonction | 1 |
# | module | 1 | 
# | classe | 2 |

# %% [markdown] tags=["gridwidth-1-2"]
# | catégorie |  OUI  |  NON  |
# |------|------------------|---------------|
# | 1    | `minuscule` | ~~`MAJUSCULE`~~ |
# | 1    | `deux_mots` | ~~`DeuxMots`~~  |
# | 2    | `Mixte`     | ~~`minuscule`~~ (sauf types prédéfinis) |
# | 2    | `DeuxMots`  | ~~`MAJUSCULE`~~ |

# %% [markdown]
# ````{admonition} exemples
#
# ```python
# # module en minuscule, classe en chasse mixte
# from argparse import ArgumentParser
#
# # fonction en minuscule, variable en minuscule
# def init(config):
#     ...
#
# ```
# ````

# %% [markdown] tags=[]
# ````{admonition} un contrexemple
# :class: warning admonition-small
#
# en théorie toute la librairie standard suit la PEP8  
# sauf que certains très vieux modules n'étaient pas dans les clous - et pour ne pas casser le code c'est resté comme ça...
#
# ```python
# # ici le second 'datetime' est un nom de classe, et devrait donc s'appeler 'DateTime'
# from datetime import datetime
#
# # du coup on recommande de l'importer comme ceci
# from datetime import datetime as DateTime
# ```
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ## largeur de la page
#
# * dans sa version orthodoxe, la largeur de la page est limitée à 80 caractères  
#   en pratique aujourd'hui on peut être un peu plus souple,   
#   mais **jamais > 100 caractères de large**
#
# * l'idée est de pouvoir juxtaposer plusieurs codes (3 voire 4 )  
#   dans la largeur d'un écran moderne
#
# * on a parfois besoin de recourir à des astuces pour y arriver

# %% [markdown]
# ### longueur des lignes
#
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
# on peut utiliser une conjonction de
# * parenthèses
# * concaténation des chaines dans le source

def longue_chaine(nom, prenom):
    return (
        f"<table><thead><tr><th>Nom</th><th>Prénom</th></tr></thead>"
        f"<tbody><tr><td>{nom}</td><td>{prenom}</td></tr></tbody>"
        f"</table>"
    )


# %% [markdown]
# ````{admonition} conseil: éviter le \ final
# :class: admonition-x-small
#
# techniquement, on *pourrait* 'échapper' les fins de ligne en mettant un `\` avant le *newline*  
# toutefois c'est une pratique *dangereuse*, car sensible à la présence d'espaces, qui ne se voient pas...
#
#   ```python3
#   # on **pourrait** écrire ça (sachez le lire) 
#   # mais je vous recommande de **ne pas faire comme ça**
#   # essayez par exemple d'ajouter un espace juste après un \ 
#   # ça ne se voit pas et pourtant ça fait tout planter
#
#   def foo():
#       if expression(args):
#           return le_resultat() and de_l_expression() \
#                   and est_susceptible() and de_prendre() \
#                   and beaucoup_de_place()
#   ```
#
# bref: **les parenthèses, c'est mieux !**  
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le docstring
#
# lorsqu'on écrit une fonction (ou une classe, ou un module) on la documente comme ceci

# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
def gcd(a, b):
    """
    returns the greatest common divisor
    of both inputs
    """
    while b:
        a, b = b, a % b
    return a


# %% tags=["gridwidth-1-2"]
help(gcd)


# %% [markdown] slideshow={"slide_type": "slide"}
# * le docstring est une simple chaine, sauf qu'elle apparaît en premier 
# * cela permet de ranger de la documentation directement dans l'objet fonction
# * nécessaire pour les fonctions exposées aux utilisateurs

# %% [markdown] slideshow={"slide_type": "slide"}
# ## type hints
#
# de manière optionnelle, on peut indiquer les types des arguments et le type de retour

# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
def gcd2(a: int, b: int) -> int:
    """
    returns the greatest common divisor
    of both inputs
    """
    while b:
        a, b = b, a % b
    return a


# %% tags=["gridwidth-1-2"]
help(gcd2)

# %% [markdown] slideshow={"slide_type": "slide"}
# * annotations de type (*type hints*) totalement optionnelles et ignorées par l'interpréteur
# * mais utiles pour une meilleure documentation
# * et aussi pour détecter des erreurs de type par **analyse statique** i.e. avant l'exécution, avec des outils dédiés [comme par exemple `mypy`](http://mypy-lang.org/)
# * techniquement, ne fait pas partie de la PEP008, car les *type hints* sont postérieurs

# %% [markdown] cell_style="center"
# ## de nombreux outils
#
# * très grand nombre d'outils de vérification de code Python
# * du plus simple qui vérifie seulement *PEP008* - par exemple `flake8`
# * au plus compliqué - genre `pylint` - qui peut trouver 
#   * les erreurs de frappe dans les noms de variable
#   * les imports inutiles,
#   * ...

# %% [markdown]
# ### command line
#
# pour vérifier / réparer, regardez du coté de 
#
# * `autopep8`
# * `black`
# * `flake8`
# * `pylint` (affiche les erreurs pep8, et bien d'autres d'ailleurs)

# %% [markdown] slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
# ### vs-code
#
# ```{image} media/vscode-problems.png
# :align: center
# :width: 500px
# ```

# %% [markdown] tags=["gridwidth-1-2"]
# et pour naviguer entre les erreurs, via la *palette* (ctrl-shift p ou cmd-shift-p)
#
# ```{image} media/vscode-next-problem.png
# :align: center
# :width: 500px
# ```

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
#     title: packages
#   rise:
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown] slideshow={"slide_type": ""}
# # packages

# %% [markdown] slideshow={"slide_type": "slide"}
# ## package = module pour un dossier

# %% [markdown]
# * il est possible d’organiser un gros code source dans un dossier
# * qui peut à son tour contenir d'autres dossiers
# * le package est un module qui correspond à un dossier
# * la structure arborescente est matérialisée par les attributs Python
#   * donc matérialisée par des `.`
#   * notation indépendante de la plate-forme

# %% [markdown] slideshow={"slide_type": "slide"}
# ### attributs pour naviguer l'arbre

# %% [markdown]
# * le package est aux dossiers ce que le module est aux fichiers
# * un objet package est **aussi un objet module**
# * son espace de nommage permet d'accéder à des modules et packages
# * qui correspondent aux fichiers et répertoires contenus dans son répertoire

# %% [markdown] tags=["gridwidth-1-2"]
# arborescence fichiers
#
#     pack1/
#       pack2/
#         mod.py
#           class Foo

# %% [markdown] tags=["gridwidth-1-2"]
# équivalence modules
#
#     pack1
#     pack1.pack2
#     pack1.pack2.mod
#     pack1.pack2.mod.Foo

# %% [markdown] slideshow={"slide_type": "slide"}
# ### import d'un package

# %%
# on peut soit importer le package directement
import pack1

# %% [markdown] slideshow={"slide_type": "slide"}
# ### importer un sous module

# %%
# ou un morceau seulement
import pack1.pack2.mod


# %% [markdown]
# * cette notation demande d’importer le module dans le répertoire `pack1/pack2/mod.py`
# * `pack1` est recherché dans `sys.path`
# * ensuite on descend dans l'arbre des dossiers et fichiers

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `__init__.py`

# %% [markdown]
# * ce fichier **peut** être présent dans le dossier
# * si oui, il est chargé lorsqu'on charge le package
#   * définit le contenu (attributs) du package
# * typiquement utilisé pour définir des raccourcis

# %% [markdown] slideshow={"slide_type": "slide"}
# ### raccourcis

# %% [markdown] slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
# sans raccourci
#
# ```
# graphobj/
#     rect.py     -> classe Rect
#     square.py   -> classe Square
# ```

# %% [markdown] tags=["gridwidth-1-2"]
#
# il faut connaitre le détail  
# des internes du package
#
# ```python
# from graphobj.rect import Rect
# from graphobj.square import Square
# ```

# %% [markdown] tags=["gridwidth-1-2"]
# avec raccourci
#
# ```
# cat graphobj/__init__.py
# from .rect import Rect
# from .square import Square
# ```

# %% [markdown] tags=["gridwidth-1-2"]
# c'est plus simple
#
# ```python
#
# from graphobj import Rect
# from graphobj import Square
# ```

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# ## imports relatifs

# %% [markdown]
# * pour importer un module dans le même package
# * outre les imports absolus (les formes vues jusqu'ici)
# * on peut faire un **import relatif**
#   
# le mécanisme est **un peu** similaire à la navigation dans l'arbre des fichiers :
#
# `from .other import variable`
#
# signifie de faire un import depuis le module `other` **dans le même package** que le module où se trouve ce code

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple

# %% cell_style="center"
pack1.pack2.mod.__package__

# %% [markdown] tags=["gridwidth-1-2"]
# * si dans `pack1/pack2/mod.py` on écrit  
#     `from .aux import foo`
#
# * on va chercher un module dont le nom est  
#     `pack1.pack2.aux`    

# %% [markdown] tags=["gridwidth-1-2"]
# * si dans `pack1/pack2/mod.py` on écrivait  
#     `from ..aux import foo`
#
# * on va chercher un module dont le nom serait  
#     `pack1.aux`    

# %% [markdown] slideshow={"slide_type": "slide"}
# ### attention !

# %% [markdown] cell_style="center"
# * l'import relatif **ne fonctionne pas**  
#   sur la base de l'arborescence de *fichiers*
#
# * mais au contraire il se base sur  
#   l'arborescence des *modules*
#   
# différence subtile, mais frustration garantie

# %% [markdown] slideshow={"slide_type": "slide"}
# #### comment ça marche
#
# * chaque objet module a un attribut `__name__`
# * qui est ce qui sert à calculer le chemin absolu de l'import (en fait l'attribut `__package__`)
# * on ne regarde pas du tout l'attribut `__file__`
#
# ***
#
# * et pour rappel le point d'entrée a toujours pour nom `__main__`, et du coup son `_package__` est `None`
# * **attention** du coup pour les test unitaires
#
# * il vaut mieux utiliser un framework de tests `unittest` ou `pytest` ou `nose`

# %% slideshow={"slide_type": "slide"} tags=["gridwidth-1-2"]
# !cat awesome/io/parser.py

# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
# !cat awesome/io/token.py

# %% tags=["gridwidth-1-2"]
# mais boom
# !python awesome/io/parser.py

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## exemples

# %% [markdown]
# juste pour nettoyer les modules d'exemple
# au cas où on les aurais chargés plus haut

# %% cell_style="center"
import sys

def cleanup():
    to_erase = [modname for modname in sys.modules
                if 'pack1' in modname or 'pack2' in modname]
    for module in to_erase:
        print(f"erasing {module}")
        del sys.modules[module]
        
cleanup()

# %% [markdown]
# ### exemple 1

# %% tags=["gridwidth-1-2"]
# !cat pack1/__init__.py

# %% tags=["gridwidth-1-2"]
# du coup à l'import:
import pack1.pack2.mod

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple 2

# %% tags=["gridwidth-1-2"]
# les imports suivant 
# ne ré-éxécutent pas __init__.py
import pack1.pack2.mod

# %% tags=["gridwidth-1-2"]
# si on recharge pack1:
import importlib
importlib.reload(pack1);

# %%
# puis pack2
importlib.reload(pack1.pack2);

# %% [markdown] slideshow={"slide_type": "slide"}
# ### inspection

 # %%
 pack1

# %%
pack1.pack2

# %%
pack1.pack2.mod

# %% tags=["gridwidth-1-2"]
pack1.x

# %% tags=["gridwidth-1-2"]
pack1.pack2.y

# %% tags=["gridwidth-1-2"]
pack1.pack2.mod.FOO

# %% tags=["gridwidth-1-2"]
pack1.FOO is pack1.pack2.mod.FOO

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour aller plus loin

# %% [markdown]
# * les imports relatifs
#   * http://sametmax.com/les-imports-en-python/
#   * https://www.python.org/dev/peps/pep-0328/

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
#     display_name: Python 3
#     language: python
#     name: python3
#   nbhosting:
#     title: packages
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# # packages

# %%
#from plan import plan; plan("modules", "packages")

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
# * le package est aux directories ce que le module est aux fichiers
# * un objet package est **aussi un objet module**
# * son espace de nommage permet d'accéder à des modules et packages
# * qui correspondent aux fichiers et répertoires contenus dans son répertoire

# %% [markdown] cell_style="split"
# arborescence fichiers
#
#     pack1/
#       pack2/
#         mod.py

# %% [markdown] cell_style="split"
# équivalence modules
#
#     pack1
#     pack1.pack2
#     pack1.pack2.mod

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
# * si oui il est chargé lorsqu'on charge le package
#   * définit le contenu (attributs) du package
# * typiquement utilisé pour définir des raccourcis

# %% [markdown] slideshow={"slide_type": "slide"}
# ### raccourcis

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# sans raccourci
#
# ```
# graphobj/
#     rect.py     -> classe Rect
#     square.py   -> classe Square
# ```

# %% [markdown] cell_style="split"
#
# il faut connaitre le détail  
# des internes du package
#
# ```python
# from graphobj.rect import Rect
# from graphobj.square import Square
# ```

# %% [markdown] cell_style="split"
# avec raccourci
#
# ```
# cat graphobj/__init__.py
# from .rect import Rect
# from .square import Square
# ```

# %% [markdown] cell_style="split"
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
# signifie de faire un import depuis le module `other` dans le même package que le module où se trouve ce code

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple

# %%
pack1.pack2.mod.__name__

# %% [markdown] cell_style="split"
# * si dans `pack1/pack2/mod.py` on écrit  
#     `from .aux import foo`
#
# * on va chercher un module dont le nom est  
#     `pack1.pack2.aux`    

# %% [markdown] cell_style="split"
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
# * mais au contraire il se base sur  
#   l'arborescence des *modules*
#   
# différence subtile, mais frustration garantie

# %% [markdown] slideshow={"slide_type": "slide"}
# #### comment ça marche
#
# * chaque objet module a un attribut `__name__`
# * qui est ce qui sert à calculer le chemin absolu de l'import
# * on ne regarde pas du tout l'attribut `__file__`
#
# ***
#
# * et pour rappel le point d'entrée a toujours pour nom `__main__`
# * **attention** du coup pour les test unitaires
#
# * il vaut mieux utiliser un framework de tests `unittest` ou `pytest` ou `nose`

# %% cell_style="split" slideshow={"slide_type": "slide"}
# !cat awesome/io/parser.py

# %% cell_style="split" slideshow={"slide_type": ""}
# !cat awesome/io/token.py

# %% cell_style="split"
# mais boom
# !python awesome/io/parser.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemples

# %% [markdown]
# juste pour nettoyer les modules d'exemple
# au cas où on les aurais chargés plus haut

# %% cell_style="center"
import sys

def cleanup():
    to_erase = [x for x in sys.modules.keys()
                if 'pack1' in x or 'pack2' in x]
    for module in to_erase:
        print(f"erasing {module}")
        del sys.modules[module]
        
cleanup()

# %% [markdown]
# ### exemple 1

# %% cell_style="split"
# !cat pack1/__init__.py

# %% cell_style="split"
# du coup à l'import:
import pack1.pack2.mod

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple 2

# %% cell_style="split"
# les imports suivant 
# ne ré-éxécutent pas __init__.py
import pack1.pack2.mod

# %% cell_style="split"
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

# %% cell_style="split"
pack1.x

# %% cell_style="split"
pack1.pack2.y

# %% cell_style="split"
pack1.pack2.mod.FOO

# %% cell_style="split"
pack1.FOO is pack1.pack2.mod.FOO

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour aller plus loin

# %% [markdown]
# * les imports relatifs
#   * http://sametmax.com/les-imports-en-python/
#   * https://www.python.org/dev/peps/pep-0328/

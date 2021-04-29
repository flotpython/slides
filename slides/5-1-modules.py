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
#     title: modules
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% slideshow={"slide_type": ""}
from plan import plan; plan("modules", "modules")

# %% [markdown]
# # modules

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour réutiliser du code en Python

# %% [markdown]
# * fonctions
#   * pas d'état après exécution
# * **modules**
#   * **garde l'état**
#   * **une seule instance par programme**
# * classes
#   * instances multiples
#   * chacune garde l'état
#   * héritage

# %% [markdown] slideshow={"slide_type": "slide"}
# ### à quoi sert un module ?

# %% [markdown]
# * réutilisation du code
#   * un module peut être importé n’importe où
# * séparation de l’espace de nommage
#   * un module définit essentiellement un espace de nommage
# * utilisation des modules
#   * un fichier top-level (celui qui est exécuté)  
#     importe des modules
#
#   * chaque module peut également importer d’autres modules

# %% [markdown] slideshow={"slide_type": "slide"}
# ### c'est quoi un module ?

# %% [markdown]
# * on peut voir les modules comme des boîtes à outils
#   * que `import` permet de charger dans son espace de travail
# * des centaines de modules sont livrés avec Python
#   * c’est la librairie standard 
# * des milliers de librairies tierces sont disponibles
#   * voir PyPI - the Python Package Index  
#     https://pypi.org/

# %% [markdown] slideshow={"slide_type": "slide"}
# ## création d’un module

# %% [markdown]
# * un module est un objet python 
#   * correspondant au chargement 
#   * d'un fichier ou répertoire source
# * dans le cas d'un répertoire on parle alors d'un *package*  
#   on y reviendra
# * le nom d'un fichier doit finir par `.py`
# * le préfixe suit les règles des variables
#   * i.e. pas de `-` mais des `_`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## importation d’un module

# %% cell_style="split"
# !cat mod.py

# %% cell_style="split"
# je peux l'importer
import mod

# %%
mod

# %% cell_style="split"
mod.spam('good')

# %% [markdown]
# * le nom `mod` dans `import mod` sert à trouver le fichier `mod.py`, 
# * mais **aussi à nommer** l’objet représentant le module importé
# * la syntaxe `mod.` donne accès aux **attributs** du module

# %% [markdown] slideshow={"slide_type": "slide"}
# ## la notion d’attribut

# %% [markdown]
# * un attribut est une annotation sur un objet (ici le module `mod`)
#   * qui associe un nom (ici `spam`) à un autre objet (la fonction)
#   * on référence un attribut par `obj.attribute`
# * un attribut n'est **pas une variable**
#   * les variables sont résolues par liaison lexicale
#   * les attributs sont résolus à run-time
#   * on en reparlera longuement

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un attribut sur quel objet ?

# %% [markdown]
# * on peut attacher un attribut à une grande variété d'objets
#   * modules, packages, classes, instances, fonctions, ..
# * mais pas attacher aux classes ni instances de classes natives

# %%
# on ne peut pas attacher d'attribut aux classes natives 
x = 3
try:
    x.foo = 12
except AttributeError as e:
    print("OOPS", e)


# %% [markdown] slideshow={"slide_type": "slide"}
# #### un attribut sur quel objet ?

# %% [markdown]
# * les familles d'objets où les attributs sont les plus utilisés
#   * modules et packages - on va le voir tout de suite
#   * instances et classes - pour la POO
#   * fonctions - cf. introspection

# %% [markdown] slideshow={"slide_type": "slide"}
# ### attribut et POO

# %% [markdown]
# on verra que l'attribut est le coeur de la POO

# %%
# en anticipant un peu
# je crée un classe vide
class Foo: 
    pass
# et une instance de cette classe
foo = Foo()
# je peux créer l'attribut 'name'
foo.name = 'Jean'

# %% [markdown]
# ## plusieurs formes d'`import`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `from module import name`

# %% cell_style="split"
from mod import spam
spam('direct') 

# %% cell_style="split"
# un peu comme
# spam = mod.spam

# %% [markdown]
# * `from mod import spam`
#   * copie le nom d’attribut `spam`
#   * du module `mod`
#   * dans l’espace de nommage local
#   * plus besoin de la référence au nom du module

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `import modulename as name`

# %% cell_style="split"
import mod as mymod
mymod.spam("module renamed")

# %% cell_style="split"
# un peu comme
# import mod
# mymod = mod
# del mod

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `from modulename import name as newname`

# %% cell_style="split"
from mod import spam as myspam
myspam('renamed function')

# %% cell_style="split"
# un peu comme
# import mod
# myspam = mod.spam
# del mod

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `import dir.dir2.modulename`

# %% cell_style="split"
# !cat pack1/pack2/mod.py

# %% cell_style="split"
import pack1.pack2.mod
pack1.pack2.mod.FOO

# %% [markdown] cell_style="center"
# * on peut donc importer un sous-module dans un package  
#   on reparlera plus longuement des packages
#
# * on peut aussi utiliser `as`:

# %% cell_style="center"
import pack1.pack2.mod as submod
submod.eggs()

# %% [markdown] slideshow={"slide_type": "slide"}
# ### autres importations

# %% cell_style="split"
from mod import *
spam('star')

# %% cell_style="split"
# un peu comme
# mod.spam = spam
# mod.GLOBALE = GLOBALE
# ...

# %% [markdown]
# * `from mod import *` 
#   * copie le nom de **tous** les attributs du module
#   * dans l’espace de nommage local
#   * plus besoin donc non plus de la référence au nom du module
# * remarque: je **déconseille d'éviter** cette directive dans du code de production
#   * on perd la traçabilité des symboles importés

# %% [markdown] slideshow={"slide_type": "slide"}
# ## que fait une importation ?

# %% [markdown]
# * trouver le fichier correspondant au module 
#   * on ne met pas le `.py` du fichier lors d’un import
# * compiler (si besoin) le module en byte-code
# * charger le module pour construire les objets qu’il définit
#   * et les ranger dans les attributs du module
# * affecter la variable locale 
#   * à l'objet module (`import module`)
#   * à l'objet dans le module (`from module import variable`)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### byte-code

# %% [markdown]
# * en première approximation,   
#   vous pouvez ignorer totalement les `.pyc`
#
# * Python se débrouille pour les recompiler au besoin
# * les `.pyc` ne sont générés que par les imports,  
#   et **pas** pour le point d'entrée
#
# * les `.pyc` sont dans un répertoire `__pycache__`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### localisation du fichier du module

# %% [markdown]
# * localisation en parcourant dans l’ordre
#   * répertoire où se trouve le point d'entrée 
#   * `PYTHONPATH` : variable d’environnement de l’OS
#   * répertoires des librairies standards
# * `sys.path` contient la liste des répertoires parcourus
#   * on peut modifier `sys.path` à l’exécution

# %% [markdown] slideshow={"slide_type": "slide"}
# ### les modules sont en cache

# %% [markdown]
# * comme l’importation est une opération lourde, un module n’est chargé qu’**une seule fois** 
#   * les imports suivants réutilisent le module déjà présent en mémoire
# * pour importer de nouveau un module (avec une réexécution du code) il faut utiliser la fonction `imp.reload()`
#   * utile principalement lors de la mise au point

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemples

# %% cell_style="split"
# !cat toplevel.py

# %% cell_style="split"
import toplevel
toplevel.eggs

# %% cell_style="split"
toplevel.eggs = 2
import toplevel
toplevel.eggs

# %% [markdown] slideshow={"slide_type": "slide"}
# ## références partagées

# %% [markdown]
# * les instructions `import` et `from` sont des **affectations implicites** de variables
#   * on a donc le problème des **références partagées** sur des mutables

# %% [markdown] slideshow={"slide_type": "slide"}
# ### pièges de l’importation

# %%
import math
math.pi = 10.

# %% [markdown]
# * en fait je viens de modifier `math.pi` **pour tout mon programme !!**
# * on n’a **pas le problème avec `from`** parce que ça crée une variable locale

# %%
from math import pi
pi = 10
# les autres modules ne sont pas impactés

# %% cell_style="split" slideshow={"slide_type": "slide"}
# !cat spam.py

# %% cell_style="split"
# !cat egg.py

# %%
# !python3 egg.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exécuter un module comme un script

# %% [markdown]
# * un module peut avoir deux rôles
#   * un module classique qui doit être importé  
#     `import module`
#   * un script exécutable  
#     `$ python module.py`
# * tous les modules ont un nom qui est défini par la variable `__name__`
# * le nom d’un module est défini par l’import

# %% cell_style="split"
# !cat toplevel.py

# %% cell_style="split"
import toplevel
print(toplevel.__name__) 

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `if __name__ == "__main__"`

# %% [markdown]
# * si le module est le point d'entrée, (`python3 foo.py`)  
#   son exécution n’est pas le résultat d’un import
#
# * alors `__name__` est mis à la chaîne  `__main__`
# * en faisant un test sur `__name__` dans le module,  
#   on peut écrire un code qui ne s’exécute  
#   que lorsque le module est le point d'entrée
#
# ```python
# # voici un idiome fréquent à la fin d'un source Python
# if __name__ == '__main__':
#     test_module()
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `if __name__ == "__main__"`

# %% cell_style="split"
# !cat samples/fib.py

# %% cell_style="split"
# À la ligne de commande on a
# !python3 samples/fib.py

# %% cell_style="split"
# mais à l'import il ne se passe rien
from samples.fib import fib

# %% [markdown]
# * on peut utiliser cette fonctionnalité pour faire des tests unitaires
# * mais ce n'est guère utilisé en production (trop limité)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `python -i`

# %% [markdown]
# * on peut aussi lancer Python en mode **interactif**
#
# ```
# $ python3 -i fib.py
# 1 1 2 3 5 8 13 21 34 
# >>>
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## attributs d’un module

# %% [markdown]
# * on accède à tous les attributs d’un module en utilisant
#   * `vars(module)` retourne l’espace de nommage de module  
#     (équivalent à `module.__dict__`, voir plus bas)
#   * `dir(module)` liste les attributs
#   * `globals()` retourne l’espace de nommage du module courant  
#
# **remarque** `locals()` retourne l’espace de nommage à l’endroit de l’appel

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `globals()`

# %% cell_style="split"
foo = 10
g = globals()
type(g)
'foo' in g and 'g' in g

# %% cell_style="split"
g['foo']

# %% cell_style="center"
# si on n'est pas dans une fonction ou une classe,
# locals() et globals() retournent la même chose
locals() == globals()


# %% [markdown] slideshow={"slide_type": "slide"}
# ### `locals()`

# %%
# par contre dans une fonction c'est différent
def f():
    tutu = 12
    print(f"tutu dans globals ? : {'tutu' in globals()}")
    print(f"tutu dans locals ? : {'tutu' in locals()}")
    print(f"foo dans globals ? : {'foo' in globals()}")
    print(f"foo dans locals ? : {'foo' in locals()}")
f()

# %% [markdown] slideshow={"slide_type": "slide"}
# ## recharger un module

# %% [markdown] slideshow={"slide_type": ""}
# ### `importlib.reload`

# %%
# pour recharger un fichier 
import importlib
importlib.reload(toplevel);

# %%
toplevel.eggs

# %% [markdown]
# **Note** l'ancien module `imp` est obsolète

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `autoreload` et IPython

# %% [markdown]
# * sous IPython, il existe une extension qui simplifie la vie
#   * pour recharger les modules modifiés
#   * logique en développement
#   * pas utile en production

# %%
# %load_ext autoreload
# %autoreload 2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `sys.modules` (avancé)

# %% [markdown]
# * `sys.modules` est un dictionnaire de tous les modules chargés  
#   nom → *objet module*
#   
# * c'est le cache qui permet le chargement unique 
#
# * `sys.modules[__name__]` 
#   permet de retrouver l'objet module  courant
#
# * `sys.modules[__name__].__dict__` 
#   est l’espace de nommage du module courant

# %% cell_style="split"
import sys
sys.modules[__name__].__dict__ == globals()

# %% cell_style="split"
# pour les geeks
sys.modules[__name__].foo is foo

# %% [markdown] slideshow={"slide_type": "slide"}
# #### recharger un module par `sys.modules`

# %% [markdown]
# * on peut en tirer parti pour recharger un module  
# * (juste pour illustration - préférer `importlib.reload`)

# %% cell_style="split"
import toplevel
toplevel.eggs = 10
toplevel.eggs

# %% cell_style="split"
# enlever du cache
del sys.modules['toplevel']
# force le rechargement
import toplevel
toplevel.eggs

# %% [markdown] slideshow={"slide_type": "slide"}
# ## notions avancées

# %% [markdown]
# ### attributs privés

# %% [markdown]
# * un import importe tous les noms d’un module
# * donc un client peut les modifier 
# * il existe un convention de nommage
# * tous les noms qui commencent par un underscore (`_`) 
#   sont privés au module, ne font pas partie de l'API
#
# * ça n’est qu’une convention, mais c’est généralement suffisant

# %% [markdown] slideshow={"slide_type": "slide"}
# ### ordre dans un module

# %% [markdown]
# * l’ordre des déclarations dans un module à de l’importance
# * le code est exécuté dans l'ordre 
# * une définition de fonction n'exécute pas le code de la fonction
# * mais le code en dehors des fonctions est exécuté à l’import

# %% [markdown] slideshow={"slide_type": "slide"}
# #### ordre dans un module

# %%
# du coup si on appelle une fonction au niveau du module
# il faut qu'elle ait déjà été déclarée
try:
    func1()    # erreur pas encore déclarée
except:
    import traceback
    traceback.print_exc()


# %% slideshow={"slide_type": "slide"}
# on peut appeler dans une fonction
# une autre fonction pas encore définie
def func1():
    func2()    # OK, func2() est déclarée après


# %%
# mais il faut qu'elle soit défini au moment de l'appel
try:
    func1()    # erreur func2() pas encore déclarée
except:
    import traceback; traceback.print_exc()


# %% cell_style="split" slideshow={"slide_type": ""}
# une fois qu'on la déclare
def func2():
    print("in func2")


# %% cell_style="split"
# on peut appeler func1
func1()

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `importlib.import_module`

# %% [markdown]
# * pour importer un module si on a son nom **dans une chaîne**
#   * voir la fonction `importlib.import_module`

# %% cell_style="center"
import importlib
nom_module = "math"
math2 = importlib.import_module(nom_module)
math2.e

# %%
# souvenez vous que celui-là, on l'a modifié sauvagement
math2.pi

# %% [markdown]
# * `exec` est déconseillé pour ce genre d'usages

# %% [markdown] slideshow={"slide_type": "slide"}
# ## espace de nommage

# %% [markdown]
# * un espace de nommage est une association entre attributs et objets
# * souvent implémenté par un dictionnaire appelé `__dict__`
# * deux espaces de nom sont étanches
#   * peuvent avoir tous les deux un attribut disons `name`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `__dict__`

# %% [markdown] slideshow={"slide_type": ""}
# * un module est un bon exemple d'espace de nommage
# * les symboles (fonctions, variables, classes) 
#   * définis au top-level dans le module, e.g. globales
#   * sont ajoutés dans l'espace de nommage attaché au module
# * ex: `mod.spam`
#   * correspond à la clé `spam` dans `mod.__dict__`

# %%
mod.spam is mod.__dict__['spam']

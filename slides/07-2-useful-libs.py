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
#   notebookname: librairies utiles
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
from plan import plan; plan("compléments", "librairies")

# %% [markdown] slideshow={"slide_type": "slide"}
# # librairies utiles

# %% [markdown]
# ## librairie standard

# %% [markdown]
# * le tutorial Python sur ce sujet occupe deux chapitres
#   * [chapitre 10](https://docs.python.org/3/tutorial/stdlib.html) et
#   * [chapitre 11](https://docs.python.org/3/tutorial/stdlib2.html)
#   
# * très très complet, je fais ici un tri arbitraire  
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `logging`

# %% [markdown]
# * dans du code de production on ne fait jamais `print()`
# * on utilise à la place `logging`; de cette façon
# * le code a seulement à choisir un **niveau** de message
#   * parmi error, warning, info, debug
# * on pourra plus tard (i.e. par l'équipe Ops) 
#   * choisir **où** doivent aller les messages
#   * avec quel niveau de gravité
#   * et même selon les modules si nécessaire

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `logging`

# %%
import logging
logging.basicConfig(level=logging.INFO)

# %% cell_style="split"
# au lieu de faire 
print(f"Bonjour le monde") 

# %% cell_style="split"
# on fera plutôt
logging.info("Bonjour le monde")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `sys` et `os`

# %% [markdown]
# #### `import sys`
#
# * gestions de variables utilisées par l’interpréteur

# %% [markdown]
# #### `import os`
#
# * accès cross-platform au système d’exploitation

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `from pathlib import Path`  ( ~~`import os.path`~~)

# %% [markdown]
# * historiquement on gérait les noms de fichiers sur disque avec le sous-module `os.path`
# * depuis la 3.4 une alternative **orientée objet** est disponible
# * il faut l'utiliser pour du nouveau code 
# * on peut tout faire avec
#   * chercher (`glob`) tous les fichiers en `*.truc`
#   * calculer les noms de fichier: concaténer, découper en morceaux, trouver le nom canonique
#   * ouvrir les fichier
#   * accéder aux métadata (taille, date, ..)
#   * etc...

# %% slideshow={"slide_type": "slide"}
from pathlib import Path

for path in Path(".").glob("samples/*.py"):
    # le nom canonique
    print(10*'=', path.absolute())
    # le dernier morceau dans le nom
    print(path.name, end=' ')
    # la taille
    print(path.stat().st_size, 'bytes')
    # touver le nom absolu
    # ouvrir le fichier en lecture
    with path.open():
        pass

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `pathlib`

# %%
# à signaler, les calculs de chemin 
# se font directement à base de l'opérateur /  
répertoire = Path(".")
fichier = répertoire / "samples" / "types01.py"

with fichier.open() as feed:
    for lineno, line in enumerate(feed, 1):
        print(f"{lineno}:{line}", end="")
    
    

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `datetime`, `math` et `random`

# %% [markdown] slideshow={"slide_type": ""}
# #### `datetime`
#
# * gestion des dates et des heures

# %% [markdown] slideshow={"slide_type": ""}
# #### `math`
#
# * fonctions mathématiques, constantes, ...

# %% [markdown] slideshow={"slide_type": ""}
# #### `random`
#
# * générations de nombres et séquences aléatoires, mélange aléatoire de séquences

# %% [markdown] slideshow={"slide_type": "slide"}
# ### formats de fichier

# %% [markdown]
# #### `json`
#
# * sérialisation d’objets python, standard du web
# * envoi et réception depuis toutes sources compatibles json

# %% [markdown]
# #### `csv`
#
# * ouverture fichier csv, compatible Excel et tableurs

# %% [markdown]
# #### `pickle`
#
# * sérialisation d’objets python, uniquement compatible avec python
# * sauvegarde et la chargement du disque dur

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `collections`
#
# * une extension des objets *built-in* `list`, `tuple`, `dict`
# * [la doc](https://docs.python.org/3.5/library/collections.html)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ####  `collections.Counter()`
#
# * à partir d'un itérable, construit un dictionnaire qui contient 
# * comme clefs les éléments uniques 
# * et comme valeurs le nombre de fois que l’élément apparaît
# * http://sametmax.com/compter-et-grouper-encore-plus-faineant/

# %% slideshow={"slide_type": "slide"}
from collections import Counter

cnt = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
cnt

# %%
isinstance(cnt, dict)

# %%
import re
words = re.findall(r'\w+', open('../data/hamlet.txt').read().lower())
Counter(words).most_common(10)

# %% [markdown]
# #### `collections.defaultdict()`
#
# * étend les dictionnaires pour en faciliter l’initialisation
# * un bon remplacement pour `dict.setdefault` qui est moins parlant
# * https://docs.python.org/3/library/collections.html?#collections.defaultdict

# %% slideshow={"slide_type": "slide"}
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# on indique que les valeurs sont des listes
d = defaultdict(list)
# si on écrit une clé qui n'est pas encore présente
# d[k] vaut alors list()
# c'est-à-dire une liste vide est crée automatiquement
for k, v in s:
    d[k].append(v)

sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `itertools` - combinatoire
#
# * implémente sous forme efficace (itérateurs)
# * des combinatoires classiques
# * et autres outils utiles pour écrire des boucles concises
# * [la doc](https://docs.python.org/3/library/itertools.html)
# * déjà abordé dans la partie 3.3 sur les itérateurs

# %% [markdown]
# fournit les combinatoires communes
#
# * [`produit cartésien`](https://docs.python.org/3.6/library/itertools.html#itertools.product)
# * [`permutations`](https://docs.python.org/3.6/library/itertools.html#itertools.permutations)
# * [`combinaisons`](https://docs.python.org/3.6/library/itertools.html#itertools.combinations) *n* parmi *p* 

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `itertools` - produit cartésien

# %%
from itertools import product
A = ['a', 'b', 'c']
B = [ 1, 2]

for x, y in product(A, B):
    print(x, y)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `itertools` - permutations

# %%
from itertools import permutations
C = ['a', 'b', 'c', 'd']

for tuple in permutations(C):
    print(tuple)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `itertools` - combinaisons

# %%
from itertools import combinations
miniloto = list(range(5))

for a, b in combinations(miniloto, 2):
    print(a, b)

# %% slideshow={"slide_type": "slide"}
# je n'ai pas trouvé pour les arrangements
# une possibilité est de générer toutes les permutations
# de chaque tirage dans les combinaisons
for tuple in combinations(miniloto, 2):
    for a, b in permutations(tuple):
        print(a, b)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### module `itertools` - divers

# %% [markdown] slideshow={"slide_type": ""}
# * parfois sans fin
#   * `count(10) --> 10 11 12 13 14 ...`
#   * `cycle('abcd') --> a b c d a b c d ...`
# * ou pas
#   * `repeat(10, 3) --> 10 10 10`
#   * `islice('abcdefg', 2, none) --> c d e f g`

# %% [markdown] slideshow={"slide_type": "slide"}
# #### module `itertools` - suite

# %% [markdown] slideshow={"slide_type": "slide"}
# * chainer plusieurs itérations
#   * `chain('ABC', 'DEF') --> A B C D E F`
#   * `chain.from_iterable(['ABC', 'DEF']) --> A B C D E F`
#
# * avec un peu de logique
#   * `takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4`
#   * `dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1`
#   * `compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F`
#   * `filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8`

# %% slideshow={"slide_type": "slide"}
from itertools import filterfalse

# %% slideshow={"slide_type": "-"}
# %timeit -n 100 for x in filterfalse(lambda x:x%2, range(10000)): pass

# %%
# %timeit -n 100 for x in (y for y in range(10000) if not (y % 2)): pass

# %% [markdown] slideshow={"slide_type": "slide"}
# ### librairies très utiles

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `operator`
#
# * en python tout est un objet, on peut donc tout passer à une fonction, mais comment passer un opérateur comme `+`, `in`, ou `>` 
# * le module `operator` contient la version fonctionnelle d’un grand nombre d’opérateurs python
# * http://sametmax.com/le-module-operator-en-python/

# %% slideshow={"slide_type": "slide"}
import random
l = [('a', random.randint(1, 1000)) for i in range(100)]
l.sort(key=lambda x: x[1])
l[-7:]

# %%
l = [('a', random.randint(1, 1000)) for i in range(100)]
import operator
l.sort(key=operator.itemgetter(1))
l[-7:]

# %% [markdown] slideshow={"slide_type": "slide"}
# ## librairies tierces (non standard)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `pypi.org`

# %% [markdown]
# * toutes les librairies importantes se trouvent ici
#   * https://pypi.python.org/
# * **attention** n'importe qui peut publier
#   * présence sur pypi ⇎ code fiable, supporté
#
# * `pip` est le programme qui permet de les installer facilement
#   * fourni avec Python à partir de 3.4 (et de 2.7.9 pour 2.x)
#   * sinon suivre la documentation officielle de pip
#   * https://pip.pypa.io/en/latest/installing.html

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `pip` : comment installer une librairie externe

# %% [markdown] slideshow={"slide_type": "slide"}
# ```
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
#   list                        List installed packages.
#   show                        Show information about installed packages.
#   search                      Search PyPI for packages
# …
# ```

# %% slideshow={"slide_type": "slide"}
# par exemple (enlever le ! si dans le terminal)

# !pip install numpy

# %% [markdown]
# * capable de gérer les setups complexes  
#   y compris lorsque du code binaire est nécessaire
#   (cf *wheels*) 
# * n'affranchit pas de bien lire la doc d'installation  
#   lorsqu'une approche naïve écohue
# * à signaler aussi :
#   utilisez `python -m pip` à la place de `pip`  
#   en cas de multiples installations + ou - stables  
#   être sûr d'installer pour le bon Python

# %% [markdown] slideshow={"slide_type": "slide"}
# ## environnements virtuels

# %% [markdown]
# * les pros ont besoin de mélanger plein de configurations
# * pour passer d'un projet à un autre
# * chacun avec ses modules et versions (ex. Django-2.x ou Django-3.x)
# * qui doivent pouvoir coexister dans le même ordi
# * une unique installation Python sur votre machine ne suffit plus
#
# les environnements virtuels répondent à ce besoin
# * facile à créer (et vide)
# * facile à détruire
# * facile à passer de l'un à l'autre
# * tout se fait sous un user 'lamda'  
#   pas besoin de droits administrateurs

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `venv` / `virtualenv`

# %% [markdown]
# * `virtualenv` : historiquement le premier  
# * `venv` : inspiré de, intégré dans la librairie standard
#
# pas mal de surcouches au dessus, mais d'une utilité 
# de plus en plus discutable amha

# %% [markdown] slideshow={"slide_type": "slide"}
# ### miniconda

# %% [markdown]
# une alternative intéressante, car elle permet **aussi** de changer de Python
#
# ex:
#
# * `enva` avec Python-3.6 et Django-2.x
# * `enbv` avec Python-3.8 et Django-3.x
#
# dans les deux cas (`virtualenv` et `miniconda`)  
# bien soigner l'environnement du terminal  
# pour bien **toujours afficher** dans quel environnement on se trouve  
# (dans le prompt du shell typiquement)  
# sinon on a facilement des surprises

# %% [markdown] slideshow={"slide_type": "slide"}
# ### mon approche personnelle
#
# * typiquement un environnement virtuel par projet
# * basé sur une convention de nommage simple
#   * projet `X` 
#   * = repository git `~/git/X`
#   * = environnement virtuel `X`
# * changer de répertoire implique changer d'environnement virtuel

# %% [markdown] slideshow={"slide_type": "slide"}
# #### *hands-on*

# %% [markdown] slideshow={"slide_type": ""}
# * on crée un *virtualenv* **vide** avec `virtualenv le/chemin/venv`
# * on y entre dans un avec `source le/chemin/venv/bin/activate`
# * on y sort avec juste `deactivate`

# %% [markdown]
# ```bash
# tparment /tmp $ virtualenv venv
# Using base prefix '/usr/local/Cellar/python/3.7.0/Frameworks/Python.framework/Versions/3.7'
# New python executable in /private/tmp/venv/bin/python3.7
# Also creating executable in /private/tmp/venv/bin/python
# Installing setuptools, pip, wheel...
# done.
#
# tparment /tmp $ ls venv/bin/activate
# venv/bin/activate
# tparment /tmp $ source venv/bin/activate
#
# [venv @ tmp] tparment /tmp $ pip3 freeze
# [venv @ tmp] tparment /tmp $ python3 -c 'import numpy'
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# ModuleNotFoundError: No module named 'numpy'
#
# [venv @ tmp] tparment /tmp $ deactivate
# tparment /tmp $
# ```

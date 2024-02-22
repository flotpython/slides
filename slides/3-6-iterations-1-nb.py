# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -rise, -version
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
#     title: "it\xE9rations (1/2)"
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# Licence CC BY-NC-ND, Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown] slideshow={"slide_type": "slide"}
# # les itérations (1/2)

# %% [markdown]
# * la boucle `for` est la méthode **préférée**   
#   pour itérer sur un ensemble de valeurs
#
# * en général préférable au `while` en Python
#   * on peut faire un `for` sur n'importe quel itérable
#   * ce n'est pas le cas pour le `while`
#   * avec `for` c'est l'itérable qui se charge de la logique

# %% [markdown] slideshow={"slide_type": "slide"}
# **les itérations en Python (suite)**
#
# * **et aussi** de nombreuses techniques  
#   pour itérer **de manière optimisée**
#
#   * compréhensions
#   * itérateurs
#   * expressions génératrices
#   * générateurs (encore appelées fonctions génératrices)
# * rappel : avec numpy, pas de `for`, programmation vectorielle

# %% [markdown] slideshow={"slide_type": "slide"}
# ## la boucle `for`

# %% [markdown] slideshow={"slide_type": ""}
# une instruction `for` ressemble à ceci :
#
# ```python
# for item in iterable:
#     bloc
#     aligné
#     d_instructions
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `break` et `continue`

# %% [markdown]
# comme dans beaucoup d'autres langages :
#
# * `break` sort complètement de la boucle
# * `continue` termine abruptement  
#   l'itération courante et passe à la suivante
#
# * on parle toujours de la boucle **la plus imbriquée**
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `for .. else`

# %% [markdown] slideshow={"slide_type": ""}
# en fait la forme générale de la boucle `for` c'est
#
#
# ```python
# for item in iterable:
#     bloc
#     aligné
# else:
#     bloc     # exécuté lorsque la boucle sort "proprement"
#     aligné   # c'est-à-dire pas avec un break
# ```
#
# <div class=note>
#     
# l'instruction `else` attachée à un `for` est d'un usage plutôt rare en pratique
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### ~~`for i in range(len(truc))`~~

# %% cell_style="split" slideshow={"slide_type": ""}
liste = [10, 20, 40, 80, 120]

# la bonne façon de faire un for

for item in liste:
    print(item, end=" ")

# %% cell_style="split"
# et **non pas** cette
# horrible périphrase !

for i in range(len(liste)):
    item = liste[i]
    print(item, end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### boucle `for` sur un dictionnaire

# %% [markdown]
# * *rappel*: on peut facilement itérer sur un dictionnaire
# * mais il faut choisir si on veut le faire 
#   * sur les clés: simplement `for k in d:`
#   * sur les valeurs: `for v in d.values():`
#   * ou sur les deux: `for k, v in d.items():`
#
# <div class=note>
#
# on peut aussi itérer sur les clés avec `for k in d.keys()`
#
#     
# </div>    

# %% [markdown] slideshow={"slide_type": "slide"}
# #### boucle `for` sur un dictionnaire

# %% cell_style="split"
agenda = {
    'paul': 12, 
    'pierre': 14,
    'jean': 16,
}

# %% cell_style="split"
# l'unpacking permet d'écrire 
# un code élégant
for key, value in agenda.items():
    print(f"{key} → {value}")

# %% [markdown]
# ---

# %% cell_style="split"
# un raccourci
for key in agenda: 
# ou for key in agenda.keys()
    print(key, end=" ")

# %% cell_style="split"
for value in agenda.values():
    print(value, end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple de boucle

# %%
# pour illustrer break, et for .. else

# boucle (1)
for p in range(2, 10):
    # boucle (2)
    for i in range(2, p):
        if p % i == 0:
            print(f"{p} = {i} x {p//i}")
            # on sort de la boucle (2)
            break
    else:
        print(f"{p} est un nombre premier")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### boucles `for` : limite importante

# %% [markdown]
# * **règle très importante:** à l'intérieur d'une boucle
# * il ne faut **pas modifier l’objet** sur lequel on itère
#

# %% cell_style="center"
s = {1, 2, 3}

# on essaie de modifier l'objet itéré
try:
    for x in s:
        if x == 1:
            s.remove(x)
except Exception as exc:
    print(f"OOPS {type(exc)} {exc}")

# %% [markdown] slideshow={"slide_type": "slide"}
# la technique usuelle consiste à utiliser une copie

# %% cell_style="center"
s = {1, 2, 3}

# avec les listes on peut aussi utiliser [:]
# mais ici sur un ensemble ça ne fonctionnerait pas 
for x in s.copy():
    if x == 1:
        s.remove(x)

s

# %% [markdown] slideshow={"slide_type": "slide"}
# ### boucles pythoniques ou pas

# %% [markdown]
# #### soyez explicite

# %% cell_style="split"
D = {'alice': 35, 'bob': 9, 'charlie': 6}

# %% cell_style="split"
# pas pythonique (implicite)

for t in D.items():
    print(t[0], t[1])

# %% cell_style="split"
# pythonique (explicite)

for nom, age in D.items():
    print(nom, age)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## itérables et itérateurs

# %% [markdown] slideshow={"slide_type": ""}
# ### c'est quoi un itérable ?
#
# * par définition, c'est un objet .. sur lequel on peut faire un `for`
# * notamment avec les séquences natives : chaînes, listes, tuples, ensembles
# * et aussi dictionnaires, et des tas d'autres objets, mais patience

# %% cell_style="split"
# une chaine est un itérable

chaine = "un été"
for char in chaine:
    print(char, end=" ")

# %% cell_style="split"
# un ensemble aussi

ensemble = {10, 40, 80} 
for element in ensemble:
    print(element, end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# #### la boucle `for`, mais pas que

# %% [markdown] cell_style="split"
# * on a défini les itérables par rapport à la boucle `for` 
# * plusieurs fonctions acceptent en argument des itérables
# * `sum`, `max`, `min`
# * `map`, `filter`
# * etc...

# %% cell_style="split"
L = [20, 34, 57, 2, 25]

min(L), sum(L)

# %% cell_style="split"
# ceci retourne un itérateur
map(lambda x: x**2, L)

# %% cell_style="split"
# pour voir "ce qu'il y a dedans"
list(map(lambda x: x**2, L))

# %% [markdown] slideshow={"slide_type": "slide"}
# ### itérateurs
#
# * les **itérateurs** sont une sous-famille des itérables
# * qui présentent la particularité de **consommer peu de mémoire**
# * en fait un objet itérateur capture uniquement  
#   **la logique de l'itération**, mais pas les données
#
# * c'est-à-dire où on en est, et comment passer au suivant

# %% cell_style="split" slideshow={"slide_type": ""}
import sys

L = list(range(1000))
sys.getsizeof(L)

# %% cell_style="split"
# avec iter() on fabrique 
# un itérateur
I = iter(L)

sys.getsizeof(I)

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# cette boucle Python
# ```python
# for i in range(100_000):
#     # do stuff
# ```

# %% [markdown] cell_style="split"
# est comparable à ceci en C
# ```C
# for (int i=0; 
#      i<100000; 
#      i++) {
#     /* do stuff */
# }
# ```

# %% [markdown] slideshow={"slide_type": ""}
# ce qui montre qu'on peut s'en sortir  
# avec **seulement un entier** comme mémoire
#
# et donc on ne veut **pas devoir allouer**  
# une liste de 100.000 éléments  
# juste pour pouvoir faire cette boucle !

# %% [markdown] slideshow={"slide_type": "slide"}
# ### combinaisons d'itérations

# %% [markdown]
# Python propose des outils pour **créer** et **combiner** les itérables:
#
# * fonctions natives *builtin* qui créent des itérateurs:
#   * `range`, `enumerate`, et `zip`
# * dans un module dédié `itertools`:
#   * `chain`, `cycle`, `islice`, ...

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `range`

# %% [markdown]
# * `range` crée un objet qui permet d'itèrer sur un intervalle de nombres entiers
# * arguments : même logique que le slicing
#   * début (inclus), fin (exclus), pas
#   * **sauf** (curiosité) : si un seul argument, c'est **la fin**

# %% cell_style="split"
# les nombres pairs de 10 à 20
for i in range(10, 21, 2):
    print(i, end=" ")

# %% cell_style="split"
# le début par défaut est 0
for i in range(5):
    print(i, end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# #### un `range` n'est **pas une liste**

# %% [markdown]
# * l'objet retourné par `range` **n'est pas une liste**
# * au contraire il crée un objet tout petit, un **itérateur** (*)
# * qui contient seulement la logique de l'itération
# * la preuve:

# %% cell_style="split"
# 10**20 c'est 100 millions de Tera

# un range est presque un iterateur
iterator = range(10**20)
iterator

# %% cell_style="split"
for item in iterator:
    if item >= 5:
        break
    print(item, end=" ")

# %% [markdown]
# <div class="note">
#
# (*) en réalité un `range()` n'est pas techniquement un itérateur; mais bon ça y ressemble beaucoup...
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# **exercice**: comment créer **une vraie liste** des entiers de 1 à 10 ?

# %% [markdown] slideshow={"slide_type": "fragment"}
# **réponse** avec
#
# ```python
# list(range(1, 11))
# ```
#
# où le type `list` se comporte, (comme tous les types)  
# comme **une usine** à fabriquer des listes

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `count` : un itérateur infini

# %% [markdown] slideshow={"slide_type": ""}
# du coup un itérateur peut même .. ne jamais terminer :

# %%
# count fait partie du module itertools
from itertools import count
# count?

# %% cell_style="split"
# si on n'arrête pas la boucle nous mêmes
# ce fragment va boucler sans fin

for i in count():
    print(i, end=" ")
    if i >= 10:
        break

# %% cell_style="split"
# on peut changer les réglages

for i in count(2, 5):
    print(i, end=" ")
    if i >= 32:
        break

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `enumerate`

# %% [markdown] cell_style="split"
# on a dit qu'on ne faisait jamais
#
# ```python
# for i in range(len(liste)):
#     item = liste[i]
#     print(item, end=" ")
# ```
#
# mais comment faire alors si on a vraiment besoin de l'index `i` ?
#
# → il suffit d'utiliser la *builtin* `enumerate()`

# %% cell_style="split"
L = [1, 10, 100]

for i, item in enumerate(L):
    print(f"{i}: {item}")

# %% cell_style="split"
# on peut aussi commencer 
# à autre chose que 0

with open("some-file.txt") as f:
    for lineno, line in enumerate(f, 1):
        print(f"{lineno}:{line}", end="")

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/iter-enumerate.svg)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `enumerate()` ...

# %% [markdown]
# * typiquement utile sur un fichier
# * pour avoir le numéro de ligne 
# * remarquez le deuxième argument de `enumerate`  
#   ici pour commencer à 1

# %%
with open("data/une-charogne.txt") as feed:
    for lineno, line in enumerate(feed, 1):
        print(f"{lineno}:{line}", end="")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `zip`

# %% [markdown]
# `zip` permet d'itérer sur plusieurs itérables "en même temps":
#
# ![](media/iter-zip.svg)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `zip`

# %% cell_style="split"
liste1 = [10, 20, 30]
liste2 = [100, 200, 300]

# %% cell_style="split"
for a, b in zip(liste1, liste2):
    print(f"{a}x{b}", end=" ")

# %% [markdown]
# **NOTES**: 
#
# * `zip` fonctionne avec autant d'arguments qu'on veut
# * elle s'arrête dès que l'entrée **la plus courte** est épuisée

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `enumerate = zip + count`

# %% [markdown]
# aucun intérêt pratique, mais juste une remarque :  
# on pourrait écrire `enumerate` à base de `zip` et `count`

# %% slideshow={"slide_type": ""}
L

# %% cell_style="split"
# zip s'arrête dès que 
# l'un de ses morceaux s'arrête
for index, item in zip(count(), L):
    print(f"{index} {item}")

# %% [markdown] cell_style="split"
# ![](media/iter-zip-count.svg)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un itérateur s'épuise
#
# **ATTENTION** il y a toutefois une limite lorsqu'on utilise un itérateur 
#
# * une fois que l'itérateur est arrivé à sa fin
# * il est "épuisé" et on ne peut plus boucler dessus
#
# <div class=note>
#     
# (*) à cet égard, les `range()` sont spéciaux
# </div>

# %% cell_style="split"
# avec une liste, pas de souci
L = [100, 200]

print('pass 1')
for i in L:
    print(i)

print('pass 2')
for i in L:
    print(i)


# %% cell_style="split"
# iter() permet de construire
# un itérateur sur un itérable

R = iter(L)

print('pass 1')
for i in R:
    print(i)

print('pass 2')
for i in R:
    print(i)    

# %% [markdown] slideshow={"slide_type": "slide"}
# du coup par exemple,  
# **ne pas essayer d'itérer deux fois** sur un `zip()` ou un `enumerate()`

# %% cell_style="split" slideshow={"slide_type": ""}
Z = zip(range(3), range(4, 7))

print('pass 1')
for a, b in Z:
    print(a, b)
    
print('pass 2')
for a, b in Z:
    print(a, b)    

# %% cell_style="split" slideshow={"slide_type": ""}
E = enumerate(L)

print('pass 1')
for a, b in E:
    print(a, b)
    
print('pass 2')
for a, b in E:
    print(a, b)    

# %% [markdown]
# <div class=note>
#     
# il suffit bien sûr de faire e.g. `for a, b in enumerate(L)` pour se débarrasser du problème
#     
# </div>    

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le module `itertools` - assemblage d'itérables

# %% [markdown]
# on trouve dans le module `itertools` plusieurs utilitaires très pratiques :
#
# * `count` pour énumérer les entiers (un `range` sans borne)
# * `chain` pour chainer plusieurs itérables
# * `cycle` pour rejouer un itérable en boucle
# * `repeat` pour énumérer plusieurs fois le même objet
# * `islice` pour n'énumérer que certains morceaux
# * `zip_longest` fonctionne comme `zip` mais s'arrête au morceau le plus long

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `chain`
#
# ![](media/iter-chain.svg)

# %% cell_style="center" slideshow={"slide_type": ""}
from itertools import chain
data1 = (10, 20, 30)
data2 = (100, 200, 300)

# %% cell_style="center"
# chain()
for d in chain(data1, data2):
    print(f"{d}", end=" ")

# %% cell_style="center"
# c'est comme un lego, on peut combiner toutes ces fonctions
for i, d in enumerate(chain(data1, data2)):
    print(f"{i}x{d}", end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `cycle`
#
# ![](media/iter-cycle.svg)

# %%
# cycle() ne termine jamais non plus

from itertools import cycle
data1 = (10, 20, 30)

for i, d in enumerate(cycle(data1)):
    print(f"{i}x{d}", end=" ")
    if i >= 10:
        break

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `repeat`

# %%
# repeat()
from itertools import repeat
data1 = (10, 20, 30)
data2 = (100, 200, 300)

# pour peut répéter le même élément plusieurs fois
padding = repeat(1000, 3)

for i, d in enumerate(chain(data1, padding, data2)):
    print(f"{i}x{d}", end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `islice`
#
# fonctionne comme le slicing, mais sur n'importe quel itérable

# %% cell_style="split"
# avec islice on peut par exemple 
# sauter une ligne sur deux dans un fichier
from pathlib import Path

# on crée un fichier 
with Path('islice.txt').open('w') as f:
    for i in range(6):
        f.write(f"{i}**2 = {i**2}\n")

# %% cell_style="split"
# pour ne relire qu'une ligne sur deux

from itertools import islice

with Path('islice.txt').open() as f:
    for line in islice(f, 0, None, 2):
        print(line, end="")


# %% cell_style="split"
# ou zapper les 3 premières

from itertools import islice

with Path('islice.txt').open() as f:
    for line in islice(f, 3, None):
        print(line, end="")

# %% cell_style="split"
# ou ne garder que les 3 premières

from itertools import islice

with Path('islice.txt').open() as f:
    for line in islice(f, 3):
        print(line, end="")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `zip_longest()`
#
# comme `zip`, mais s'arrête à l'entrée la plus longue  
# du coup il faut dire par quoi remplacer les données manquantes

# %% cell_style="split"
from itertools import zip_longest
for i, d in zip_longest(
        range(6), L, fillvalue='X'):
    print(f"{i} {d}")

# %% [markdown] cell_style="split"
# ![](media/iter-zip-longest.svg)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `itertools` & combinatoires

# %% [markdown]
# Le module `itertools` propose aussi quelques combinatoires usuelles:
#
# * `product`: produit cartésien de deux itérables
# * `permutations`: les permutations ($n!$)
# * `combinations`: *p parmi n*
# * et d'autres... 
# * <https://docs.python.org/3/library/itertools.html>

# %% [markdown] slideshow={"slide_type": "slide"}
# #### exemple avec `product`

# %%
from itertools import product

dim1 = (1, 2, 3)
dim2 = '♡♢♤'

for i, (d1, d2) in enumerate(product(dim1, dim2), 1):
    print(f"i={i}, d1={d1} d2={d2}")

# %% [markdown] slideshow={"slide_type": "slide"}
# **exercice** (voir notebook séparé)
#
# * vigenere

# %% [markdown] slideshow={"slide_type": "slide"}
# ## sous le capot

# %% [markdown]
# ### comment marche la boucle `for`

# %% [markdown] cell_style="split"
# lorsqu'on itère sur un itérable

# %% cell_style="split"
iterable = [10, 20, 30]

# %% [markdown]
# sous le capot, la boucle `for` va faire:
#
#   * créer un itérateur en appelant `iter(iterable)`
#   * appeler `next()` sur cet itérateur
#   * jusqu'à obtenir l'exception `StopIteration`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `iter()` et `next()`

# %% [markdown] slideshow={"slide_type": ""}
# voici un équivalent approximatif

# %% cell_style="split" slideshow={"slide_type": ""}
# cette boucle for 

for item in iterable:
    print(item)

# %% cell_style="split" slideshow={"slide_type": ""}
# est en gros équivalente
# à ce fragment

iterateur = iter(iterable)
while True:
    try:
        item = next(iterateur)
        print(item)
    except StopIteration:
        # print("fin")
        break


# %% [markdown]
# <div class=note>
#
# il peut être parfois pratique d'utiliser `iter()` et `next()`  
# par exemple, comment prendre un élément - n'importe lequel - dans un ensemble ?
#
# </div>    

# %% [markdown] slideshow={"slide_type": "slide"}
# ### quel objet est itérable ?

# %% [markdown]
# * il existe beaucoup d’objets itérables en python
#   * tous les objets séquence: listes, tuples, chaînes, etc.
#   * les sets, les dictionnaires
#   * les vues (`dict.keys()`, `dict.values()`), etc.
#   * les fichiers
#   * les générateurs
# * il faut **penser à les utiliser**, c’est le plus rapide et le plus lisible

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### quel objet est un itérateur ?

# %% [markdown] cell_style="split"
# pour savoir si un objet est un itérateur  
# tester si  
#   `iter(obj) is obj`

# %% cell_style="split" slideshow={"slide_type": ""}
def is_iterator(obj):
    return iter(obj) is obj


# %% [markdown] slideshow={"slide_type": "slide"}
# ### par exemple
#
# * une liste **n'est pas** son propre itérateur
# * un fichier **est** son propre itérateur

# %% cell_style="split" slideshow={"slide_type": "slide"}
# créons un fichier
with open("tmp.txt", 'w') as F:
    for i in range(6):
        print(f"{i=} {i**2=}", file=F)

# pour voir qu'un fichier ouvert en
# lecture est son propre itérateur
with open("tmp.txt") as F:
    print(f"{is_iterator(F)=}")

# %% cell_style="split"
# la liste non
L = list(range(5))
print(f"{is_iterator(L)=}")

# %% cell_style="split"
# cycle en est un
C = cycle(L)
print(f"{is_iterator(C)=}")

# %% cell_style="split"
# un zip() est un itérateur
Z = zip(L, L)
print(f"{is_iterator(Z)=}")

# %% [markdown]
# * bien se souvenir : **un itérateur s'épuise**  
#   de manière générale, un objet qui est un itérateur  
#   ne peut être itéré qu'une seule fois

# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: containers
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% run_control={"frozen": false, "read_only": false} slideshow={"slide_type": ""}
from plan import plan; plan("types", "containers")

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# # les containers

# %% [markdown]
# ## la liste

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * permet de créer une liste de n’importe quels objets
# * les listes sont dynamiques, de **taille variable**
# * une liste peut être **hétérogène** (avoir des composants de types différents)
# * peuvent être **imbriquées** 
#   * comme une liste est un objet, on peut avoir une liste de listes
#   * ou y mettre d'autres containers
#   

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### basique

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
L = []
L = [4, 'bob', 10 + 1j, True]

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
L

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# les indices en python
# commencent à 0
L[2]

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
L[0] = 10

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
L

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### modification par index

# %% cell_style="center"
L

# %% cell_style="split"
# modifier un élément précis
L[3] = False

# %% cell_style="split"
# ce que ça donne
L

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### modification par slice

# %% cell_style="split"
liste = [1, 2, 4, 8, 16, 32]

# %% cell_style="split" slideshow={"slide_type": ""}
# le slicing est disponible
# sur les listes
liste[2:]

# %% cell_style="split" run_control={"frozen": false, "read_only": false} slideshow={"slide_type": ""}
# on peut aussi modifier 
# toute une slice
liste[2:4] = [10, 20, 30]
liste

# %% [markdown] cell_style="split" run_control={"frozen": false, "read_only": false} slideshow={"slide_type": ""}
# ![](pictures/writing-a-list-slice.png)

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### attention

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": ""}
# * `L[i] = L2`
#   * **remplace** le i-ème élément de `L` par la liste `L2`
# * `L[i:j] = L2`
#   * **insère** tous les éléments de la liste `L2` à la position `i`
#   * après avoir supprimé les éléments `i` jusqu’à `j-1` dans `L`

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### modification sous pythontutor

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
liste = [1, 2, 4, 8, 16, 32]
liste

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
liste[2:4] = [10, 20, 30]
liste

# %% run_control={"frozen": false, "read_only": false}
liste[3] = [100, 200]
liste

# %% slideshow={"slide_type": "slide"}
# %load_ext ipythontutor

# %% slideshow={"slide_type": ""}
# %%ipythontutor curInstr=1 width=1000
liste = [1, 2, 4, 8, 16, 32]
liste[2:4] = [10, 20, 30]
liste[3] = [100, 200]

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### méthodes sur les listes

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * les méthodes sur les listes
# * sont optimisées pour les ajouts **à la fin** de la liste

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
L = []
for i in range(4):
    L.append(i)
L

# %% cell_style="split"
while L:
    print(L.pop())

# %% [markdown]
# si nécessaire, envisager la liste **doublement chainée**

# %%
from collections import deque
# deque?

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### ajouts et tris

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * des méthodes spécifiques aux types mutables  
#   (modifications *in-place*)
#
#   * `L.append(x)` ajoute `x` à la fin de `L`
#   * `L.extend(L2)` ajoute chaque élément de `L2` à la fin de `L`
#   * `L.insert(i, x)` ajoute x à la position `i`
#   * `L.sort()`  trie `L`
#   * `L.reverse()` renverse les éléments de `L`

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### retraits

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * `L.pop(i)` supprime l’élément à la position `i`, si i n’est pas fourni, supprime le dernier élément. La fonction retourne l’élément supprimé
#   * utilisé pour faire une pile d’éléments
# * `L.remove(x)` supprime la première occurrence de `x` dans `L`. S’il n’y a pas de `x`, une exception est retournée
# * `del L[i:j:k]` supprime tous les éléments entre `i` et `j-1` par pas de `k` éléments
#   * si `i == j` supprime l’élément `i`

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### digression: `range()`

# %% [markdown] cell_style="center" run_control={"frozen": false, "read_only": false}
# * `range()` est une fonction native (en anglai *builtin*)
# * qui retourne un objet **itérateur**
# * c'est-à-dire sur lequel on peut faire un `for`
# * on y reviendra longuement

# %% cell_style="center"
for i in range(4):
    print(i, end=" ")

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# #### digression: `range()`

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * essentiellement, **même logique que le slicing**
# * `range(j)` balaie de `0` à `j-1`
# * `range(i, j)` balaie de `i` à `j-1`
# * `range(i, j, k)` balaie de `i` à `j-1` par pas de `k`
# * pour obtenir une liste on transforme (*cast*)  
#   en liste en appelant `list()`

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
for i in range(1, 21, 5):
    print(i, end=" ")

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
list(range(1, 21, 5))

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### exemples

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# la fonction list() permet
# de convertir en liste
L = list(range(5))
L

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# un par un
L.append(100)

# ou plusieurs à la fois
L.extend([10, 20])
L

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# très souvent utilisé
# rappel: optimisé pour ça
L.pop()
L

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# pour trier c'est simple
# on va creuser ça tout de suite
L.sort()
L

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### tri sur les listes

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * le tri des listes est très puissant en Python
#   * tri **en place** méthode `list.sort()`
# * il a aussi la fonction built-in `sorted()`  
#   qui trie toutes les séquences  
#   et retourne **une nouvelle liste**

# %% cell_style="split"
L = [10, -5, 3, 100]

# tri en place
L.sort()
L

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
L1 = [10, -5, 3, 100]

# crée une copie
L2 = sorted(L1)
print(L1)
print(L2)

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * on peut aussi trier selon un critère *ad hoc*
# * on en reparlera plus tard
# * voir aussi <https://docs.python.org/3.5/howto/sorting.html>

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### avertissements à propos des listes

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": ""}
# #### les itérateurs sont plus forts
#
# * outil très très pratique
# * **mais** parfois (souvent) pas nécessaire
# * car nécessite de la mémoire
# * alors qu'on veut juste itérer sur le contenu
# * dans ce cas, techniques + adaptées : itérateurs et autres générateurs
# * sujet avancé que l’on verra plus tard

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# #### pas efficace pour calculs
#
# * le coté flexible en taille et en type rend la liste **très pratique**
# * mais attention ça peut devenir **très inefficace** 
# * notamment pour le calcul scientifique
# * pas d'équivalent parmi les types Python natifs  
#   d'un bon vieux tableau C/C++/Fortran
# * penser absolument aux **tableaux `numpy`** pour ce type d'application

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## le tuple

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * comme des listes, mais **immutables**
# * syntaxe: `()` au lieu de `[]`

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# syntaxe pour un tuple vide
T = ()
T

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# syntaxe pour un singleton
T1 = (4,)
# ou encore
T2 = 4,

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
T1 == T2

# %% [markdown] cell_style="split" run_control={"frozen": false, "read_only": false}
# * **attention** 
#   * `(4)` est un **entier**, et
#   * `(4,)` est un **tuple**
# * c'est la virgule qui est importante
# * on peut omettre les `()` - la plupart du temps

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### basique

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# syntaxe pour plusieurs éléments
T1 = (3, 5, 'alice', 10+1j)
# ou encore
T2 =  3, 5, 'alice', 10+1j
# ou encore
T3 =  3, 5, 'alice', 10+1j,

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
T1 == T2

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
T1 == T3

# %% [markdown] run_control={"frozen": false, "read_only": false}
#
# * un tuple est **non mutable**
# * les fonctions faisant des modifications *in-place* ne s’appliquent donc pas aux tuples
#

# %% run_control={"frozen": false, "read_only": false}
try: T1[3] = 5   # python n'est pas content
except Exception as e: print("OOPS", e)

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## problèmes avec les séquences

# %% [markdown]
# ### les recherches sont lentes

# %% run_control={"frozen": false, "read_only": false}
a = range(30000000)
'x' in a      # c’est long !

# %% [markdown] slideshow={"slide_type": "slide"}
# ### on ne peut indexer que par un entier

# %% run_control={"frozen": false, "read_only": false}
a[3]          # on peut utiliser un indice entier

# %% run_control={"frozen": false, "read_only": false}
a = []
# on ne peut pas indexer avec un nom ou autre chose qu'un entier
try:
    a['alice'] = 10
except TypeError as e:
    print("OOPS", e)

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### récapitulons

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * une séquence est une liste ordonnée d’éléments  
#   indexés par des entiers
#
#   * les recherches sont longues *O(n)*
#   * impossible d’avoir un index autre qu’entier
#   * comment faire, par exemple, un annuaire ?
# * on voudrait
#   * une insertion, effacement et recherche en *O(1)*
#   * une indexation par clef quelconque

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## la solution : les tables de hash

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * une table de hash T indexe des valeurs par des clefs
#   * chaque clef est unique
#   * T[clef] = valeur
#   * insertion, effacement, recherche en O(1)

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### table de hash

# %% [markdown] run_control={"frozen": false, "read_only": false}
# ![hash](pictures/hash.png)

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# #### table de hash

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * la fonction de hash *f()* choisie de façon à ce que
#   * *f(key, size)* retourne toujours la même valeur 
#   * *key* doit être **immutable**
# * minimise le risque de collision
#   * *f(key1, size)* == *f(key2, size)*
# * une bonne façon de minimiser les collisions  
#   est de garantir une distribution uniforme

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### table de hash et Python

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * le dictionnaire `dict` est une table de hash  
#   qui utilise comme clef un **objet immutable**  
#   et comme valeur n’importe quel objet
#
#   * association clé → valeur  

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "fragment"}
# * l'ensemble `set` est une table de hash  
#   qui utilise comme clef un **objet immutable**  
#   et qui n’associe pas la clef à une valeur
#
#   * notion d’ensemble mathématique

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## le `set`

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * collection non ordonnée d’objets uniques et **immutables**
# * utile pour tester l’appartenance
#   * optimisé, beaucoup + rapide que `list`
# * et éliminer les entrées doubles d’une liste
# * test d’appartenance plus rapide que pour les listes
# * les sets autorisent les opérations sur des ensembles
#   * union (|), intersection (&), différence (-), etc.

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### le `set`

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# attention: {} c'est 
# un DICTIONNAIRE vide 
set()          # ensemble vide

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
L1 = [1, 2, 3, 1, 1, 6, 4]
S1 = set(L1)
S1

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### le `set`

# %% cell_style="center" run_control={"frozen": false, "read_only": false}
# attention: il faut passer 
# à set UN itérable
try:
    S = set(1, 2, 3, 4, 5)
except Exception as exc:
    print(f"OOPS {type(exc)}")    

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### le `set`

# %% cell_style="split"
S1


# %% cell_style="split" run_control={"frozen": false, "read_only": false}
L2 = [3, 4, 1]
S2 = set(L2)
S2

# %% cell_style="split"
4 in S2

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
S1 - S2            # différence

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
S1 | S2            # union

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
S1 & S2            # intersection

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### le `set`: méthodes

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# ensemble littéral
S3 = {1, 2, 3, 4}        
S3

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# ajout d'un élément

S3.add('spam')
S3

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# pas de duplication
# et pas d'ordre particulier
S3.update([10, 11, 10, 11])
S3

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
S3.remove(11)
S3

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### le `set`

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * un `set` est un objet **mutable**
# * le `frozenset` est équivalent mais **non mutable**
# * un peu comme `list` et `tuple`
# * par exemple pour servir de clé dans un hash

# %% cell_style="split"
fs = frozenset([1, 2, 3, 4])

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# frozenset pas mutable
try:
    fs.add(5)
except AttributeError as e:
    print("OOPS", e)   

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### rapide test de performance

# %% [markdown] cell_style="split" run_control={"frozen": false, "read_only": false}
# pour la recherche d’un élément  
# les sets sont **beaucoup plus rapides**

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
import timeit

# %% run_control={"frozen": false, "read_only": false}
timeit.timeit(setup= "x = list(range(100000))", stmt = '"c" in x',
              number = 300)

# %% run_control={"frozen": false, "read_only": false}
timeit.timeit(setup= "x = set(range(100000))", stmt = '"c" in x',
              number = 300)

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# #### rapide test de performance

# %% run_control={"frozen": false, "read_only": false}
timeit.timeit(setup= "x = list(range(2))", stmt = '"c" in x',
              number = 6000000)

# %% run_control={"frozen": false, "read_only": false}
timeit.timeit(setup= "x = set(range(2))", stmt = '"c" in x',
              number = 6000000)

# %% [markdown] run_control={"frozen": false, "read_only": false}
# même si la liste est très petite

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# #### rapide test de performance

# %% run_control={"frozen": false, "read_only": false}
timeit.timeit(setup= "x = list(range(2))", stmt = '0 in x',
              number = 6000000)

# %% run_control={"frozen": false, "read_only": false}
timeit.timeit(setup= "x = set(range(2))", stmt = '0 in x',
              number = 6000000)

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * il faut que l’élément cherché soit le premier de la liste pour que les listes soient un peu plus rapides que les sets
# * donc, toujours utiliser les sets pour les tests d’appartenance

# %% [markdown] slideshow={"slide_type": "slide"}
# ### remarque 

# %% [markdown]
# avec `ipython` vous pouvez faire vos benchmarks un peu plus simplement

# %% run_control={"frozen": false, "read_only": false}
timeit.timeit(setup= "x = set(range(2))", stmt = '0 in x',
              number = 6000000)

# %% run_control={"frozen": false, "read_only": false}
x = set(range(2))
# %timeit -n 6000000 0 in x

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ## les dictionnaires

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * généralisation d’une table de hash
# * collection non ordonnée d’objets
# * techniquement, uniquement les pointeurs sont stockés, mais pas une copie des objets
# * on accède aux objets à l’aide d’une clef (et non d’un indice comme pour une liste)
# * une **clef** peut être n’importe quel objet **immutable**: chaîne, nombre, tuple d’objets immutables...
# * c’est une structure de données très puissante
# * le dictionnaire est un type **mutable**

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### les dictionnaires

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * on peut voir les dictionnaires comme une collection non ordonnée de couples (clef, valeur)
# * chaque clef est unique** et permet d’accéder à **une** valeur qui pointe vers un objet

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### les dictionnaires

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * construction

# %% run_control={"frozen": false, "read_only": false}
# ATTENTION : {} n'est pas un ensemble
# les dictionnaires étaient là avant les ensembles !
D = {}
D

# %% run_control={"frozen": false, "read_only": false}
# un dictionnaire créé de manière littérale
{ 'douze' : 12, 1: 'un', 'liste' : [1, 2, 3] }

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# une autre façon quand 
# les clés sont des chaînes
dict( a = 'A', b = 'B')

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# à partir d'une liste de couples
dict( [ ('a', 'A'), ('b', 'B') ] )

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### méthodes sur les dictionnaires

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * `len(D)` retourne le nombre de clefs dans D
# * `D[clef]` retourne la valeur pour la clef
# * `D[clef] = x` change la valeur pour la clef
# * `del D[clef]` supprime la clef et la valeur
# * `clef in D` teste l’existence de clef dans D
# * `clef not in D` teste la non existence
# * `D.copy()` *shallow copy* de D

# %% cell_style="split" slideshow={"slide_type": "slide"}
d = {'alice': 35, 'bob' : 9, 'charlie': 6}
d

# %% cell_style="split"

len(d)

# %% cell_style="split"
d['alice']

# %% cell_style="split"
'bob' in d

# %% cell_style="split"
d['jim'] = 32
d

# %% cell_style="split"
del d['jim']
d

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### méthodes sur les dictionnaires

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * `D.get(clef)`
#   * retourne la valeur associée à cette clé si elle est présente, `None` sinon
#   * notez bien que `D[clef]` lance une exception si la clé n'est pas présente
#   * `D.get(clef, un_truc)` retourne `un_truc` quand la clé n'est pas présente

# %% run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
d

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# la clé n'est pas présente
try:
    d['marc']
except KeyError as e:
    print("OOPS", e)

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# on peut utiliser `get` plutôt si on préfère un retour de fonction
d.get('marc', '?')

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### méthodes sur les dictionnaires

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * `D.setdefault(clef, x)`
#   * si la clé est présente: retourne `D[clef]`
#   * sinon fait `D[clef] = x` et retourne `x`
#   * pour simplifier les ajouts
# * voir aussi `collections.defaultdict`

# %% cell_style="split" slideshow={"slide_type": "slide"}
from collections import defaultdict

# les valeurs sont des listes
dd = defaultdict(list)
dd[0].append(1)
dd[0]

# %% cell_style="split" slideshow={"slide_type": ""}
# sans defaultdict
# besoin d'alourdir le code

try: 
    ddb = {}
    ddb[0].append(1)
    ddb[0]
except Exception as exc:
    print(f"OOPS {type(exc)}")

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### méthodes sur les dictionnaires

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * `D.items()` retourne **une vue** sur les (clef, valeur) de `D`
# * `D.keys()` retourne une vue sur les clefs de `D`
# * `D.values()` retourne une vue sur les valeurs de `D`

# %% run_control={"frozen": false, "read_only": false}
len(dir(dict))

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### qu’est-ce qu’une vue ?

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * c’est un objet qui donne une vue **dynamique** sur un dictionnaire `D`
#   * permet le test d’appartenance avec `in`
#   * permet l’itération (une vue est itérable)
# * si on ne modifie pas `D` en cours d’itération
#   * on a la garantie d’itérer dans le même ordre sur les clefs et sur les valeurs

# %% cell_style="center" slideshow={"slide_type": "slide"}
del d['bob']
d

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
clefs = d.keys()
clefs

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
d['bob'] = 20
d

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
clefs

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### méthodes sur les dictionnaires

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * [beaucoup d’autres méthodes](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

# %% run_control={"frozen": false, "read_only": false}
# les clés / valeurs ne sont pas forcément de même type
d = {'alice': 35, (1, 2): {3: '9', 10 + 1j: 6}}
d

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
d['alice']

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
d[1, 2]

# %% cell_style="split" run_control={"frozen": false, "read_only": false}
# retire une clé au hasard
d.popitem()

# %% cell_style="split"
d

# %% [markdown] run_control={"frozen": false, "read_only": false} slideshow={"slide_type": "slide"}
# ### quel avantage d’un objet vue ?

# %% [markdown] run_control={"frozen": false, "read_only": false}
# * une vue est compacte - pas de liste temporaire
#   * Python 3.x utilise uniquement les vues
# * si on modifie `D`, la modification sera immédiatement reflétée dans la vue
# * **attention**
#   * si on itère sur un vue de `D` et que l’on modifie en même temps `D`,  
#     on peut avoir une exception ou une inconsistance
#
#   * dans ce cas, on fait une copie sous forme de liste

# %% [markdown] slideshow={"slide_type": "slide"}
# ### ordre des éléments dans un dictionnaire

# %% [markdown]
# **remarque d'ordre historique**
#
# * jusque et y-compris 3.5, un dictionnaire ne préservait pas l'ordre
#   * ce qui est logique par rapport à la technologie de hachage
#   * mais peut être déroutant pour les débutants, - et les autres aussi...
# * depuis 3.6, l'ordre de création est préservé
#   * d'abord annoncé comme un "détail d'implémentation"
#   * maintenant (3.7) annoncé comme un *feature* sur laquelle on peut compter

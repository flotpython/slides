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
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   nbhosting:
#     title: containers
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown] slideshow={"slide_type": ""}
# # les containers
#
# plusieurs types pratiques et efficaces sont fournis *de base*, et notamment
#
# * liste
# * dictionnaire
# * ensemble

# %% [markdown] slideshow={"slide_type": "slide"}
# ## la liste

# %% [markdown]
# * permet de créer une liste de n’importe quels objets
# * les listes sont dynamiques, de **taille variable**
# * une liste peut être **hétérogène** (avoir des composants de types différents)
# * peuvent être **imbriquées**
#   * comme une liste est un objet, on peut avoir une liste de listes
#   * ou y mettre d'autres containers
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### basique

# %% cell_style="split"
L = []
L = [4, 'bob', 10 + 1j, True]

# %% cell_style="split"
# on peut mélanger les types
L

# %% cell_style="split"
# les indices en python
# commencent à 0
L[2]

# %% [markdown] slideshow={"slide_type": "slide"}
# ### modification par index

# %% cell_style="center"
# les indices commencent à 0
L

# %% cell_style="split"
# pour modifier un élément précis
L[2] = "BOOM"

# %% cell_style="split"
# pas besoin de préserver les types
# ni rien de ce genre

L

# %% [markdown] slideshow={"slide_type": "slide"}
# ### modification par slice

# %% cell_style="split"
liste = [1, 2, 4, 8, 16, 32]

# %% cell_style="split" slideshow={"slide_type": ""}
# le slicing est disponible
# sur les listes
liste[2:]

# %% cell_style="split" slideshow={"slide_type": ""}
# on peut aussi modifier
# toute une slice
liste[2:4] = [10, 20, 30]
liste

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ![](media/writing-a-list-slice.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### attention

# %% [markdown] slideshow={"slide_type": ""}
# * `L[i] = L2`
#   * **remplace** le i-ème élément de `L` par la liste `L2`
# * `L[i:j] = L2`
#   * **insère** tous les éléments de la liste `L2` à la position `i`
#   * après avoir supprimé les éléments `i` jusqu’à `j-1` dans `L`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### modification sous pythontutor

# %% cell_style="split"
liste = [1, 2, 4, 8, 16, 32]
liste

# %% cell_style="split"
liste[2:4] = [10, 20, 30]
liste

# %%
liste[3] = [100, 200]
liste

# %% slideshow={"slide_type": "slide"}
# %load_ext ipythontutor

# %% slideshow={"slide_type": ""}
# %%ipythontutor curInstr=1 width=1000
liste = [1, 2, 4, 8, 16, 32]
liste[2:4] = [10, 20, 30]
liste[3] = [100, 200]

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `.append()` et `.pop()`

# %% [markdown]
# * les méthodes sur les listes
# * sont plutôt optimisées pour les ajouts **à la fin** de la liste
# * les deux méthodes les plus couramment utilisées sont  
#   `.apppend()` et `.pop()`

# %% cell_style="split"
L = []
for i in range(4):
    L.append(i)
L

# %% cell_style="split"
while L:
    print(L.pop())

# %% [markdown]
# <div class="rise-footnote">
#
# si nécessaire, envisager la liste **doublement chainée**
#
# ```
# from collections import deque
# deque?
# ```
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### ajouts et tris

# %% [markdown]
# * des méthodes qui mutent la liste (mutable)  
#   (modifications *in-place*)
#
#   * `L.append(x)` ajoute `x` à la fin de `L`
#   * `L.extend(L2)` ajoute chaque élément de `L2` à la fin de `L`
#   * `L.insert(i, x)` ajoute x à la position `i`
#   * `L.sort()`  trie `L`
#   * `L.reverse()` renverse les éléments de `L`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### retraits

# %% [markdown]
# * toujours des modification en place:
#   * `L.pop(i)` supprime l’élément à la position `i`  
#     si `i` n’est pas fourni, supprime le dernier élément  
#     la fonction retourne l’élément supprimé
#   * `L.remove(x)` supprime la première occurrence de `x` dans `L`  
#     s’il n’y a pas de `x`, une exception est retournée
#   * `del L[i]` supprime le i-ème élément
#   * `del L[i:j]`  
#     `del L[i:j:k]` supprime tous les éléments de la slice

# %% [markdown] slideshow={"slide_type": "slide"}
# ### digression: `range()`

# %% [markdown] cell_style="center"
# * `range()` est une fonction native (en anglais *builtin*)
# * qui retourne un objet **itérable**
# * c'est-à-dire sur lequel on peut faire un `for`
# * on y reviendra longuement

# %% cell_style="center"
for i in range(4):
    print(i, end=" ")

# %% [markdown]
# <div class="rise-footnote">
#
# le paramètre `end=" "` indique à `print` de ne pas ajouter de fin de ligne, 
# mais plutôt un espace, à la fin de l'impression
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# #### digression: `range()`

# %% [markdown]
# * essentiellement, **même logique que le slicing**
# * `range(j)` balaie de `0` à `j-1`
# * `range(i, j)` balaie de `i` à `j-1`
# * `range(i, j, k)` balaie de `i` à `j-1` par pas de `k`
# * pour obtenir une liste on transforme (*cast*) en liste en appelant `list()`

# %% cell_style="split"
for i in range(1, 21, 5):
    print(i, end=" ")

# %% cell_style="split"
list(range(1, 21, 5))

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemples

# %% cell_style="split"
# la fonction list() permet
# de convertir en liste
L = list(range(5))
L

# %% cell_style="split"
# un par un
L.append(100)

# ou plusieurs à la fois
L.extend([10, 20])
L

# %% cell_style="split"
# très souvent utilisé
# rappel: optimisé pour ça
L.pop()
L

# %% cell_style="split"
# pour trier c'est simple
# on va creuser ça tout de suite
L.sort()
L

# %% [markdown] slideshow={"slide_type": "slide"}
# ### tri sur les listes

# %% [markdown]
# * le tri des listes est très puissant en Python
#   * tri **en place** méthode `list.sort()`
# * il a aussi la fonction built-in `sorted()`  
#   qui trie toutes les séquences  
#   et retourne **une nouvelle liste**

# %% cell_style="split"
L = [10, -5, 3, 100]

# tri en place: retourne None
this_is_none = L.sort()
# par contre L est modifiée
L

# %% cell_style="split"
L1 = [10, -5, 3, 100]

# crée une copie
L2 = sorted(L1)
# voyez
print(L1)
print(L2)

# %% [markdown]
# <div class=rise-footnote>
#
# dans l'exemple de gauche, le retour de la méthode `sort` est `None`; cela pour bien manifester le fait qu'il n'y a pas eu de copie
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# #### tri et renversement de liste

# %% [markdown]
# pour conclure - temporairement - sur ce sujet:
#
# * on peut aussi trier selon un critère *ad hoc*  
#   on en reparlera plus tard
#
# * on retrouve la même dualité pour le renversement  
#   `L.reverse()` renverse la liste en place  
#   `reversed(L)` retourne une **copie** renversée

# %% [markdown] slideshow={"slide_type": "slide"}
# ### avertissements à propos des listes

# %% [markdown] slideshow={"slide_type": ""}
# #### (1) les itérateurs sont plus forts
#
# * la liste est un outil très très pratique
# * **mais** parfois (souvent) pas nécessaire
# * car nécessite **de la mémoire**
# * alors qu'on a souvent **seulement besoin d'itérer** sur le contenu
# * dans ce cas, techniques + adaptées : itérateurs et autres générateurs
#
# sujet avancé que l’on verra plus tard

# %% [markdown]
# <div class="rise-footnote">
#
# si on repense par exemple au `range()` vu plus haut, pour itérer sur un entier de 1 à 1 million, 
# a-t-on vraiment besoin pour cela d'allouer
# explicitement un million d'entiers, plus la place pour les cellules de la liste ? bien sûr que non....
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# #### (2) pas efficace pour calcul scientifique
#
# * le coté flexible en taille et en type rend la liste **très pratique**
# * mais attention ça peut devenir **très inefficace**
# * notamment pour le calcul scientifique
# * pas d'équivalent parmi les types Python natifs  
#   d'un bon vieux tableau C/C++/Fortran
#
# * penser absolument aux **tableaux `numpy`**  
#   pour ce type d'application

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le tuple

# %% [markdown]
# * comme des listes, mais **immutables**
# * syntaxe: `()` au lieu de `[]`

# %% cell_style="split"
# syntaxe pour un tuple vide
T = ()
T

# %% cell_style="split"
# syntaxe pour un singleton
T1 = (4,)

# ou encore
T2 = 4,

# %% cell_style="split"
T1 == T2

# %% [markdown] cell_style="center"
# <div class="rise-footnote">
#
# **attention**: c'est la virgule qui est importante, on peut omettre les `()` - la plupart du temps
#
#  * `(4)` est un **entier**, et
#  * `(4,)` est un **tuple**
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### basique

# %% cell_style="split"
# syntaxe pour plusieurs éléments
T1 = (3, 5, 'alice', 10+1j)
# ou encore
T2 =  3, 5, 'alice', 10+1j
# ou encore
T3 =  3, 5, 'alice', 10+1j,

# %% cell_style="split"
T1 == T2

# %% cell_style="split"
T1 == T3

# %% [markdown]
#
# * un tuple est **non mutable**
# * les fonctions faisant des modifications *in-place*  
#   ne s’**appliquent** donc **pas aux tuples**
#

# %%
try: T1[3] = 5   # Python n'est pas content
except Exception as e: print("OOPS", e)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### pourquoi le tuple ?
#
# * à ce stade, vous vous demandez sans doute:  
#   *pourquoi créer un tuple ?*  
#   si c'est juste moins puissant que la liste ?
#
# * la réponse est liée aux tables de hachage  
#   (dictionnaires et ensembles)  
#   que l'on va voir un peu plus tard  
#   un peu de patience donc…

# %% [markdown] slideshow={"slide_type": "slide"}
# ## problèmes avec les séquences
#
# de deux ordres principalement

# %% [markdown]
# ### (1) les recherches sont lentes

# %%
a = list(range(30000000))
'x' in a      # c’est long !

# %% [markdown] slideshow={"slide_type": "slide"}
# ### (2) on ne peut indexer que par un entier

# %%
a[3]          # on peut utiliser un indice entier

# %%
a = []
# on ne peut pas indexer avec un nom ou autre chose qu'un entier
try:
    a['alice'] = 10
except TypeError as e:
    print("OOPS", e)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### récapitulons

# %% [markdown]
# * une séquence est une liste ordonnée d’éléments  
#   indexés par des entiers
#
#   * les recherches sont longues *O(n)*
#   * impossible d’avoir un index autre qu’entier
#   * comment faire, par exemple, un annuaire ?
# * on voudrait
#   * une insertion, effacement et recherche en *O(1)*
#   * une indexation par clef quelconque

# %% [markdown] slideshow={"slide_type": "slide"}
# ## la solution : les tables de hash

# %% [markdown]
# * une table de hash T indexe des valeurs par des clefs
#   * T[clef] = valeur
#   * insertion, effacement, recherche en O(1)
#   * chaque clef est unique (une seule valeur pour une clé)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### table de hash

# %% [markdown]
# ![hash](media/hash.svg)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### table de hash

# %% [markdown]
# * la fonction de hash *f()* choisie de façon à ce que
#   * *f(key, size)* retourne toujours la même valeur
#   * *key* ne doit pas pouvoir changer au cours du temps
#   * et donc en particulier être **immutable**
# * minimise le risque de collision
#   * *f(key1, size)* == *f(key2, size)*
# * une bonne façon de minimiser les collisions  
#   est de garantir une distribution uniforme

# %% [markdown] slideshow={"slide_type": "slide"}
# ### table de hash et Python

# %% [markdown]
# * le dictionnaire `dict` est une table de hash  
#   qui utilise comme clef un **objet immutable**  
#   et comme valeur n’importe quel objet
#
#   * association clé → valeur

# %% [markdown] slideshow={"slide_type": "fragment"}
# * l'ensemble `set` est une table de hash  
#   qui utilise comme clef un **objet immutable**  
#   et qui n’associe pas la clef à une valeur
#
#   * notion d’ensemble mathématique

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le `set`

# %% [markdown]
# * collection non ordonnée(♤) d’objets uniques et **immutables**
# * utile pour tester l’appartenance
#   * optimisé, beaucoup + rapide que `list`
# * et éliminer les entrées doubles (*dedup*) d’une liste
# * test d’appartenance plus rapide que pour les listes
# * les sets autorisent les opérations sur des ensembles
#   * union (|), intersection (&), différence (-), etc.

# %% [markdown]
# <div class="rise-footnote">
#
# (♤) depuis la 3.7 le dictionnaire est une structure ordonnée (il "retient" l'ordre des ajouts)  
# toutefois cela ne s'applique pas à l'ensemble, ce qui peut créer une légère confusion
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le `set`

# %% cell_style="split"
# attention: {} c'est
# un DICTIONNAIRE vide

set()          # ensemble vide

# %% cell_style="split"
# ou sinon, on peut comme toujours
# utiliser le type comme une
# usine à objets

L1 = [1, 2, 3, 1, 1, 6, 4]
S1 = set(L1)
S1

# %% [markdown] slideshow={"slide_type": "slide"}
# #### attention pour créer un `set`

# %% cell_style="split"
# attention: il faut passer
# à set UN itérable
try:
    S = set(1, 2, 3, 4, 5)
except Exception as exc:
    print(f"OOPS {type(exc)}")

# %% cell_style="split"
# comme ceci

S = set([1, 2, 3, 4, 5])
S

# %% [markdown] slideshow={"slide_type": "slide"}
# ### opérations sur `set`

# %% cell_style="split"
S1


# %% cell_style="split"
L2 = [3, 4, 1]
S2 = set(L2)
S2

# %% cell_style="split"
4 in S2

# %% cell_style="split"
S1 - S2            # différence

# %% cell_style="split"
S1 | S2            # union

# %% cell_style="split"
S1 & S2            # intersection

# %%
# toujours vrai

(S1 & S2) | (S1 - S2) | (S2 - S1) == (S1 | S2)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le `set`: méthodes

# %% cell_style="split"
# ensemble littéral
S3 = {1, 2, 3, 4}
S3

# %% cell_style="split"
# ajout d'un élément

S3.add('spam')
S3

# %% cell_style="split"
# pas de duplication
# et pas d'ordre particulier
S3.update([10, 11, 10, 11])
S3

# %% cell_style="split"
S3.remove(11)
S3

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le `set` est mutable

# %% [markdown]
# * un `set` est un objet **mutable**
# * le `frozenset` est équivalent mais **non mutable**(♤)
# * par exemple pour servir de clé dans un hash

# %% cell_style="split"
fs = frozenset([1, 2, 3, 4])

# %% cell_style="split"
# frozenset pas mutable
try:
    fs.add(5)
except AttributeError as e:
    print("OOPS", e)

# %% [markdown]
# <div class=rise-footnote>
#
# (♤) du coup on peut dire que, en quelque sort, le `frozenset` est au `set` ce que le `tuple` est à la `list`
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### éléments acceptables

# %% [markdown]
# * on a le droit d'y mettre tout ce qui est non-mutable
# * pour que la fonction de hachage retourne toujours la même chose

# %% cell_style="split"
S = set()
S.add(1)
S.add("abc")
# je peux y ajouter un tuple !
S.add((1, 2))
S

# %% cell_style="split"
# mais pas une liste !
try:
    S.add([1, 2])
except TypeError as e:
    print("OOPS", e)

# %% [markdown]
# <div class="rise-footnote">
#
# **Question**: à votre avis, peut-on ajouter dans un ensemble un tuple de 2 listes ?
#
# ```
# S.add( ([1, 2], [3, 4]) )
# ```
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### rapide test de performance

# %% [markdown] cell_style="center"
# pour la recherche d’un élément, le set est **beaucoup plus rapide**

# %%
x = list(range(100000))

# %timeit -n 300 "c" in x

# %%
x = set(range(100000))

# %timeit -n 300 "c" in x

# %% [markdown] slideshow={"slide_type": "slide"}
# #### rapide test de performance

# %% [markdown]
# même si la liste est très petite

# %%
x = list(range(2))

# %timeit -n 300 "c" in x

# %%
x = set(range(2))

# %timeit -n 300 "c" in x

# %% [markdown] slideshow={"slide_type": "slide"}
# #### rapide test de performance

# %% [markdown]
# * il faut que l’élément cherché soit **le premier** de la liste  
#   pour que la liste soit comparable avec le set
# * donc, toujours utiliser les sets pour les tests d’appartenance

# %%
x = list(range(2))

# %timeit -n 300 0 in x

# %%
x = set(range(2))

# %timeit -n 300 0 in x

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les dictionnaires

# %% [markdown]
# * généralisation d’une table de hash
# * collection **ordonnée** d’objets (depuis la 3.7)
# * on accède aux objets à l’aide d’une clef  
#   (et non d’un indice comme pour une liste)
#
# * une **clef** peut être n’importe quel objet **immutable**  
#   chaîne, nombre, tuple d’objets immutables...
#
# * c’est une structure de données très puissante
# * le dictionnaire est un type **mutable**

# %% [markdown] slideshow={"slide_type": "slide"}
# ### création

# %%
# ATTENTION : {} n'est pas un ensemble
# les dictionnaires étaient là avant les ensembles !

D = {}
D

# %%
# un dictionnaire créé de manière littérale
{ 'douze' : 12, 1: 'un', 'liste' : [1, 2, 3] }

# %% cell_style="split"
# une autre façon quand
# les clés sont des chaînes
dict( a = 'A', b = 'B')

# %% cell_style="split"
# à partir d'une liste de couples
dict( [ ('a', 'A'), ('b', 'B') ] )

# %% [markdown] slideshow={"slide_type": "slide"}
# ### manipulations usuelles

# %% [markdown]
# * `len(D)` retourne le nombre de clefs dans `D`
# * `D[clef]` retourne la valeur pour la clef
# * `D[clef] = x` change la valeur pour la clef
# * `del D[clef]` supprime la clef et la valeur
# * `clef in D` teste l’existence de `clef` dans `D`
# * `clef not in D` teste la non existence
# * `D.copy()` *shallow copy* de `D`

# %% cell_style="split" slideshow={"slide_type": "slide"}
d = {'alice': 35, 'bob' : 9, 'charlie': 6}
d

# %% cell_style="split"
# combien d'entrées

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

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `D.get()`

# %% [markdown]
# * `D.get(clef)`
#   * retourne la valeur associée à cette clé si elle est présente, `None` sinon
#   * notez bien que `D[clef]` lance une exception si la clé n'est pas présente
#   * `D.get(clef, un_truc)` retourne `un_truc` quand la clé n'est pas présente

# %% cell_style="split"
# la clé 'marc' n'est pas présente
try:
    x = d['marc']
except KeyError as e:
    x = "?"

x

# %% cell_style="split"
# c'est quand même plus lisible

d.get('marc', '?')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### itération sur un dictionnaire

# %% [markdown] cell_style="split"
# * `D.items()` retourne **une vue** sur les (clef, valeur) de `D`
# * `D.keys()` retourne une vue sur les clefs de `D`
# * `D.values()` retourne une vue sur les valeurs de `D`

# %% cell_style="split"
# l'idiome pour itérer sur
# un dictionnaire

for k, v in d.items():
    print(f"{k=} {v=}")

# %% [markdown]
# <div class=rise-footnote>
#
# on peut aussi itérer directement sur le dictionnaire, qui est équivalent à itérer sur `d.keys()`
#
# ```python
# for k in d:
#     #   clé  valeur
#     print(k, d[k])
# ```
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### méthodes sur les dictionnaires

# %% [markdown]
# * [beaucoup d’autres méthodes](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### création automatique de valeurs

# %% [markdown] tags=["level_intermediate"]
# * utile pour alléger votre code  
#   si vous savez que vos valeurs seront toujours, par exemple une liste
#
# * `collections.defaultdict` est une sous-classe de `dict`  
#   qui ne lève pas d'exception en cas de défaut de la clé  
#   mais dans ce cas va créer, toujours par exemple, une liste vide
#
# * ce qui évite de devoir tester la présence de la clé

# %% cell_style="center" slideshow={"slide_type": "slide"} tags=["level_intermediate"]
from collections import defaultdict

# ici je décide que les valeurs sont des listes
dd = defaultdict(list)

# pas d'exception alors que la clé 0 est absente
# au contraire on appelle list() pour l'initialiser
dd[0].append(1)
dd[0].append(2)
dd[0]

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_advanced"]
# #### qu’est-ce qu’une vue ?

# %% [markdown] tags=["level_advanced"]
# * c’est un objet qui donne une vue **dynamique** sur un dictionnaire `D`
# * i.e. qui "suit" les changements futurs
# * par oppposition à: on calculerait les propriétés de d à cet instant

# %% cell_style="split" tags=["level_advanced"]
clefs = d.keys()

clefs

# %% cell_style="split" tags=["level_advanced"]
# ici clefs est une vue
del d['bob']

clefs

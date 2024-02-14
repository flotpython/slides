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
#     title: containers
#   rise:
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
# # containers (1/2)
#
# plusieurs types pratiques et efficaces sont fournis *de base*, et notamment
#
# * liste et tuple: ce notebook
# * dictionnaire, ensemble: un peu plus tard

# %% [markdown] slideshow={"slide_type": "slide"}
# ## la liste

# %% [markdown]
# * permet de créer une liste de n’importe quels objets
# * les listes sont dynamiques, de **taille variable**
# * une liste peut être **hétérogène** (avoir des composants de types différents)
# * peuvent être **imbriquées**
#   * comme une liste est un objet, on peut avoir une liste de listes
#   * ou y mettre d'autres containers
# * bref, c'est super malléable et hyper pratique
#   * toutefois, pas toujours hyper-efficace 

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
# ```{image} media/writing-a-list-slice.png
# :align: center
# ```

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
# ````{admonition} ajouter des deux cotés ?
#
# si vous avez besoin de massivement insérer aussi **en début de liste**, alors envisagez la liste **doublement chainée**
#
# ```
# from collections import deque
# deque?
# ```
#
# ````

# %% [markdown]
# ### ajouts et tris
#
# * des méthodes qui **mutent** la liste (modifications *in-place*)
#
#   * `L.extend(L2)` ajoute chaque élément de `L2` à la fin de `L`
#   * `L.insert(i, x)` ajoute x à la position `i`
#   * `L.sort()`  trie `L`
#   * `L.reverse()` renverse les éléments de `L`

# %% [markdown]
# ### retraits
#
# * toujours des modification en place:
#   * `L.pop(i)` pour supprimer à un endroit précis
#   * `L.remove(x)` supprime la première occurrence de `x` dans `L`  
#     s’il n’y a pas de `x`, une exception est retournée
#   * `del L[i]` supprime le i-ème élément
#   * `del L[i:j]`  
#     `del L[i:j:k]` supprime tous les éléments de la slice
#
# ```{admonition} et plein d'autres...
# en réalité il y a une foultitude de méthodes disponibles sur les listes, on ne signale ici que l'essentiel  
# entrainez-vous à retrouver la page de la doc qui vous les décrit, en googlant *python builtin types*  
# qui devrait vous amener rapidement à 
# <https://docs.python.org/3/library/stdtypes.html>   
# et notammment cette section: <https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types>
# ```

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
# ````{admonition} c'est quoi ce end=" " ?
#
# le paramètre `end=" "` indique à `print` de ne pas ajouter de fin de ligne, 
# mais plutôt un espace, à la fin de l'impression
#
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# #### les paramètres de `range()`

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
# ### exemples de listes

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
# * il y a aussi la fonction built-in `sorted()`  
#   qui trie toutes les séquences  
#   et retourne **une nouvelle liste**

# %% cell_style="split"
L = [10, -5, 3, 100]

# tri en place: attention cela retourne None !
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
# ````{admonition} attention au retour de L.sort()
# :class: warning
#
# dans le premier exemple, le retour de la méthode `sort` est `None`; cela pour bien manifester le fait qu'il n'y a pas eu de copie
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# #### tri et renversement de liste

# %% [markdown]
# pour conclure - temporairement - sur ce sujet:
#
# * on peut aussi trier selon un critère *ad hoc*  
#   on en reparlera plus tard
#
# * on retrouve la même dualité pour le renversement  
#   `L.reverse()` renverse la liste en place (et retourne `None`)  
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
# * dans ce cas, on a recours a des techniques plus adaptées : itérateurs et autres générateurs
#
# sujet avancé que l’on verra plus tard

# %% [markdown]
# ````{admonition} exercice de pensée
# :class: seealso admonition-smaller
#
# vous devez calculer la somme des carrés des n premiers entiers  
# pour cela le fait de construire d'abord une liste avec tous ces entiers est **inutile** et **contreproductif**,   
# car cela signifie allouer tout un tas de mémoire dont on n'a pas besoin !
#
# c'est pourquoi `range()` **ne renvoie pas une liste** mais un itérateur  
# mais on reparlera longuement de tout ça
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# #### (2) pas efficace pour calcul scientifique
#
# * le coté flexible en taille et en type rend la liste **très pratique**
# * mais attention ça peut devenir **très inefficace**
# * notamment pour le calcul scientifique
# * pas d'équivalent parmi les types Python natifs d'un bon vieux tableau C/C++/Fortran
# * penser absolument aux **tableaux `numpy`** pour ce type d'application !

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
# ````{admonition} c'est la virgule qui fait le tuple
# :class: attention
#
# **attention**: c'est la virgule qui est importante, on peut omettre les `()` - la plupart du temps
#
#  * `(4)` est un **entier**, et
#  * `(4,)` est un **tuple**
# ````

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
# ### le tuple est non mutable

# %% [markdown]
#
# * un tuple est **non mutable**
# * les fonctions faisant des modifications *in-place*  
#   ne s’**appliquent** donc **pas aux tuples**
#

# %%
# Python n'est pas content
try: 
    T1[3] = 5      
except Exception as e:
    print("OOPS", e)

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

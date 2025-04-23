---
celltoolbar: Slideshow
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: containers
---

+++ {"slideshow": {"slide_type": ""}}

# containers (1/2)

plusieurs types pratiques et efficaces sont fournis *de base*, et notamment

* liste et tuple: ce notebook
* dictionnaire, ensemble: un peu plus tard

+++

## la liste

* permet de créer une liste de n’importe quels objets
* les listes sont dynamiques, de **taille variable**
* une liste peut être **hétérogène** (avoir des composants de types différents)
* peuvent être **imbriquées**
  * comme une liste est un objet, on peut avoir une liste de listes
  * ou y mettre d'autres containers
* bref, c'est super malléable et hyper pratique
  * toutefois, pas toujours hyper-efficace

+++ {"slideshow": {"slide_type": "slide"}}

### basique

```{code-cell} ipython3
:tags: [gridwidth-1-2]

L = []
L = [4, 'bob', 10 + 1j, True]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# on peut mélanger les types
L
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# les indices en python
# commencent à 0
L[2]
```

+++ {"slideshow": {"slide_type": "slide"}}

### modification par index

```{code-cell} ipython3
:cell_style: center

# les indices commencent à 0
L
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pour modifier un élément précis
L[2] = "BOOM"
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pas besoin de préserver les types
# ni rien de ce genre

L
```

+++ {"slideshow": {"slide_type": "slide"}}

### modification par slice

```{code-cell} ipython3
:tags: [gridwidth-1-2]

liste = [1, 2, 4, 8, 16, 32]
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
# le slicing est disponible
# sur les listes
liste[2:]
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
# on peut aussi modifier
# toute une slice
liste[2:4] = [10, 20, 30]
liste
```

+++ {"slideshow": {"slide_type": ""}, "tags": ["gridwidth-1-2"]}

```{image} media/writing-a-list-slice.png
:align: center
```

+++ {"slideshow": {"slide_type": ""}}

### attention

* `L[i] = L2`
  * **remplace** le i-ème élément de `L` par la liste `L2`
* `L[i:j] = L2`
  * **insère** tous les éléments de la liste `L2` à la position `i`
  * après avoir supprimé les éléments `i` jusqu’à `j-1` dans `L`

+++ {"slideshow": {"slide_type": "slide"}}

### modification sous pythontutor

```{code-cell} ipython3
:tags: [gridwidth-1-2]

liste = [1, 2, 4, 8, 16, 32]
liste
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

liste[2:4] = [10, 20, 30]
liste
```

```{code-cell} ipython3
liste[3] = [100, 200]
liste
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
%load_ext ipythontutor
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
---
%%ipythontutor curInstr=1 width=1000
liste = [1, 2, 4, 8, 16, 32]
liste[2:4] = [10, 20, 30]
liste[3] = [100, 200]
```

### `.append()` et `.pop()`

* les méthodes sur les listes
* sont plutôt optimisées pour les ajouts **à la fin** de la liste
* les deux méthodes les plus couramment utilisées sont  
  `.apppend()` et `.pop()`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

L = []
for i in range(4):
    L.append(i)
L
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

while L:
    print(L.pop())
```

````{admonition} ajouter des deux cotés ?

si vous avez besoin de massivement insérer aussi **en début de liste**, alors envisagez la liste **doublement chainée**

```python
from collections import deque
deque?
```

````

+++

### ajouts et tris

* des méthodes qui **mutent** la liste (modifications *in-place*)

  * `L.extend(L2)` ajoute chaque élément de `L2` à la fin de `L`
  * `L.insert(i, x)` ajoute x à la position `i`
  * `L.sort()`  trie `L`
  * `L.reverse()` renverse les éléments de `L`

+++

### retraits

* toujours des modifications en place:
  * `L.pop(i)` pour supprimer à un endroit précis
  * `L.remove(x)` supprime la première occurrence de `x` dans `L`  
    s’il n’y a pas de `x`, une exception est retournée

  * `del L[i]` supprime le i-ème élément
  * `del L[i:j]`  
    `del L[i:j:k]` supprime tous les éléments de la slice

```{admonition} et plein d'autres...
en réalité il y a une foultitude de méthodes disponibles sur les listes, on ne signale ici que l'essentiel  
entrainez-vous à retrouver la page de la doc qui vous les décrit, en googlant *python builtin types*  
qui devrait vous amener rapidement à 
<https://docs.python.org/3/library/stdtypes.html>   
et notammment cette section: <https://docs.python.org/3/library/stdtypes.html#mutable-sequence-types>
```

+++ {"cell_style": "center"}

### digression: `range()`

* `range()` est une fonction native (en anglais *builtin*)
* qui retourne un objet **itérable**
* c'est-à-dire sur lequel on peut faire un `for`
* on y reviendra longuement

```{code-cell} ipython3
:cell_style: center

for i in range(4):
    print(i, end=" ")
```

````{admonition} c'est quoi ce end=" " ?

le paramètre `end=" "` indique à `print` de ne pas ajouter de fin de ligne, 
mais plutôt un espace, à la fin de l'impression

````

+++

#### les paramètres de `range()`

* essentiellement, **même logique que le slicing**
* `range(j)` balaie de `0` à `j-1`
* `range(i, j)` balaie de `i` à `j-1`
* `range(i, j, k)` balaie de `i` à `j-1` par pas de `k`
* pour obtenir une liste on transforme (*cast*) en liste en appelant `list()`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

for i in range(1, 21, 5):
    print(i, end=" ")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

list(range(1, 21, 5))
```

+++ {"slideshow": {"slide_type": "slide"}}

### exemples de listes

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# la fonction list() permet
# de convertir en liste
L = list(range(5))
L
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# un par un
L.append(100)

# ou plusieurs à la fois
L.extend([10, 20])
L
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# très souvent utilisé
# rappel: optimisé pour ça
L.pop()
L
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pour trier c'est simple
# on va creuser ça tout de suite
L.sort()
L
```

### tri sur les listes

* le tri des listes est très puissant en Python
  * tri **en place** méthode `list.sort()`
* il y a aussi la fonction built-in `sorted()`  
  qui trie toutes les séquences  
  et retourne **une nouvelle liste**

```{code-cell} ipython3
:tags: [gridwidth-1-2]

L = [10, -5, 3, 100]

# tri en place: attention cela retourne None !
this_is_none = L.sort()
# par contre L est modifiée
L
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

L1 = [10, -5, 3, 100]

# crée une copie
L2 = sorted(L1)
# voyez
print(L1)
print(L2)
```

````{admonition} attention au retour de L.sort()
:class: warning

dans le premier exemple, le retour de la méthode `sort` est `None`; cela pour bien manifester le fait qu'il n'y a pas eu de copie
````

+++

#### tri et renversement de liste

pour conclure - temporairement - sur ce sujet:

* on peut aussi trier selon un critère *ad hoc*  
  on en reparlera plus tard

* on retrouve la même dualité pour le renversement  
  `L.reverse()` renverse la liste en place (et retourne `None`)  
  `reversed(L)` retourne une **copie** renversée

+++ {"slideshow": {"slide_type": "slide"}}

### avertissements à propos des listes

+++ {"slideshow": {"slide_type": ""}}

#### (1) les itérateurs sont plus forts

* la liste est un outil très très pratique
* **mais** parfois (souvent) pas nécessaire
* car nécessite **de la mémoire**
* alors qu'on a souvent **seulement besoin d'itérer** sur le contenu
* dans ce cas, on a recours a des techniques plus adaptées : itérateurs et autres générateurs

sujet avancé que l’on verra plus tard

+++

````{admonition} exercice de pensée
:class: seealso admonition-smaller

vous devez calculer la somme des carrés des n premiers entiers  
pour cela le fait de construire d'abord une liste avec tous ces entiers est **inutile** et **contreproductif**,  
car cela signifie allouer tout un tas de mémoire dont on n'a pas besoin !

c'est pourquoi `range()` **ne renvoie pas une liste** mais un itérateur  
mais on reparlera longuement de tout ça
````

+++ {"slideshow": {"slide_type": "slide"}}

#### (2) pas efficace pour calcul scientifique

* le coté flexible en taille et en type rend la liste **très pratique**
* mais attention ça peut devenir **très inefficace**
* notamment pour le calcul scientifique
* pas d'équivalent parmi les types Python natifs d'un bon vieux tableau C/C++/Fortran
* penser absolument aux **tableaux `numpy`** pour ce type d'application !

+++

## le tuple

* comme des listes, mais **immutables**
* syntaxe: `()` au lieu de `[]`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# syntaxe pour un tuple vide
T = ()
T
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# syntaxe pour un singleton
T1 = (4,)

# ou encore
T2 = 4,
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

T1 == T2
```

+++ {"cell_style": "center"}

````{admonition} c'est la virgule qui fait le tuple
:class: attention

**attention**: c'est la virgule qui est importante, on peut omettre les `()` - la plupart du temps

 * `(4)` est un **entier**, et
 * `(4,)` est un **tuple**
````

+++ {"slideshow": {"slide_type": "slide"}}

### basique

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# syntaxe pour plusieurs éléments
T1 = (3, 5, 'alice', 10+1j)
# ou encore
T2 =  3, 5, 'alice', 10+1j
# ou encore
T3 =  3, 5, 'alice', 10+1j,
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

T1 == T2
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

T1 == T3
```

### le tuple est non mutable

* un tuple est **non mutable**
* les fonctions faisant des modifications *in-place*  
  ne s’**appliquent** donc **pas aux tuples**

```{code-cell} ipython3
# Python n'est pas content
try: 
    T1[3] = 5      
except Exception as e:
    print("OOPS", e)
```

+++ {"slideshow": {"slide_type": "slide"}}

### pourquoi le tuple ?

* à ce stade, vous vous demandez sans doute:  
  *pourquoi créer un tuple ?*  
  si c'est juste moins puissant que la liste ?

* la réponse est liée aux tables de hachage  
  (dictionnaires et ensembles)  
  que l'on va voir un peu plus tard  
  un peu de patience donc…

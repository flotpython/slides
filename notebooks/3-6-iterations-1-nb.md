---
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
  title: "it\xE9rations (1/2)"
---

# itér.. (1/3) - for, itertools

* la boucle `for` est la méthode **préférée** pour itérer sur un ensemble de valeurs
* en général préférable au `while` en Python
  * on peut faire un `for` sur n'importe quel itérable
  * ce n'est pas le cas pour le `while`
  * avec `for` c'est l'itérable qui se charge de la logique

+++ {"slideshow": {"slide_type": "slide"}}

* **et aussi** de nombreuses techniques pour itérer **de manière optimisée**
  * compréhensions
  * itérateurs
  * expressions génératrices
  * générateurs (encore appelées fonctions génératrices)
* attention / rappel : avec numpy, pas de `for`, programmation vectorielle

+++ {"slideshow": {"slide_type": ""}}

## la boucle `for`

une instruction `for` ressemble à ceci :

```python
for item in iterable:
    bloc
    aligné
    d_instructions
```

+++

### `break` et `continue`

comme dans beaucoup d'autres langages, et comme pour le `while` :

* `break` sort complètement de la boucle
* `continue` termine abruptement  
  l'itération courante et passe à la suivante

+++ {"slideshow": {"slide_type": ""}}

### `for .. else`

en fait la forme générale de la boucle `for` c'est


```python
for item in iterable:
    bloc
    aligné
else:
    bloc     # exécuté lorsque la boucle sort "proprement"
    aligné   # c'est-à-dire pas avec un break
```


````{admonition} c'est assez rare
    
l'instruction `else` attachée à un `for` est d'un usage plutôt rare en pratique
````

+++ {"slideshow": {"slide_type": "slide"}}

### bouh c'est vilain !

dès que vous voyez {del}`` `for i in range(len(truc))` `` vous devez vous dire qu'il y a mieux à faire:

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
liste = [10, 20, 40, 80, 120]

# la bonne façon de faire un for

for item in liste:
    print(item, end=" ")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et **non pas** cette
# horrible périphrase !

for i in range(len(liste)):
    item = liste[i]
    print(item, end=" ")
```

### boucle `for` sur un dictionnaire

* *rappel*: on peut facilement itérer sur un dictionnaire
* la plupart du temps, sur à la fois clés et valeurs
  `for k, v in d.items():`

* pour itérer sur les clés, restons simple: `for k in d:`
* enfin sur les valeurs `for v in d.values():`

````{admonition} remarque
:class: admonition-small

on peut aussi itérer sur les clés avec `for k in d.keys()`, mais c'est moche..
````

```{code-cell} ipython3
:tags: [gridwidth-1-2]

agenda = {
    'paul': 12, 
    'pierre': 14,
    'jean': 16,
}
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# l'unpacking permet d'écrire 
# un code élégant
for key, value in agenda.items():
    print(f"{key} → {value}")
```

### boucles `for` : limite importante

* **règle très importante:** à l'intérieur d'une boucle
* il ne faut **pas modifier l’objet** sur lequel on itère

```{code-cell} ipython3
:cell_style: center

s = {1, 2, 3}

# on essaie de modifier l'objet itéré
try:
    for x in s:
        if x == 1:
            s.remove(x)
except Exception as exc:
    print(f"OOPS {type(exc)} {exc}")
```

+++ {"slideshow": {"slide_type": "slide"}}

la technique usuelle consiste à utiliser une copie

```{code-cell} ipython3
:cell_style: center

s = {1, 2, 3}

# avec les listes on peut aussi utiliser [:]
# mais ici sur un ensemble ça ne fonctionnerait pas 
for x in s.copy():
    if x == 1:
        s.remove(x)

s
```

### question de style

rappelez-vous qu'on peut *unpack* dans un for; ça permet souvent d'utiliser des noms de variables explicites

```{code-cell} ipython3
:tags: [gridwidth-1-2]

D = {'alice': 35, 'bob': 9, 'charlie': 6}
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pas pythonique (implicite)

for t in D.items():
    print(t[0], t[1])
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pythonique (explicite)

for nom, age in D.items():
    print(nom, age)
```

+++ {"slideshow": {"slide_type": ""}}

## itérables et itérateurs

### c'est quoi un itérable ?

* par définition, c'est un objet .. sur lequel on peut faire un `for`
* notamment avec les séquences natives : chaînes, listes, tuples, ensembles
* et aussi dictionnaires, et des tas d'autres objets, mais patience

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# une chaine est un itérable

chaine = "un été"
for char in chaine:
    print(char, end=" ")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# un ensemble aussi

ensemble = {10, 40, 80} 
for element in ensemble:
    print(element, end=" ")
```

+++ {"tags": ["gridwidth-1-2"]}

### la boucle `for`, mais pas que

* on a défini les itérables par rapport à la boucle `for` 
* mais plusieurs fonctions acceptent en argument des itérables
* `sum`, `max`, `min`
* `map`, `filter`
* etc...

```{code-cell} ipython3
:tags: [gridwidth-1-2]

L = [20, 34, 57, 2, 25]

min(L), sum(L)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ceci retourne un itérateur
map(lambda x: x**2, L)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pour voir "ce qu'il y a dedans"
list(map(lambda x: x**2, L))
```

+++ {"slideshow": {"slide_type": "slide"}}

### itérateurs

* les **itérateurs** sont une sous-famille des itérables
* qui présentent la particularité de **consommer peu de mémoire**
* en fait un objet itérateur capture uniquement  **la logique de l'itération**, mais pas les données
* c'est-à-dire où on en est, et comment passer au suivant

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
import sys

L = list(range(1000))
sys.getsizeof(L)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# avec iter() on fabrique 
# un itérateur
I = iter(L)

sys.getsizeof(I)
```

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["gridwidth-1-2"]}

cette boucle Python
```python
for i in range(100_000):
    # do stuff
```

+++ {"tags": ["gridwidth-1-2"]}

est comparable à ceci en C
```C
for (int i=0; 
     i<100000; 
     i++) {
    /* do stuff */
}
```

+++ {"slideshow": {"slide_type": ""}}

ce qui montre qu'on peut s'en sortir avec **seulement un entier** comme mémoire  
et donc on ne veut **pas devoir allouer** une liste de 100.000 éléments juste pour pouvoir faire cette boucle !

+++

### combinaisons d'itérations

Python propose des outils pour **créer** et **combiner** les itérables:

* fonctions natives *builtin* qui créent des itérateurs:
  * `range`, `enumerate`, et `zip`
* dans un module dédié `itertools`:
  * `chain`, `cycle`, `islice`, ...

+++

### `range`

* `range` crée un objet qui permet d'itèrer sur un intervalle de nombres entiers
* arguments : même logique que le slicing
  * début (inclus), fin (exclus), pas
  * **sauf** (curiosité) : si un seul argument, c'est **la fin**

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# les nombres pairs de 10 à 20
for i in range(10, 21, 2):
    print(i, end=" ")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# le début par défaut est 0
for i in range(5):
    print(i, end=" ")
```

#### un `range` n'est **pas une liste**

* l'objet retourné par `range` **n'est pas une liste**
* au contraire il crée un objet tout petit, un **itérateur** (*)
* qui contient seulement la logique de l'itération
* la preuve:

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# 10**20 c'est 100 millions de Tera

# un range est presque un iterateur
iterator = range(10**20)
iterator
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

for item in iterator:
    if item >= 5:
        break
    print(item, end=" ")
```

````{admonition} je chipote, mais...

en réalité un `range()` n'est pas techniquement un itérateur; mais bon ça y ressemble beaucoup...
````

+++ {"slideshow": {"slide_type": "fragment"}}

`````{admonition} exercice
:class: seealso

comment créer **une vraie liste** des entiers de 1 à 10 ?

````{admonition} réponse
:class: tip dropdown

```python
list(range(1, 11))
```

où le type `list` se comporte, (comme tous les types)
comme **une usine** à fabriquer des listes
````
`````

+++ {"slideshow": {"slide_type": ""}}

### `count` : un itérateur infini

du coup un itérateur peut même .. ne jamais terminer :

```{code-cell} ipython3
# count fait partie du module itertools

from itertools import count
count?
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# si on n'arrête pas la boucle nous mêmes
# ce fragment va boucler sans fin

for i in count():
    print(i, end=" ")
    if i >= 10:
        break
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# on peut changer les réglages
# ici en partant de 2 avec un step de 5

for i in count(2, 5):
    print(i, end=" ")
    if i >= 32:
        break
```

+++ {"tags": ["gridwidth-1-2"]}

### `enumerate`

on a dit qu'on ne faisait jamais

```python
for i in range(len(liste)):
    item = liste[i]
    print(item, end=" ")
```

mais comment faire alors si on a vraiment besoin de l'index `i` ?  
→ il suffit d'utiliser la *builtin* `enumerate()`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

L = [1, 10, 100]

for i, item in enumerate(L):
    print(f"{i}: {item}")
```

+++ {"slideshow": {"slide_type": "slide"}}

```{image} media/iter-enumerate.svg
:align: center
```

+++

`enumerate` est typiquement utile sur un fichier, pour avoir le numéro de ligne  
remarquez le deuxième argument de `enumerate`, ici pour commencer à 1

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# on peut aussi commencer 
# à autre chose que 0

with open("some-file.txt") as f:
    for lineno, line in enumerate(f, 1):
        print(f"{lineno}:{line}", end="")
```

+++ {"slideshow": {"slide_type": "slide"}}

### `zip`

+++

`zip` permet d'itérer sur plusieurs itérables "en même temps":

```{image} media/iter-zip.svg
:align: center
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

liste1 = [10, 20, 30]
liste2 = [100, 200, 300]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

for a, b in zip(liste1, liste2):
    print(f"{a}x{b}", end=" ")
```

+++ {"tags": ["gridwidth-1-2"]}

````{admonition} les arguments 

* `zip` fonctionne avec autant d'arguments qu'on veut
* elle s'arrête dès que l'entrée **la plus courte** est épuisée
````

+++ {"tags": ["gridwidth-1-2"]}

`````{admonition} exercice: enumerate = zip + count
:class: seealso admonition-small

aucun intérêt pratique, mais juste pour le fun :  
voyez-vous un moyen d'écrire `enumerate` à base de `zip` et `count` ?

````{admonition} réponse
:class: tip dropdown

```python
# zip s'arrête dès que 
# l'un de ses morceaux s'arrête

for index, item in zip(count(), L):
    print(f"{index} {item}")
```

```{image} media/iter-zip-count.svg
:align: center
```
````
`````

+++ {"slideshow": {"slide_type": "slide"}}

### un itérateur s'épuise

**ATTENTION** il y a toutefois une limite lorsqu'on utilise un itérateur

* une fois que l'itérateur est arrivé à sa fin
* il est "épuisé" et on ne peut plus boucler dessus

````{admonition} note
    
à cet égard, les `range()` sont spéciaux
````

```{code-cell} ipython3
:lines_to_next_cell: 2
:tags: [gridwidth-1-2]

# avec une liste, pas de souci
L = [100, 200]

print('pass 1')
for i in L:
    print(i)

print('pass 2')
for i in L:
    print(i)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# iter() permet de construire
# un itérateur sur un itérable

R = iter(L)

print('pass 1')
for i in R:
    print(i)

print('pass 2')
for i in R:
    print(i)    
```

+++ {"slideshow": {"slide_type": "slide"}}

du coup par exemple,  
**ne pas essayer d'itérer deux fois** sur un `zip()` ou un `enumerate()`, vous observeriez le même phénomène

+++

## le module `itertools` - assemblage d'itérables

on trouve dans le module `itertools` plusieurs utilitaires très pratiques :

* `count` pour énumérer les entiers (voir plus haut)
* `chain` pour chainer plusieurs itérables
* `cycle` pour rejouer un itérable en boucle
* `repeat` pour énumérer plusieurs fois le même objet
* `islice` pour n'énumérer que certains morceaux
* `zip_longest` fonctionne comme `zip` mais s'arrête au morceau le plus long

+++ {"slideshow": {"slide_type": "slide"}}

### `chain`

```{image} media/iter-chain.svg
:align: center
```

```{code-cell} ipython3
---
cell_style: center
slideshow:
  slide_type: ''
---
from itertools import chain
data1 = (10, 20, 30)
data2 = (100, 200, 300)
```

```{code-cell} ipython3
:cell_style: center

# chain()
for d in chain(data1, data2):
    print(f"{d}", end=" ")
```

```{code-cell} ipython3
:cell_style: center

# c'est comme un lego, on peut combiner toutes ces fonctions
for i, d in enumerate(chain(data1, data2)):
    print(f"{i}x{d}", end=" ")
```

+++ {"slideshow": {"slide_type": "slide"}}

### `cycle`

```{image} media/iter-cycle.svg
:align: center
```

```{code-cell} ipython3
# cycle() ne termine jamais non plus

from itertools import cycle
data1 = (10, 20, 30)

for i, d in enumerate(cycle(data1)):
    print(f"{i}x{d}", end=" ")
    if i >= 10:
        break
```

+++ {"slideshow": {"slide_type": "slide"}}

### `repeat`

```{code-cell} ipython3
# repeat()
from itertools import repeat
data1 = (10, 20, 30)
data2 = (100, 200, 300)

# pour peut répéter le même élément plusieurs fois
padding = repeat(1000, 3)

for i, d in enumerate(chain(data1, padding, data2)):
    print(f"{i}x{d}", end=" ")
```

+++ {"slideshow": {"slide_type": "slide"}}

### `islice`

fonctionne comme le slicing, mais sur n'importe quel itérable

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# avec islice on peut par exemple 
# sauter une ligne sur deux dans un fichier
from pathlib import Path

# on crée un fichier 
with Path('islice.txt').open('w') as f:
    for i in range(6):
        f.write(f"{i}**2 = {i**2}\n")
```

```{code-cell} ipython3
:lines_to_next_cell: 2
:tags: [gridwidth-1-2]

# pour ne relire qu'une ligne sur deux

from itertools import islice

with Path('islice.txt').open() as f:
    for line in islice(f, 0, None, 2):
        print(line, end="")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ou zapper les 3 premières

from itertools import islice

with Path('islice.txt').open() as f:
    for line in islice(f, 3, None):
        print(line, end="")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ou ne garder que les 3 premières

from itertools import islice

with Path('islice.txt').open() as f:
    for line in islice(f, 3):
        print(line, end="")
```

+++ {"slideshow": {"slide_type": "slide"}}

### `zip_longest()`

comme `zip`, mais s'arrête à l'entrée la plus longue  
du coup il faut dire par quoi remplacer les données manquantes

```{code-cell} ipython3
:tags: [gridwidth-1-2]

from itertools import zip_longest
for i, d in zip_longest(
        range(6), L, fillvalue='X'):
    print(f"{i} {d}")
```

+++ {"tags": ["gridwidth-1-2"]}

```{image} media/iter-zip-longest.svg
```

+++

## `itertools` & combinatoires

Le module `itertools` propose aussi quelques combinatoires usuelles:

* `product`: produit cartésien de deux itérables
* `permutations`: les permutations ($n!$)
* `combinations`: *p parmi n*
* et d'autres... 
* <https://docs.python.org/3/library/itertools.html>

+++ {"slideshow": {"slide_type": "slide"}}

### exemple avec `product`

```{code-cell} ipython3
from itertools import product

dim1 = (1, 2, 3)
dim2 = '♡♢♤'

for i, (d1, d2) in enumerate(product(dim1, dim2), 1):
    print(f"i={i}, d1={d1} d2={d2}")
```

+++ {"slideshow": {"slide_type": "slide"}}

````{admonition} exercice
:class: seeaso

le code de Vigenere se prête particulièrement bien à ces outils d'assembage d'itérabes (voir notebook séparé)
````

+++ {"slideshow": {"slide_type": "slide"}}

(label-for-under-the-hood)=
## sous le capot

pour les curieux..

+++ {"tags": ["gridwidth-1-2"]}

### comment marche la boucle `for` ?

lorsqu'on itère sur un itérable
```python
iterable = [10, 20, 30]
```

+++ {"tags": ["gridwidth-1-2"]}

sous le capot, la boucle `for` va faire:

  * créer un itérateur en appelant `iter(iterable)`
  * appeler `next()` sur cet itérateur
  * jusqu'à obtenir l'exception `StopIteration`

+++ {"slideshow": {"slide_type": ""}}

### `iter()` et `next()`

voici un équivalent approximatif

```{code-cell} ipython3
:tags: [gridwidth-1-2]

iterable = [10, 20, 30]

# cette boucle for 

for item in iterable:
    print(item)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
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
```

````{admonition} iter() et next()

il peut être parfois pratique d'utiliser `iter()` et `next()`  
par exemple, comment prendre un élément - n'importe lequel - dans un ensemble ?
````

+++

### quel objet est itérable ?

* il existe beaucoup d’objets itérables en python
  * tous les objets séquence: listes, tuples, chaînes, etc.
  * les sets, les dictionnaires
  * les vues (`dict.keys()`, `dict.values()`), etc.
  * les fichiers
  * les générateurs
* il faut **penser à les utiliser**, c’est le plus rapide et le plus lisible

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_intermediate"]}

### quel objet est un itérateur ? (avancé)

+++ {"tags": ["gridwidth-1-2"]}

pour savoir si un objet est un itérateur  
tester si  
  `iter(obj) is obj`

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
def is_iterator(obj):
    return iter(obj) is obj
```

+++ {"slideshow": {"slide_type": "slide"}}

### par exemple

* une liste **n'est pas** son propre itérateur
* un fichier **est** son propre itérateur

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
tags: [gridwidth-1-2]
---
# créons un fichier
with open("tmp.txt", 'w') as F:
    for i in range(6):
        print(f"{i=} {i**2=}", file=F)

# pour voir qu'un fichier ouvert en
# lecture est son propre itérateur
with open("tmp.txt") as F:
    print(f"{is_iterator(F)=}")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# la liste non
L = list(range(5))
print(f"{is_iterator(L)=}")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# cycle en est un
C = cycle(L)
print(f"{is_iterator(C)=}")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# un zip() est un itérateur
Z = zip(L, L)
print(f"{is_iterator(Z)=}")
```

````{admonition} bien se souvenir

**un itérateur s'épuise**, et donc un objet qui est un itérateur ne peut être itéré qu'une seule fois
````

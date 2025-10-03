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

# containers (2/2)

plusieurs types pratiques et efficaces sont fournis *de base*, et notamment

* liste, tuple (vus précédemment)
* dictionnaire, ensemble: ce notebook

+++

## problèmes avec les séquences

de deux ordres principalement

+++

### (1) les recherches sont lentes

```{code-cell} ipython3
a = list(range(30000000))
'x' in a      # c’est long !
```

### (2) on ne peut indexer que par un entier

```{code-cell} ipython3
a[3]          # on peut utiliser un indice entier
```

```{code-cell} ipython3
a = []
# on ne peut pas indexer avec un nom ou autre chose qu'un entier
try:
    a['alice'] = 10
except TypeError as e:
    print("OOPS", e)
```

### récapitulons

* une séquence est une liste ordonnée d’éléments  
  indexés par des entiers

  * les recherches sont longues *O(n)*
  * impossible d’avoir un index autre qu’entier
  * comment faire, par exemple, un annuaire ?
* on voudrait
  * une insertion, effacement et recherche en *O(1)*
  * une indexation par clef quelconque

+++

## la solution : les tables de hash

* une table de hash T indexe des valeurs par des clefs
  * T[clef] = valeur
  * insertion, effacement, recherche en O(1)
  * chaque clef est unique (une seule valeur pour une clé)

+++

### le principe

```{image} media/hash.svg
:align:center
```

+++

### la fonction de hash

* la fonction de hash *f()* choisie de façon à ce que
  * *f(key, size)* retourne **toujours la même valeur**
  * *key* ne doit pas pouvoir changer au cours du temps
  * et donc en particulier être **immutable**
* minimise le risque de collision
  * *f(key1, size)* == *f(key2, size)*
* une bonne façon de minimiser les collisions  
  est de garantir une distribution uniforme

+++

### table de hash et Python

* l'ensemble `set` est une table de hash qui utilise
  * comme clef un **objet immutable**
  * et qui n’associe pas la clef à une valeur

  cela matérialise donc la notion d’ensemble mathématique

* le dictionnaire `dict` est une table de hash qui utilise
  * comme clef un **objet immutable**  
  * et comme valeur n’importe quel objet

  il fournit donc une association clé → valeur

+++

## le `set`

* collection non ordonnée(♤) d’objets uniques et **immutables**
* utile pour tester l’appartenance
  * optimisé, beaucoup + rapide que `list`
* et éliminer les entrées doubles (*dedup*) d’une liste
* les sets autorisent les opérations sur des ensembles
  * union (|), intersection (&), différence (-), etc.

+++

````{admonition} l'ensemble est non ordonné
:warning:

(♤) depuis la 3.7 le dictionnaire est une structure ordonnée (il "retient" l'ordre des ajouts)  
toutefois cela ne s'applique pas à l'ensemble, ce qui peut créer une légère confusion
````

+++

### création

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ATTENTION : les dictionnaires étaient là avant les ensembles !
# du coup {} n'est pas un ensemble, mais un dict !

set()          # ensemble vide
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ou sinon, on peut comme toujours
# utiliser le type comme une
# usine à objets

L1 = [1, 2, 3, 1, 1, 6, 4]
S1 = set(L1)
S1
```

### opérations sur `set`

```{code-cell} ipython3
:lines_to_next_cell: 2
:tags: [gridwidth-1-2]

S1
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

L2 = [3, 4, 1]
S2 = set(L2)
S2
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

4 in S2
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

S1 - S2            # différence
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

S1 | S2            # union
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

S1 & S2            # intersection
```

```{code-cell} ipython3
# toujours vrai

(S1 & S2) | (S1 - S2) | (S2 - S1) == (S1 | S2)
```

### le `set`: méthodes

les plus utiles sont `add()` et `.remove()` (et là encore il y en a toute un paquet...)

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ensemble littéral
S3 = {1, 2, 3, 4}
S3
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ajout d'un élément

S3.add('spam')
S3
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pas de duplication
# et pas d'ordre particulier
S3.update([10, 11, 10, 11])
S3
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

S3.remove(11)
S3
```

### le `set` est mutable

* un `set` est un objet **mutable**
* le `frozenset` est équivalent mais **non mutable**(♤)
* par exemple pour servir de clé dans un hash

```{code-cell} ipython3
:tags: [gridwidth-1-2]

fs = frozenset([1, 2, 3, 4])
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# frozenset pas mutable
try:
    fs.add(5)
except AttributeError as e:
    print("OOPS", e)
```

````{admonition} frozenset et set
:class: info admonition-small

(♤) du coup on peut dire, en quelque sorte, que le `frozenset` est au `set` ce que le `tuple` est à la `list`
````

+++

### éléments acceptables

* on a le droit d'y mettre tout ce qui est **non-mutable**
* pour que la fonction de hachage retourne toujours la même chose

```{code-cell} ipython3
:tags: [gridwidth-1-2]

S = set()
S.add(1)
S.add("abc")
# je peux y ajouter un tuple !
S.add((1, 2))
S
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# mais pas une liste !
try:
    S.add([1, 2])
except TypeError as e:
    print("OOPS", e)
```

`````{admonition} exercice de pensée
:class: seealso

**Question**: à votre avis, peut-on ajouter dans un ensemble un tuple de 2 listes ?

```python
S.add( ([1, 2], [3, 4]) )
```

````{admonition} réponse
:class: dropdown

en fait non! ce tuple est immutable, mais on peut tout de même changer ses éléments car ce sont des listes !
````

`````

+++ {"cell_style": "center"}

### rapide test de performance

pour la recherche d’un élément, le set est **beaucoup plus rapide**

```{code-cell} ipython3
x = list(range(100000))

%timeit -n 300 "c" in x
```

```{code-cell} ipython3
x = set(range(100000))

%timeit -n 300 "c" in x
```

#### le set est beaucoup plus rapide

et cela même si la liste est très petite

```{code-cell} ipython3
x = list(range(2))

%timeit -n 300 "c" in x
```

```{code-cell} ipython3
x = set(range(2))

%timeit -n 300 "c" in x
```

#### le meilleur cas pour la liste

en fait pour obtenir des performances comparables

* il faut que l’élément cherché soit **le premier** de la liste  
* donc, toujours utiliser les sets pour les tests d’appartenance

```{code-cell} ipython3
x = list(range(2))

%timeit -n 300 0 in x
```

```{code-cell} ipython3
x = set(range(2))

%timeit -n 300 0 in x
```

## le dictionnaire

* généralisation d’une table de hash
* collection **ordonnée** (depuis la 3.7)  
  d'associations *clé → valeur*

* on accède aux objets à l’aide d’une clef  
  (et non d’un indice comme pour une liste)

* une **clef** peut être n’importe quel objet **immutable**  
  chaîne, nombre, tuple d’objets immutables...

* c’est une structure de données très puissante
* le dictionnaire est un type **mutable**

+++

### création

```{code-cell} ipython3
# ATTENTION : les dictionnaires étaient là avant les ensembles !
# du coup {} n'est pas un ensemble, mais un dict !

D = {}
D
```

````{admonition} autre moyen ?
:class: seealso

voyez-vous un autre moyen de créer un dictionnaire vide ?

```{admonition} réponse
:class: dropdown

oui vous pouvez deviner que `dict()` renvoie aussi un dictionnaire vide
```
````

```{code-cell} ipython3
# un dictionnaire créé de manière littérale

{ 'douze' : 12, 1: 'un', 'liste' : [1, 2, 3] }
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# une autre façon, quand les clés sont des chaînes

dict( a = 'A', b = 'B')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ou aussi, plus rare, mais à partir d'une liste de couples...
# juste pour montrer qu'il y a souvent plein de façons de faire...

dict( [ ('a', 'A'), ('b', 'B') ] )
```

### manipulations usuelles

* `len(D)` retourne le nombre de clefs dans `D`
* `D[clef]` retourne la valeur pour la clef
* `D[clef] = x` change la valeur pour la clef
* `del D[clef]` supprime la clef et la valeur
* `clef in D` teste l’existence de `clef` dans `D`
* `clef not in D` teste la non existence
* `D.copy()` *shallow copy* de `D`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

D = {'alice': 35, 'bob' : 9, 'charlie': 6}
D
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# combien d'entrées

len(D)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

D['alice']
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# appartenance = est-ce une clé ?
'bob' in D
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

D['jim'] = 32
D
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# on n'avait pas encore vu cet opérateur..

del D['jim']
D
```

### `D.get()`

notez bien que `D[clef]` lance **une exception** si la clé n'est pas présente  
une alternative - sans exception - est d'utiliser la méthode `get()`

* `D.get(cle)` retourne la valeur associée à la clé si elle est présente, `None` sinon
* `D.get(clef, un_truc)` retourne `un_truc` quand la clé n'est pas présente

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# la clé 'marc' n'est pas présente

# plutôt que cette vilaine circonlocution...

try:
    x = D['marc']
except KeyError as e:
    x = "?"

x
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# c'est quand même plus lisible comme ça:

D.get('marc', '?')
```

+++ {"tags": ["gridwidth-1-2"]}

### itération sur un dictionnaire

* `D.items()` retourne **une vue** sur les (clef, valeur) de `D`
* `D.keys()` retourne une vue sur les clefs de `D`
* `D.values()` retourne une vue sur les valeurs de `D`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# l'idiome pour itérer sur
# un dictionnaire

for k, v in D.items():
    print(f"{k=} {v=}")
```

````{admonition} itérer sur le dictionnaire ?

on peut aussi itérer directement sur le dictionnaire, qui est équivalent à itérer sur `d.keys()`

```python
for k in D:
    # c'est légal, on itère sur les clés
    print(k)
```

c'est à rapprocher d'ailleurs du comportement de l'opérateur `in` sur le dictionnaire, voir plus haut
````

+++ {"tags": ["level_advanced"]}

### qu’est-ce qu’une vue ?

* c’est un objet qui donne une vue **dynamique** sur un dictionnaire `D`
* i.e. qui "suit" les changements futurs
* par oppposition à: on calculerait les propriétés de D à cet instant

```{code-cell} ipython3
:tags: [level_advanced, gridwidth-1-2]

clefs = D.keys()

clefs
```

```{code-cell} ipython3
:tags: [level_advanced, gridwidth-1-2]

# ici clefs est une vue
del D['bob']

clefs
```

### méthodes sur les dictionnaires

ici à nouveau, il y a [plein d'autres méthodes très utiles, à découvrir ici](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

+++ {"cell_style": "center", "tags": ["level_intermediate"]}

### création automatique de valeurs (avancé)

* utile pour alléger votre code  
  si vous savez que vos valeurs seront toujours, par exemple, une liste

* `collections.defaultdict` est une sous-classe de `dict`  
  qui ne **lève pas d'exception** en cas de défaut de la clé  
  mais dans ce cas va créer, toujours par exemple, une liste vide

* ce qui évite de devoir tester la présence de la clé

```{code-cell} ipython3
:cell_style: center
:tags: [level_intermediate]

from collections import defaultdict

# ici je décide que les valeurs sont des listes
dd = defaultdict(list)

# pas d'exception alors que la clé 0 est absente
# au contraire on appelle list() pour l'initialiser
dd[0].append(1)
dd[0].append(2)
dd[0]
```

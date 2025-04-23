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
  title: "r\xE9f\xE9rences partag\xE9es"
---

# références partagées

pour visualiser le comportement de nos programmes, et notamment cet aspect de partage de la mémoire  
nous allons utiliser des illustrations produites par l'excellent <https://pythontutor.com>

```{code-cell} ipython3
%load_ext ipythontutor
```

## composition des types de base

* tous ces containers peuvent être imbriqués  
  liste de dictionnaires de …

* donc ils peuvent être composés sans limite
* uniquement votre faculté à vous y retrouver  
  (enfin, vous et ceux qui vous lisent …)

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
%%ipythontutor heapPrimitives=true curInstr=1 width=900 height=850

# une liste avec une sous-liste qui contient un dict et un tuple
L = ['abc', [ { (1, 2) : 1}, ([3], 4)], 5]
```

## typage dynamique

* si on exécute `a = 3`
* Python va
  * créer un objet représentant 3
  * créer une variable `a` si elle n’existe pas encore  
    (une entrée dans une table)

  * faire de `a` une **référence** de l’objet (ou vers l'objet, si vous préférez)

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
%%ipythontutor heapPrimitives=true width=800 curInstr=1
a = 3
```

## références partagées

du coup on peut **facilement** avoir **plusieurs variables** qui référencent le **même** objet

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
%%ipythontutor heapPrimitives=true width=800 curInstr=2

# on aurait pu écrire aussi
# a = b = 3
a = 3
b = a
```

## rappel : mutable *vs* immutable

les entiers, les chaines, les tuples sont `immutables`

* ils ne **peuvent pas** être modifiés
* il n’y a **pas d’effet de bord** possible sur un objet immutable
* il est impossible qu’une modification sur `b` affecte `a`

+++

### références partagées vers objet immutable

````{admonition} b += 1
:class: warning

du coup dans notre exemple, si je faisais à présent `b += 1`, et contrairement à ce que vous pourriez penser 
si vous avez fait du C++, on se retrouverait avec `b` qui vaut 4 et `a` qui vaut toujours 3 !
````

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
%%ipythontutor heapPrimitives=true width=800 curInstr=1

a = 3
b = a
b += 1
```

### idem avec objet mutable

on prend de nouveau deux références vers le même objet  
mais que se passe-t-il si l’objet est mutable ? eh bien il peut **être changé**  
et alors cela impacte **toutes** les références vers cet objet  
que ce soit depuis une variable, ou depuis l'intérieur d'un autre objet

```{code-cell} ipython3
---
cell_style: center
lines_to_next_cell: 2
slideshow:
  slide_type: slide
---
%%ipythontutor heapPrimitives=true width=800 height=300 curInstr=1
a = [1, 2]
b = a
# en changeant a on change b
a[0] = 'spam'
```

+++ {"slideshow": {"slide_type": ""}}

### types mutables / immutables

| type  | mutable ? |
|-------:|:-----------|
| **`int`** et autres nombres | non       |
| **`str`** | non |
| **`list`** | **mutable** |
| **`tuple`** | non |
| **`dict`** | **mutable** |
| **`set`** | **mutable** |
| **`frozenset`** | non |

+++ {"slideshow": {"slide_type": ""}}

````{admonition} rappel

les types `tuple` et `frozenset` permettent notamment de construire des **clés** pour les dictionnaires et ensembles

````

+++

## *shallow* et *deep* copies

la solution pour ne pas modifier `b`: faire une **copie** de `a`  
il y a deux types de copies en Python:

* la *shallow copy* (superficielle)
  * pour les toutes les séquences, utiliser simplement `a[:]`
  * pour les dictionnaires utiliser `D.copy()`
  * sinon, utiliser le module `copy.copy()`
* la *deep copy* (profonde)
  * `copy.deepcopy()` pour tout copier de manière récursive

+++

### différence

* la différence entre *shallow* et *deep* copy n’existe que pour les  
  objets composites (les objets qui contiennent d’autres objets)

* ***shallow copy***: crée un nouvel objet composite et y insère  
  les **références** vers les objets contenus dans l’original

* ***deep copy***: crée un nouvel objet et insère de **manière récursive**  
  une copie des objets trouvés dans l’original  
  évite les boucles infinies

+++

### exemple d'utilisation de *shallow copy*

```{code-cell} ipython3
---
cell_style: center
slideshow:
  slide_type: slide
---
%%ipythontutor heapPrimitives=true height=400 width=800 curInstr=1

# comme ci-dessus
a = [1, 2]

# mais cette fois-ci on (shallow) copie d'abord
b = a[:]

# b n'est pas modifié
a[0] = 'spam'
```

````{admonition} remarque

dans ce cas de figure, la donnée de départ n'est pas assez profonde pour qu'il puisse y avoir une différence entre les deux modes de copie
````

+++ {"tags": ["gridwidth-1-2"]}

### illustration *shallow*

```{image} ../media/copy-1-shallow.svg
:align: center
:width: 500px
```

+++ {"tags": ["gridwidth-1-2"]}

### illustration *deep*

```{image} ../media/copy-2-deep.svg
:align: center
:width: 500px
```

+++ {"slideshow": {"slide_type": "slide"}, "cell_style": "center"}

### rappel: `is` et `==`

+++ {"tags": ["gridwidth-1-2"]}

* `obj1 is obj2`
  * ssi obj1 et obj2 sont **le même objet**
  * forme inverse: `obj1 is not obj2`

+++ {"tags": ["gridwidth-1-2"]}

* `obj1 == obj2`
  * ssi **les valeurs des objets sont égales**
  * forme inverse `obj1 != obj2`

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
a = [0, 1, 2]
b = a[:]
a is b
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

a == b
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

c = d = [0, 1, 2]
c is d
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

c == a
```

+++ {"slideshow": {"slide_type": "slide"}}

### copie profonde nécessaire ?

voyons maintenant un cas où la donnée de départ est -un peu - plus profonde, maintenant ça fait une différence de choisir l'une ou l'autre copie

```{code-cell} ipython3
---
cell_style: center
slideshow:
  slide_type: '-'
---
%%ipythontutor heapPrimitives=true height=450 width=800 curInstr=1

# cette fois a est un peu plus profond
a = [1, [2]]
# si on ne fait qu'une copie 'shallow'
b = a[:]
# on peut toujours modifier b à travers a
a[1][0] = 'boom'

print(a)
print(b)
```

```{code-cell} ipython3
:cell_style: center
:slideshow: {}

%%ipythontutor heapPrimitives=true height=500 width=900 curInstr=2
import copy
a = [1, [2]]
# maintenant avec une copie profonde: on n'a plus de souci
b = copy.deepcopy(a)
a[1][0] = 'boom'
print(a)
print(b)
```

## autres types de références partagées (avancé)

on n'a parlé jusqu'ici que de références partagées créées par **affectation**  
**mais** il existe (plein) d'autres cas de figure :

* appel de fonction: l'objet passé en argument à une fonction  
  se retrouve affecté au **paramètre** dans la **fonction**

* se méfier aussi des références **entre objets**

+++ {"slideshow": {"slide_type": "slide"}}

### appel de fonction

```{code-cell} ipython3
%%ipythontutor
L = [1, 2, 3]

def foo(x):
    x[1] = 'BOOM'

foo(L)
print(L)
```

+++ {"tags": ["level_intermediate"]}

### références entre objets

toutes les parties d'objet qui sont atteignables à partir d'autres objets peuvent devenir des références partagées  
pas besoin qu'il y ait nécessairement plusieurs variables dans le paysage  
on peut le voir sur l'exemple pathologique suivant

```{code-cell} ipython3
---
cell_style: center
slideshow:
  slide_type: slide
tags: [level_intermediate]
---
%%ipythontutor heapPrimitives=true height=400 width=900 curInstr=1

repete = 4 * [[0]]
print(f"repete avant {repete}")

repete[0][0] = 1
print(f"repete après {repete}")
```

+++ {"tags": ["level_advanced"]}

### structures cycliques

ainsi on peut aussi créer des structures cycliques

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [level_advanced]
---
%%ipythontutor

L = [None]
L[0] = L
print(L)
```

+++ {"tags": ["level_advanced"]}

## gestion de la mémoire (avancé)

* Python sait réutiliser les objets  
  *e.g.* les petits entiers - slide suivant

* Python sait libérer les objets non utilisés (garbage collector)
  * un objet sans référence est libéré
  * contrôle via le module `gc`
* chaque objet contient deux champs dans l’entête
  * un champ désignant le typage - cf `type(obj)`
  * un champ contenant un compteur de références  
    voir `sys.getrefcount(obj)`

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_advanced"]}

### optimisation interne à Python

```{code-cell} ipython3
:tags: [level_advanced, gridwidth-1-2]

# avec cette forme
# on crée deux objets liste
L = [1, 2]
M = [1, 2] # nouvel objet liste
L is M
```

```{code-cell} ipython3
:tags: [level_advanced, gridwidth-1-2]

# ici aussi on pourrait penser
# créer deux objets int
I = 18
J = 18   # nouvel objet entier ?
I is J   # non: partage
         # (optimisation)
```

+++ {"tags": ["level_advanced"]}

est-ce que ça pose un problème ?  
non ! l’optimisation n’est que pour des types **immutables**

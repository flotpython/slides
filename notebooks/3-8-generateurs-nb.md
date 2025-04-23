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
  title: "les g\xE9n\xE9rateurs"
---

+++ {"slideshow": {"slide_type": ""}}

# itér.. (3/3) - générateurs

+++ {"slideshow": {"slide_type": "slide"}}

## résumé

+++

ce qu'on a vu jusqu'ici pour faire des boucles en Python

* itérations 1/3
  - la boucle `for` sur les types de base / containers (`list`, `set`, `dict`)
  - combinatoires usuelles: `range`, `itertools` ...

* itérations 2/3
  - compréhensions (de liste, d'ensemble, de dictionnaire)
  - expressions génératrices: itération "paresseuse"

le sujet de ce dernier notebook sur les itérations, ce sont les **fonctions génératrices**

````{admonition} raccourci de langage

techniquement, comme on va le voir tout de suite, le terme *générateur* est applicable à la fois aux **expressions** génératrices et aux **fonctions** génératrices  
toutefois bien souvent quand on dit simplement *générateur* on veut dire en fait **fonction** génératrice
````

+++

## à quoi ça sert ?

en gros, la fonction génératrice va nous permettre de faire

- le même genre de choses qu'une expression génératrice (au sens: **itération paresseuse**)
- mais avec des **possibilités élargies** - voir notre premier exemple, la suite de Syracuse
- et du coup avec une syntaxe qui n'a plus rien à voir avec la compréhension:
  une fonction génératrice ressemble beaucoup .. à une fonction normale (d'où le nom évidemment)

+++

## exemple: la suite de Syracuse

il s'agit d'une suite ultra-classique de nombres (voyez aussi wikipedia ou autres): on se fixe $n$ et on pose

$$
u_0 = n\\
u_{n+1} = u_n / 2 \hspace{1cm}si\ u_n\ pair  \\
u_{n+1} = 3* u_n + 1 \hspace{1cm}si\ u_n\ impair 
$$

on conjecture que toutes les suites de Syracuse atteignent 1  
quoi qu'il en soit, ce qui est sûr c'est que si elle atteint 1, elle va "boucler" avec 1, 4, 2, 1, ...

```{code-cell} ipython3
# voici comment on pourrait implémenter cela en Python
# avec un fonction génératrice

def syracuse(n):
    current = n
    yield n
    while True:
        if current % 2 == 0:
            current = current // 2
            yield current
        else:
            current = 3 * current + 1
            yield current
        # bon ici on aurait pu faire autrement, par exemple
        # en faisant plutôt while current != 1
        # mais j'en profite pour bien illustrer 
        # la différence entre yield et return
        if current == 1:
            return
```

### c'est une fonction génératrice

comme vous le voyez cette **fonction génératrice** ressemble à une fonction *normale*  
.. sauf qu'**elle contient ces instructions `yield`** que l'on n'a pas encore rencontrées

````{admonition} comment savoir si une fonction est génératrice ?
en fait dès qu'une fonction **contient au moins un `yield`**, c'est une fonction génératrice
````

voyons maintenant comment on peut s'en servir...

+++

### dans un `for`

comment on s'en sert ? le premier usage consiste à utiliser le résultat dans un `for`:

```{code-cell} ipython3
for i in syracuse(4):
    print(i, end=" ")
```

mais bon, si on fait ça on peut avoir l'impression que la fonction renvoie une liste ou quelque chose comme cela  

c'est pourquoi on va inspecter les choses un peu plus en détail; commençons par appeler la fonction toute seule

```{code-cell} ipython3
# en fait quand je fais ça il ne se passe rien, ou presque

g = syracuse(4)
```

par exemple à ce stade, je ne peux pas savoir combien il y a d'éléments dedans  
pour la bonne raison qu'en fait on n'a pas encore commencé à calculer quoi que ce soit !!!

```{code-cell} ipython3
:tags: [raises-exception]

try:
    len(g)
except Exception as exc:
    print(f"{type(exc)}:  {exc}")
```

car oui, cet objet `g` est en fait de type `generator`; c'est exactement le même type qu'une expression génératrice:

```{code-cell} ipython3
# g a le même type que par exemple cette genexpr

genexpr = (x**2 for x in range(3))
type(g) is type(genexpr)
```

### c'est un itérateur

du coup comme pour les genexprs, notre objet `g` est un itérateur, et donc il s'épuise comme tous les itérateurs:

```{code-cell} ipython3
g = syracuse(4)
print("premier tour")
for i in g:
    print(i, end=" ")
print("\nsecond tour")
for i in g:
    print(i, end=" ")
```

### avec `next()`

et comme tous les itérateurs aussi, on peut le "faire avancer" pas à pas en utilisant `next()`, quitte à se protéger de la fin de la boucle avec `StopIteration`:

```{code-cell} ipython3
:lines_to_next_cell: 2

# pour 2 il n'y a que 2 termes dans la suite

g = syracuse(2)

print("le premier", next(g))
print("le deuxième", next(g))

# du coup ici ça va faire boom
# en levant l'exception prédéfinie StopIteration
try:
    next(g)
except StopIteration:
    print("pas de troisieme")
```

+++ {"slideshow": {"slide_type": "slide"}}

## expression génératrice *vs* fonction génératrice

+++ {"slideshow": {"slide_type": "slide"}}

### rappel: vocabulaire

* une expression génératrice `(expr(x) for x in iterable)`  
  retourne un objet de type `generator`

* l'appel à une fonction génératrice produit aussi un objet de type *generator*
* il est fréquent - par abus de langage - d'appeler aussi simplement *générateur*  
  une fonction génératrice

+++

### quand c'est simple

prenons un cas simpliste: on veut calculer les carrés d'une collection d'objets  
dans ce cas-là on peut utiliser n'importe laquelle des deux formes (genexpr ou générateur)

```{code-cell} ipython3
:cell_style: split

data = (2, -1, 4)
```

```{code-cell} ipython3
:cell_style: split

# ces deux façons de faire sont équivalentes

gen1 = (x**2 for x in data)
type(gen1)
```

```{code-cell} ipython3
:cell_style: split

def squares(iterable):
    for i in iterable:
        yield i**2

gen2 = squares(data)
type(gen2)
```

```{code-cell} ipython3
:cell_style: split

for x in gen1:
    print(x, end=" ")
```

```{code-cell} ipython3
:cell_style: split

for x in gen2:
    print(x, end=" ")
```

### quand ça se complique

par contre bien évidemment, ce serait un défi d'écrire `syracuse` avec une genexpr !

en fait la fonction génératrice apporte une **puissance d'expression** nettement supérieure  
et cela notamment car elle permet de **conserver l'état** de l'itération  
et en particulier les différentes variables locales, les paramètres, etc...

````{admonition} en termes d'implémentation
:class: admonition-small

pour les curieux: cela signifie que le langage doit "mettre au freezer" (des morceaux de) la pile d'exécution entre deux `next()`; incidemment c'est ce trait qui a permis de développer ensuite la programmation asynchrone avex la librairie `asyncio`; mais c'est une autre histoire complètement...
````

+++ {"slideshow": {"slide_type": "slide"}}

## exercice

comme avec `itertools.count()`, on peut imaginer un générateur infini
1. implémentez un générateur qui parcourt tous les nombres premiers
2. comment l'utiliser pour obtenir le n-ième nombre premier ?

+++

````{admonition} le reste est pour les avancés

en première lecture vous pouvez vous arrêter ici
````

+++

## `yield from`

une fonction génératrice est une fonction  
donc elle peut appeler d'autres fonctions  
qui peuvent elles-mêmes être des fonctions génératrices...

+++

### parcours d'arbre

pour bien le voir, prenons un *use case* très usuel, le cas du parcours d'un arbre en profondeur d'abord

pour rappel, dans un style de programmation "usuel" ce parcours s'écrit tout simplement

```{code-cell} ipython3
# un parcours d'arbre itératif

def scanner(tree, depth=0):
    if isinstance(tree, list):
        for child in tree:
            scanner(child, depth+1)
    else:
        # do something with the leaf
        print(f"{depth=} leaf={tree}")
```

```{code-cell} ipython3
# que l'on utilise comme ceci

tree = [0,  [1, 2], [ [3, 4], [5, 6]]]

scanner(tree)
```

maintenant on voudrait avoir la même chose, mais sous la forme d'un itérateur  
sauriez-vous le faire de votre coté sans regarder la suite ? 

````{admonition} on peut le faire avec ce qui précède
:class: seealso

c'est réalisable uniquement avec ce qu'on a vu avant  
toutefois vous allez voir il y a un moment où c'est un peu *awkward*...
````

+++

voici une première façon de faire

```{code-cell} ipython3
def iter_scan(tree, depth=0):
    if isinstance(tree, list):
        for child in tree:
            for x in iter_scan(child, depth+1):
                yield x
    else:
        yield depth, tree

for depth, leaf in iter_scan(tree):
        print(f"{depth=} {leaf=}")
```

mais vous voyez que la double boucle `for child in ...: for x in ...`  
est un peu bizarre, si on compare avec le code qu'on avait écrit en premier

pour ce genre d'usage, on a à notre disposition une instruction `yield from` qui va faire le travail de manière beaucoup plus élégante; voici ce que ça donne si on l'utilise

```{code-cell} ipython3
def iter_scan2(tree, depth=0):
    if isinstance(tree, list):
        for child in tree:
            yield from iter_scan(child, depth+1)
    else:
        yield depth, tree

for depth, leaf in iter_scan2(tree):
        print(f"{depth=} {leaf=}")
```

remarquez que cette version du code ressemble déjà beaucoup plus au code d'origine !

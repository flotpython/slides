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
  title: enums & dataclasses
---

# enums et dataclasses

(et namedtuples)

dans ce notebook nous allons découvrir - très rapidement - quelques façons de créer rapidement des classes qui répondent à des besoins spécifiques

+++

## `enums`

la notion de classe énumérée est à rapprocher de la notion de catégorie en pandas, c'est-à-dire un type qui peut prendre un nombre fini, et généralement petit, de valeurs.

```{code-cell} ipython3
# un tout petit exemple de classes énumérées

from enum import Enum, IntEnum, auto

class Color(Enum):
    HEARTS = '♡'
    CLUBS = '♧'
    DIAMONDS = '♢'
    SPADES = '♤'
    
    def __format__(self, spec):
        return format(self.value, spec)
        
    
class Value(IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    # you get the picture...
    
    def __format__(self, spec):
        return format(self.value, spec)
```

```{code-cell} ipython3
# la classe se comporte comme un itérable
for color in Color:
    print(color, f"{color}")
```

```{code-cell} ipython3
from itertools import product
for value, color in product(Value, Color):
    print(f"{value}of{color}", end=" ")
```

```{code-cell} ipython3
# et si on a précisé le type IntEnum on peut utiliser les valeurs comme des entiers
Value.ONE <= Value.TWO
```

### pour en savoir plus

ceci est un rapide aperçu, pour plus de détails voyez cette page  
<https://docs.python.org/3/library/enum.html>

+++

(label-dataclasses)=
## `dataclass`

les dataclasses sont conçues pour pouvoir créer facilement des classes de type 'enregistrement', c'est-à-dire lorsqu'un objet contient simplement quelques attributs de données

```{code-cell} ipython3
# un petit exemple de dataclass

from dataclasses import dataclass

# cette fois l'outil de confort se préseten sous la forme d'un décorateur

@dataclass
class Vector:
    x: float
    y: float = 0.
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
```

```{code-cell} ipython3
# on a gratuitment le constructeur et la représentation

v = Vector(12)
v
```

```{code-cell} ipython3
# et d'autres trucs pratiques comme la comparaison ==

Vector(8) + Vector(4, 12) == Vector(12, 12)
```

### les réglages disponibles

on voit donc que la classe obtenue a été remplie automatiquement, du moins en partie - 
par exemple ici le constructeur et l'afficheur ont été écrits pour nous

à savoir: on peut agir sur l'ensemble des méthodes spéciales "automatiques", en passant au décorateur différentes options  
par exemple on peut lui demander de rendre nos objets comparables:

```{code-cell} ipython3
# cette fois on veut des objets comparables

@dataclass(order=True)
class Vector:
    x: float
    y: float = 0.
```

```{code-cell} ipython3
# par contre c'est rustique - ici ordre lexicographique...

v1, v2 = Vector(2, 4), Vector(3, 1)
v1 <= v2
```

### pour en savoir plus

de nouveau pour approfondir, voyez cette page  
<https://docs.python.org/3/library/dataclasses.html>

+++

## `namedtuple`

dans une veine similaire, on peut citer également la notion de `namedtuple`, exposée par le module `collections`  
comme son nom l'indique, il permet de fabriquer des objets qui se comportent comme des tuples, mais dans lesquels les différents éléments sont nommés  
ou si vous préférez, qui se comportent comme des objets, mais qu'on peut aussi accéder comme des tuples :)

```{code-cell} ipython3
from collections import namedtuple

# on fabrique une classe comme ceci
Person = namedtuple("Person", ('name', 'age'))
```

```{code-cell} ipython3
# on l'utilise comme une classe usuelle

p1 = Person("jean", 32)
p1
```

```{code-cell} ipython3
# au travers de ses attributs

p1.name
```

```{code-cell} ipython3
# sauf que ça peut s'utiliser **aussi** comme un tuple

p1[0]
```

```{code-cell} ipython3
# vraiment comme un tuple, donc unpacking disponible

n, a = p1
n
```

### pour en savoir plus

plus de détails ici  
<https://docs.python.org/3/library/collections.html#collections.namedtuple>

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
  title: librairies utiles
---

# la librairie standard

le tutorial Python sur ce sujet occupe à lui tout seul deux chapitres: [chapitre 10](https://docs.python.org/3/tutorial/stdlib.html) et [chapitre 11](https://docs.python.org/3/tutorial/stdlib2.html)  
le spectre est très très complet, je fais ici un tri totalement arbitraire...

+++ {"slideshow": {"slide_type": ""}}

Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

## `logging`

dans du code de production on ne fait jamais `print()` ! on utilise à la place `logging`, car de cette façon:

* le code a seulement à choisir un **niveau** de message parmi `exception`, `error`, `warning`, `info`, `debug`
* on pourra **choisir plus tard** (i.e. par l'équipe Ops) :
  * **si** on veut les messages (avec quel niveau de gravité, et depuis quels modules)
  * **où** doivent aller les messages (`/var/log`, *syslog*, *stdout*, ...)

```{code-cell} ipython3
# voici comment configurer logging pour avoir un comportement 'à la' print

import logging
logging.basicConfig(level=logging.INFO)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# au lieu de faire 

print(f"Bonjour le monde") 
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# on fera plutôt

logging.info("Bonjour le monde")
```

```{code-cell} ipython3
# ou encore 

logging.error("OOPS")
```

## `sys` et `os`

sont utilisés très fréquemment, surtout dans du code ancien, pour

* `import sys`  
  * gestions de variables utilisées par l’interpréteur
  * e.g. `sys.path`, et plein plein d'autres dans ce module un peu fourre-tout
* `import os`
  * accès cross-platform au système d’exploitation
    ````{admonition} os n'est plus vraiment utile
    notez toutefois que ses usages principaux ont été remplacés:
    -  par `pathlib` pour les fichiers (voir slide suivant)
    - par `subprocess` pour lancer des sous-processes
    ````

+++

## `from pathlib import Path`

( ~~`import os.path`~~)

historiquement on gérait les noms de fichiers sur disque avec le sous-module `os.path`  
mais depuis la 3.4 une alternative **orientée objet** est disponible! 

````{admonition} n'utilisez plus os.path !

il **faut utiliser `pathlib.Path`** pour du nouveau code ! on peut tout faire avec:

* chercher (`glob`) tous les fichiers en `*.truc`
* calculer les noms de fichier: concaténer, découper en morceaux, trouver le nom canonique
* ouvrir les fichier
* accéder aux métadata (taille, date, ..)
* etc...
````

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
from pathlib import Path

for path in Path(".").glob("samples/*.py"):
    # le nom canonique
    print(10*'=', path.absolute())
    # le dernier morceau dans le nom
    print(path.name, end=' ')
    # la taille
    print(path.stat().st_size, 'bytes')
    # touver le nom absolu
    # ouvrir le fichier en lecture
    with path.open():
        pass
```

+++ {"slideshow": {"slide_type": "slide"}}

````{admonition} orienté objet

avec `pathlib`, les calculs de chemin se font **directement à base de l'opérateur `/`**
````

```{code-cell} ipython3
# c'est très facile de se promener dans l'arbre des fichiers

répertoire = Path(".")
fichier = répertoire / "samples" / "fib.py"

with fichier.open() as feed:
    for lineno, line in enumerate(feed, 1):
        print(f"{lineno}:{line}", end="")  
```

+++ {"slideshow": {"slide_type": "slide"}}

## `datetime`, `math` et `random`

+++ {"slideshow": {"slide_type": ""}}

### `datetime`

* gestion des dates et des heures

+++ {"slideshow": {"slide_type": ""}}

### `math`

* fonctions mathématiques, constantes, ...

+++ {"slideshow": {"slide_type": ""}}

### `random`

* générations de nombres et séquences aléatoires, mélange aléatoire de séquences

+++ {"slideshow": {"slide_type": "slide"}}

## formats de fichier

+++

### `json`

* sérialisation d’objets python, standard du web
* envoi et réception depuis toutes sources compatibles json

+++

### `csv`

* ouverture fichier csv, compatible Excel et tableurs

+++

### `pickle`

* sérialisation d’objets python, uniquement compatible avec python
* sauvegarde et la chargement du disque dur

+++ {"slideshow": {"slide_type": "slide"}}

## le module `collections`

une extension des objets *built-in* `list`, `tuple`, `dict`  
[la doc est ici](https://docs.python.org/3/library/collections.html), voici une petite sélection

+++ {"slideshow": {"slide_type": "slide"}}

###  `collections.Counter()`

à partir d'un itérable, construit un dictionnaire qui contient

* comme clefs les éléments uniques
* et comme valeurs le nombre de fois que l’élément apparaît

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
from collections import Counter

cnt = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
cnt
```

```{code-cell} ipython3
isinstance(cnt, dict)
```

```{code-cell} ipython3
# par exemple pour compter les mots dans un texte

import re
words = re.findall(r'\w+', open('../data/hamlet.txt').read().lower())

Counter(words).most_common(10)
```

### `collections.defaultdict()`

* étend les dictionnaires pour en faciliter l’initialisation
* <https://docs.python.org/3/library/collections.html?#collections.defaultdict>

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
from collections import defaultdict

# on va fabriquer un dict    word -> liste d'indices où il apparait
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

# pour cela on indique que les valeurs sont des listes
d = defaultdict(list)

# si on écrit une clé qui n'est pas encore présente
# d[k] vaut alors list()
# c'est-à-dire une liste vide est crée automatiquement
for k, v in s:
    d[k].append(v)

sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
```

## `itertools` - combinatoire

* implémente sous forme efficace (itérateurs)
* des combinatoires classiques
* et autres outils utiles pour écrire des boucles concises
* [la doc](https://docs.python.org/3/library/itertools.html)
* déjà abordé dans la partie 3.3 sur les itérateurs

fournit les combinatoires communes

* [`produit cartésien`](https://docs.python.org/3/library/itertools.html#itertools.product)
* [`permutations`](https://docs.python.org/3/library/itertools.html#itertools.permutations)
* [`combinaisons`](https://docs.python.org/3/library/itertools.html#itertools.combinations) *n* parmi *p*

+++ {"slideshow": {"slide_type": "slide"}}

### `itertools` - produit cartésien

```{code-cell} ipython3
from itertools import product
A = ['a', 'b', 'c']
B = [ 1, 2]

for x, y in product(A, B):
    print(x, y)
```

+++ {"slideshow": {"slide_type": "slide"}}

### `itertools` - permutations

```{code-cell} ipython3
from itertools import permutations
C = ['a', 'b', 'c', 'd']

for tuple in permutations(C):
    print(tuple)
```

+++ {"slideshow": {"slide_type": "slide"}}

### `itertools` - combinaisons

```{code-cell} ipython3
from itertools import combinations
miniloto = list(range(5))

for a, b in combinations(miniloto, 2):
    print(a, b)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# les arrangements ne sont pas disponibles tel-quel
# mais une possibilité est de générer toutes les permutations
# de chaque tirage dans les combinaisons

def arrangements(collection, n):
    for tuple_ in combinations(collection, n):
        yield from permutations(tuple_)

for t in arrangements(miniloto, 2):
    print(t)
```

+++ {"slideshow": {"slide_type": ""}}

### module `itertools` - divers

* parfois sans fin
  * `count(10) --> 10 11 12 13 14 ...`
  * `cycle('abcd') --> a b c d a b c d ...`
* ou pas
  * `islice('abcdefg', 2, none) --> c d e f g`
  * `repeat(10, 3) --> 10 10 10`

+++ {"slideshow": {"slide_type": "slide"}}

### module `itertools` - suite

* chainer plusieurs itérations
  * `chain('ABC', 'DEF') --> A B C D E F`
  * `chain.from_iterable(['ABC', 'DEF']) --> A B C D E F`

* avec un peu de logique
  * `takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4`
  * `dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1`
  * `compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F`
  * `filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8`

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
from itertools import filterfalse
```

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
%timeit -n 100 for x in filterfalse(lambda x:x%2, range(10000)): pass
```

```{code-cell} ipython3
%timeit -n 100 for x in (y for y in range(10000) if not (y % 2)): pass
```

+++ {"slideshow": {"slide_type": "slide"}}

## `operator`

* en python tout est un objet, on peut donc tout passer à une fonction, mais comment passer un opérateur comme `+`, `in`, ou `>` 
* le module `operator` contient la version fonctionnelle d’un grand nombre d’opérateurs python

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
import random
l = [('a', random.randint(1, 1000)) for i in range(100)]
l.sort(key=lambda x: x[1])
l[-7:]
```

```{code-cell} ipython3
l = [('a', random.randint(1, 1000)) for i in range(100)]
import operator
l.sort(key=operator.itemgetter(1))
l[-7:]
```

````{admonition} et plein d'autres

à nouveau cette présentation est **loin d'être exhaustive**, n'hésitez pas à aller farfouiller par vous-même en fonction de vos besoins...

````

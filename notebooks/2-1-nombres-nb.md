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
  title: nombres
---

+++ {"slideshow": {"slide_type": "slide"}}

# les nombres

les types de base pour les nombres sont:`int`, `float`, `complex`, `bool`

+++ {"slideshow": {"slide_type": "slide"}}

## les entiers

* les `int` ont une précision illimitée
  * Python peut calculer nativement

```{code-cell} ipython3
92857234957203457234572203957 * 948572349572039457029347529347
```

ceux qui ont eu à faire ça en C apprécieront

+++ {"slideshow": {"slide_type": "slide"}}

### nombres : division

les opérations usuelles ne posent pas de souci, c'est bien sûr `+` `-` `*` avec `(` et `)`  
mais la division mérite quelques mots:

```{code-cell} ipython3
:tags: [gridwidth-1-3]

# division exacte/flottante
8 / 5
```

```{code-cell} ipython3
:tags: [gridwidth-1-3, gridwidth-1-2]

# division entière (quotient)
8 // 5
```

```{code-cell} ipython3
:tags: [gridwidth-1-3, gridwidth-1-2]

# reste div. entière
8 % 5
```

+++ {"slideshow": {"slide_type": "slide"}}

### nombres : opérateurs

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# bcp d'autres opérations disponibles
# et notamment:

2 ** 32         # puissance
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# tous les opérateurs peuvent être utilisés
# pour faire un effet de bord comme ceci

x = 10
x += 2
x
```

````{admonition} une cheatsheet

à bookmarker: [une cheat sheet avec la liste des opérateurs en Python](https://cheatography.com/nouha-thabet/cheat-sheets/python-operators-and-booleans/)

````

+++ {"slideshow": {"slide_type": "slide"}}

### conversions

```{code-cell} ipython3
int(234.5)      # cast float ➔ int
```

````{admonition} à retenir !

un **type** en Python est aussi une **usine à objets**,  
il peut être utilisé comme une fonction  
ici l'appel `int(234.5)` consiste à appeler le type `int`  
pour fabriquer un objet,  de type `int` donc, à partir de la valeur `234.5`
````

+++

````{admonition} moins crucial
:class: tip admonition-small

il existe aussi des fonctions `floor()` et `ceil()` dans le module `math`  
toutefois la méthode ci-dessus est plus générale, elle s'applique à tous les types en Python
````

+++ {"slideshow": {"slide_type": "slide"}}

### nombres complexes

```{code-cell} ipython3
:tags: [gridwidth-1-3]

# pour écrire un complexe
# il faut utiliser j et non pas i

1j * 1j
```

```{code-cell} ipython3
:tags: [gridwidth-1-3]

a = 3 + 4j

# partie réelle
a.real
```

```{code-cell} ipython3
:tags: [gridwidth-1-3]

# partie imaginaire
a.imag          
```

````{admonition} les attributs, encore..

remarquez qu'ici à nouveau, le terme `a.real` consiste à rechercher l'**attribut** `real` dans l'objet (désigné par) `a`
````

+++ {"slideshow": {"slide_type": "slide"}}

### le module `math`

```{code-cell} ipython3
:tags: []

# pour anticiper un peu
# sur les listes...
# ici on veut les 6 derniers
# symboles dans le module math

import math

dir(math)[-6:]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

math.tau
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

math.sin(math.pi)
```

````{admonition} exo: entrainez-vous à chercher dans google

entraînez vous à trouver rapidement la doc de ce module dans google en cherchant par exemple "`python module math`"

<https://www.google.com/search?q=python+module+math>

+++

````{admonition} décortiquons un peu
:class: admonition-small seealso

après l'import, la variable `math` désigne donc un objet de type `module`  
et à nouveau, l'écriture `math.tau` consiste à rechercher l'attribut `tau` dans cet objet module  
et pareil exactement pour `math.sin`, qui désigne … un objet fonction
````

+++ {"slideshow": {"slide_type": "slide"}}

## booléens

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# il y a aussi le type booléen

10 <= 12
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# avec comme valeurs True et False

10 >= 12
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# True c'est presque exactement 1

True == 1
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et False presque exactement 0

False == 0
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# mais pas tout à fait quand même

type(True)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# alors que

type(1)
```

### opérateurs sur les booléens

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# tout simplement avec les mots-clé and, or, et not

x = 10

(8 <= x) and (x <= 12)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# cela dit dans ce cas-là on peut écrire
# de manière plus simple

8 <= x <= 12
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pour tester l'égalité (on en a déjà parlé)

x == 10
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pour tester l'inégalité

x != 10
```

### opérateurs `is` et `in`

* `is` permet de savoir si deux objets sont **le même objet** - c'est-à-dire correspondent à la même adresse en mémoire
* `in` permet de savoir si un objet **fait partie** d'un autre objet

avec ces deux opérateurs, le `not` permet des syntaxes plutôt lisibles

* `x is not y`
* `x not in y`

voyons cela sur un exemple
vous vous souvenez de l'exemple avec les deux objets liste ?

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# ici on crée deux objets liste distincts

# le premier (avec deux références)
a = b = [1, 2]
# le deuxième
c = [1, 2]
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
%load_ext ipythontutor
```

```{code-cell} ipython3
:cell_style: center

%%ipythontutor curInstr=2

a = b = [1, 2]
c = [1, 2]
```

+++ {"cell_style": "center", "slideshow": {"slide_type": "slide"}}

du coup on peut écrire des choses comme

```{code-cell} ipython3
:tags: [gridwidth-1-2]

a is b
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# plus lisible que   not (a is c)
a is not c
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

a == c
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

a != c
```

+++ {"slideshow": {"slide_type": "slide"}}

ou encore comme

```{code-cell} ipython3
:tags: [gridwidth-1-2]

1 in a
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# plus lisible que   not (1 in a)
1 not in a
```

+++ {"slideshow": {"slide_type": "slide"}}

### test sur un booléen

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# on peut - bien sûr - faire un `if`
# (ou un while) sur un booléen
a = 3
b = 4

type(a == b)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ici le sujet du if est bien booléen

if a == b:
    print("pareils")
else:
    print("différents")
```

+++ {"slideshow": {"slide_type": "slide"}}

### test sur un non-booléen

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# mais aussi : avec n'importe quoi d'autre
# ici le sujet du if est un nombre

if a:
    print("pas faux")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# en fait équivalent à ceci:

if bool(a):
    print("pas faux")
```

````{admonition} valeurs "fausses" ?

les valeurs "fausses" correspondent à un **nombre nul**, ou à un **container vide** (liste, chaine, ..)
````

+++ {"slideshow": {"slide_type": "slide"}}

### tests sur une valeur non booléenne & conversion

+++

en fait ce qui est à l'oeuvre ici, c'est la **mécanique générale** pour convertir entre types de données:

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# si on appelle int() on convertit en entier

int(3.4)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# eh bien de la même manière
# si on appelle bool() on convertit en booléen

bool(3.4)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# un nombre nul est "faux"

bool(0)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# une chaine vide est "fausse"

bool("")
```

```{code-cell} ipython3
:lines_to_next_cell: 2
:tags: [gridwidth-1-2]

# un nombre non nul est "vrai"
bool(1)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# une chaine non vide - même avec 
# un seul espace - est "vraie"
bool(" ")
```

+++ {"slideshow": {"slide_type": "slide"}}

## l'encodage des flottants

+++

* représentés en machine comme des fractions en base 2
* le plus souvent une approximation
  * quand pas une fraction binaire exacte
* pas une spécificité de Python
  * IEE-754: [WikiPedia](https://en.wikipedia.org/wiki/IEEE_754) - [interactif **64bits**](http://www.binaryconvert.com/convert_double.html)

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
# flottant = imprécision structurelle !

0.1 + 0.2
```

+++ {"slideshow": {"slide_type": "slide"}}

### `float` = 64 bits

+++

* sur une machine 64 bits, un float est encodé en double précision, i.e. avec:
  * 1 bit de signe
  * 11 bits pour représenter l'exposant
  * 52 bits pour représenter la mantisse

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pour obtenir des infos sur la précision des flottants

import sys
sys.float_info
```

+++ {"tags": ["gridwidth-1-2"]}

````{admonition} à retenir
:class: info

sur 64 bits, l'erreur relative est de l'ordre de $10^{-15}$ / $10^{-16}$
````

+++ {"slideshow": {"slide_type": "slide"}}

### pas spécifique à Python

+++ {"cell_style": "center"}

* pas un problème spécifique à Python
* si vous ne faites pas de l’analyse numérique
  * ce problème n’a probablement aucun impact pour vous
* sinon, vous êtes déjà au courant
  * et vous savez notamment qu'il ne faut pas tester avec une égalité stricte
  * mais plutôt avec un *presque égal* : utiliser `math.isclose`

```{code-cell} ipython3
:lines_to_next_cell: 2
:tags: [gridwidth-1-2]

0.3 == 0.1 + 0.2
```

```{code-cell} ipython3
:lines_to_next_cell: 2
:tags: [gridwidth-1-2]

import math

math.isclose(0.3, 0.1+0.2)
```

+++ {"slideshow": {"slide_type": "slide"}}

### contournements

+++

##### pour contourner

* le [module `decimal`](https://docs.python.org/3/library/decimal.html), pour travailler sur des nombres décimaux
  * avec plus de précision et de contrôle qu’avec le type float
* le [module `fractions`](https://docs.python.org/3/library/fractions.html) permet de travailler sur des rationnels

+++ {"slideshow": {"slide_type": "slide"}}

### exemples - `decimal`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

from decimal import Decimal
x = Decimal('0.1') + Decimal('0.2')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

x == Decimal('0.3')
```

+++ {"slideshow": {"slide_type": "slide"}}

### exemples - `fractions`

```{code-cell} ipython3
:cell_style: center

from fractions import Fraction
x = Fraction(1, 10) + Fraction(2, 10)
x
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

x == Fraction(3, 10)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

x == 0.3
```

## plus exotique

+++ {"slideshow": {"slide_type": "slide"}}

### entrer un entier en hexa, binaire, octal

+++

pour créer des entiers sous forme littérale, dans d'autres bases

```{code-cell} ipython3
:tags: [gridwidth-1-3]

# hexadécimal
0xff
```

```{code-cell} ipython3
:tags: [gridwidth-1-3]

# binaire
0b11111111
```

```{code-cell} ipython3
:tags: [gridwidth-1-3]

# octal
0o377
```

+++ {"slideshow": {"slide_type": "slide"}}

### afficher un entier sous forme hexa, binaire, octale

+++

dans l'autre sens, trouver la représentation en base *n*  
sous forme de chaine de caractères du coup

```{code-cell} ipython3
:cell_style: center
:tags: [gridwidth-1-3]

hex(255)    # traduire en hexa (-> str)`
```

```{code-cell} ipython3
:cell_style: center
:tags: [gridwidth-1-3]

bin(255)    # traduire en binaire (-> str)
```

```{code-cell} ipython3
:cell_style: center
:tags: [gridwidth-1-3]

oct(255)    # traduire en octal (-> str)
```

````{admonition} fonctions prédéfinies ou *builtin*

remarquez que nous n'avons pas défini les variables `hex`, `bin` et `oct`  
ce sont des fonctions *prédéfinies*, connues de Python **dès le lancement**  
le terme anglais pour désigner de telles fonctions est *builtin*

````

+++ {"slideshow": {"slide_type": "slide"}}

### opérations *bitwise*

```{code-cell} ipython3
y = 4
y | 2      # bitwise OR de 0100 (4) et 0010 (2)
```

```{code-cell} ipython3
y & 2      # bitwise AND de 0100 (4) et 0010 (2)
```

```{code-cell} ipython3
y & 15     # bitwise AND de 0100 (4) et 1111 (15)
```

```{code-cell} ipython3
~ y        # bitwise NOT - en pratique ~x == -(x+1)
```

* rarement utile d’utiliser les opérations bitwise en Python usuel
* mais par contre **très utile** avec numpy et pandas  
  pour manipuler notamment les masques

+++ {"slideshow": {"slide_type": "slide"}}

### décalages

```{code-cell} ipython3
:tags: [gridwidth-1-2]

x = 3
y = x << 10 # décalage à gauche
y
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

2**11 + 2**10
```

```{code-cell} ipython3
x          # l'argument n'est pas modifié
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

y >> 3     # décalage à droite
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

2**8 + 2**7
```

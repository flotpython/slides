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
  title: "op\xE9rateurs"
---

# opérateurs

un survol des opérateurs pour construire les expressions

````{admonition} précédence des opérateurs
:class: attention

comme pour tous les langages, les opérateurs ont une précédence; dans le doute: mettez des parenthèses !
````

+++ {"cell_style": "center"}

Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

```{code-cell} ipython3
:lines_to_next_cell: 2

from IPython.display import HTML
HTML(filename="_static/style.html")
```

## rappels

* appel de fonction avec `()` comme dans `foo(0)`
* indexation avec `[]` comme dans `L[0]`
* attribut avec `.` comme dans `S.upper()`

+++

## arithmétiques

* arithmétiques:  `+` | `-` | `*` | `/`
  * pas que sur les nombres

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
'on peut juste juxtaposer' ' deux chaines'
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
'ou les' + ' additioner'
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
['et', 'les'] + ['listes', 'aussi']
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
4 * '-00-'
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
4 * [1, 2]
```

### dépendants du type

digression: tous les opérateurs du langage sont dépendants du type des opérandes

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
10 + 20
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
"10" + "20"
```

et comme on le verra, chaque type (y compris les classes qui sont des types définis par l'utilisateur) peut redéfinir le comportement des opérateurs

par exemple

* une classe `Vector` donnera du sens à `v1 + v2`
* une classe `Path` donnera du sens à `path / file`

+++

### quotient et reste `//` et `%`

* rappel division entière: quotient et reste: `//`  et `%`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# avec des entiers
19 // 3
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

19 % 3
```

+++ {"slideshow": {"slide_type": "slide"}}

### puissance `**`

+++

* $x^y$ : `x ** y`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

2 ** 100
```

## opérateurs logiques

* opérateurs logiques: `and` - `or` - `not`
* opérateurs d'appartenance: `in` et `not in`

+++

### comparaison

* comparaison: `==` et `is`  - déjà mentionnés
* négation: `!=` et `is not` respectivement

* comparaisons dans espaces ordonnés:
  * `>=`, `>`, `<=`, `<`
  * curiosité: on peut les chainer

```{code-cell} ipython3
:tags: [gridwidth-1-2]

def est_moyenne(note):
    return 10 <= note <= 12
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

est_moyenne(11)
```

+++ {"tags": ["gridwidth-1-2"]}

### évaluation paresseuse (avancé)

* `and` et `or` sont opérateurs *short-circuit*
  * on évalue les opérandes de gauche à droite
  * et **on s'arrête** dès que le résultat est connu

* A `and` B
  * Si A est `False`,  
    B ne sera pas évalué

* A `or` B
  * Si A est `True`,  
    B ne sera pas évalué

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
# une fonction avec side-effect
counter = 0

def greater(a, b):
    global counter
    counter += 1 
    return a >= b
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ceci n'imprime rien
note = 11.5

if (greater(note, 10) and greater(note, 12)
    and greater(note, 14) and greater(note, 16)):
    print("excellent")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ce qui intéressant, c'est 
# combien de fois on a appelé greater
counter
```

## opérateurs bitwise

* opérateurs dits *bitwise*:
  * `&` - `|` : **et** et **ou** logique, respectivement
  * `^` : **xor**
  * `~` : **not** 
* on les a aussi déjà rencontrés avec les ensembles

````{admonition} important pour `pandas`
:class: attention

ça semble anecdotique, mais ces opérateurs sont **super utilisés** notamment en pandas !
````

```{code-cell} ipython3
:tags: [gridwidth-1-2]

a = 0b111100 
b = 0b110011
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

bin(a | b)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

bin(a & b)
```

## POO : opérateurs redéfinis 

tous ces opérateurs peuvent être **redéfinis**

* c'est le propos des 'méthodes magiques' 
* que l'on verra à propos des classes
* exemple intéressant, la classe `Path`

+++ {"slideshow": {"slide_type": "slide"}}

### ex:  `/` sur la classe `Path`

```{code-cell} ipython3
# la classe Path nous a montré 
# un bel exemple d'opérateur redéfini 

from pathlib import Path
```

```{code-cell} ipython3
home = Path.home()

# l'opérateur / est défini sur Path
# et bien sûr ici CE N'EST PAS une division !

subdir = home / "git"

if subdir.exists():
    print(f"le répertoire {subdir} existe")
```

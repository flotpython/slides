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
  title: formatage et impressions
---

# formatage et impressions

+++

## formatage des chaînes : f-strings

+++

pour le formatage des chaines: utilisez les ***f-strings***, qui évitent les répétitions fastidieuses  
l'idée consiste à

* faire précéder la chaine par un `f`
* et embarquer directement dans la chaine des `{}`
* qui peut contenir une expression Python (un nom de variable, ou plus élaboré)
* et toute la partie dans le `{}` sera remplacé par le résultat de l'expression

```{code-cell} ipython3
:tags: [gridwidth-1-2]

import math
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

nom, age = "Pierre", 42
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

f"{nom} a {age} ans"
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

f"360° = {2*math.pi} radians"
```

````{admonition} n'importe quelle expression entre {}
:class: info

notez qu'entre les `{}`, on peut mettre un **nom de variable** mais aussi, plus généralement, écrire **une expression** (faire un calcul)
````

+++

### *f-string* : expression et format

```{image} media/f-string.svg
:align: center
```

```{code-cell} ipython3
print(f"ᴨ arrondi à deux décimales = {math.pi:.2f}")
```

### `=` dans une f-string

grâce au `=` optionnel, on peut obtenir en une seule fois un double affichage:

* le code de l'expression
* et la valeur de l'expression

```{code-cell} ipython3
# et c'est très pratique pour le debugging
def add(x, y):
    return x+y

a, b = 10, 30

# c'est ici:      ⬇
print(f"{add(a, b)=}")
```

### formats - scientifiques

formats scientifiques usuels: `e` `f` et `g`, cf. `printf`

```{code-cell} ipython3
x = 23451.23423536563
f'{x:e} | {x:f} | {x:g} | {x:010.1f} | {x:.2f}'
```

```{code-cell} ipython3
y = 769876.11434
f'{x:e} | {y:f} | {x:g} | {y:010.2f} | {x:.2f}'
```

Voir aussi pour plus de détails:  
<https://mkaz.blog/code/python-string-format-cookbook/>

+++

### justification

pour faire de la justification, on dispose des formats `<` `ˆ` et `>`

```{code-cell} ipython3
f"|{nom:<12}|{nom:^12}|{nom:>12}|"
```

```{code-cell} ipython3
# on peut aussi préciser avec quel caractère remplir
num = 123
f"|{num:<12}|{num:-^12}|{num:0>12}|"
```

### expression dans le format

un peu plus avancé, mais notez qu'on peut également utiliser des expressions dans le format

```{code-cell} ipython3
:tags: [gridwidth-1-2]

from decimal import Decimal
value = Decimal('12.34567')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ici la précision de 4
# signifie 4 chiffres
# significatifs en tout

f"value = >{value:10.4}<"
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# si nécessaire la précision 
# peut aussi être un paramètre !

width = 10
precision = 4
f"value = >{value:{width}.{precision}}<"
```

## affichage avec `print()`

```python
print(obj1, .., objn, sep=' ', end='\n',
      file=sys.stdout, flush=False)
```

* affiche les objets *obj*  convertis en chaînes de caractères
* séparés par `sep` (un espace par défaut)
* dans le fichier `file` (`sys.stdout` par défaut)  
* la ligne se termine par `end` (un retour chariot par défaut)

+++

#### enlever le *newline*

* suppression du retour à la ligne automatique

```{code-cell} ipython3
for i in range(10):
    print(i, end='')
```

#### redirection dans un fichier

* pour que `print()` écrive sur le disque dur plutôt que dans le terminal

```{code-cell} ipython3
:tags: [gridwidth-1-2]

with open('test.txt', 'w') as channel:
    L = list(range(10))
    for item in L:
        print(item, file=channel, end=' + ')
    print("\n", file=channel)
```

```{literalinclude} test.txt
```

+++

#### plusieurs paramètres

```{code-cell} ipython3
:tags: [gridwidth-1-2]

print(1, 'x', True)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

print(1, 'x', True, sep='_')
```

```{code-cell} ipython3
# dans un notebook ce n'est pas très parlant
# mais ici on n'obtiendrait PAS de retour à la ligne
print(1, 'x', True, sep='_', end='FIN')
```

```{code-cell} ipython3
# et ici on en obtiendrait deux (soit une ligne blanche)
print(1, 'x', True, sep='_', end='\n\n')
```

### module logging (avancé)

* pour le logging plus évolué qu’un simple print redirigé dans un fichier, on peut utiliser le module de la librairie standard `logging`
* documentation du module
  * https://docs.python.org/3/library/logging.html
* tutorial
  * https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

c'est **la bonne façon** de conserver des traces d'exécutionpour un programme en production

+++

## formatage : méthodes *old-school*

* avant Python-3.6, il y a eu deux autres méthodes pour formatter
  * `str.format()`
  * l'opérateur `%`
* il est **recommandé** d'utiliser les f-strings
* mais les deux autres formes existent encore, a minima savoir les lire

+++

### formatage avec `str.format()` (*old-school*)

```{code-cell} ipython3
# anonyme (dans l'ordre)
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
```

```{code-cell} ipython3
# par index
print('{1} and {0} {0}'.format('spam', 'eggs'))
```

```{code-cell} ipython3
# par nom
print('This {food} is {adjective}'
      .format(food='spam', adjective='absolutely horrible'))
```

### formatage avec `%` (*very old-school*)

* encore plus ancienne méthode

```{code-cell} ipython3
nom = "Alice"
"%s dit bonjour" % nom
```

```{code-cell} ipython3
d = 3
"%i + %i = %i" % (d, d, d + d)
```

```{code-cell} ipython3
"%(food)s is %(adjective)s" % {'food' : 'bacon',
                               'adjective' : 'delicious' }
```

### attention avec `+`

+++

* on peut être parfois tenté d’utiliser la concaténation `+`

```{code-cell} ipython3
'abc' + 'def'
```

* par contre **attention**, on ne peut concaténer que des `str`, il faut convertir explicitement avec `str()`

```{code-cell} ipython3
age = 35
try: 'alice a ' + age + ' ans'
except Exception as e: print ("OOPS", e)
```

```{code-cell} ipython3
'alice a ' + str(age) + ' ans'
```

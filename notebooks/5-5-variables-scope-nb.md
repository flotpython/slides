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
  title: "port\xE9e d\u2019une variable"
---

Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
%load_ext ipythontutor
```

+++ {"slideshow": {"slide_type": "slide"}}

# portée d’une variable

+++

* la portée d’une variable (ou scope) consiste  
  à répondre à deux questions

  * quand je référence une variable X,  
    à quelle variable je fais référence ?

  * quand j’affecte (un objet) à une variable X,  
    depuis quelles parties de mon code 
    je peux accéder à cette variable ?

+++ {"slideshow": {"slide_type": "slide"}}

## portée lexicale

+++

Python utilise la **portée lexicale**,  
c’est-à-dire que la portée des variables  
est déterminée exclusivement  
 en fonction de leur place dans le code source

+++

````{admonition} pourquoi lexicale ?
:class: admonition-small tip

la liaison lexicale est faite à *compile-time*  
le terme *lexical* signifie qu'on n'a que besoin de **lire** le programme, et pas de l'exécuter  
a contrario, la résolution des attributs ne peut se faire que à *run-time*    
````

+++ {"slideshow": {"slide_type": "slide"}}

## déclaration ?

+++

* dans d'autres langages, il y a nécessité de **déclarer** une variable  
  avant de s'en servir (typiquement les langages compilés)

* ce n'est pas le cas en Python

toutefois:

* **le fait d'affecter** une variable joue ce rôle-là
* et il y a aussi bien sûr **les paramètres** de la fonction

+++ {"tags": ["gridwidth-1-2"]}

```python
# ici la variable `y` n'est pas considérée 
# comme déclarée puisqu'on se contente
# de la lire, et qu'on ne l'affecte pas
# (pas de code avec `y = ...`

def foo(x):
    print(x)  # <-- une variable locale
              #     (paramètre)
    print(y)  # <-- PAS une variable locale
              #     (et donc ici BOOM)
```

+++ {"tags": ["gridwidth-1-2"]}

```python
# ici au contraire la variable y
# est locale à la fonction
# comme le paramètre x

def foo(x):
    y = 10    # <-- on "déclare" y
    print(x)  # <-- une variable locale
              #     (paramètre)
    print(y)  # <-- aussi (car affectée
              #     plus haut dans foo)
```

+++ {"slideshow": {"slide_type": "slide"}}

## règle **LEGB**

+++

une variable est cherchée dans cet ordre **LEGB**

* **L** comme **L**ocal
  * nom déclaré dans la fonction où il est référencé 
* **E** comme fonctions **E**nglobantes
  * nom déclaré dans les fonctions englobant la fonction où il est référencé (de l’intérieur vers l’extérieur) 
* **G** comme **G**lobal 
  * nom déclaré dans le fichier hors d’une fonction 
* **B** comme **B**uilt-in 
  * nom provenant du module *builtins*

+++

````{admonition} pas de portée de bloc
:class: attention

l'unité de base est la **fonction** - il **n'y pas de visibilité de bloc**  
(comme on la trouve dans d'autres langages)
````

+++ {"slideshow": {"slide_type": "slide"}}

## variable globale

+++

du coup toutes les variables affectées **à l’extérieur** d’une classe ou fonction sont globales

i.e. susceptibles d'être lues depuis tout le code dans le fichier (on dit un **module**)

```{code-cell} ipython3
GLOBALE = 10

def foo():
    print("from foo:", GLOBALE)
    
    def bar():
        print("from bar:", GLOBALE)
    bar()
     
foo()
```

+++ {"slideshow": {"slide_type": "slide"}}

## exemple de visibilité (1)

```{code-cell} ipython3
def foo():
    
    level1 = 10
    
    def bar():
        level2 = 20
        
        def tutu():
            level3 = 30
            
            print("from tutu:", level1, level2, level3)
        
        print("from bar: ", level1, level2) # level3 NOT visible
        tutu()
    
    print("from foo: ", level1) # level2 or level3 NOT visible here
    bar()
```

```{code-cell} ipython3
foo()
```

+++ {"slideshow": {"slide_type": "slide"}}

## exemple de visibilité (2) cassé

+++

une variable ne peut pas être à la fois globale et locale !

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [raises-exception]
---
L = [1, 2]

def f():
    # ici on pourrait penser utiliser la globale 
    L.append(3) 
    # mais en fait non, ici on dit que L est locale !
    L = 1

try:
    f()
except UnboundLocalError:
    print("OOPS")
```

````{admonition} pourquoi UnboundLocalError ?
    
`UnboundLocalError` signifie textuellement qu'on évalue une variable locale  
qui n'a pas encore été initialisée
````

+++ {"slideshow": {"slide_type": "slide"}}

## exemple de visibilité (2) revu

+++

pour réparer, on peut:

1. enlever le `L = 1` qui ne sert à rien :)
1. ou encore passer la globale en paramètre

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
---
L = [1, 2]
 
def f(L):
    # ici L est le paramètre donc une locale
    L.append(3) 
    # 
    L = 1
f(L)
print(L)
```

+++ {"slideshow": {"slide_type": "slide"}}

## attention aux classes

+++

**attention** que ce système ne s'étend pas aux classes

en effet les symboles définis au premier niveau dans une instruction `class`  
sont rangés **comme des attributs de la classe**

et à ce titre ils ne sont **pas accessibles lexicalement**

```{code-cell} ipython3
class Foo:
    
    class_variable = 10
    
    def method(self):
        # in this scope the symbols
        # 'class_variable' and `method`
        # ARE NOT lexically visible !!
        pass
```

+++ {"slideshow": {"slide_type": "slide"}}

## `global` et `nonlocal`

+++

mais revenons à nos fonctions:

* on peut donc utiliser (lire) dans une fonction  
  une variable définie au dehors / au dessus 

* mais du coup on ne peut **pas la modifier** (affecter)  
  puisque si on essaie de l'affecter cela est considéré   
  comme une déclaration de variable locale

* c'est à cela que servent les mots clefs  
  `global` ou `nonlocal`

+++ {"slideshow": {"slide_type": "slide"}}

## exemple avec `global` (1)

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# écrire une globale depuis une fonction

G = 10

def modify_G(x):
    # une fois la variable déclarée
    global G
    # je peux l'affecter
    G = x
    
modify_G(1000)

# combien vaut G ?
G
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# à votre avis 
# que se passe-t-il si on n'utilise
# pas global

G = 10

def does_not_modify_G(x):
    G = x
    
does_not_modify_G(1000)

# combien vaut G ?
G
```

````{admonition} pourquoi ?
:class: tip dropdown

dans la deuxième forme, on a juste créé une **deuxième variable G** qui est locale à la fonction, et "cache" la globale, qui donc n'est pas modifiée
````

+++ {"slideshow": {"slide_type": "slide"}}

## exemple avec `global` (2)

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# un exemple un peu plus tordu
# car ici dans la fonction
# on lit et on écrit G

G = 10

def increment_G():
    global G
    G = G + 10

increment_G()

# combien vaut G ?
G
```

```{code-cell} ipython3
:tags: [raises-exception, gridwidth-1-2]

# que se passe-t-il ici 
# d'après vous ?

G = 10

def increment_G():
    # pas de 'global'
    G = G + 10

try:
    increment_G()
except UnboundLocalError:
    print("OOPS !!")

# combien vaut G ?
G
```

````{admonition} pourquoi ?
:class: tip dropdown

ce qui se passe ici c'est: on commence par lire `G`; mais comme `G` est affectée dans `increment_G`, c'est une variable *locale* à la fonction (et donc pas la globale); mais elle n'a pas encore de valeur ! d'où l'erreur `UnboundLocalError`
````

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_intermediate"]}

## faut-il utiliser `global` ?

+++

* utiliser des variables globales est - presque toujours - une mauvaise idée
* car cela gêne la réutilisabilité
* la bonne manière est de
  * ne pas utiliser de variable globale
  * penser aux classes
* exemple archi-classique
  * la configuration d'une application
  * est souvent implémentée comme un singleton

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_intermediate"]}

## spécificités de `global`

+++

* la déclaration `global` 
  * doit apparaître avant l'utilisation
  * c'est mieux de la mettre en premier dans le bloc
* une variable déclarée `global`
  * et assignée dans une fonction
  * est automatiquement créée dans le module
  * même si elle n’existait pas avant

+++ {"slideshow": {"slide_type": "slide"}}

## exemple avec `nonlocal`

```{code-cell} ipython3
# nonlocal est très utile pour implémenter une cloture 

def make_counter():
    # cette variable est capturée dans la cloture
    counter = 0
    def increment():
        nonlocal counter
        counter += 1
        return counter
    # on retourne la fonction, qui a "capturé" le compteur
    return increment
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

c1 = make_counter()

c1()
c1()
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

c2 = make_counter()

c2()
c2()
c2()
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

c1()
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

c2()
```

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_intermediate"]}

## les noms de builtins

+++ {"tags": ["level_intermediate"]}

* ce sont les  noms prédéfinis, comme `list` ou `enumerate` ou `OSError`
* grâce à la règle LEGB, pas besoin de les importer
* par contre, on peut redéfinir un nom de `builtins` dans son programme
  * c’est une mauvaise idée et une source de bug
  * python ne donne aucun warning dans ce cas
 * dans ce cas - comme toujours - `pylint` est un outil très utile

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_intermediate"]}

### les noms de builtins

```{code-cell} ipython3
:tags: [level_intermediate, gridwidth-1-2]

# on peut accéder à la variable `__builtins__` 
# qui est .. une variable *builtin* 
__builtins__
```

```{code-cell} ipython3
:tags: [level_intermediate, gridwidth-1-2]

# ou encore on peut
# importer le module `builtins`
import builtins
```

```{code-cell} ipython3
:tags: [level_intermediate]

# je n'en montre que 5 pour garder de la place
dir(builtins)[-5:]
```

```{code-cell} ipython3
:tags: [level_intermediate]

# en fait il y en a vraiment beaucoup ! 
len(dir(__builtins__))
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
tags: [level_intermediate]
---
errors = (x for x in dir(builtins) if 'Error' in x or 'Warning' in x)

columns, width = 4, 18
for i, error in enumerate(errors, 1):
    print(f"{error:^{width}}", end=" ")
    if i % columns == 0:
        print()
```

```{code-cell} ipython3
---
cell_style: center
slideshow:
  slide_type: slide
tags: [level_intermediate]
---
others = (x for x in dir(builtins) 
          if not ('Error' in x or 'Warning' in x or '__' in x))

columns, width = 6, 16
for i, other in enumerate(others, 1):
    print(f"{other:^{width}}", end=" ")
    if i % columns == 0:
        print()
```

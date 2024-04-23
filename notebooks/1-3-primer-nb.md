---
celltoolbar: Slideshow
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  encoding: '# -*- coding: utf-8 -*-'
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
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
  title: 'primer: un rapide survol'
rise:
  slideNumber: c/t
  start_slideshow_at: selected
  theme: sky
  transition: cube
---

+++ {"slideshow": {"slide_type": "slide"}}

Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

+++

# survol du langage


> *Python3 : des fondamentaux à l'utilisation du langage*

+++ {"slideshow": {"slide_type": "slide"}}

## les concepts majeurs de python

+++ {"tags": ["gridwidth-1-2"]}

* **tout est un objet**
* objets mutables ou non

  ````{admonition} c'est le sujet de ce notebook
  :class: note

  nous allons illustrer ces 2 points de suite

  ````

+++ {"tags": ["gridwidth-1-2"]}

* références partagées
* liaison statique
* itérateurs
* espaces de nommage

  ````{admonition} ce sera abordé plus loin dans le cours
  :class: note

  nous verrons ces notions plus en détail dans le reste du cours

  ````

+++ {"slideshow": {"slide_type": "slide"}}

## modèle mental : tout est objet

```{code-cell} ipython3
%load_ext ipythontutor
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
%%ipythontutor heapPrimitives=true height=500 width=800 curInstr=2
a = 1
b = "ma chaine"

liste = [1, 10., 10 + 10j]

import math

def foo(x):
    return 2 * x
```

````{admonition} par rapport à un langage compilé
:class: warning admonition-smaller

si vous connaissez un langage compilé, vous pouvez avoir cette idée que  
*une variable = une case mémoire*  
en Python la réalité est donc subtilement différente; c'est l'objet qui occupe la mémoire (en fait toujours dans la mémoire dynamique et jamais dans la pile), et la variable est toujours une référence (pensez en gros: pointeur) vers l'objet.
````

+++ {"slideshow": {"slide_type": "slide"}}

### modèle mental : tout objet est typé

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# créons quelques objets
a = 1
b = "ma chaine"
liste = [1, 10., 10 + 10j]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et définissons une fonction
# en fait c'est un objet aussi !
def foo(x):
    return x * 2

# et le module aussi !
import math
```

```{code-cell} ipython3

:tags: [gridwidth-1-3]

# a désigne un entier
# b désigne une chaine
type(a), type(b)
```

```{code-cell} ipython3
:tags: [gridwidth-1-3, gridwidth-1-2]

# une liste
type(liste)
```

```{code-cell} ipython3
:tags: [gridwidth-1-3, gridwidth-1-2]

# les indices commencent à 0
# un complexe
type(liste[2])
```

```{code-cell} ipython3
:tags: [gridwidth-1-3, gridwidth-1-2]

# un module
type(math)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-3, gridwidth-1-2]
---
# une fonction
type(foo)
```

````{admonition} objets typés, variables non typées
:class: warning

attention toutefois que ce sont les **objets** qui sont typés et **pas les variables**  
ainsi la même variable peut désigner par ex. d'abord un entier, puis une liste…

(en fait les variables sont seulement **des références** aux objets)
````

+++ {"slideshow": {"slide_type": "slide"}}

### modèle mental : objets mutables

+++

selon leur type, les objets sont

* modifiables : **mutables**
* ou pas : **immutables**  
  (ou parfois immuables)

par exemple une liste est **mutable**...

```{code-cell} ipython3
---

slideshow:
  slide_type: slide
---
%%ipythontutor heapPrimitives=true

# je peux MODIFIER la liste

liste1 = [1, 2, 3]
liste1[1] = 100
```

### modèle mental : objets non mutables

par contre, une chaine est **non mutable** ou **immutable**

```{code-cell} ipython3
# je ne PEUX PAS modifier la chaine !

chaine = 'abc'
try:
    chaine[1] = 'z'
except Exception as exc:
    print("BOOM !", exc)
```

### modèle mental: objets égaux, mêmes objets ?

c'est super important de bien comprendre 

- quand on crée un nouvel objet
- et quand on se contente de retrouver un objet déjà créé

on en reparlera longuement, mais voyons cet exemple pour bien illustrer le concept

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
%load_ext ipythontutor
```

```{code-cell} ipython3


%%ipythontutor curInstr=2

a = b = [1, 2]
c = [1, 2]
```

dans ce cas de figure, on a 

- deux objets de type liste différents - chacune des deux lignes crée un objet liste
- et trois variables, dont les deux premières désignent (on dit aussi réfèrent, ou pointent vers) le même objet liste

en Python on a deux opérateurs qui permettent de savoir

- avec `==` si deux objets sont **égaux** - si leurs contenus sont identiques
- avec `is` si les deux objets sont en fait **le même objet** - c'est-à-dire si ils sont rangés au même endroit dans la mémoire, si on veut

```{code-cell} ipython3
a = b = [1, 2]
c = [1, 2]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# les deux premières variables 
# réfèrent bien le même objet
a is b
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ce n'est pas le cas pour a et c
a is c
```

```{code-cell} ipython3
# par contre les trois variables sont égales
# au sens de == car dans les deux listes on a 
# les mêmes valeurs
a == b == c
```

+++ {"slideshow": {"slide_type": "slide"}}

## primer

+++

* survol du langage à 30.000 pieds
* sur quelques exemples hyper simples
* pour introduire les notions les plus importantes
* fonctions, classes, modules
* **sans approfondir**

+++ {"slideshow": {"slide_type": "slide"}}

### primer : les commentaires

+++

tout ce qu’il y a après un `#` est ignoré par l’interpréteur

```{code-cell} ipython3
# programme de test qui ne fait pas grand-chose
L = [1, 2]
x = 5
if x > 3:   # on peut commenter où on veut
    # mais en pratique c'est mieux de prendre
    # toute la ligne comme ceci car on s'efforce
    # de garder la largeur de page < 80 caractères
    print(L)
```

+++ {"slideshow": {"slide_type": "slide"}}

### primer : indentation et syntaxe

+++ {"tags": ["gridwidth-1-2"]}

* contrairement à beaucoup d'autres langages
  * la mise en page (sauts de ligne et indentations)
  * **fait partie** de la syntaxe
  * ce qui élimine le besoin de `{}` ou `begin`/`end`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

if 2**5 == 32:
    print("c'est l'alignement des lignes")
    print("qui produit les blocs")
    print("pas de sucre syntaxique superflu")
    print("genre begin/end ou {}")
else:
    print("on ne passe pas ici")
```

+++ {"slideshow": {"slide_type": "slide"}}

### primer : types "fournis"

avec le langage sont fournis des types de base (*batteries included*) 

* nombres:
  * entiers, flottants, complexes, booléens
* containers:
  * listes, dictionnaires, ensembles, tuples

qui permettent de traiter rapidement pas mal de sujets

+++

### primer: librairie standard et écosystème

il y a aussi la "librairie standard" qui vient avec plein d'utilitaires:

- `path`: gestion des fichiers, et calculs de chemins 
- `datetime`: date et heure
- `random`: générateur de nombres aléatoires
- `itertools`: itérations comme permutations, combinaisons, produit cartésien, ...
- `queue`: priority queues
- la liste est très très longue...

là encore cela signifie qu'on a rapidement accès à des fonctionnalités puissantes, et bien optimisées

et si ce dont on a besoin n'est pas dans la librairie standard,  
il y a ... des centaines de milliers de librairies disponibles sur <https://pypi.org>  
y compris notamment `numpy`, `pandas`, `scikit-learn`, et énormément d'autres...

+++ {"slideshow": {"slide_type": "slide"}}

### primer : fonction

```{code-cell} ipython3
:tags: [gridwidth-1-2]

def my_first_function(a, b):
    if a <= b:
        return a * b
    else:
        return a + b
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

my_first_function(10, 2)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

my_first_function(2, 10)
```

* brique de base de la réutilisabilité
* remarquez la syntaxe orientée *bloc*

+++ {"slideshow": {"slide_type": "slide"}}

### primer : classe

```{code-cell} ipython3
:tags: [gridwidth-1-2]

class MyFirstClass:

    def __init__(self, nom, age):
        print("init instance", nom)
        self.nom = nom
        self.age = age

    def __repr__(self):
        return f"{self.nom}, {self.age} ans"
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

person = MyFirstClass(
    "Jean Dupont", 25)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

person
```

à quoi ça sert ?

* étendre les types de base fournis par le langage
* avec des types spécifiques à votre application
* pour pouvoir passer des objets 'composites' (encapsulation)
* et éventuellement réutiliser par héritage

+++ {"slideshow": {"slide_type": "slide"}}

### primer : *type hints*

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ici j'utilise un trait qui date de la version 3.9

# on peut donner une indication sur le type attendu de la variable

# comme ceci :     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
persons = []       # type: list[MyFirstClass]

# ou encore ici:    ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓   et  ↓↓↓  et ↓↓↓↓↓↓↓↓↓↓↓↓
def search(persons: list[MyFirstClass], nom: str) -> MyFirstClass:
    for p in persons:
        if p.nom == nom:
            return p
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

group = [
    MyFirstClass("Jean Dupont", 25),
    MyFirstClass("Pierre Durand", 42),
]

search(group, "Jean Dupont")
```

+++ {"tags": ["gridwidth-1-2"]}

les *type hints*, traduites en "annotations de type"

* sont **entièrement optionnelles**
* mais aident à lire, à utiliser, et à documenter le code
* vérifiables par un outil externe  
  e.g. [`mypy`](http://mypy-lang.org/)

+++ {"slideshow": {"slide_type": "slide"}}

### primer : module

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# le module standard math s'importe comme ceci
import math

type(math)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# je peux me définir une variable 'pi'

pi = "la tour de Pi"
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# qui n'interfère pas avec celle définie dans le module

math.pi
```

* brique de base de la **réutilisabilité**
* correspond à un fichier (ou répertoire) de source
* fonctionne comme un espace de noms
* ma variable `pi` coexiste avec celle de `math`  
  mais elles sont différentes - **pas de conflit**

+++ {"slideshow": {"slide_type": "slide"}}

### primer : attributs

+++

* programmation orientée objet

* notation `objet.methode()`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# appeler une méthode
x = "abc"
x.upper()
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# accéder à un attribut
p = MyFirstClass("jean", 43)
p.age
```

en fait le `.` correpond à un mécanisme général, dit de **recherche d'attributs**, dont on reparlera bien sûr

```{admonition} remarque
:class: note

on a dit plus haut par abus de langage "la variable `pi` du module `math`"; en réalité ça correspond en effet à une variable globale au module, mais techniquement lorsqu'on écrit `math.pi` on fait référence à un **attribut** du module `pi`
```

+++ {"slideshow": {"slide_type": "slide"}}

### primer : itérations

+++

l'instruction `for` et les itérateurs permettent de dissocier

* la logique d'itération
* du traitement à chaque tour de boucle

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# partant par exemple d'une liste

liste = [10, 20, 30]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# on itére toujours comme ceci

for item in liste:
    print(item)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et JAMAIS comme ceci

for i in range(len(liste)):
    print(liste[i])
```

````{admonition} et si on a besoin de l'index ?
:class: note

on verra qu'avec la fonction `enumerate()` on peut toujours éviter ce vilain `for i in range(len(truc))` même si dans la boucle on a besoin de `i`
````

+++ {"slideshow": {"slide_type": "slide"}}

### primer : exceptions

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# une fonction qui fait boom
# mais pas immédiatement
def boom(n):
    if n > 0:
        return boom(n-1)
    else:
        return 1/n
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

try:
    boom(2)
except Exception as exc:
    print("BOOM", exc)

print("la vie continue")
```

```{code-cell} ipython3
%load_ext ipythontutor
```

```{code-cell} ipython3
---

slideshow:
  slide_type: slide
---
%%ipythontutor height=500 width=850

# sans exception : le programme crashe

def boom(n):
    if n > 0:
        return boom(n-1)
    else:
        return 1/n

boom(2)
print("la vie ne continue pas !")
```

```{code-cell} ipython3
---

slideshow:
  slide_type: slide
---
%%ipythontutor height=500 width=850 curInstr=12

# avec exception

def boom(n):
    if n > 0:
        return boom(n-1)
    else:
        return 1/n

try:
    boom(2)
except Exception as exc:
    print("BOOM", exc)

print("la vie continue")
```

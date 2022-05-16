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
nbhosting:
  title: 'primer: un rapide survol'
rise:
  autolaunch: true
  slideNumber: c/t
  start_slideshow_at: selected
  theme: sky
  transition: cube
---

+++ {"slideshow": {"slide_type": "slide"}}

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
</div>

+++

# survol du langage 


> *Python3 : des fondamentaux à l'utilisation du langage*

+++ {"slideshow": {"slide_type": "slide"}}

## les concepts majeurs de python

+++ {"cell_style": "split"}

* **tout est un objet**
* objets mutables ou non

<div class="rise-footnote">

nous allons illustrer ces 2 points de suite

</div>

+++ {"cell_style": "split"}

* références partagées
* liaison statique
* itérateurs
* espaces de nommage

<div class="rise-footnote">

nous verrons ces notions plus en détail dans le reste du cours

</div>

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

+++ {"slideshow": {"slide_type": "slide"}}

### modèle mental : tout objet est typé

```{code-cell} ipython3
:cell_style: split

# créons quelques objets
a = 1
b = "ma chaine"
liste = [1, 10., 10 + 10j]
```

```{code-cell} ipython3
:cell_style: split

def foo(x):
    return x * 2
import math
```

```{code-cell} ipython3
:cell_style: center

# a désigne un entier, b désigne une chaine
type(a), type(b)
```

```{code-cell} ipython3
:cell_style: split

# une liste
type(liste)
```

```{code-cell} ipython3
:cell_style: split

# les indices commencent à 0
# un complexe 
type(liste[2])
```

```{code-cell} ipython3
:cell_style: split

# un module
type(math)
```

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: ''
---
# une fonction
type(foo)
```

<div class="rise-footnote">
    
attention toutefois que ce sont les **objets** qui sont typés et **pas les variables**  
ainsi une variable peut désigner par ex. d'abord un entier, puis une liste…

</div>

+++ {"slideshow": {"slide_type": "slide"}}

### modèle mental : objets mutables ou non

+++ {"cell_style": "center"}

selon leur type, les objets sont  

* modifiables : **mutables**
* ou pas : **immutables**  
  (ou parfois immuables)

par exemple une liste est **mutable**...

```{code-cell} ipython3
---
cell_style: center
slideshow:
  slide_type: slide
---
%%ipythontutor heapPrimitives=true
liste1 = [1, 2, 3]
liste1[1] = 100 
```

+++ {"slideshow": {"slide_type": "slide"}}

### modèle mental : objets mutables ou non

+++

par contre, une chaine est non **mutable**

```{code-cell} ipython3
chaine = 'abc'
try:
    chaine[1] = 'z'
except Exception as exc:
    print("BOOM !", exc)
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

### les commentaires

+++

tout ce qu’il y a après un `#` est ignoré par l’interpréteur

```{code-cell} ipython3
# programme de test qui ne fait pas grand-chose
L = [1, 2]
x = 5  
if x > 3:   # teste la comparaison dans if 
    print(L)
```

+++ {"slideshow": {"slide_type": "slide"}}

### indentation et syntaxe

+++

* contrairement à beaucoup d'autres langages
  * la mise en page (sauts de ligne et indentations)
  * **fait partie** de la syntaxe
  * ce qui élimine le besoin de `{}` ou `begin`/`end`

```{code-cell} ipython3
if 2**5 == 32:
    print("pas de sucre syntaxique")
else:
    print("du genre if (exp) {do_this()} else {do_that()}")
```

+++ {"slideshow": {"slide_type": "slide"}}

### primer : fonction

```{code-cell} ipython3
:cell_style: split

def my_first_function(a, b):
    if a <= b:
        return a * b
    else:
        return a + b
```

```{code-cell} ipython3
:cell_style: split

my_first_function(10, 2)
```

```{code-cell} ipython3
:cell_style: split

my_first_function(2, 10)
```

* brique de base de la réutilisabilité 
* remarquez la syntaxe orientée *bloc*

+++ {"slideshow": {"slide_type": "slide"}}

### primer : classe

```{code-cell} ipython3
:cell_style: split

class MyFirstClass:
    
    def __init__(self, nom, age):
        print("init instance", nom)
        self.nom = nom
        self.age = age
        
    def __repr__(self):
        return f"{self.nom}, {self.age} ans"
```

```{code-cell} ipython3
:cell_style: split

person = MyFirstClass(
    "Jean Dupont", 25)
```

```{code-cell} ipython3
:cell_style: split

person
```

* étendre les types de base fournis par le langage
* avec des types spécifiques à votre application
* pour pouvoir passer des objets 'composites' (encapsulation)
* et éventuellement réutiliser par héritage

+++ {"slideshow": {"slide_type": "slide"}}

### primer : *type hints*

```{code-cell} ipython3
:cell_style: center

# ici j'utilise un trait qui date de la version 3.9

# on peut donner une indication sur le type attendu, avec
# ce commentaire   ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
global_index = {}  # type: dict[name, MyFirstClass]

# ou encore ici:  ↓↓↓↓↓↓↓↓↓↓↓↓ et ↓↓↓↓↓↓↓↓ 
def index(instance: MyFirstClass) -> None:
    global_index[instance.nom] = instance
    
def find_instance(name: str) -> MyFirstClass:
    return global_index.get(name, None)
```

```{code-cell} ipython3
:cell_style: split

index(MyFirstClass("dupont", 25))
index(MyFirstClass("durand", 52))

print(find_instance("dupont"))
```

+++ {"cell_style": "split"}

les annotations de type 
* sont **entièrement optionnelles**
* mais aident à lire, utiliser  
  et documenter le code
* vérifiables par un outil externe  
  e.g. [`mypy`](http://mypy-lang.org/)

+++ {"slideshow": {"slide_type": "slide"}}

### primer : module

```{code-cell} ipython3
:cell_style: split

import math
type(math)
```

```{code-cell} ipython3
:cell_style: split

pi = "la tour de Pi"
```

```{code-cell} ipython3
:cell_style: split

math.pi
```

* correspond à un fichier (ou répertoire) de source 
* fonctionne comme un espace de noms
* ma variable `pi` coexiste avec celle de `math`  
  mais elles sont différentes - **pas de conflit**

+++ {"slideshow": {"slide_type": "slide"}}

### primer : attributs

+++ {"cell_style": "center"}

* programmation  
  orientée objet

* notation `objet.methode()`

```{code-cell} ipython3
:cell_style: split

# appeler une méthode
x = "abc"
x.upper()
```

```{code-cell} ipython3
:cell_style: split

# accéder à un attribut
p = MyFirstClass("jean", 43)
p.age
```

en fait mécanisme plus général
dit de recherche d'attributs  
comme par exemple `math.pi`

+++ {"slideshow": {"slide_type": "slide"}}

### primer : itérations

+++

l'instruction `for` et les itérateurs permettent de dissocier 

* la logique d'itération
* du traitement à chaque tour de boucle

```{code-cell} ipython3
:cell_style: split

# partant par exemple d'une liste
liste = [10, 20, 30]
```

```{code-cell} ipython3
:cell_style: split

# on itére toujours comme ceci
for item in liste:
    print(item)
```

```{code-cell} ipython3
:cell_style: split

# et JAMAIS comme ceci
for i in range(len(liste)):
    print(liste[i])
```

+++ {"slideshow": {"slide_type": "slide"}}

### primer : exceptions

```{code-cell} ipython3
:cell_style: split

# une fonction qui fait boom
# mais pas immédiatement
def boom(n):
    if n > 0:
        return boom(n-1)
    else:
        return 1/n
```

```{code-cell} ipython3
:cell_style: split

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
cell_style: center
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
cell_style: center
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

***

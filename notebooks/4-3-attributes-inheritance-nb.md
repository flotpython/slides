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
  title: "attributs et h\xE9ritage"
---

+++ {"slideshow": {"slide_type": "slide"}}

Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

+++ {"slideshow": {"slide_type": ""}}

(label-classes-inheritance)=

# attributs & héritage

+++

## pour réutiliser du code en python

**DRY = *don't repeat yourself*** : *cut'n paste is evil*

```{list-table}

* - fonctions
  - pas d'état après exécution

* - modules
  - garde l'état, une seule instance par programme

* - **classes**
  - **instances multiples**, **chacune garde l'état**, **héritage**
```

+++ {"tags": []}

## programmation orientée objet

pourquoi et comment ?

```{list-table}

* - objectif
  - réutilisabilité, donc

* - comment
  - modularité & héritage (a.k.a. espaces de nom et recherche d'attribut)
```

+++ {"tags": []}

### réutilisabilité & modularité

une façon d'écrire du code **modulaire**:  

* regrouper *le code* dans une classe et *les données* dans un objet  
* de cette façon, la classe constitue *un tout cohérent* (**modularité**)
* l'*encapsulation* consiste à séparer l'*interface* (les méthodes) et l'*implémentation*
* le code qu utilise la classe n'utilise que l'*interface*
* ce qui permet de garantir certains invariants
* et de cette façon on se réserve le droit de changer l'implémentation,  
  sans avoir avoir à modifier le code qui utilise la classe

````{admonition} remarques

- plus on découpe en petits morceaux, plus on a de chances de pouvoir réutiliser
- en Python, l'encapsulation est moins contraignante que des langages plus dogmatiques comme C++; 
  ici pas de public/protected/private, on se base sur des conventions de nommage
````

+++ {"tags": []}

### réutilisabilité & héritage

une autre approche consiste à écrire du code **générique**

* par exemple, un moteur de jeu fait "avancer" une collection d'objets
* et fournit quelques objets de base, facilement extensibles (grâce à l'**héritage**)
* dès qu'un objet explique comment il avance, il peut faire partie du jeu

````{admonition} un exemple intéressant

un exemple de librairie qui utilise massivement ce trait est [la librairie arcade](https://api.arcade.academy/en/latest/)  
et par exemple [ce petit programme de démo](https://api.arcade.academy/en/latest/examples/sprite_move_keyboard.html#sprite-move-keyboard)

pour écrire un jeu on n'a pas besoin d'écrire la boucle d'événements (*mainloop*), c'est du code générique  
on se contente d'hériter des classes fournies par la librairie
````

dans les deux cas, pour bien comprendre les classes en Python, il faut comprendre deux mécanismes fondamentaux, qui sont

- la notion d'espace de nom
- et la recherche d'attributs

+++

## espaces de nom

et pour commencer parlons des espaces de nom:

* tous les objets qui sont **un module**, **une classe** ou **une instance**
* constituent chacun **un espace de nom**, *i.e.* une association *attribut* → *objet*

````{admonition} enfin presque
:class: dropdown

ce n'est pas le cas pour les instances des types natifs, mais bon..
````

+++

### espaces de nom - pourquoi

* permet de lever l'ambigüité en cas d'homonymie
  * par ex. si 2 modules utilisent tous les 2 une globale `truc`, elles peuvent coexister sans souci
* les espaces de nom sont imbriqués (*nested*) - par ex. `package.module.classe.methode`
* l'héritage rend cela dynamique, *i.e.* la résolution des attributs **est faite à *runtime***

+++ {"slideshow": {"slide_type": "slide"}}

### variables et attributs

ce qui nous donne l'occasion d'insister sur ceci; c'est assez basique mais ça va mieux en le disant:  
```{image} ../media/variable-attribut.svg
:align: center
:width: 300px
```

dans l'expression `foo.bar.tutu()`, il y a une différence fondamentale dans la nature de la variable et des attributs:

- la *variable* est recherchée **dans le code du programme**; on parlera un peu plus tard de la notion de **portée des variables**, mais pour faire court on va chercher la variable `foo` d'abord dans la fonction où se trouve ce code (y compris les paramètres), puis si on ne trouve pas dans la fonction englobante, etc..
  on parle de **liaison lexicale**, un terme bien savant qui veut juste dire qu'on peut savoir avec certitude à quoi correspond la variable **rien qu'en lisant le programme**
- par contre, et c'est le point qui nous importe, pour calculer `bar` à partir de (l'objet référencé par) `foo`, le calcul est fait **à *run-time***, c'est-à-dire à l'exécution - on parle de **liaison dynamique**: il faut que l'objet `foo` soit un espace de nom, et disons, pour faire simple à ce stade, qu'il contienne l'attribut `bar`; bien entendu le processus est répété pour trouver `tutu` à partir de (l'objet référencé par) `foo.bar`

````{admonition} c'est simplifié
:class: admonition-smaller

on va voir justement que la recherche d'attributs est plus compliquée que ça, mais l'important est de bien comprendre la différence entre les deux types de liaison:

```{list-table}

* - variable
  - liaison lexicale, en remontant dans le code

* - attribut
  - liaison dynamique, en remontant dans les espaces de nom
```
````

+++ {"cell_style": "center"}

### lecture ou écriture des attributs

nous allons voir cela en détail tout de suite, et pour cela il nous faut distinguer deux cas

```{list-table}

* - attribut en **écriture**  
  - `obj.attribute = ...`  
  - i.e. à gauche d'une affectation

* - attributs en **lecture** 
  - `obj.attribute` 
  - les autres cas
```

+++ {"slideshow": {"slide_type": ""}}

(label-access-attributes-usual)=
## écriture d'attribut: pas de recherche

quand on **écrit** un attribut dans un objet, le mécanisme est simple:  
on écrit **directement dans l'espace de nom** de l'objet

````{admonition} exemple typique

en entrant dans le constructeur, l'objet `self` n'a pas encore l'attribut `name`  
et quand on écrit `self.name = name`, on le crée
````

````{admonition} lecture ou écriture ?
:class: admonition-small seealso

on considère que c'est une écriture si le terme `obj.attribute` est **à gauche** d'une affectation
````

+++ {"slideshow": {"slide_type": ""}, "cell_style": "center"}

## résolution d'attribut pour la lecture

pour la lecture par contre, le mécanisme de résolution des attributs est plus élaboré

* fil ournit la **mécanique de base** de la POO
* et sous-tend notamment (mais pas que) la mécanique de l'héritage

+++

### lecture: recherche de bas en haut

**pour la lecture :**  
la règle pour chercher un attribut en partant d'un objet consiste à

* le chercher dans l'espace de nom de l'objet lui-même
* sinon dans l'espace de nom de sa classe
* sinon dans les super-classes (on verra les détails plus loin)

````{admonition} cas particulier des dunders
:class: admonition-small

on a vu que le langage peut faire une **recherche implicite** de *dunder* - 
c'est le cas par exemple quand on recherche `__iter__` parce que l'objet est itéré, 
ou qu'on cherche `__call__` parce que l'objet est appelé  
dans ces cas-là on ne **regarde pas dans l'objet lui-même**  
c'est une subtilité, qui ne va pas trop nous concerner dans ce chapitre, mais dont on verra l'impact dans [la section sur les métaclasses](label-metaclasses)
````

+++ {"slideshow": {"slide_type": "slide"}}

### ex1. de résolution d'attribut

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# cas simple sans héritage
# appel d'une méthode
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# quand on cherche vector.length
# on cherche
# 1. dans vector - pas trouvé
# 2. dans Vector - bingo

vector = Vector(3, 4)
vector.length()
```

```{code-cell} ipython3
:tags: []

# on va voir ça en détail 
# dans pythontutor
%load_ext ipythontutor
```

+++ {"slideshow": {"slide_type": "slide"}}

#### 2 espaces de nom distincts

+++ {"slideshow": {"slide_type": ""}, "tags": ["gridwidth-1-2"]}

* la classe `Vector` a les attributs
  * `__init__`
  * `length`

+++ {"slideshow": {"slide_type": ""}, "tags": ["gridwidth-1-2"]}

* l'objet `vector` a les attributs
  * `x` et `y`,
  * mais pas `length` !

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
%%ipythontutor width=1000 height=400 curInstr=7
import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

vector = Vector(2, 2)
```

+++ {"slideshow": {"slide_type": "slide"}}

````{admonition} les fonctions vars() et dirs()
:class: admonition-small

ce n'est pas forcément à retenir, mais c'est utile si on essaie d'inspecter les espaces de nom sans ipythontutor:

- avec la fonction *builtin* `vars(obj)`, on peut inspecter le contenu d'un espace de noms (et **seulement lui**) 
- avec la *builtin* `dirs(obj)` on peut cette fois accéder à **l'ensemble des attributs** qui sont disponibles sur `x`, c'est donc la somme des attributs trouvés:

    * dans l'espace de nom de `x`
    * dans l'espace de nom de sa classe
    * et de ses super-classes

enfin notez que, quand on se livre à ce genre d'introspection, on enlève souvent, pour clarifier, les attributs qui contiennent `__`
````

+++ {"slideshow": {"slide_type": "slide"}}

#### résumé

donc dans ce cas simple de la classe `Vector` et de l'instance `vector`:

* `vector.x` fait référence à l'attribut posé **directement sur l'instance**
* `vector.length` fait référence à la méthode qui est **dans la classe**

+++ {"slideshow": {"slide_type": ""}}

### ex2. résolution d'attribut avec héritage

jusqu'ici on n'a pas d'héritage puisque pour l'instant on n'a qu'une classe  
mais l'héritage est une **simple prolongation** de cette logique

on verra un peu plus loin la syntaxe pour créer une sous-classe, mais voici déjà un premier exemple simplissime (et un peu bidon du coup)

```{code-cell} ipython3
# ici pour l'instant, une classe fille sans aucun contenu
class SubVector(Vector):
    pass

subvector = SubVector(6, 8)

# grâce à l'héritage on peut tout à fait écrire ceci
subvector.length()
```

+++ {"slideshow": {"slide_type": "slide"}}

comment fait-on pour trouver `subvector.length` ? c'est exactement le même mécanisme qui est à l'oeuvre ! pour évaluer `subvector.length()`, on cherche l'attribut `length` 

* dans l'instance `subvector` : non
* dans sa classe `SubVector` : non
* dans la super-classe `Vector` : ok, on prend ça

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
%%ipythontutor width=1000 height=400 curInstr=8
import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
class SubVector(Vector):
    pass

subvector = SubVector(6, 8)
```

+++ {"tags": ["level_intermediate"]}

## lecture *vs* écriture - cas limites 

(avancé)

il faut se méfier parfois: il y a écriture si  et seulement si il y a **affectation**; du coup dans les deux phrases suivantes, qui semblent pourtant faire la même chose, en réalité la mécanique est **totalement différente** !

```{list-table}

* - `obj.liste += ['foo']`
  - **écriture**

* - `obj.liste.append('foo')`
  - **lecture** !
```

alors même que dans les deux cas il y a bien modification des données, évidemment

+++ {"slideshow": {"slide_type": "slide"}}

## héritage

+++ {"slideshow": {"slide_type": "slide"}}

### syntaxe

+++ {"slideshow": {"slide_type": ""}, "tags": ["gridwidth-1-2"]}

une classe peut hériter d’une (ou plusieurs) autre classes
  
```python
# la syntaxe est
class Class(Super):
    pass

# ou 
class Class(Super1, Super2):
    pass
```

+++ {"slideshow": {"slide_type": ""}, "tags": ["gridwidth-1-2"]}

* si A hérite de B, ont dit que
  * A est une **sous-classe** de B
  * et B est la **super-classe** de A
* de ce qui précède:
  * la sous-classe hérite (des attributs) de sa (ses) super-classe(s)
  * l’instance hérite de la classe qui la crée

+++

### `isinstance()` et `issubclass()`

* `isinstance(x, class1)` retourne `True` si `x` est une instance de `class1` **ou d’une super classe**
* `issubclass(class1, class2)` retourne `True` si `class1` est une sous-classe de `class2`

````{admonition} préférez isinstance() plutôt que type()
:class: attention

pour savoir si un objet est d'un certain type, on peut aussi penser à utiliser `type(obj) is Class`  
toutefois il est **de beaucoup préférable** le plus souvent de faire `isinstance(obj, Class)` et cela pour deux raisons

- d'abord parce `isinstance()` vérifie aussi les super-classes de `Class`
- ensuite, mais c'est de la commodité, on peut passer plusieurs types à isinstance, comme e.g. `isinstance(x, (int, float)`
````

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# A est la super-classe
class A:
    pass


class B(A):
    pass


a, b = A(), B()
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
isinstance(a, A), issubclass(B, A)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

isinstance(b, A), isinstance(a, B)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# accepte plusieurs types/classes
isinstance(a, (A, B))
```

### `super()`

* utile lorsque la spécialisation  
  consiste à ajouter ou modifier  
  par rapport à la classe mère

* le cas typique est d'ailleurs le constructeur  
  dès qu'on ajoute un attribut de donnée

* permet de ne pas mentionner explicitement  
  le nom de la classe mère (code + générique)

+++ {"slideshow": {"slide_type": "slide"}}

#### `super()` dans le constructeur

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
# illustration de super() 
# dans le constructeur

class C:
    def __init__(self, x):
        print("init x par superclasse")
        self.x = x

class D(C):
    def __init__(self, x, y):
        # initialiser : la classe C
        super().__init__(x)
        print("init y par classe")
        self.y = y
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

c = C(10)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

d = D(100, 200)
```

+++ {"slideshow": {"slide_type": "slide"}}

#### `super()` dans une méthode standard

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
# super() est souvent rencontrée
# dans __init__ mais s'applique
# partout
class C:
    def f(self):
        print('f dans C')
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
class D(C):
    def f(self):
        # remarquez l'absence
        # de self !
        super().f()
        print('f dans D')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

c = C(); c.f()
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

d = D(); d.f()
```

+++ {"slideshow": {"slide_type": "slide"}}

## résumé

* les instances et classes sont des objets mutables (sauf classes *builtin*)
* chaque instance et chaque classe est un espace de nom
* lorsqu'on écrit un attribut, on écrit directement dans l'espace de nom de cet objet
* en lecture, on résoud la référence d'un attribut de bas en haut
* on utilise `isinstance()` pour tester le type d'un objet
* une méthode peut faire référence à la super-classe avec `super()`
* en général
  * les classes ont des attributs de type méthode
  * les objets ont des attributs de type donnée
  * mais le modèle est flexible, dans le notebook suivant on va voir quelques exceptions notables

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_intermediate"]}

## annexe: MRO & graphe d’héritage

(très avancé)

+++ {"slideshow": {"slide_type": ""}, "tags": ["level_intermediate"]}

### graphe d'héritage

* on peut donc construire un graphe d’héritage
* allant des super-classes aux instances

+++ {"tags": ["level_intermediate", "gridwidth-1-2"]}

```{image} media/classes.png
:align: center
:width: 300px
```

```{code-cell} ipython3
:tags: [level_intermediate, gridwidth-1-2]

class C1:
    pass
class C2:
    pass
class C(C1, C2):
    def func(self, x):
        self.x = 10
o1 = C()
o2 = C()
```

+++ {"tags": ["level_intermediate"]}

### MRO: *method resolution order*

lors de la recherche, si on ne trouve pas dans l'objet ni dans sa classe, il faut décider dans quel ordre on recherche dans les super-classes - pour le cas pathologique où l'attribut serait présent dans plusieurs d'entre elles

on utilise pour cela le *MRO : method resolution order*; l’algorithme est le suivant

* liste toutes les super-classes en utilisant un algorithme DFLR (depth first, left to right)
* si classe dupliquée, **ne garder que la dernière** occurrence

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_intermediate", "gridwidth-1-2"]}

```{image} media/mro.png
:align: center
```

```{code-cell} ipython3
:tags: [level_intermediate, gridwidth-1-2]

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
```

+++ {"tags": ["level_intermediate"]}

* parcours DFLR: `D`, `B`, `A`, `object`, `C`, `A`, `object`
* suppressions : `D`, `B`, ~~`A`~~, ~~`object`~~, `C`, `A`, `object`

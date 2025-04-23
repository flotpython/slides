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
  title: fonctions
---

+++ {"slideshow": {"slide_type": ""}}

# passage de paramètres

+++ {"slideshow": {"slide_type": "slide"}}

Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

## paramètres multiples

Python propose une large gamme de mécanismes pour le passage de paramètres,  
pour **définir** aussi bien que pour **appeler** une fonction  

chacun de ces mécanismes est assez simple pris individuellement,  
mais un peu de soin est nécessaire pour bien expliquer le mécanisme général

+++

### *use case*: un *wrapper*

* on veut écrire un *wrapper* autour de `print()`, c'est-à-dire
* une fonction `myprint()` qui ajoute `HELLO` au début de chaque impression
* mais sinon l'interface de `myprint()` doit être exactement celle de `print()`, i.e.  

  * nombre variable de paramètres
  * réglages inchangés - e.g. `myprint(..., file=f)`
  
```python
# on doit pouvoir faire ceci

>>> myprint(1, 2, 3, sep='+')
HELLO 1+2+3
```

+++ {"slideshow": {"slide_type": "slide"}}

### et une variante 

* ou encore, on veut pouvoir écrire une variante de `myprint`, 
* qui attend un premier argument obligatoire, le texte pour pour remplacer `HELLO`,…

```python
# on doit pouvoir faire ceci

>>> myprint2('HEY', 1, 2, 3, sep='==')
HEY 1==2==3
```

+++ {"slideshow": {"slide_type": "slide"}}

### implémentation

et pour commencer voyons comment on ferait ça en Python

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [gridwidth-1-2]
---
# la première variante

def myprint(*args, **kwds):
    print("HELLO", end=" ")
    print(*args, **kwds)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ajout automatique de 'HELLO', et on peut utiliser tous
# les paramètres spéciaux de print()

myprint(1, 2, 3, sep='+')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# la deuxième variante, avec le premier paramètre obligatoire

def myprint2(obligatoire, 
             *args, **kwds):
    print(obligatoire, end=" ")
    print(*args, **kwds)    
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# le premier paramètre sert à remplacer 'HELLO'

myprint2('HEY', 1, 2, 3, sep='==')
```

## vocabulaire

+++

### paramètres et arguments

précisons le vocabulaire  
lorsqu'il peut y avoir ambiguïté :

* `paramètre`: le nom qui apparaît dans le `def`
* `argument`: l'objet réellement passé à la fonction

```{code-cell} ipython3
:slideshow: {}
:tags: [gridwidth-1-2]

# ici x est un PARAMÈTRE

def foo(x):
    print(x)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et ici a est un ARGUMENT

a = 134 + 245
foo(a)
```

le sujet que nous abordons ici, ce sont les règles qui permettent de **lier les arguments aux paramètres**  
de façon à ce que tous les arguments soient exposés à la fonction

* il y a 4 manières de **déclarer un paramètre** 
* et 2 manières **de passer un argument** à une fonction (en fait 2+2)
* les deux familles se ressemblent un peu, mais il y a tout de même des différences

+++ {"slideshow": {"slide_type": "slide"}}

### les 4 sortes de paramètres

```{list-table}

* - (I)
  - `def foo(x):`
  - paramètre **positionnel** ou ordonné ou usuel/normal

* - (II)
  - `def foo(x=10):`
  - paramètre avec **valeur par défaut**

* - (III)
  - `def foo(*args):`
  - correspond aux arguments non nommés "en plus"

* - (IV)
  - `def foo(**kwds):`
  - correspond aux arguments nommés "en plus"
```

+++ {"slideshow": {"slide_type": "slide"}}

### les 2+2 sortes d'arguments

la différence fondamentale est à faire entre

```{list-table}

* - (A)
  - `foo(argument)`
  - argument non nommé

* - (B)
  - `foo(parametre=argument):`
  - argument nommé
```

````{admonition} et deux variantes
:class: admonition-small

```{list-table}

* - (C)
  - `def foo(*args):`
  - les objets dans `args` (itérable) sont passés comme des arguments (A) non nommés

* - (D)
  - `def foo(**kwds):`
  - les objets dans `kwds` (un dictionnaire) sont passés comme des arguments (B) nommés
```
on va faire abstraction de (C) et (D) pour l'instant, et [on verra plus bas](label-args-unpacking) comment ça fonctionne  
(et d'ailleurs c'est très simple...)

````

````{admonition} ça devient vite incompréhensible !

si on reste raisonnamble, cela fonctionne de bon sens  
mais attention aux mélanges trop hardis, cela devient vite inextricable
en cas de doute n'hésitez pas à tout nommer, ou en tous cas plus que strictement nécessaire
````

+++

## les paramètres

+++

### (I) paramètre positionnel

* c'est le mécanisme le plus simple et le plus répandu  
* les paramètres obtiennent un rang de gauche à droite  
  par exemple ci-dessous le paramètre `prenom` est le deuxième paramètre positionnel

```{code-cell} ipython3
# pour afficher quel argument est attaché à quel paramètre

def agenda(nom, prenom, tel, age, job):
    
    print(f"{nom=}, {prenom=}, {tel=}, {age=}, {job=}")
```

#### appel

comment peut-on alors appeler la fonction ?

```{code-cell} ipython3
# appel usuel, sans nommage
# c'est l'ordre des arguments qui compte

agenda('doe', 'alice', '0404040404', 35, 'medecin')
```

```{code-cell} ipython3
# et aussi, en nommant les arguments lors de l’appel
# on peut les mettre dans n’importe quel ordre

agenda(prenom='alice', nom='doe', age=35, tel='0404040404', job='medecin')
```

+++ {"slideshow": {"slide_type": "slide"}}

### (II) paramètre avec valeur par défaut

dans le code précédent, qu'on les mette dans l'ordre ou pas, on **doit** passer à la fonction 5 arguments

parfois on veut dire "si on ne passe pas d'argument pour `job`, alors on prendra par défaut `"medecin`"

````{admonition} c'est très utilisé
:class: admonition-small

pour la clarté de l'exposé on va garder notre exemple avec `agenda`; en pratique, cet usage est **très répandue**, par exemple avec les librairies graphiques où on ne veut pas avoir à passer à chaque appel tous les paramètres comme la couleur, la fonte, ... et dans plein d'autres cas de figure aussi
````

```{code-cell} ipython3
#           ┌──────┬─────┬──────────────────  positionnels 
#           │      │     │    ┌─────────┬───  avec valeurs par défaut
#           ↓      ↓     ↓    ↓         ↓     
def agenda(nom, prenom, tel, age = 35, job = 'medecin'):
    
    print(f"{nom=}, {prenom=}, {tel=}, {age=}, {job=}")
```

#### appels

* comment on peut alors appeler la fonction ?

```{code-cell} ipython3
# appel en suivant la signature
# il manque deux arguments, on utilise les valeurs par défaut

agenda('Dupont', 'Jean', '123456789')
```

```{code-cell} ipython3
# on peut aussi nommer les arguments, et à nouveau 
# ça permet de mélanger l'ordre des paramètres imposés
# ici aussi job est manquant, on utilise la valeur par défaut

agenda(prenom = 'alice', nom = 'doe', age = 25, tel = '0404040404')
```

```{code-cell} ipython3
# on peut mixer les deux approches
# ici les trois premiers sont liés dans l'ordre

agenda('Dupont', 'Jean', '123456789', age = 25, job = 'avocat')
```

````{admonition} le = a deux sens vraiment différents
:class: attention admonition-small

**attention** à ne pas confondre la forme `name=value` dans une entête de fonction et lors d’un appel:

* **dans un entête** c’est une **déclaration de paramètre (avec valeur) par défaut**
* **lors d’un appel**, cela signifie que l'argument doit être lié au paramètre de ce nom
````

+++

### (III) paramètre multiple `*args`

jusqu'ici c'est assez simple, c'est maintenant que ça devient un peu plus inhabituel

le paramètre `*args` s'appelle aussi parfois *attrape-tout*; lorsqu'on en met un, (et on n'a droit d'en mettre qu'un seul):

* alors Python collecte **tous les arguments non nommés restants** - i.e. non liés à un paramètre
* il les range dans un tuple
* qu'il lie au paramètre `args`

de cette façon on peut donc créer très simplement une fonction qui accepte un nombre variable d'arguments (non nommés)  
et pour les exploiter la fonction n'a qu'à, par exemple, itérer sur le paramètre `args`

````{admonition} le nom args n'est pas un mot clé
:class: admonition-small

un peu comme avec `self` dans les méthodes de classe, le nom de paramètre `args` correspond à un usage assez fréquent, mais en réalité c'est un paramètre usuel et on peut lui donner n'importe quel nom
````

+++ {"slideshow": {"slide_type": "slide"}}

#### ex. avec 0 ou plus arguments

```{code-cell} ipython3
:tags: []

# définition

def variable(*args):
    print(f"args={args}")
```

```{code-cell} ipython3
:tags: []

# 0 argument

variable()
```

```{code-cell} ipython3
:tags: []

# 1 argument

variable(1)
```

```{code-cell} ipython3
:tags: []

# 5 arguments 

variable(1, 2, 3, 4, "cinq")
```

+++ {"slideshow": {"slide_type": "slide"}}

#### ex. avec au moins 2 arguments 

on peut aussi très simplement créer une fonction qui attend au moins deux arguments, le reste étant optionnel

```{code-cell} ipython3
:tags: []

# au moins deux arguments

def variable2(one, two, *args):
    print(f"one={one}, two={two}, args={args}")
```

```{code-cell} ipython3
:tags: []

# 2 arguments

variable2(1, 2)
```

```{code-cell} ipython3
:tags: []

# 3 arguments
variable2(1, 2, 3)
```

```{code-cell} ipython3
:tags: []

# 5 arguments 

variable2(1, 2, 3, 4, "cinq")
```

```{code-cell} ipython3
:tags: [raises-exception]

# 1 seul argument -> TypeError

variable2(1)
```

#### un seul `*args`

redisons-le: `*args` **ne peut apparaître qu'une fois**  (car sinon il y aurait ambiguïté)

```{code-cell} ipython3
:tags: [raises-exception]

# si on met plusieurs paramètres *args, python n'est pas content

def variable(*args1, *args2):
    pass
```

### (IV) paramètre multiple `**kwds`

le mécanisme est exactement le même, mais avec les **arguments nommés**:

* on regarde tous ceux qui n'ont pas encore été liés à un paramètre,
* au lieu de créer un tuple, on crée cette fois un **un dictionnaire**, de façon à mémoriser les noms en plus des valeurs  
* et c'est ce dictionnaire qui est affecté au paramètre `kwds`

ici encore le nombre d’arguments nommés peut être quelconque

+++ {"slideshow": {"slide_type": "slide"}}

#### ex. 1

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: []
---
# cette fonction peut être appelée avec autant d'arguments
# qu'on veut, mais il doivent tous être nommés

def named_args(**kwds):
    print(f"kwds={kwds}")

# var_named
named_args()
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

named_args(a = 1)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

named_args(a = 1, b = 2)
```

```{code-cell} ipython3
:tags: [raises-exception]

# si on essaie de lui passer un argument non nommé, python n'est pas content !

named_args(10)
```

#### ex. 2

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: []
---
# pareil ici, autant d'arguments nommés qu'on veut
# et cette fois on peut aussi lui passer un argument nommé

def named_args1(a=0, **kwds):
    print(f"a={a} kwds={kwds}")
    
# var_named
named_args1(a=1)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

named_args1(1, b=2)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

named_args1(a = 1, b = 2)
```

```{code-cell} ipython3
:tags: []

named_args1(b = 2, c=3)
```

#### un seul `**kwds`

* ici encore cette forme de paramètre **ne peut apparaître qu'une fois**
* car sinon, comme avec `*args`, la liaison serait ambigüe

+++ {"slideshow": {"slide_type": "slide"}}

## ordre des paramètres et arguments

+++ {"tags": []}

### paramètres

l'ordre dans lequel sont déclarés les différents types de paramètres est imposé par le langage  
historiquement à l'origine, on **devait déclarer dans cet ordre** :  

```{list-table}

* - positionnels,
  - avec défaut,
  - forme `*` (1 max),
  - forme `**` (1 max)
```

````{admonition} une petite exception
:class: warning

nous verrons [un peu plus loin](label-keyword-only-argument) que le paramètre attrape-tout `*args` peut aussi être mis un peu plus tôt que cela dans la liste des paramètres
````

+++ {"cell_style": "center", "slideshow": {"slide_type": ""}}

### arguments

dans un appel de fonction, on recommande de matérialiser deux groupes

1. en premier les non-nommés:

   * argument(s) positionnels (`name`), 
   * forme(s) `*name`
2. puis ensuite les arguments nommés

   * argument(s) nommés (`name=value`),
   * forme(s) `**name`

+++ {"slideshow": {"slide_type": "slide"}}

### exemple: appel

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
---
# une fonction passe-partout qui affiche juste ses paramètres 
# pour nous permettre d'illustrer les appels 

def show_any_args(*args, **kwds):
    print(f"args={args} - kwds={kwds}")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# les cas simples pour la voir marcher

show_any_args(1)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et 

show_any_args(x=1)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# on recommande de mettre les arguments non-nommés en premier

show_any_args(1, 4, 5, 3, x = 1, y = 2)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [raises-exception]
---
# car ceci est illégal et déclenche une SyntaxError

foo(1, x=1, 4, 5, 3, y=2)
```

### exemple: définition

```{code-cell} ipython3
:tags: [raises-exception]

# même punition ici: SyntaxError, on n'a pas respecté le bon ordre !

def foo(b=10, a):
    pass
```

+++ {"slideshow": {"slide_type": ""}}

## *keyword-only* / *positional-only* 

(avancé)

l'ordre dans lequel on devait déclarer les paramètres 

```{list-table}

* - positionnels,
  - avec défaut,
  - forme `*` (1 max),
  - forme `**` (1 max)
```

reste une bonne approximation, mais:

* en Python-3 on a introduit [les paramètres *keyword-only*](https://www.python.org/dev/peps/pep-3102/)
  * on peut ainsi définir un paramètre qu'il **faut impérativement** nommer lors de l'appel
* et également en 3.8 [les paramètres *positional-only*](https://docs.python.org/3/whatsnew/3.8.html#positional-only-parameters)
  * qui introduit des paramètres usuels qu'on **ne peut pas nommer** lors de l'appel
 
voyons comment marchent ces deux mécanismes

+++

(label-keyword-only-argument)=
### paramètre *keyword-only*

on va prendre une fonction qui combine un peu tous les types de paramètres, et pour commencer on va les mettre dans l'ordre standard

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# une fonction qui combine les différents types de paramètres

def normal(a, b=100, *args, **kwds):
    print(f"a={a}, b={b}, args={args}, kwds={kwds}")
```

et profitons-en pour voir comment on peut l'appeler et ce que ça donne:

```{code-cell} ipython3
:tags: [gridwidth-1-2]

normal(1)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

normal(1, 2)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

normal(1, 2, 3)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

normal(1, 2, 3, bar=1000)
```

```{code-cell} ipython3
normal(1, 2, 3, bar=1000)
```

imaginons maintenant que je veuille **imposer à l'appelant de nommer `b`**  
pour cela il me suffit de déplacer **l'attrape-tout avant le paramètre `b`** comme ceci

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# on peut déclarer un paramètre nommé **après** l'attrape-tout *args
# du coup ici le paramètre nommé `b` devient un *keyword-only* parameter

def must_name_b(a, *args, b=100, **kwds):
    print(f"a={a}, b={b}, args={args}, kwds={kwds}")
```

avec cette déclaration, je **dois nommer** le paramètre `b`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# je peux toujours faire ceci
must_name_b(1)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# mais si je fais ceci l'argument 2 
# va aller dans args
must_name_b(1, 2)
```

```{code-cell} ipython3
# pour passer b=2, je **dois** nommer mon argument
must_name_b(1, b=2)
```

+++ {"slideshow": {"slide_type": "slide"}, "tags": []}

### paramètre *positional-only*

en général on peut toujours nommer, des arguments même si le paramètre, est positionnel

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
tags: [gridwidth-1-2]
---
# on peut nommer un paramètre positionnel

def normal(a, b, c):
    print(f"{a=} {b=} {c=}")
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
tags: [gridwidth-1-2]
---
# la preuve    
normal(b=2, a=1, c=3)
```

imaginons que je veuille maintenant, au contraire **empêcher l'appelant de nommer `a`**  
pour cela je vais insérer artificiellement un `/` dans les paramètres; tous ceux qui sont déclarés **avant le `/`** seront dits *positional-only*, ce qui signifie qu'on ne pourra plus les nommer

```{code-cell} ipython3
# avec cette déclaration, on ne pourra plus nommer a

def cannot_name_a(a, /, b, c):
    print(f"{a=} {b=} {c=}")
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: [raises-exception]
---
# la preuve

cannot_name_a(b=2, a=1, c=3)
```

```{code-cell} ipython3
# par contre on peut toujours nommer les deux autres

cannot_name_a(1, c=3, b=2)
```

+++ {"slideshow": {"slide_type": "slide"}}

(label-args-unpacking)=
## *unpacking* des arguments

où on voit comment sont traités les formes `*L` et `**D`, mais **dans les arguments de la fonction** cette fois - on avait appelé ça (C) et (D)

cette fois le mécanisme est plutôt simple: cela revient à "déballer" le contenu de L (qui doit être itérable) ou `D` (qui doit être un dictionnaire)

voici un exemple: admettons que l'on ait calculé ces deux trucs

```python
L = [10, 20]
D = ['a': 1, 'b': 2]
```

alors l'appel `foo(100,  *L, 1000, *L, x=0,  **D1)` sera *récrit* comme ceci par Python

```{image} media/star-args.svg
:align: center
:width: 500px
```

comme on le voit, cela revient à insérer les contenus en place dans les arguments

* les éléments de `L` comme des arguments non nommés
* et ceux de `D` comme des arguments nommés

````{admonition} autant de fois qu'on veut

du coup on peut utiliser **autant de fois qu'on veut** ces deux formes dans un appel de fonction, cette fois-ci il n'y a pas d'ambigüité !
````

+++

### ex. (C) avec *

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
tags: [gridwidth-1-2]
---
def f4(a, b, c, d):
    print(f"{a=} {b=} {c=} {d=}")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

L = [1, 2, 3, 4]

f4(*L)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# n'importe quel itérable

f4(*"abcd")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

L1, L2 = (1, 2), (3, 4)

# 2 *params dans le même appel
# ne posent pas problème
f4(*L1, *L2)
```

```{code-cell} ipython3
:tags: []

# et on peut utiliser * avec une expression

f4(*range(1, 3), *range(10, 12))
```

### ex. (D) avec **

```{code-cell} ipython3
def f3(a, b, c):
    print(f"{a=} {b=} {c=}")
    
D = {'a': 1, 'c': 3, 'b': 2}

# équivalent à func(a=1, b=2, c=3)
f3(**D)
```

### retombées sur la syntaxe de base

sachez qu'on peut également faire ceci - qui n'a plus rien à voir avec les appels de fonction, mais qui utilise le même principe

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# construire une liste avec *args
l1 = [2, 3]
l2 = [4, 5]
[1, *l1, *l2, 6]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pareil avec un dictionnaire
d1 = {2: 'b', 3: 'c'}
d2 = {4: 'd', 5: 'e'}
{1: 'a', **d1, **d2, 6: 'f' }
```

## piège fréquent avec les arguments par défaut

* les valeurs par défaut sont évaluées à l’endroit de la déclaration de la fonction

```{code-cell} ipython3
i = 5

def f(arg = i):  # i vaut 5 au moment de la déclaration
    print(arg)
    
i = 6            # i est mis à 6 après la déclaration, ça
                 # n’est pas pris en compte

f()
```

### pas de mutable !

* les valeurs par défaut de f ne sont évaluées **qu’une fois** à la création de l’objet fonction
  (et mises dans **f.__defaults__**)

* si la **valeur par défaut est mutable**, elle pourra être modifiée dans la fonction
* et dans ce cas, la valeur par défaut **est modifiée pour l'appel suivant** !!

````{admonition} à retenir !
:class: attention 
➔ **ne jamais utiliser un mutable comme valeur par défaut !!!**
````

+++ {"slideshow": {"slide_type": "slide"}}

#### exemple

```{code-cell} ipython3
:tags: []

# on pourrait penser en lisant ceci, que sans préciser L on devrait 
# toujours retourner une liste [a]

def f(a, L = []):
    L.append(a)
    return L
```

```{code-cell} ipython3
:tags: []

# MAIS: la valeur par défaut est évaluée par l'instruction def:

f.__defaults__
```

```{code-cell} ipython3
:tags: []

# donc ici le premier coup OK, ça fait ce qu'on attend

f(1)
```

```{code-cell} ipython3
:tags: []

# sauf que ATTENTION, on a modifié ceci

f.__defaults__
```

```{code-cell} ipython3
# si bien qu'à l'appel suivant il se passe ceci !

f(2)
```

#### comment faire alors ?

la bonne pratique consiste à remplacer le mutable par `None` et à tester "à la main"  
de cette manière l'expression `[]` - qui crée effectivement la liste - est exécutée **à chaque fois** que nécessaire,  
au lieu d'une seule fois au moment du `def`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# la bonne pratique

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    print(L)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# comme ça pas d'embrouille

f(1)
f(2)
f(3)
```

+++ {"slideshow": {"slide_type": "slide"}}

## pour résumer

+++ {"slideshow": {"slide_type": ""}}

### 2 groupes d'arguments : positionnels et nommés

**attention**: les arguments ne sont pas pris dans l’ordre de l’appel !

1. en premier on résoud les arguments positionnels et `*args`
2. puis les arguments nommés et `**kwds`

+++

### le bon ordre pour les paramètres

l'ordre dans lequel il est conseillé de déclarer sa fonction reste toujours

```{list-table}

* - positionnels,
  - avec défaut,
  - forme `*` (1 max),
  - forme `**` (1 max)
```

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
  title: dunder methods
---

+++ {"slideshow": {"slide_type": ""}}

# classes : méthodes spéciales

aussi appelées *dunder methods*

+++

Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

+++ {"slideshow": {"slide_type": "slide"}}

## méthodes spéciales / *dunder methods*

* sur une classe on peut définir des **méthodes spéciales**  
* pour bien intégrer les objets dans le langage  
* c'est-à-dire donner du sens à des constructions du langage

c'est-à-dire donner un sens à des phrases commme:

* appeler les fonctions *builtin*: `len(obj)`, `int(obj)`
* opérateurs: e.g. `obj + x`  
* itération: `for item in obj`
* test d'appartenance: `x in obj` 
* indexation: `obj[x]` 
* et même appel! `obj(x)`
* etc...

+++ {"slideshow": {"slide_type": "slide"}}

## `len(obj)`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

class Classe:
    
    def __init__(self, students):
        self.students = students
        
    def __len__(self):
        return len(self.students)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

classe = Classe(['jean', 'laurent', 'benoit'])

len(classe)
```

de manière similaire : 

* `__int__(self)` pour redéfinir `int(obj)` et similaires

+++ {"slideshow": {"slide_type": "slide"}}

## opérateurs: `obj1 + obj2`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

class Classe:
    
    def __init__(self, students):
        self.students = students
        
    def __add__(self, other):
        return Classe(self.students + other.students)
    
    def __repr__(self):
        return f"[{len(self.students)} students]"
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

classe1 = Classe(['marie', 'claire'])
classe2 = Classe(['jean', 'laurent'])

classe1 + classe2
```

````{admonition} en réalité c'est un peu plus subtil
:class: admonition-small dropdown

dans la pratique, on peut aussi avoir à définir `__radd__` de façon à redéfinir le cas où on pourrait s'additionner avec des objets d'un autre type, comme des types *builtin* de nombres par exemple; mais ne nous égarons pas..
````

+++ {"slideshow": {"slide_type": "slide"}}

## itérations: `for item in obj:`

```{code-cell} ipython3
:tags: []

class Classe:

    def __init__(self, students):
        self.students = students

    def __iter__(self):
        """
        iterate on self as if it was self.students
        """
        return iter(self.students)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

classe = Classe(['jean', 'laurent', 'benoit'])

for s in classe:
    print(s)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et même d'ailleurs
x, y, z = classe
y
```

````{admonition} utiliser un générateur
:class: admonition-small

lorsque la logique d'itération devient moins triviale que de simplement "sous-traiter" le travail à un autre objet, on utilise fréquemment un générateur pour implémenter la *dunder* `__iter__`  
ici par exemple on aurait pu écrire
```python
    def __iter__(self):
        for s in self.students:
            yield s
```
````

+++ {"slideshow": {"slide_type": "slide"}}

## appartenance: `x in obj`

on l'a vu déjà avec la classe `Circle`:

```{code-cell} ipython3
:tags: [gridwidth-1-2]

class Classe:

    def __init__(self, students):
        self.students = students

    def __contains__(self, student):
        return student in self.students
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

classe = Classe(['jean', 'laurent', 'benoit'])

'jean' in classe
```

+++ {"slideshow": {"slide_type": "slide"}}

## indexations: `obj[x]`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

class Classe:

    def __init__(self, students):
        self.students = students

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.students[index]
        elif isinstance(index, str):
            if index in self.students:
                return index
            else:
                return None
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

classe = Classe(['jean', 'laurent', 'benoit'])

classe[1]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

classe['jean']
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

classe['pierre'] is None
```

+++ {"slideshow": {"slide_type": "slide"}}

## classe *callable*: `obj(x)`

on peut même donner du sens à `obj(x)`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# make it callable

class Line:
    """
    the line of equation y = ax + b
    """
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __call__(self, x):
        """
        can be used as function that
        computes y = ax+b given x
        """
        return self.a * x + self.b
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# cet objet se comporte comme une fonction

line = Line(2, 2)


# du coup c'est intéressant de pouvoir l'appeler
# comme si c'était réellement une fonction

line(1)
```

## classe *sortable*: `obj < obj2`

pour ne pas changer d'exemple, imaginons que l'on veuille pouvoir **trier** une collection d'instances de `Line`  
pour cela il suffit d'expliciter l'ordre entre les instances  
et pour cela une technique consiste à redéfinir la *dunder* `__lt__` (pour *lower than*)

ça se présenterait comme suit

```{code-cell} ipython3
# make it sortable

class Line:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"{self.a}x + {self.b}"


    # on définit l'ordre entre éléments, ici: self < other
    
    def __lt__(self, other):
        return (self.a, self.b) < (other.a, other.b)


lines = [ Line(3, 1), Line(1, 2), Line(3, -1), Line(2, 0)]
```

```{code-cell} ipython3
# du coup la classe sait comparer deux éléments entre eux

# prenons par exemple les deux premiers éléments
L1, L2, *_ = lines

# et comparons-les
L1 < L2
```

```{code-cell} ipython3
# du coup on peut trier ces éléments sans avoir à préciser la fonction de tri

sorted(lines)
```

````{admonition} trier, mais pas que
:class: tip
et pour le même prix on peut ainsi utiliser également tous les algorithmes qui reposent sur un ordre entre les éléments;  
par exemple `PriorityQueue`/`heapq` pour les queues de priorité, ou encore `bisect` pour la recherche binaire, ...
````

````{admonition} 1 sur 6
:class: dropdown info

pour notre exemple simple cela suffit bien, mais en toute rigueur pour pouvoir comparer deux objets il faudrait définir 6 opérateurs (`<`, `<=`, `>`, `>=`, `==` et `!=`); pour davantage de détails voyez notamment cette page 
<https://docs.python.org/3/library/functools.html#functools.total_ordering>
````

+++

## classe *hashable*: D[obj]

on a pu dire que les clés des dictionnaires devaient être des objets *non mutables*; c'est vrai pour les types de base du langage  
par contre lorsqu'il s'agit de classes *user-defined*, cette contrainte est levée si la classe implémente le **protocole dit des objets *hashables***

toujours avec notre exemple de la classe `Line`: on pourrait avoir envie de créer des ensembles d'objets de type `Line`; ou bien encore d'utiliser un objet `Line` comme un clé de dictionnaire

cela est possible par exemple comme ceci: la classe doit implémenter deux *dunder* méthodes `__eq__` et `__hash__`

```{code-cell} ipython3
# make it hashable

class Line:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b


    # pour définir à quelle condition deux objets
    # sont considérés égaux - au sens de == 
    
    def __eq__(self, other):
        return (self.a == other.a) and (self.f == other.b)


    # comment doit-on calculer le hash d'un objet Line ?

    def __hash__(self):
        # on n'a qu'à le hasher comme le tuple (a, b)
        return hash( (self.a, self.b) )
```

```{code-cell} ipython3
:lines_to_next_cell: 2

# on peut alors utiliser les objets dans un dict ou dans un set !

D, S = {}, set()
line = Line(0, 0)

D[line] = "Yes !"
S = {line, line}

print(f"{D=}, {len(S)=}")
```

+++ {"slideshow": {"slide_type": "slide"}}

## résumé
  
une classe peut définir des **méthodes spéciales**

* notamment le constructeur pour l'initialisation,
* souvent un afficheur pour `print()`
* optionnellement d'autres pour donner du sens à des constructions du langage sur ces objets
* ces méthodes ont toutes un nom en `__truc__` (*dunder methods*)

+++ {"slideshow": {"slide_type": "slide"}, "tags": []}

## pour en savoir plus

la (longue) liste exhaustive des méthodes spéciales est donnée dans la documentation officielle ici

<https://docs.python.org/3/reference/datamodel.html#special-method-names>

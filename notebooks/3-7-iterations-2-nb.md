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
  title: "les it\xE9rations (2/2)"
---

+++ {"slideshow": {"slide_type": ""}}

# itér.. (2/3) - compr. et genexpr

+++ {"slideshow": {"slide_type": "slide"}}

Licence CC BY-NC-ND, Thierry Parmentelat

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

+++ {"tags": []}

## compréhensions

très fréquemment on veut construire un mapping

### `map`

pour appliquer une fonction à un ensemble de valeurs

```{image} media/iter-map.svg
:align: center
```

+++ {"tags": []}

### `map` + `filter`

idem en excluant certaines entrées

```{image} media/iter-map-filter.svg
:align: center
```

+++ {"tags": ["gridwidth-1-2"]}

### compréhension de liste

c'est le propos de la compréhension (de liste):

```python
[expr(x) for x in iterable]
```

qui est équivalent à 

```python
result = []
for x in iterable:
    result.append(expr(x))
```

+++ {"tags": ["gridwidth-1-2"]}

### compréhension de liste avec filtre

si nécessaire on peut
ajouter un test de filtre:

```python
[expr(x) for x in iterable 
     if condition(x)]
```

qui est équivalent à 

```python
result = []
for x in iterable:
    if condition(x):
        result.append(expr(x))
```

+++

#### compréhensions de liste - exemple 1

sans filtre

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# la liste des carrés 
# des entiers entre 0 et 5

[x**2 for x in range(6)]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# si on décortique

result = []

for x in range(6):
    result.append(x**2)

result
```

#### compréhensions de liste - exemple 2

avec filtre

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# la liste des cubes
# des entiers pairs entre 0 et 5

[x**2 for x in range(6) if x % 2 == 0]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# si on décortique

result = []

for x in range(6):
    if x % 2 == 0:
        result.append(x**3)

result
```

### compréhension de liste - imbrications

* on peut **imbriquer plusieurs niveaux** de boucle
* la profondeur du résultat dépend **du nombre de `[`**  
  et **pas du nombre de `for`**

```{code-cell} ipython3
# une liste toute plate comme résultat
# malgré deux boucles for imbriquées
[10*x + y for x in (1, 2) for y in (1, 2)]
```

+++ {"cell_style": "center"}

#### compréhensions imbriquées - exemple

l'ordre dans lequel se lisent les compréhensions imbriquées:  
il faut imaginer des for imbriqués **dans le même ordre**

```{code-cell} ipython3
:tags: [gridwidth-1-2]

[10*x + y for x in range(1, 5) 
     if x % 2 == 0 
         for y in range(1, 5)
             if y % 2 == 1]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# est équivalent à
# (dans le même ordre)
L = []
for x in range(1, 5):
    if x % 2 == 0:
        for y in range(1, 5):
            if y % 2 == 1:
                L.append(10*x + y)
L
```

### compréhension d'ensemble

même principe exactement, mais avec des `{}` au lieu des `[]`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# en délimitant avec des {} 
# on construit une
# compréhension d'ensemble
{x**2 for x in range(-6, 7) 
    if x % 2 == 0}
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# rappelez-vous que {} est un dict
result = set()

for x in range(-6, 7):
    if x % 2 == 0:
        result.add(x**2)
        
result
```

### compréhension de dictionnaire

syntaxe voisine, avec un `:` pour associer clé et valeur

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# sans filtre
 
{x : x**2 for x in range(4)}
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# avec filtre

{x : x**2 for x in range(4) if x%2 == 0}
```

#### exemple : créer un index par une compréhension

un idiome classique :

* on a une liste d'éléments - beaucoup, genre $10^6$
* on veut pouvoir accéder **en temps constant**  
  à un élément à partir d'un id

* solution: créer un dictionnaire - qu'on appelle un *index*  
  (comme dans les bases de données)

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# créer un dict qui permet un accès direct à partir du nom
personnes = [
    {'nom': 'Martin', 'prenom': 'Julie', 'age': 18},
    {'nom': 'Dupont', 'prenom': 'Jean', 'age': 32},
    {'nom': 'Durand', 'prenom': 'Pierre', 'age': 25},  
]

# l'idiome pour créer un index
index = {personne['nom']: personne for personne in personnes}

index
```

```{code-cell} ipython3
# le concept est le même que dans une base de données
# en termes d'accès rapide à partir du nom qui jour le rôle d'id

index['Martin']
```

## expression génératrice

### performance des compréhensions

la compréhension **n'est pas l'arme absolue** ! elle a un **gros défaut**, c'est qu'on va toujours :

* parcourir **tout** le domaine
* et **allouer** de la mémoire   
* au moment où on évalue la compréhension,  
  i.e. **avant même** de faire quoi que ce soit d'autre

````{admonition} note

finalement c'est **exactement** la même discussion que itérateur *vs* itérable  
ou quand on avait comparé `range()` avec une liste
````

+++ {"slideshow": {"slide_type": "slide"}}

### expression génératrice

pour éviter ces problèmes: utiliser une *genexpr*

* ça se présente un peu comme une compréhension de liste  
* mais **avec des `()` à la place des `[]`**
* supporte les `if` et les imbrications  
  exactement comme les compréhensions

```{code-cell} ipython3
data = [0, 1]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# compréhension

C = [10*x + y for x in data for y in data]

for y in C:
    print(y)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# genexpr

G = (10*x + y for x in data for y in data)

for y in G:
    print(y)
```

### les genexprs sont des itérateurs

* même "contenu" que la compréhension
* mais pas la même implémentation: une *genexpr* est de type `generator` (en particulier c'est un **itérateur**)

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# compréhension

C = [x**2 for x in range(4)]

type(C), C
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# genexpr

G = (x**2 for x in range(4))

type(G), G
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# une compréhension est une vraie liste

C2 = [x**2 for x in range(100_000)]

import sys
sys.getsizeof(C2)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# les genexprs sont des itérateurs
# et donc sont tout petits

G2 = (x**2 for x in range(100_000))

sys.getsizeof(G2)
```

+++ {"slideshow": {"slide_type": "slide"}}

### compréhension ou genexpr ?

* les compréhensions de *dictionnaire* et d'*ensemble* sont souvent justifiées
* par contre, pour les *listes*: **toujours bien se demander** si on a vraiment besoin de **construire la liste**

* ou si au contraire on a juste **besoin d'itérer** dessus (souvent une seule fois d'ailleurs)

+++

* si on a vraiment besoin de cette liste, alors la compréhension est OK
* mais dans le cas contraire il faut **préférer un itérateur**, c'est le propos de l'**expression génératrice**
* qui souvent revient à remplacer `[]` par `()` - ou même juste enlever les `[]`

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["gridwidth-1-2"]}

apprenez à bien choisir entre compréhension et genexpr (les deux sont utiles)

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# remplissons une classe imaginaire
from random import randint

matieres = ('maths', 'français', 'philo')

def notes_eleve_aleatoires():
    return {matiere: randint(0, 20) for matiere in matieres}
```

```{code-cell} ipython3
:cell_style: center

# ici je crée une compréhension; pourquoi ?
notes_classe = [notes_eleve_aleatoires() for _ in range(4)]
notes_classe
```

```{code-cell} ipython3
# pour calculer la moyenne de la classe en maths
# pas besoin de garder les résultats intermédiaires
# du coup, on fabrique une genexpr
# en toute rigueur il aurait fallu écrire ceci
sum((notes_eleve['maths'] for notes_eleve in notes_classe)) / len(notes_classe)
```

```{code-cell} ipython3
# mais la syntaxe nous permet de nous en affranchir
# (remarquez une seul niveau de parenthèses, et l'absence de [])
sum(notes_eleve['maths'] for notes_eleve in notes_classe) / len(notes_classe)
```

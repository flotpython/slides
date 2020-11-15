# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: "les it\xE9rations en Python"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% slideshow={"slide_type": "-"}
#from plan import plan; plan("syntaxe", "itération")

# %% [markdown] slideshow={"slide_type": "slide"}
# # les itérations en Python

# %% [markdown]
# * la boucle `for` est la méthode **préférée**   
#   pour itérer sur un ensemble de valeurs
#
# * en général préférable au `while` en Python
#   * on peut faire un `for` sur n'importe quel itérable
#   * ce n'est pas le cas pour le `while`
#   * avec `for` c'est l'itérable qui se charge de la logique
# * de nombreuses techniques pour itérer de manière optimisée
#   * compréhensions
#   * itérateurs
#   * expressions génératrices
#   * générateurs

# %% [markdown] slideshow={"slide_type": "slide"}
# ## la boucle `for`

# %% [markdown] slideshow={"slide_type": ""}
# ```python
# for item in iterable:
#     bloc
#     aligné
# else:
#     bloc     # exécuté lorsque la boucle sort "proprement"
#     aligné   # c'est-à-dire pas avec un break
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `break` et `continue`

# %% [markdown]
# comme dans beaucoup d'autres langages :
#
# * `break` sort complètement de la boucle
# * `continue` termine abruptement l'itération courante et passe à la suivante
# * on parle toujours de la boucle **la plus imbriquée**
#
# l'instruction `else` attachée à un `for` est d'un usage plutôt rare en pratique

# %% cell_style="split" slideshow={"slide_type": "slide"}
liste = [10, 20, 40, 80, 120]

# la bonne façon de faire un for

for item in liste:
    print(item, end=" ")

# %% cell_style="split"
# et **non pas**
# cette horrible périphrase !

for i in range(len(liste)):
    item = liste[i]
    print(item, end=" ")

# %% [markdown] cell_style="center"
# * voir [une revue de code intéressante ici](http://sametmax.com/revue-de-code-publique/)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### boucle `for` et itérable

# %% [markdown]
# c'est quoi un itérable ?
#
# * par définition, c'est un objet .. sur lequel on peut faire un `for`
# * notamment avec les séquences natives : chaînes, listes, tuples, ensembles
# * et aussi dictionnaires, et des tas d'autres objets, mais patience

# %% cell_style="split"
# une chaine est un itérable

chaine = "un été"
for char in chaine:
    print(char, end=" ")

# %% cell_style="split"
# un ensemble aussi

ensemble = {10, 40, 80} 
for element in ensemble:
    print(element, end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### boucle `for` sur un dictionnaire

# %% [markdown]
# * on peut facilement itérer sur un dictionnaire
# * mais il faut choisir si on veut le faire 
#   * sur les clés,
#   * sur les valeurs,
#   * ou sur les deux
# * c'est à ça que servent les méthodes
#   * `keys()`
#   * `values()`
#   * `items()`

# %% [markdown] slideshow={"slide_type": "slide"}
# #### boucle `for` sur un dictionnaire

# %% cell_style="split"
agenda = {
    'paul': 12, 
    'pierre': 14,
    'jean': 16,
}

# %% cell_style="split"
# l'unpacking permet d'écrire 
# un code élégant
for key, value in agenda.items():
    print(f"{key} → {value}")

# %% [markdown]
# ---

# %% cell_style="split"
# un raccourci
for key in agenda:      # ou agenda.keys()
    print(key, end=" ")

# %% cell_style="split"
for value in agenda.values():
    print(value, end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple de boucles

# %%
# boucle (1)
for n in range(2, 10):
    # boucle (2)
    for x in range(2, n):
        if n % x == 0:
            print(n, ' = ' , x , '*', n//x)
            # on sort de la boucle (2)
            break
    else:
        print(n, 'est un nombre premier')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### opérations sur les itérables

# %% [markdown]
# Python propose des outils pour **créer** et **combiner** les itérables:
#
# * fonctions natives *builtin* :
#   * `range`, `enumerate`, et `zip`
# * dans un module dédié `itertools`:
#   * `chain`, `cycle`, `islice`, ...

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `range`

# %% [markdown]
# * `range` crée un itérable qui itère sur des nombres entiers
# * arguments : même logique que le slicing
#   * début (inclus), fin (exclus), pas
# * curiosité :
#   * si un seul argument, c'est **la fin**

# %% cell_style="split"
# les nombres pairs de 10 à 20
for i in range(10, 21, 2):
    print(i, end=" ")

# %% cell_style="split"
# le début par défaut est 0
for i in range(5):
    print(i, end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un itérateur n'est **pas une liste**

# %% [markdown]
# * l'objet retourné par `range` **n'est pas une liste**
# * au contraire il crée un objet tout petit
# * qui contient seulement la logique de l'itération
# * la preuve:

# %% cell_style="split"
# 10**20 c'est 100 millions de Tera

iterateur = range(10**20)
iterateur

# %% cell_style="split"
for item in iterateur:
    if item >= 5:
        break
    print(item, end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# #### un itérateur n'est **pas une liste**

# %% [markdown] slideshow={"slide_type": ""}
# du coup un itérateur peut même .. ne jamais terminer :

# %%
from itertools import count
# count?

# %%
for i in count():
    print(i, end=" ")
    if i >= 5:
        break

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `enumerate`

# %% [markdown] cell_style="center"
# * si on a vraiment besoin de l'index, il suffit d'utiliser la *builtin* `enumerate`

# %% cell_style="split"
L = [1, 10, 100, 1000]

# %% cell_style="split"
# quand on a besoin 
# de l'indice dans la boucle
for i in range(len(L)):
    print(f"{i}: {L[i]}")

# %% cell_style="split"
# on utilise enumerate
for i, item in enumerate(L):
    print(f"{i}: {item}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](pictures/iter-enumerate.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `enumerate`

# %% [markdown]
# * typiquement utile sur un fichier
# * pour avoir le numéro de ligne 
# * remarquez le deuxième argument de `enumerate` pour commencer à 1 

# %%
with open("../data/une-charogne.txt") as feed:
    for lineno, line in enumerate(feed, 1):
        print(f"{lineno}:{line}", end="")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `zip`

# %% [markdown]
# `zip` fonctionne un peu comme `enumerate` mais entre deux itérables:
#
# ![](pictures/iter-zip.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `zip`

# %% cell_style="split"
liste1 = [10, 20, 30]
liste2 = [100, 200, 300]

# %% cell_style="split"
for a, b in zip(liste1, liste2):
    print(f"{a}x{b}", end=" ")

# %% [markdown]
# **NOTES**: 
#
# * `zip` fonctionne avec autant d'argument qu'on veut
# * elle s'arrête dès que l'entrée la plus courte est épuisée
# * du coup on pourrait voir `enumerate` comme: 
#   * `enumerate(iterable)` $\Leftrightarrow$ `zip(count(), iterable)`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le module `itertools` - assemblage d'itérables

# %% [markdown]
# on trouve dans le module `itertools` plusieurs utilitaires très pratiques :
#
# * `count` pour énumérer les entiers (un `range` sans borne)
# * `chain` pour chainer plusieurs itérables
# * `cycle` pour rejouer un itérable en boucle
# * `repeat` pour énumérer plusieurs fois le même objet
# * `islice` pour n'énumérer que certains morceaux
# * `zip_longest` fonctionne comme `zip` mais s'arrête au morceau le plus long

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `enumerate(iterable) = zip(count(), iterable)`

# %% slideshow={"slide_type": ""}
# par exemple on peut récrire enumerate
# à base de zip et count
L

# %% cell_style="split"
# zip s'arrête dès que 
# l'un de ses morceaux s'arrête
for index, item in zip(count(), L):
    print(f"{index} {item}")

# %% [markdown] cell_style="split"
# ![](../pictures/iter-zip-count.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `chain()`, `cycle()` et `repeat()`

# %% cell_style="center" slideshow={"slide_type": ""}
from itertools import chain, cycle, repeat
data1 = (10, 20, 30)
data2 = (100, 200, 300)

# %% cell_style="center"
# chain()
for i, d in enumerate(chain(data1, data2)):
    print(f"{i}x{d}", end=" ")

# %%
# cycle() ne termine jamais non plus

for i, d in enumerate(cycle(data1)):
    print(f"{i}x{d}", end=" ")
    if i >= 10:
        break

# %%
# repeat()
padding = repeat(1000, 3)

for i, d in enumerate(chain(data1, padding, data2)):
    print(f"{i}x{d}", end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `islice()`

# %% cell_style="split"
# avec islice on peut par exemple 
# sauter une ligne sur deux dans un fichier
from pathlib import Path

# on crée un fichier 
with Path('islice.txt').open('w') as f:
    for i in range(6):
        f.write(f"{i}**2 = {i**2}\n")

# %% cell_style="split"
# pour ne relire qu'une ligne sur deux

from itertools import islice

with Path('islice.txt').open() as f:
    for line in islice(f, 0, None, 2):
        print(line, end="")

# %% cell_style="split"
# ou zapper les 3 premières

from itertools import islice

with Path('islice.txt').open() as f:
    for line in islice(f, 3, None):
        print(line, end="")

# %% cell_style="split"
# ou ne garder que les 3 premières

from itertools import islice

with Path('islice.txt').open() as f:
    for line in islice(f, 3):
        print(line, end="")

# %% [raw] slideshow={"slide_type": "slide"}
# ### `zip_longest()`

# %% cell_style="split"
from itertools import zip_longest
for i, d in zip_longest(
        range(6), L, fillvalue='X'):
    print(f"{i} {d}")

# %% [markdown] cell_style="split"
# ![](../pictures/iter-zip-longest.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le module `itertools` - combinatoires

# %% [markdown]
# Le module `itertools` propose aussi quelques combinatoires usuelles:
#
# * `product`: produit cartésien de deux itérables
# * `permutations`: les permutations ($n!$)
# * `combinations`: *p parmi n*
# * et d'autres... 
# * https://docs.python.org/3/library/itertools.html

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le module `itertools`

# %%
from itertools import product

dim1 = (1, 2, 3)
dim2 = (10, 20, 30)

for i, (d1, d2) in enumerate(product(dim1, dim2)):
    print(f"i={i}, d1={d1} d2={d2}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exercice: code de Vigenère

# %% [markdown]
# Voir [sur wikipedia](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re)

# %% cell_style="split"
from string import ascii_lowercase
ascii_lowercase

# %% cell_style="split"
from string import ascii_letters
ascii_letters

# %% cell_style="split"
# le codepoint d'un caractère
ord('a')

# %% cell_style="split"
# la caractère associé 
# à un codepoint
chr(97)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## boucles `for` : limite importante

# %% [markdown]
# * **règle très importante:** à l'intérieur d'une boucle
# * il ne faut **pas modifier l’objet** sur lequel on itère
# * on peut, par contre, en faire une copie

# %% [markdown] cell_style="split"
# ce code-ci provoque une boucle infinie
# ```
# L = ['a', 'b', 'c']
# for i in L:
#     if i == 'c':
#         L.append(i)
# ```

# %% cell_style="split"
# il suffit de prendre la précaution
# de faire une shallow copie
L = ['a', 'b' , 'c']
for i in L[:]:
    if i == 'c':
        L.append(i)
L

# %% [markdown] slideshow={"slide_type": "slide"}
# ## boucles pythoniques ou pas

# %% [markdown]
# ### soyez explicite

# %% cell_style="split"
D = {
    'alice': 35,
    'bob': 9,
    'charlie': 6,
}

# pas pythonique (implicite)
for t in D.items():         
    print(t[0], t[1])

# %% cell_style="split"
# pythonique (explicite)

for nom, age in D.items():
    print(nom, age)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### une vilaine boucle

# %%
L = [x**2 for x in (-2, 3, 10)]

# %% cell_style="split"
# il faut faire bien sûr
for item in L:
    print(item)

# %% cell_style="split"
# et NE SURTOUT PAS faire
for i in range(len(L)):
    print(L[i])

# %% [markdown]
# et en plus, si vous remplacez la compréhension par une expression génératrice, la premiere forme ne marche plus du tout 

# %% [markdown] slideshow={"slide_type": "slide"}
# ## compréhensions

# %% [markdown]
# très fréquemment on veut construire un mapping

# %% [markdown] cell_style="split"
# * appliquer une fonction à un ensemble de valeurs: `map`
#
# ![](pictures/iter-map.png)

# %% [markdown] cell_style="split"
# * idem en excluant certaines entrées: `map` + `filter`
#
# ![](pictures/iter-map-filter.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### compréhension de liste

# %% [markdown] cell_style="split"
# c'est le propos de la compréhension (de liste):
#
# ```python
# [expression(x) for x in iterable
#                  if condition(x)]
# ```

# %% [markdown] cell_style="split"
# équivalent à 
#
# ```python
# result = []
# for x in iterable:
#     if condition(x):
#         result.append(expression(x))
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# #### compréhensions de liste - équivalence

# %% cell_style="split"
[x**3 for x in range(6) if x % 2 == 0]

# %% cell_style="split"
result = []
for x in range(6):
    if x % 2 == 0:
        result.append(x**3)
result

# %% [markdown] slideshow={"slide_type": "slide"}
# ### compréhension de liste - imbrications

# %% [markdown]
# * la clause `if condition` est bien entendu optionnelle
# * on peut imbriquer plusieurs niveaux de boucle
#   * la profondeur du résultat dépend du nombre de `[`

# %%
# une liste toute plate comme résultat
# malgré deux boucles for imbriquées
[x+y for x in (1, 2) for y in (3, 4)]

# %% [markdown] slideshow={"slide_type": "slide"}
# #### compréhensions imbriquées - équivalence

# %% [markdown] cell_style="center"
# l'ordre dans lequel se lisent les compréhensions imbriquées:

# %% cell_style="split"
[(x, y) for x in range(7) 
        if x % 2 == 0 
            for y in range(x) 
                if y % 2 == 1]

# %% cell_style="split"
# est équivalent à
L = []
for x in range(7):
    if x % 2 == 0:
        for y in range(x):
            if y % 2 == 1:
                L.append((x, y))
L

# %% [markdown] slideshow={"slide_type": "slide"}
# ### compréhension d'ensemble

# %% [markdown]
# même principe exactement, mais avec des `{}` au lieu des `[]`

# %% cell_style="split"
# en délimitant avec des {} 
# on construit une
# compréhension d'ensemble
{x**2 for x in range(-4, 5) 
 if x % 2 == 0}

# %% cell_style="split"
# ATTENTION, rappelez-vous
# que {} est un dict !
result = set()

for x in range(-4, 5):
    if x % 2 == 0:
        result.add(x**2)
        
result

# %% [markdown] slideshow={"slide_type": "slide"}
# ### compréhension de dictionnaire

# %% [markdown]
# syntaxe voisine, avec un `:` pour associer clé et valeur

# %%
# créer une table qui permet un accès direct à partir du nom
personnes = [
    {'nom': 'Martin', 'prenom': 'Julie', 'age': 18},
    {'nom': 'Dupont', 'prenom': 'Jean', 'age': 32},
    {'nom': 'Durand', 'prenom': 'Pierre', 'age': 25},  
]

hash = {personne['nom']: personne for personne in personnes}
hash

# %%
# ici hash ressemble à un index dans une base de données
# en termes d'accès rapide à partir du nom
hash['Martin']


# %% [markdown] slideshow={"slide_type": "slide"}
# ### performance des compréhensions

# %% [markdown]
# la compréhension **n'est pas l'arme absolue**  
# elle a un **gros défaut**, c'est qu'on va toujours :
#
# * parcourir tout le domaine
# * allouer de la mémoire  
# au moment où on évalue la compréhension,  
# i.e. **avant même** de faire quoi que ce soit d'autre  

# %% cell_style="center" slideshow={"slide_type": ""}
# une fonction qui ne parcourt pas
# entièrement son paramètre iterable
def search_100(iterable):
    for i in iterable:
        if i == 100:
            return True


# %% cell_style="split"
# cherchons 100 parmi les <n> premiers carrés
n = 10**6

# avec une compréhension 
# on fait beaucoup de travail
# pour rien
# %timeit search_100([x**2 for x in range(n)])

# %% cell_style="split"
# avec une exp. génératrice ...
# entre 50 et 100.000 fois plus rapide,
# c'est normal :
# on n'a pas eu besoin de créer
# la liste des carrés 
# %timeit search_100(x**2 for x in range(n))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## expression génératrice et générateur

# %% [markdown]
# * les compréhensions de dictionnaire et d'ensemble sont souvent justifiées
# * par contre, pour les listes: **toujours bien se demander**  
#   si on a vraiment besoin de **construire la liste**
#
# * ou si au contraire on a juste **besoin d'itérer** dessus  
#   souvent une seule fois d'ailleurs

# %% [markdown]
# * si on a vraiment besoin de cette liste  
#   alors la compréhension est OK
#
# * mais dans le cas contraire il faut **préférer un itérateur**   
#   c'est le propos de l'**expression génératrice**
#
# * qui souvent revient à simplement enlever les `[]`  
#   ou les remplacer par des `()`
#
# * exemple...

# %% [markdown] slideshow={"slide_type": "slide"}
# ### expression génératrice

# %%
# j'ai un ensemble de valeurs
# je cherche à trouver la somme des carrés de ces valeurs
data = [-10, 5, -9, 15, -21, 7, 12]

# %% cell_style="split"
# je peux faire ceci
# je calcule la liste des carrés
carres = [x**2 for x in data]
carres

# %% cell_style="split"
# j'utilise ensuite la builtin `max` 
sum(carres)

# %%
# mais en fait je peux remplacer ceci
sum([x**2 for x in data])

# %%
# par juste ceci - remarquez l'absence des []
sum(x**2 for x in data)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### expression génératrice

# %% cell_style="split"
# on peut examiner ces deux objets
[x**2 for x in data]

# %% cell_style="split"
# attention ici il faut les parenthèses
(x**2 for x in data)

# %%
# c'est un itérateur !
generator1 = (x**2 for x in data)

# %% cell_style="split"
next(generator1)

# %% cell_style="split"
next(generator1)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### expression génératrice

# %%
# remplissons une classe imaginaire
from random import randint

matieres = ('maths', 'français', 'philo')
eleves = ('jean', 'julie', 'marie', 
          'apolline', 'mathilde', 'adrien')

def eleve_alea():
    return [randint(0, 20) for matiere in matieres]

classe = [eleve_alea() for eleve in eleves]

# %%
# la moyenne de la classe en maths
notes_maths = [maths for maths, *_ in classe]
notes_maths

# %%
moyenne = sum(notes_maths) / len(notes_maths)
moyenne

# %%
# observez l'absence des []
sum(maths for maths, *_ in classe) / len(eleves)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### fonction génératrice

# %% [markdown]
# * une dernière forme très commune d'itérateurs
# * décrite sous la forme d'une fonction  
#   qui fait `yield` au lieu de `return`
# * souvent appelé simplement *générateur* (par abus de langage car techniquement l'expression génératrice
#   est un générateur aussi)
#
# * c'est plus clair avec un exemple

# %% cell_style="split"
def squares(n):
    for i in range(n):
        yield i**2


# %% cell_style="split"
for square in squares(3):
    print(square, end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# #### fonction génératrice

# %% cell_style="split"
# voyons un peu cet objet
generator2 = squares(4)
generator2

# %% cell_style="split"
# ça ressemble beaucoup 
# à une expression génératrice
next(generator2)

# %%
# c'est en effet un iterateur
iter(generator2) is generator2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### expression génératrice *vs* fonction génératrice

# %%
# generator1 provient d'une expression génératrice
# generator2 provient d'une fonction génératrice

# %% cell_style="split"
type(generator1)

# %% cell_style="split"
type(generator2)


# %% [markdown]
# * les deux formes de générateur sont de même type
# * la fonction a une puissance d'expression supérieure
# * notamment elle permet de conserver l'état  
#   sous la forme de variables locales
#
# * et même en fait c'est plus fort que ça  
#   car la fonction génératrice peut en appeler d'autres

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `yield from`

# %% [markdown]
# partant d'une fonction génératrice qui énumère  
# tous les diviseurs d'un entier (1 et lui-même exclus)

# %% cell_style="split"
def divs(n):
    for i in range(2, n):
        if n % i == 0:
            yield i

# %% cell_style="split"


for div in divs(30):
    print(div, end=" ")


# %% [markdown]
# * maintenant si je veux écrire une fonction génératrice  
#   qui énumère tous les diviseurs des diviseurs de `n`
#
# * il s'agit donc d'une fonction génératrice qui en appelle une autre
# * il y a nécessité pour une syntaxe spéciale: `yield from`

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `yield from`

# %% cell_style="split"
def divdivs(n):
    for i in divs(n):
        yield from divs(i)


# %% cell_style="split"
for div in divdivs(30):
    print(div, end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### fonction génératrice - épilogue

# %% [markdown]
# pour évaluer la boucle `for` dans ce dernier cas:
#
# * la **pile** principale (de la fonction qui fait `for`)
# * **et** une **pile** annexe qui évalue la fonction génératrice
# * et qui se fait "mettre au congélateur" à chaque itération de la boucle
# * l'état de l'itération: toutes les variables locales de la pile annexe
#   * les deux `i` dans l'exemple précédent
#
# c'est cette propriété qui est utilisée pour implémenter la librairie asynchrone `asyncio` 

# %% [markdown] slideshow={"slide_type": "slide"}
# ### sous le capot de la boucle `for`

# %% [markdown] cell_style="split"
# lorsqu'on itère sur un itérable avec itérateur

# %% cell_style="split"
iterable = [10, 20, 30]

# %% [markdown]
# sous le capot, la boucle `for` va faire:
#
#   * créer un itérateur en appelant `iter(iterable)`
#   * appeler `next()` sur cet itérateur
#   * jusqu'à obtenir l'exception `StopIteration`

# %% cell_style="split" slideshow={"slide_type": "slide"}
for item in iterable:
    print(item)

# %% cell_style="split" slideshow={"slide_type": ""}
iterateur = iter(iterable)
while True:
    try:
        item = next(iterateur)
        print(item)
    except StopIteration:
        # print("fin")
        break


# %% [markdown] slideshow={"slide_type": "slide"}
# #### sous le capot de la boucle `for`

# %% [markdown]
# * `next()` et `iter()` sont des fonctions natives
# * et naturellement:
#   * `iter(obj)` appelle `obj.__iter__()`
#   * `next(obj)` appelle `obj.__next__()`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## itérations et itérables (partie optionnelle)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### rendre un objet itérable

# %% [markdown]
# * en python, avec les classes, on peut 
#   * se définir des types utilisateur
#   * et bien les intégrer dans le langage 
# * par exemple, il existe un *protocole* 
#   * pour rendre un objet itérable
#   * i.e. pour pouvoir l'utiliser dans un for
# * deux moyens
#   * via `__getitem__` (une séquence - accès direct)
#   * via `__iter__()` qui doit retourner un itérateur

# %% [markdown] slideshow={"slide_type": "slide"}
# ### itérable avec `__getitem__`

# %% [markdown]
# * si votre objet est une séquence
# * vous pouvez définir la méthode `__getitem__()`
#   * qui sera alors appelée par le `for` 
#   * avec en argument `0`, `1`, ...
#   * jusqu'à ce que `__getitem__` lève `StopIteration`
# * c'est adapté pour des objets qui ont un accès direct 
#   * à leurs sous-composants
# * technique assez *old-school* 
#   * conservé pour compatibilité
#   * mais on n'en parle plus dans la suite du cours

# %% cell_style="split" slideshow={"slide_type": "slide"}
# un itérable implémenté avec __getitem__

class PseudoSequence:
    
    def __init__(self, top):
        self.top = top
        
    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self.top: 
            return 2 ** index
        else:
            raise IndexError


# %% cell_style="split"
seq = PseudoSequence(4)
for i in seq:
    print(i)

# %% cell_style="split"
seq[0], seq[2]

# %% [markdown] slideshow={"slide_type": "slide"}
# ### itérable avec itérateur

# %% [markdown]
# * on peut rendre un objet **itérable**
#   * en écrivant la méthode magique `__iter__()`  
#     qui doit retourner un itérateur
#
# * Q: d'accord, mais alors c'est quoi un itérateur ?  
#   A: ici à nouveau il y a un *protocole*

# %% [markdown]
# * protocole **itérateur**
#   * une méthode `__next__()`  
#     qui à chaque appel retourne l’élément suivant
#     ou qui lève une exception `StopIteration`  
#     lorsqu’il n’y a plus d’élément à retourner
#
#   * une méthode `__iter__()` qui retourne l’itérateur lui-même
#     * et donc un itérateur est lui-même itérable

# %% [markdown] slideshow={"slide_type": "slide"}
# ### séparer itérateur et itérable

# %% [markdown]
# * le plus souvent possible
#   * on définit les itérateurs "sans donnée"
#   * comme `range()` ou `count()`
#   * ou comme des générateurs
# * lorsqu'on définit un itérateur sur une "vraie" structure de données
#   * l'itérable contient les données
#   * l'iterateur ne contient **que** la logique/état d'itération
#   * il est important alors **séparer** les deux objets
#   * ne serait-ce que pour pouvoir faire des boucles imbriquées

# %% [markdown] slideshow={"slide_type": "slide"}
# #### séparer itérateur et itérable

# %% cell_style="center"
liste = [0, 10, 100]

# %% cell_style="split"
for item in liste:
    print(item, end=" ")

# %% cell_style="split"
# avec une seule boucle, 
# on peut itérer sur l'itérateur
iterator = iter(liste)

for item in iterator:
    print(item, end=" ")

# %% cell_style="split"
# avec deux boucles par contre
for item1 in liste:
    for item2 in liste:
        print(f"{item1}x{item2}")

# %% cell_style="split"
# ça ne fonctionne plus du tout !
iterator = iter(liste)

for item1 in iterator:
    for item2 in iterator:
        print(f"{item1}x{item2}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### utilisation des itérables

# %% [markdown]
#
# * on a défini les itérables par rapport à la boucle `for` 
# * mais plusieurs fonctions acceptent en argument des itérables
# * `sum`, `max`, `min`
# * `map`, `filter`
# * etc...

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple de la puissance des itérateurs

# %% [markdown]
# * imaginons que je veuille afficher toutes les lignes d’un fichier qui contienne le mot 'matin'
# * est-ce possible de le faire en seulement 4 lignes ?
# * sans notation cryptique et incompréhensible

# %%
with open('../data/une-charogne.txt') as feed:
    for lineno, line in enumerate(feed, 1):
        if 'matin' in line:
            print(f"{lineno}:{line}", end="")


# %% [markdown] slideshow={"slide_type": "slide"}
# ### quel objet est itérable ?

# %% [markdown]
# * il existe beaucoup d’objets itérables en python
#   * tous les objets séquence: listes, tuples, chaînes, etc.
#   * les sets, les dictionnaires
#   * les vues (dict.keys(), dict.values()), etc.
#   * les fichiers
#   * les générateurs
# * il faut les utiliser, c’est le plus rapide et le plus lisible

# %% [markdown] slideshow={"slide_type": "slide"}
# ### quel objet est un itérateur ?

# %% [markdown] cell_style="split"
# * on peut voir si  
#   `iter(obj) is obj`
#

# %% cell_style="split"
def is_iterator(obj):
    return iter(obj) is obj


# %% [markdown]
# * à la lumière de ce qu'on a vu
#   * une liste **n'est pas** son propre itérateur
#   * un fichier **est** son propre itérateur

# %% cell_style="split" slideshow={"slide_type": "slide"}
# un fichier est son propre itérateur
with open("../data/une-charogne.txt") as F:
    print("propre itérateur ? ",
          is_iterator(F))

# %% cell_style="split"
# la liste non
L = list(range(5))
print("propre itérateur ? ",
      is_iterator(L))

# %% cell_style="split"
# range() non plus 
R = range(5)
print("propre itérateur ? ",
      is_iterator(R))

# %% cell_style="split"
# range() non plus 
Z = zip(L, L)
print("propre itérateur ? ",
      is_iterator(Z))

# %% [markdown]
# * de manière générale, un objet qui est un itérateur  
#   ne peut être itéré qu'une seule fois
#
# * attention donc par exemple à ne pas essayer  
#   d'itérer plusieurs fois sur le même objet `zip` 

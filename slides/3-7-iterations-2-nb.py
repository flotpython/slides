# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -rise, -version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: "les it\xE9rations (2/2)"
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# Licence CC BY-NC-ND, Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown] slideshow={"slide_type": ""}
# # les itérations (2/2)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## compréhensions

# %% [markdown]
# très fréquemment on veut construire un mapping

# %% [markdown] cell_style="split"
# * appliquer une fonction à un ensemble de valeurs: `map`
#
# ![](media/iter-map.svg)

# %% [markdown] cell_style="split"
# * idem en excluant certaines entrées: `map` + `filter`
#
# ![](media/iter-map-filter.svg)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### compréhension de liste

# %% [markdown] cell_style="split"
# c'est le propos de la  
# compréhension (de liste):
#
# ```python
# [expr(x) for x in iterable]
# ```

# %% [markdown] cell_style="split"
# qui est  
# équivalent à 
#
# ```python
# result = []
# for x in iterable:
#     result.append(expr(x))
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### compréhension de liste avec filtre

# %% [markdown] cell_style="split"
# si nécessaire on peut
# ajouter un test de filtre:
#
# ```python
# [expr(x) for x in iterable 
#      if condition(x)]
# ```

# %% [markdown] cell_style="split"
# qui est  
# équivalent à 
#
# ```python
# result = []
# for x in iterable:
#     if condition(x):
#         result.append(expr(x))
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# #### compréhensions de liste - exemple 1

# %% [markdown]
# sans filtre

# %% cell_style="split"
# la liste des carrés 
# des entiers entre 0 et 5

[x**2 for x in range(6)]

# %% cell_style="split"
# si on décortique

result = []

for x in range(6):
    result.append(x**2)

result

# %% [markdown] slideshow={"slide_type": "slide"}
# #### compréhensions de liste - exemple 2

# %% [markdown]
# avec filtre

# %% cell_style="split"
# la liste des cubes
# des entiers pairs entre 0 et 5

[x**2 for x in range(6) if x % 2 == 0]

# %% cell_style="split"
# si on décortique

result = []

for x in range(6):
    if x % 2 == 0:
        result.append(x**3)

result

# %% [markdown] slideshow={"slide_type": "slide"}
# ### compréhension de liste - imbrications

# %% [markdown]
# * on peut **imbriquer plusieurs niveaux** de boucle
# * la profondeur du résultat dépend **du nombre de `[`**  
#   et **pas du nombre de `for`**

# %%
# une liste toute plate comme résultat
# malgré deux boucles for imbriquées
[10*x + y for x in (1, 2) for y in (1, 2)]

# %% [markdown] slideshow={"slide_type": "slide"}
# #### compréhensions imbriquées - exemple

# %% [markdown] cell_style="center"
# l'ordre dans lequel se lisent les compréhensions imbriquées:  
# il faut imaginer des for imbriqués **dans le même ordre**

# %% cell_style="split"
[10*x + y for x in range(1, 5) 
     if x % 2 == 0 
         for y in range(1, 5)
             if y % 2 == 1]

# %% cell_style="split"
# est équivalent à
# (dans le même ordre)
L = []
for x in range(1, 5):
    if x % 2 == 0:
        for y in range(1, 5):
            if y % 2 == 1:
                L.append(10*x + y)
L

# %% [markdown] slideshow={"slide_type": "slide"}
# ### compréhension d'ensemble

# %% [markdown]
# même principe exactement, mais avec des `{}` au lieu des `[]`

# %% cell_style="split"
# en délimitant avec des {} 
# on construit une
# compréhension d'ensemble
{x**2 for x in range(-6, 7) 
    if x % 2 == 0}

# %% cell_style="split"
# rappelez-vous que {} est un dict
result = set()

for x in range(-6, 7):
    if x % 2 == 0:
        result.add(x**2)
        
result

# %% [markdown] slideshow={"slide_type": "slide"}
# ### compréhension de dictionnaire

# %% [markdown]
# syntaxe voisine, avec un `:` pour associer clé et valeur

# %% cell_style="split"
# sans filtre
 
{x : x**2 for x in range(4)}

# %% cell_style="split"
# avec filtre

{x : x**2 for x in range(4) if x%2 == 0}

# %% [markdown] slideshow={"slide_type": "slide"} cell_style="center"
# #### exemple : créer un index par une compréhension

# %% [markdown]
# un idiome classique :
#
# * on a une liste d'éléments - beaucoup, genre $10^6$
# * on veut pouvoir accéder **en temps constant**  
#   à un élément à partir d'un id
#
# * solution: créer un dictionnaire - qu'on appelle un *index*  
#   (comme dans les bases de données)

# %% slideshow={"slide_type": "slide"}
# créer une table qui permet un accès direct à partir du nom
personnes = [
    {'nom': 'Martin', 'prenom': 'Julie', 'age': 18},
    {'nom': 'Dupont', 'prenom': 'Jean', 'age': 32},
    {'nom': 'Durand', 'prenom': 'Pierre', 'age': 25},  
]

index = {personne['nom']: personne for personne in personnes}
index

# %%
# le concept est le même que dans une base de données
# en termes d'accès rapide à partir du nom qui jour le rôle d'id
index['Martin']

# %% [markdown] slideshow={"slide_type": "slide"}
# ## expression génératrice

# %% [markdown] slideshow={"slide_type": ""}
# ### performance des compréhensions
#
# la compréhension **n'est pas l'arme absolue**  
# elle a un **gros défaut**, c'est qu'on va toujours :
#
# * parcourir **tout** le domaine
# * et **allouer** de la mémoire   
# * au moment où on évalue la compréhension,  
#   i.e. **avant même** de faire quoi que ce soit d'autre

# %% [markdown]
# <div class=note>
#
# finalement c'est **exactement** la même discussion que itérateur *vs* itérable  
# ou quand on avait comparé `range()` avec une liste
#     
# </div>    

# %% [markdown] slideshow={"slide_type": "slide"}
# ### expression génératrice
#
# * ça se présente un peu comme une compréhension de liste  
# * mais **avec des `()` à la place des `[]`**
# * supporte les `if` et les imbrications  
#   exactement comme les compréhensions

# %%
data = [0, 1]

# %% cell_style="split"
# compréhension

C = [10*x + y for x in data for y in data]

for y in C:
    print(y)

# %% cell_style="split"
# genexpr

G = (10*x + y for x in data for y in data)

for y in G:
    print(y)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### les genexprs sont des itérateurs

# %% [markdown]
# * même "contenu" que la compréhension
# * mais pas la même implémentation: les genexps sont de  
#   type `generator` (en particulier ce sont des **itérateurs**)

# %% cell_style="split"
# compréhension

C = [x**2 for x in range(4)]

type(C), C

# %% cell_style="split"
# genexpr

G = (x**2 for x in range(4))

type(G), G

# %% cell_style="split"
# une compréhension est une vraie liste

C2 = [x**2 for x in range(100_000)]

import sys
sys.getsizeof(C2)

# %% cell_style="split"
# les genexprs sont des itérateurs
# et donc sont tout petits

G2 = (x**2 for x in range(100_000))

sys.getsizeof(G2)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### compréhension ou genexpr ?
#
# * les compréhensions de *dictionnaire* et d'*ensemble* sont souvent justifiées
# * par contre, pour les *listes*: **toujours bien se demander**  
#   si on a vraiment besoin de **construire la liste**
#
# * ou si au contraire on a juste **besoin d'itérer** dessus  
#   (souvent une seule fois d'ailleurs)

# %% [markdown]
# * si on a vraiment besoin de cette liste  
#   alors la compréhension est OK
#
# * mais dans le cas contraire il faut **préférer un itérateur**   
#   c'est le propos de l'**expression génératrice**
#
# * qui souvent revient à remplacer `[]` par `()`  
#   (ou même juste enlever les `[]`)

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# apprenez à bien choisir entre  
# compréhension et genexpr  
# (les deux sont utiles)

# %% cell_style="split"
# remplissons une classe imaginaire
from random import randint

matieres = ('maths', 'français', 'philo')

def notes_eleve_aleatoires():
    return {matiere: randint(0, 20) 
            for matiere in matieres}


# %% cell_style="center"
# ici je crée une compréhension; pourquoi ?
notes_classe = [notes_eleve_aleatoires() for _ in range(4)]
notes_classe

# %%
# pour calculer la moyenne de la classe en maths
# pas besoin de garder les résultats intermédiaires
# du coup, on fabrique une genexpr
# en toute rigueur il aurait fallu écrire ceci
sum((notes_eleve['maths'] for notes_eleve in notes_classe)) / len(notes_classe)

# %%
# mais la syntaxe nous permet de nous en affranchir
# (remarquez une seul niveau de parenthèses, et l'absence de [])
sum(notes_eleve['maths'] for notes_eleve in notes_classe) / len(notes_classe)

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# # épilogue
#
# pour terminer le tour des concepts Python qui contribuent aux itérations,
# il nous restera à voir la notion de **fonction génératrice** que l'on verra plus tard

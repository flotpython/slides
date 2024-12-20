# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
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
#     title: lambdas
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown]
# # fonctions lambda
#
# `lambda` est une ***expression***, pas une ***instruction***  
# qui permet de créer un objet **fonction anonyme** et à la volée

# %% tags=["gridwidth-1-2"]
# un objet fonction 
# qui n'a pas de nom
lambda x: x**2

# %% tags=["gridwidth-1-2"]
# mais que je peux appeler
(lambda x: x**2)(10)


# %% tags=["gridwidth-1-2"]
# comme si j'avait fait
def anonymous(x):
    return x**2

anonymous(10)


# %% [markdown]
# ## `lambda` : une expression
#
# * elle peut donc apparaître  
#   là où une fonction classique ne peut pas
#
# * typiquement à l'intérieur d'une expression
# * par contre pas trop adapté pour du code compliqué 
#   * doit pouvoir être écrit sous forme d'une seule expression

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `lambda` *vs* `def`
#
# * les deux formes suivantes sont donc équivalentes

# %% tags=["gridwidth-1-2"]
def foo(x):
    return x*x
foo

# %% tags=["gridwidth-1-2"]
foo = lambda x: x*x
foo

# %% [markdown]
# ## limitation de `lambda`
#
# * le corps d’une fonction lambda  
#   doit tenir sur **une seule expression**
#
#   * uniquement applicable à des fonctions simples
#   * pas de déclaration de variable locale
#   * pas d'impact sur la portée des variables
# * forme générale
#
# ```python
# lambda arg1, arg2, … argN : expression using args
# ```

# %% tags=["gridwidth-1-2"]
f = lambda x: x+1
f(1)

# %% tags=["gridwidth-1-2"]
(lambda x: x+1)(12)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemples d'utilisation

# %%
# pour appeler un objet fonction
# c'est la syntaxe habituelle
def call(func, a, b):
    return(func(a, b))

# j'appelle l'addition sur ces deux nombres
call(lambda a, b: a + b, 3, 5)

# %%
# pareil avec la multiplication
call(lambda a, b: a * b, 3, 5)

# %% [markdown]
# ## application au tri
#
# **Rappel :**
#
# * `sort()` est une **méthode** qui trie les listes en place
# * `sorted()` est une **fonction** *built-in* qui trie n’importe quel itérable et retourne un **nouvel** itérateur
# * argument `key`:  
#   une fonction pour spécifier le critère de tri  
#   typiquement une fonction lambda
#
# * argument `reverse`:  
#   booléen qui définit l’ordre de tri  
#   par défaut `reverse=False`: tri ascendant

# %% slideshow={"slide_type": "slide"}
sample = "This is a test string from Andrew".split()
sample

# %%
# une copie triée de sample
sorted(sample)

# %% tags=["gridwidth-1-2"]
# avec un autre critère
sorted(sample, key=str.lower)


# %% tags=["gridwidth-1-2"]
# pareil que
sorted(sample, key=lambda s: str.lower(s))


# %% [markdown] slideshow={"slide_type": ""}
# ou encore avec une autree donnée

# %% slideshow={"slide_type": ""}
student_marks = [('marc', 12), ('eric', 15), ('jean', 12), ('gabriel', 18)]

# on n'indique pas comment trier : c'est l'ordre "naturel" des tuples
sorted(student_marks)

# %%
# pour trier sur la note cette fois
sorted(student_marks, key=lambda student_tuple: student_tuple[1])

# %%
# remarque:
# des utilitaires sont disponibles aussi
# dans le module standard `operator` 
import operator
sorted(student_marks, key=operator.itemgetter(1))

# %% [markdown] slideshow={"slide_type": ""}
# ````{admonition} pour en savoir plus
#
# pour aller plus loin sur le tri, voir <https://docs.python.org/3/howto/sorting.html>
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `reverse()` et `reversed()`

# %% [markdown]
# * un schéma analogue existe  
#   pour renverser / retourner une liste
#
# * `list.reverse()` comme **méthode**  
#   sur les listes qui retourne **en place**
#
# * `reversed()` comme fonction *builtin* qui renvoie  
#   un itérateur pour parcourir à l'envers

# %% tags=["gridwidth-1-2"]
source = [1, 10, 100, 1000]

# %% tags=["gridwidth-1-2"]
source.reverse()
source

# %% tags=["gridwidth-1-2"]
reversed(source)

# %% tags=["gridwidth-1-2"]
list(reversed(source))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `map()` et `filter()`

# %% [markdown]
# **rappel** : appliquent une fonction à un itérable
#
# * `map(func, iter)`
#   * applique la fonction `func` à chaque élément de `iter`
#   * retourne (un itérateur sur) les valeurs retournées par `func`
# * `filter(func, iter)`
#   * similaire à `map`, mais retourne seulement les valeurs  
#     qui sont vraies (techniquement, telles que `bool(val) == True`)

# %% slideshow={"slide_type": "slide"} tags=["gridwidth-1-2"]
L = [1, 2, 3, 4]
m = map(lambda x: x**2, L)
# le résultat est un itérateur
m

# %% tags=["gridwidth-1-2"]
# pour voir le résultat la liste on
# peut par exemple transformer
# explicitement en list()
list(m)              

# %% cell_style="center"
# si on essaie une deuxième fois
# il ne se passe plus rien car on a déjà itéré sur m
list(m)          

# %% tags=["gridwidth-1-2"]
m = map(lambda x: x**2, L) 

# %% tags=["gridwidth-1-2"]
for i in m: 
    print(i, end=' ')

# %% slideshow={"slide_type": "slide"} tags=["gridwidth-1-2"]
source = range(1, 5)
f = filter(lambda x: x%2 == 0, 
           map(lambda x:x**2, source))

# f est bien un itérateur
f is iter(f)   

# %% tags=["gridwidth-1-2"]
list(f)

# %% [markdown] cell_style="center"
# cette forme est toutefois passée de mode au profit des expressions génératrices

# %% tags=["gridwidth-1-2"]
# ceci est vraiment équivalent 
g = (x**2 for x in source
     if x%2 == 0)

g is iter(g)

# %% tags=["gridwidth-1-2"]
list(g)

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## introspection (avancé)

# %% [markdown]
# * en Python tout est un objet  
#   on peut accéder à tous les attributs d’un objet
#
# * en particulier donc pour les objets de type fonction
# * modifier directement les attributs n’est pas recommandé,  
#   sauf si on comprend vraiment ce que l’on fait
#
# * par contre c’est intéressant en lecture  
#   pour comprendre les détails d’implémentation

# %% [markdown] slideshow={"slide_type": "slide"}
# ### lecture d'attributs

 # %% tags=["gridwidth-1-2"]
 def f(name="jean"):
    """le docstring"""
    pass
f.__name__

# %% tags=["gridwidth-1-2"]
f.__doc__

# %% tags=["gridwidth-1-2"]
f.__code__

# %% tags=["gridwidth-1-2"]
f.__module__

# %% tags=["gridwidth-1-2"]
f.__defaults__

# %% [markdown] slideshow={"slide_type": "slide"}
# ### aller plus loin

# %% [markdown] slideshow={"slide_type": ""}
# * si le sujet vous intéresse  
#   voyez [le module inspect](https://docs.python.org/3/library/inspect.html) dans la librairie standard

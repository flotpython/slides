# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   nbhosting:
#     title: lambdas
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown] slideshow={"slide_type": ""}
# # fonctions lambda

# %% [markdown]
# * `lambda` est une *expression*, pas une *instruction*
# * qui permet de créer **un objet fonction** anonyme et à la volée

# %% cell_style="split"
# un objet fonction 
# qui n'a pas de nom
lambda x: x**2

# %% cell_style="split"
# mais que je peux appeler
(lambda x: x**2)(10)


# %% cell_style="split"
# comme si j'avait fait
def anonymous(x):
    return x**2

anonymous(10)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## `lambda` : une expression

# %% [markdown]
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

# %% cell_style="split"
def foo(x):
    return x*x
foo

# %% cell_style="split"
foo = lambda x: x*x
foo

# %% [markdown] slideshow={"slide_type": "slide"}
# ## limitation de `lambda`

# %% [markdown]
# * le corps d’une fonction lambda  
#   doit tenir sur **une seule expression**
#
#   * uniquement applicable à des fonctions simples
#   * pas de déclaration de variable locale
#   * pas d'impact sur la portée des variables
# * forme générale
#
# ```
# lambda arg1, arg2, … argN : expression using args
# ```

# %% cell_style="split"
f = lambda x: x+1
f(1)

# %% cell_style="split"
(lambda x: x+1)(12)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemples d'utilisation

# %%
# pour appeler un objet fonction
# c'est la syntaxe habituelle
def call(func, a, b):
    return(func(a, b))

print(call(lambda a, b: a + b, 3, 5))
print(call(lambda a, b: a * b, 3, 5))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## application au tri

# %% [markdown]
# **Rappel :**
#
# * `sort()` est une **méthode** qui trie les listes en place
# * `sorted()` est une **fonction** *built-in* qui trie n’importe quel itérable et retourne un **nouvel** itérateur

# %% [markdown]
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
sorted(sample)

# %% cell_style="split"
sorted(sample, key=str.lower)


# %% cell_style="split"
# pareil que
sorted(sample,
       key=lambda s: str.lower(s))


# %% [markdown] slideshow={"slide_type": "slide"}
# ou encore

# %% slideshow={"slide_type": ""}
student_marks = [('marc', 12), ('eric', 15), ('jean', 12), ('gabriel', 18)]

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
# <div class=note>
#
# pour aller plus loin sur le tri, voir <https://docs.python.org/3/howto/sorting.html>
#     
# </div>

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

# %% cell_style="split"
source = [1, 10, 100, 1000]

# %% cell_style="split"
source.reverse()
source

# %% cell_style="split"
reversed(source)

# %% cell_style="split"
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

# %% cell_style="split" slideshow={"slide_type": "slide"}
L = [1, 2, 3, 4]
m = map(lambda x: x**2, L)
# le résultat est un itérateur
m

# %% cell_style="split"
# pour voir le résultat la liste on
# peut par exemple transformer
# explicitement en list()
list(m)              

# %% cell_style="center"
# si on essaie une deuxième fois
# il ne se passe plus rien car on a déjà itéré sur m
list(m)          

# %% cell_style="split"
m = map(lambda x: x**2, L) 

# %% cell_style="split"
for i in m: 
    print(i, end=' ')

# %% cell_style="split" slideshow={"slide_type": "slide"}
source = range(1, 5)
f = filter(lambda x: x%2 == 0, 
           map(lambda x:x**2, source))

# f est bien un itérateur
f is iter(f)   

# %% cell_style="split"
list(f)

# %% [markdown] cell_style="center"
# cette forme est toutefois passée de mode au profit des expressions génératrices

# %% cell_style="split"
# ceci est vraiment équivalent 
g = (x**2 for x in source
     if x%2 == 0)

g is iter(g)

# %% cell_style="split"
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

 # %% cell_style="split"
 def f(name="jean"):
    """le docstring"""
    pass
f.__name__

# %% cell_style="split"
f.__doc__

# %% cell_style="split"
f.__code__

# %% cell_style="split"
f.__module__

# %% cell_style="split"
f.__defaults__

# %% [markdown] slideshow={"slide_type": "slide"}
# ### aller plus loin

# %% [markdown] slideshow={"slide_type": ""}
# * si le sujet vous intéresse  
#   voyez [le module inspect](https://docs.python.org/3/library/inspect.html) dans la librairie standard

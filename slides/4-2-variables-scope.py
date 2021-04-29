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
#     display_name: Python 3
#     language: python
#     name: python3
#   nbhosting:
#     title: "port\xE9e d\u2019une variable"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% slideshow={"slide_type": "slide"}
#from plan import plan; plan("fonctions", "portée")

# %% [markdown] slideshow={"slide_type": "slide"}
# # portée d’une variable

# %% [markdown]
# * la portée d’une variable (ou scope) consiste  
#   à répondre à deux questions
#
#   * quand je référence une variable X,  
#     à quelle variable je fais référence ?
#
#   * quand j’affecte (un objet) à une variable X,  
#     depuis quelles parties de mon code 
#     je peux accéder à cette variable ?

# %% [markdown] slideshow={"slide_type": "slide"}
# ## portée lexicale

# %% [markdown]
# * python utilise la **portée lexicale**,  
#   c’est-à-dire que la portée des variables  
#   est déterminée exclusivement  
#   en fonction de leur place dans le code source

# %% [markdown] slideshow={"slide_type": "slide"}
# ## règle LEGB

# %% [markdown]
# * python cherche les affectations des variables  
#   suivant la règle **LEGB** qui suis l’ordre 
#
#   * **L**ocal
#   * fonctions **E**nglobantes
#   * **G**lobal
#   * **B**uilt-in

# %% [markdown] slideshow={"slide_type": "slide"}
# ### règle LEGB

# %% [markdown]
# * **L**: local
#   * nom affecté localement à la fonction où il est référencé 
# * **E**: fonctions englobantes
#   * nom affecté dans les fonctions englobant la fonction où il est référencé (de l’intérieur vers l’extérieur) 
# * **G**: global 
#   * nom affecté dans le fichier hors d’une fonction 
# * **B**: built-in 
#   * nom déclaré dans le module builtins 

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `global` et `nonlocal`

# %% [markdown]
# * on peut donc utiliser (lire) dans une fonction  
#   une variable définie au dehors / au dessus 
#
# * mais on ne peut **pas la modifier** (écrire) 
#   sauf si elle est déclarée avec les mots clefs  
#   `global` ou `nonlocal`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## variable locale à une fonction

# %% [markdown]
# * pas de déclaration dans le sens par exemple des langages compilés
# * les **paramètres** d’une fonction, ainsi que toutes 
# * les **variables affectées** dans la fonction 
# * sont locaux à cette fonction
# * les variables locales sont créées à chaque appel
# * il y a deux exceptions:
#   * si la variable `X` est déclarée `global`, l’affectation va modifier la variable `X` du module
#   * si la variable `X` est déclarée `nonlocal`, l’affectation va modifier la variable `X` dans la fonction englobante la plus proche ayant déjà défini `X`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## variable globale

# %% [markdown]
# * toutes les variables affectées à l’extérieur d’une classe ou fonction sont globales (*sous-entendu* au module)
# * leur portée est limitée au fichier dans lequel elles sont déclarées
# * on dira un **module** dans la suite

# %% [markdown] slideshow={"slide_type": "slide"}
# ### spécificités de `global`

# %% [markdown]
# * la déclaration `global` 
#   * doit apparaître avant l'utilisation
#   * c'est mieux de la mettre en premier dans le bloc
# * une variable déclarée `global`
#   * et assignée dans une fonction
#   * est automatiquement créée dans le module
#   * même si elle n’existait pas avant

# %% [markdown] slideshow={"slide_type": "slide"}
# #### spécificités de `global`

# %% cell_style="split"
# juste pour s'assurer que 'x' est indéfini
try:      del x
except:   pass

y, z = 1, 2  # variables globales

# déclare une variable globale x
# y, z sont globales (en lecture)

def f():
    global x   
    print("dans f", y, z)
    x = y + z       

# %% cell_style="split"




# à ce stade, f() n'a pas 
# encore été appelée 
# et x n’est pas
# encore définie
try: 
    print(x)
except Exception as exc: 
    print(f"{type(exc)}: {exc}")

# %% cell_style="split"
f()

# %% cell_style="split"
# en appelant f(), on a défini la variable x
print(x)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## faut-il utiliser `global` ?

# %% [markdown]
# * utiliser des variables globales est - presque toujours - une mauvaise idée
# * car cela crée les dépendances difficiles à détecter
# * la bonne manière est de
#   * ne pas utiliser de variable globale
#   * penser aux classes
# * exemple archi-classique
#   * la configuration d'une application
#   * est souvent implémentée comme un singleton

# %% [markdown] slideshow={"slide_type": "slide"}
# ### faut-il utiliser `global` ?

# %% cell_style="split"
# v1: utilisation de global 

x = 10

def func():
    global x
    x = x + 10

func()

# %% cell_style="split"
# v2: modification explicite
x = 10

def func():
    return x + 10

x = func()

# %%
# v3: Accès et modifications explicites
x = 10

def func(x):
    return x + 10

x = func(x)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `nonlocal`

# %% [markdown]
# * une variable `nonlocal` référence la variable locale  
#   de la fonction englobante la plus proche
#
# * une variable déclarée `nonlocal` 
#   * doit obligatoirement avoir été affectée  
#     dans une fonction englobante
#
#   * en particulier, ne pourra être résolue dans le module  
#     au niveau global ou dans les built-ins
#
#   * si ça n’est pas le cas, erreur de syntaxe
#   * ne doit pas être un paramètre de la fonction

# %% [markdown] slideshow={"slide_type": "slide"}
# ### spécificités de `nonlocal`

# %% [markdown] tags=["raises-exception"]
# ```python
# # ce code produit une erreur de syntaxe
# x = 1
# def f():
#     def g():
#         # il FAUT mettre 'global' ici
#         nonlocal x
#         x = x + 1
#         print("dans g", x)
#     g()
#     print("dans f", x)
#
# f()
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# #### spécificités de `nonlocal`

# %%
# ici le code est correct
x = 1
def f():
    x = 2
    def g():
        nonlocal x
        x = x + 1
        print("dans g", x)
    g()
    print("dans f", x)
f()
print("module:", x)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### spécificités de `nonlocal`

# %% [markdown]
# ```python
# # ce code produit une erreur de syntaxe
# x = 1
# def f():
#     x = 2
#     # le paramètre x empêche 
#     # de référencer le nonlocal
#     def g(x):
#         nonlocal x
#         x = x + 1
#         print("dans g", x)
#     g(x)
#     print("dans f", x)
# f()
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### faut-il utiliser `nonlocal` ?

# %% [markdown]
# * c’est très utile lorsqu’on utilise la notion de clôture 
# * c’est un concept de programmation avancé,  
#   on a parlera lorsqu’on verra les décorateurs

# %%
# %load_ext ipythontutor

# %% slideshow={"slide_type": "slide"}
# %%ipythontutor cumulative=false heapPrimitives=false
L = [1, 2]
def func():
    L = [3, 4]
    return L
x = func()
print(x)
print(L)

# %% slideshow={"slide_type": "slide"}
# %%ipythontutor cumulative=false heapPrimitives=false
L = [1, 2]
def func():
    global L
    L = [3, 4]
    return L
x = func()
print(x)
print(L)

# %% slideshow={"slide_type": "slide"}
# %%ipythontutor cumulative=false heapPrimitives=false
L = [1, 2]
def f(L):
    L.append(3) 
    L = 1
f(L)
print(L)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les noms de builtins

# %% [markdown]
# * les  noms prédéfinis, comme `list` ou `enumerate` ou `OSError`
# * grâce à la règle LEGB, pas besoin de les importer
# * par contre, on peut redéfinir un nom de `builtins` dans son programme
#   * c’est une mauvaise idée et une source de bug
#   * python ne donne aucun warning dans ce cas
#  * dans ce cas à nouveau, `pylint` est un outil très utile

# %% [markdown] slideshow={"slide_type": "slide"}
# ### les noms de builtins

# %% cell_style="split"
# on peut accéder à la variable `__builtins__` 
# qui est .. une variable *builtin* 
__builtins__

# %% cell_style="split"
# ou encore on peut
# importer le module `builtins`
import builtins

# %%
# je n'en montre que 5 pour garder de la place
dir(builtins)[-5:]

# %%
len(dir(__builtins__))

# %% slideshow={"slide_type": "slide"}
errors = (x for x in dir(builtins) if 'Error' in x or 'Warning' in x)

columns, width = 4, 18
for i, error in enumerate(errors, 1):
    print(f"{error:^{width}}", end=" ")
    if i % columns == 0:
        print()

# %% slideshow={"slide_type": "slide"}
others = (x for x in dir(builtins) 
          if not ('Error' in x or 'Warning' in x or '__' in x))

columns, width = 5, 12
for i, other in enumerate(others, 1):
    print(f"{other:^{width}}", end=" ")
    if i % columns == 0:
        print()

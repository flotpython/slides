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
#     title: "port\xE9e d\u2019une variable"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% slideshow={"slide_type": "-"}
# %load_ext ipythontutor

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
# Python utilise la **portée lexicale**,  
# c’est-à-dire que la portée des variables  
# est déterminée exclusivement  
#  en fonction de leur place dans le code source

# %% [markdown]
# <div class=note>
#
# la liaison lexicale est faite à *compile-time*  
# le terme *lexical* signifie qu'on n'a que besoin de **lire** le programme, et pas de l'exécuter  
# a contrario, la résolution des attributs ne peut se faire que à *run-time*    
#     
# </div>    

# %% [markdown] slideshow={"slide_type": "slide"}
# ## déclaration ?

# %% [markdown]
# * dans d'autres langages, il y a nécessité de **déclarer** une variable  
#   avant de s'en servir (typiquement les langages compilés)
# * ce n'est pas le cas en Python
#
# toutefois:
# * **le fait d'affecter** une variable joue ce rôle-là
# * et il y a aussi bien sûr **les paramètres** de la fonction

# %% [markdown] cell_style="split"
# ```python
# # ici la variable `y` n'est pas considérée 
# # comme déclarée puisqu'on se contente
# # de la lire, et qu'on ne l'affecte pas
# # (pas de code avec `y = ...`
#
# def foo(x):
#     print(x)  # <-- une variable locale
#               #     (paramètre)
#     print(y)  # <-- PAS une variable locale
#               #     (et donc ici BOOM)
# ```

# %% [markdown] cell_style="split"
# ```python
# # ici au contraire la variable y
# # est locale à la fonction
# # comme le paramètre x
#
# def foo(x):
#     y = 10    # <-- on "déclare" y
#     print(x)  # <-- une variable locale
#               #     (paramètre)
#     print(y)  # <-- aussi (car affectée
#               #     plus haut dans foo)
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## règle **LEGB**

# %% [markdown]
# une variable est cherchée dans cet ordre **LEGB**
#
# * **L** comme **L**ocal
#   * nom déclaré dans la fonction où il est référencé 
# * **E** comme fonctions **E**nglobantes
#   * nom déclaré dans les fonctions englobant la fonction où il est référencé (de l’intérieur vers l’extérieur) 
# * **G** comme **G**lobal 
#   * nom déclaré dans le fichier hors d’une fonction 
# * **B** comme **B**uilt-in 
#   * nom provenant du module *builtins*

# %% [markdown]
# <div class=note>
#
# l'unité de base est la **fonction** - il **n'y pas de visibilité de bloc**  
# (comme on la trouve dans d'autres langages)
#     
# </div>    

# %% [markdown] slideshow={"slide_type": "slide"}
# ## variable globale

# %% [markdown]
# du coup toutes les variables affectées **à l’extérieur** d’une classe ou fonction sont globales
#
# i.e. susceptibles d'être lues depuis tout le code dans le fichier (on dit un **module**)

# %%
GLOBALE = 10

def foo():
    print("from foo:", GLOBALE)
    
    def bar():
        print("from bar:", GLOBALE)
    bar()
     
foo()


# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple de visibilité (1)

# %%
def foo():
    
    level1 = 10
    
    def bar():
        level2 = 20
        
        def tutu():
            level3 = 30
            
            print("from tutu:", level1, level2, level3)
        
        print("from bar: ", level1, level2) # level3 NOT visible
        tutu()
    
    print("from foo: ", level1) # level2 or level3 NOT visible here
    bar()


# %%
foo()

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple de visibilité (2) cassé

# %% [markdown]
# une variable ne peut pas être à la fois globale et locale !

# %% slideshow={"slide_type": ""} tags=["raises-exception"]
L = [1, 2]

def f():
    # ici on pourrait penser utiliser la globale 
    L.append(3) 
    # mais en fait non, ici on dit que L est locale !
    L = 1

try:
    f()
except UnboundLocalError:
    print("OOPS")

# %% [markdown]
# <div class=note>
#     
# `UnboundLocalError` signifie textuellement qu'on évalue une variable locale  
# qui n'a pas encore été initialisée
#     
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple de visibilité (2) revu

# %% [markdown]
# pour réparer, on peut:
#
# 1. enlever le `L = 1` qui ne sert à rien :)
# 1. ou encore passer la globale en paramètre
#

# %% slideshow={"slide_type": ""}
L = [1, 2]
 
def f(L):
    # ici L est le paramètre donc une locale
    L.append(3) 
    # 
    L = 1
f(L)
print(L)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## attention aux classes

# %% [markdown]
# **attention** que ce système ne s'étend pas aux classes
#
# en effet les symboles définis au premier niveau dans une instruction `class`  
# sont rangés **comme des attributs de la classe**
#
# et à ce titre ils ne sont **pas accessibles lexicalement**

# %%
class Foo:
    
    class_variable = 10
    
    def method(self):
        # in this scope the symbols
        # 'class_variable' and `method`
        # ARE NOT lexically visible !!
        pass


# %% [markdown] slideshow={"slide_type": "slide"}
# ## `global` et `nonlocal`

# %% [markdown]
# mais revenons à nos fonctions:
#
# * on peut donc utiliser (lire) dans une fonction  
#   une variable définie au dehors / au dessus 
#
# * mais du coup on ne peut **pas la modifier** (affecter)  
#   puisque si on essaie de l'affecter cela est considéré   
#   comme une déclaration de variable locale
#
# * c'est à cela que servent les mots clefs  
#   `global` ou `nonlocal`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple avec `global` (1)

# %% cell_style="split"
# écrire une globale depuis une fonction

G = 10

def modify_G(x):
    # une fois la variable déclarée
    global G
    # je peux l'affecter
    G = x
    
modify_G(1000)

# combien vaut G ?
G

# %% cell_style="split"
# à votre avis 
# que se passe-t-il si on n'utilise
# pas global

G = 10

def does_not_modify_G(x):
    G = x
    
does_not_modify_G(1000)

# combien vaut G ?
G

# %% [markdown]
# <div class=note>
#
# dans la deuxième forme, on a juste créé une **deuxième variable G** qui est locale à la fonction, et "cache" la globale, qui donc n'est pas modifiée
#     
# </div>    

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple avec `global` (2)

# %% cell_style="split"
# un exemple un peu plus tordu
# car ici dans la fonction
# on lit et on écrit G

G = 10

def increment_G():
    global G
    G = G + 10

increment_G()

# combien vaut G ?
G

# %% cell_style="split" tags=["raises-exception"]
# que se passe-t-il ici 
# d'après vous ?

G = 10

def increment_G():
    # pas de 'global'
    G = G + 10

try:
    increment_G()
except UnboundLocalError:
    print("OOPS !!")

# combien vaut G ?
G


# %% [markdown]
# <div class=note>
#
# ce qui se passe ici c'est: on commence par lire `G`; mais comme `G` est affectée dans `increment_G`, c'est une variable *locale* à la fonction (et donc pas la globale); mais elle n'a pas encore de valeur ! d'où l'erreur `UnboundLocalError`
#     
# </div>    

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## faut-il utiliser `global` ?

# %% [markdown]
# * utiliser des variables globales est - presque toujours - une mauvaise idée
# * car cela gêne la réutilisabilité
# * la bonne manière est de
#   * ne pas utiliser de variable globale
#   * penser aux classes
# * exemple archi-classique
#   * la configuration d'une application
#   * est souvent implémentée comme un singleton

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## spécificités de `global`

# %% [markdown]
# * la déclaration `global` 
#   * doit apparaître avant l'utilisation
#   * c'est mieux de la mettre en premier dans le bloc
# * une variable déclarée `global`
#   * et assignée dans une fonction
#   * est automatiquement créée dans le module
#   * même si elle n’existait pas avant

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple avec `nonlocal`

# %%
# nonlocal est très utile pour implémenter une cloture 

def make_counter():
    # cette variable est capturée dans la cloture
    counter = 0
    def increment():
        nonlocal counter
        counter += 1
        return counter
    # on retourne la fonction, qui a "capturé" le compteur
    return increment


# %% cell_style="split"
c1 = make_counter()

c1()
c1()

# %% cell_style="split"
c2 = make_counter()

c2()
c2()
c2()

# %% cell_style="split"
c1()

# %% cell_style="split"
c2()

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## les noms de builtins

# %% [markdown] tags=["level_intermediate"]
# * ce sont les  noms prédéfinis, comme `list` ou `enumerate` ou `OSError`
# * grâce à la règle LEGB, pas besoin de les importer
# * par contre, on peut redéfinir un nom de `builtins` dans son programme
#   * c’est une mauvaise idée et une source de bug
#   * python ne donne aucun warning dans ce cas
#  * dans ce cas - comme toujours - `pylint` est un outil très utile

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### les noms de builtins

# %% cell_style="split" tags=["level_intermediate"]
# on peut accéder à la variable `__builtins__` 
# qui est .. une variable *builtin* 
__builtins__

# %% cell_style="split" tags=["level_intermediate"]
# ou encore on peut
# importer le module `builtins`
import builtins

# %% tags=["level_intermediate"]
# je n'en montre que 5 pour garder de la place
dir(builtins)[-5:]

# %% tags=["level_intermediate"]
# en fait il y en a vraiment beaucoup ! 
len(dir(__builtins__))

# %% slideshow={"slide_type": "slide"} tags=["level_intermediate"]
errors = (x for x in dir(builtins) if 'Error' in x or 'Warning' in x)

columns, width = 4, 18
for i, error in enumerate(errors, 1):
    print(f"{error:^{width}}", end=" ")
    if i % columns == 0:
        print()

# %% slideshow={"slide_type": "slide"} tags=["level_intermediate"] cell_style="center"
others = (x for x in dir(builtins) 
          if not ('Error' in x or 'Warning' in x or '__' in x))

columns, width = 6, 16
for i, other in enumerate(others, 1):
    print(f"{other:^{width}}", end=" ")
    if i % columns == 0:
        print()

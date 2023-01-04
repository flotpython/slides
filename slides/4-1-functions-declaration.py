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
#     title: fonctions
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
# # fonctions: généralités

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour réutiliser du code en Python

# %% [markdown]
# * **fonctions**
#   * **pas d'état après exécution**
# * modules
#   * garde l'état
#   * une seule instance par programme
# * classes
#   * instances multiples
#   * chacune garde l'état
#   * héritage

# %% [markdown] slideshow={"slide_type": "slide"}
# ## comment définir une fonction ?

# %% [markdown]
# ```
# def name(arg1, arg2, .. argN):
#     <statement>
#     return <value>   # peut apparaitre n’importe où
# ```
#
# * `def` crée un objet fonction, l'assigne dans la variable `name`
#   * tout est objet en Python
#   * assimilable à une simple affectation `name = ..`
# * les arguments sont passés **par référence**
#   * donc crée des **références partagées**
#   * attention aux types mutables
#   * on en reparlera

# %% [markdown] slideshow={"slide_type": "slide"}
# ### comment définir une fonction ?

# %% [markdown]
# * une fonction dans Python est un **objet fonctionnel**
#   * auquel on donne un nom
# * un `def` peut apparaitre n’importe où
#   * et se comporte donc **comme une affectation**
# * le code n’est évalué que quand la fonction est appelée 
#
# ```
# # on peut parfaitement écrire ceci
# if test:
#     def func():
#         ...
# else:
#     def func():
#         ...
# func() # exécute une version qui dépend du test
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# #### comment définir une fonction ?

# %% cell_style="split"
# pas de typage statique en Python
# on ne sait pas de quel type 
# doivent être x et y
# tant que ça fait du sens,
# le code est correct
def times(x, y):
    return x * y


# %% cell_style="split"
# deux entiers
times(2, 3)         

# %% cell_style="split"
# deux floats
times(1.6, 9)       

# %% cell_style="center"
# la magie du duck typing
times('-spam-', 4)

# %% cell_style="split" slideshow={"slide_type": "slide"}
# la fonction est un objet 
times   

# %% cell_style="split"
# pas forcément recommandé mais:
# on peut affecter cet objet à
# une autre variable
foo = times  
foo(3, 14)


# %% cell_style="split"
# et redéfinir `times` pour faire
# + à la place de * !
def times(x, y):
    # ne vraiment pas faire ça en vrai !!
    return x + y


# %% cell_style="split"
# maintenant times fait une addition !
times(3, 4)

# %%
# et foo fait bien la multiplication
foo(3, 4)


# %% [markdown]
# bref : les noms de fonction sont des variables normales

# %% [markdown] slideshow={"slide_type": "slide"}
# ## digression : docstrings

# %% [markdown]
# ### documentation automatique
#
# * si dans un objet de type fonction, classe ou module
# * la première instruction est une chaîne de caractères
# * c'est le ***docstring*** de cet objet
# * qui constitue la documentation de l’objet

# %%
def hyperbolic(x, y):
    """
    computes xˆ2 - y^2
    """
    return x**2 - y**2


# %% [markdown] slideshow={"slide_type": "slide"}
# * les docstrings sont retournés par `help(objet)`
# * ils sont rangés dans `objet.__doc__`

# %%
help(hyperbolic)

# %%
# le doctring est rangé dans un attribut spécial
hyperbolic.__doc__


# %% [markdown] slideshow={"slide_type": "slide"}
# ### un peu de documentation

# %% [markdown]
# * c’est une bonne habitude de toujours documenter
# * on peut utiliser une simple chaîne,  
#   ou le plus souvent multiligne (avec `"""`)

# %% [markdown]
# * pas utile de répéter le nom de l’objet,  
#   qui est extrait automatiquement (DRY) 
#
# * la première ligne décrit brièvement ce que fait l’objet
# * la deuxième ligne est vide
# * les lignes suivantes décrivent l’objet avec plus de détails

# %% [markdown] slideshow={"slide_type": "slide"}
# ### format des *docstrings*

# %% [markdown]
# * historiquement basé sur ReST, mais jugé peu lisible
# * il y a plusieurs conventions pour le contenu du docstring
# * voir principalement `sphinx` pour l'extraction automatique et la mise en forme
# * recommande personnellement:
#   * styles `google` et/ou `numpy` [voir doc ici](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
#   * exemples slide suivant
#   

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple de *docstrings*

# %% [markdown]
# **exemple**
#
# * tel que publié  
#   https://asynciojobs.readthedocs.io/en/main/API.html#asynciojobs.purescheduler.PureScheduler
#
# * source  
# https://github.com/parmentelat/asynciojobs/blob/main/asynciojobs/purescheduler.py#L44

# %% [markdown] slideshow={"slide_type": "slide"}
# ### les *type hints* sont utiles

# %% [markdown]
# il est possible de typer les paramètres et le retour de la fonction

# %%
def type_hints_1(x: int, y: float) -> str:
    """
    pour des types simples
    """
    ...


# %%
# un peu plus compliqué (attention, nécessite 3.9)

def type_hints_2(x: tuple[int, str, bool],
                 y: dict[str, list[int]]) -> None:
    ...


# %% [markdown]
# on en reparlera, mais un des principaux intérêts des *type hints* c'est précisément pour améliorer la documentation et faciliter l'usage de la librairie en question

# %% [markdown] slideshow={"slide_type": "slide"}
# ## digression : conventions de style

# %% [markdown]
# * d'après PEP8
# * utiliser une (ou plusieurs) ligne(s) vide(s)  
#   pour séparer les fonctions, classes  
#   et les grands blocs d’instructions
#
# * espace autour des opérateurs et après les virgules
#
# ```python
# a = f(1, 2) + g(3, 4)
# ```
#
# * des espaces autour de l'`=`, et **pas** après la fonction  
#   ~~`f (1, 2)`~~ un espace en trop `f(1, 2)`  
#   ~~`a=f(1, 2)`~~ manque des espaces `a = f(1, 2)`
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### chasses de caractères

# %% [markdown]
# * chasses de caractères 
#   * une classe s'écrira `MaClasse`
#   * une instance s'écrira `ma_classe` ou `maclasse`
#   * une fonction ou méthode ressemblera à `ma_fonction()`
#   * les packages et modules sont aussi en minuscules
#   * une globale à un module devrait être `EN_MAJUSCULES`

# %%
# module en minuscule, classe en chasse mixte
from argparse import ArgumentParser

# %% cell_style="split"
# un contrexemple
# bien que ceci appartienne à la librairie standard
# ici le premier 'datetime' est un nom de classe
# et devrait s'appeler 'DateTime'
# trop tard pour rectifier !
from datetime import datetime

# %% cell_style="split"
# du coup on recommande
from datetime import datetime as DateTime

# %% [markdown] slideshow={"slide_type": "slide"}
# ## reprenons : l'instuction `return`

# %% [markdown]
# * un appel de fonction est **une expression**
# * le **résultat** de cette expression est spécifié  
#   dans le corps de la fonction par l'instruction `return`
#
# * le **premier** `return` rencontré provoque   
#   **la fin** de l'exécution de la fonction (￮)
#
# * si la fonction se termine **sans rencontrer** un `return`
#   * on retourne `None`
#   * `None` est un mot-clé de Python,  
#     qui désigne un objet unique (singleton)
#     
# <div class=note>
#
# (￮) sauf en cas de `finally` comme on va le voir tout de suite
#     
# </div>    
#     

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### `return` et `finally``

# %% [markdown]
# * si l’expression `return` se trouve à l'intérieur  
#   d'un `try` avec une clause `finally`
#
#   * la clause `finally` est exécutée avant de quitter la fonction
#   * voir la section sur les exceptions 
#     pour comprendre la sémantique de l'instruction `try .. finally`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## passage d’arguments et références partagées

# %% [markdown]
# * le passage de paramètres se fait par référence
# * ce qui crée donc des références partagées

# %% slideshow={"slide_type": "slide"}
# nous allons illustrer ce mécanisme de 
# références partagées grâce à pythontutor.com

# %load_ext ipythontutor

# %% slideshow={"slide_type": "slide"}
# %%ipythontutor curInstr=2 width=1000 height=400

# les arguments d'une fonction sont toujours passés par référence
liste = [1, 2, 3]

def mess_with(reference):
    reference[1] = 100
    
mess_with(liste)
    
print(liste)


# %% slideshow={"slide_type": "slide"}
# %%ipythontutor width=800 height=450 heapPrimitives=true
def mess_with2(a, b):
    a = 3          # ceci n'aura pas de conséquence sur A
    b[0] = 'boom'  # ceci va changer B

A = 1      # immutable ne peut pas être modifiée
B = [10, 20] # mutable, l'objet liste est modifié par
           # changer() par une modification in-place
mess_with2(A, B)
print(A)
print(B)

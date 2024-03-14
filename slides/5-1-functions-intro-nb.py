# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted,-editable
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -version
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
#     title: fonctions
#   rise:
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

# %% [markdown]
# ## pour réutiliser du code en python
#
# **DRY = *don't repeat yourself*** : *cut'n paste is evil*
#
# ```{list-table}
#
# * - **fonctions**
#   - **pas d'état après exécution**
# * - modules
#   - garde l'état, une seule instance par programme
# * - classes
#   - instances multiples, chacune garde l'état, héritage
# ```

# %% [markdown]
# ## comment définir une fonction ?

# %% [markdown]
# ### syntaxe
#
# ```
# def name(arg1, arg2, .. argN):
#     <statement>
#     return <value>   # peut apparaitre n’importe où
# ```
#
# * `def` crée un objet fonction, et l'**assigne** dans la variable `name`
#   * assimilable à une simple affectation `name = ..`
#   * tout est objet en Python, la fonction aussi !
# * bien entendu, le code n’est évalué que quand la fonction est appelée
#
# ````{admonition} une fonction peut modifier ses paramètres !
# les arguments sont passés **par référence**
# * donc crée des **références partagées**
# * attention aux types mutables, ils peuvent être modifiés par la fonction
# ````

# %% [markdown]
# ```
# # pas du tout usuel, mais pour bien comprendre :
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
# ### *duck typing*
#
# il n'y a **pas de typage statique** en Python: on ne sait pas de quel type doivent être x et y, et tant que ça fait du sens au moment de l'exécution, le code est correct ! on appelle ça aussi le *duck typing*

# %% tags=["gridwidth-1-2"]
# on va pouvoir appeler cette fonction ...
def times(x, y):
    return x * y


# %% tags=["gridwidth-1-2"]
# ... aveec deux entiers
times(2, 3)         

# %% tags=["gridwidth-1-2"]
# ou avec deux floats
times(1.6, 9)       

# %% cell_style="center" tags=["gridwidth-1-2"]
#  ... et même comme ceci !
times('-spam-', 4)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### *type hints*
#
# si on le souhaite, on **peut** indiquer le type des paramètres attendus et du résultat  
#

# %% tags=["gridwidth-1-2"]
def type_hints_1(x: int, y: float) -> str:
    """
    pour des types simples
    """
    ...


# %% tags=["gridwidth-1-2"]
# un peu plus compliqué (depuis la nécessite 3.9)

def type_hints_2(x: tuple[int, str, bool],
                 y: dict[str, list[int]]) -> None:
    ...


# %% [markdown]
# il faut savoir que c'est **totalement optionnel** et que ça **ne modifie pas** le comportement du code
#
# à quoi ça sert du coup, me direz-vous ? eh bien surtout à deux choses
#
# - d'abord et surtout à **améliorer la documentation** et faciliter l'usage de la librairie en question
# - ensuite et de manière plus optionnelle, on peut utiliser un outil externe appelé *type checker* [comme par exemple mypy](https://mypy.readthedocs.io/en/stable/) qui, lui, va utiliser cette information pour **détecter les incohérences** entre types attendus et appels effectifs; par contre pour que cette approche soit effective il faut en général que les *type hints* soient généralisés dans le code...

# %% [markdown]
# ````{admonition} note historique
# :class: admonition-small
#
# les *type hints* sont disponibles depuis la version 3.5, mais étaient à l'époque peu utilisables - notamment pour définir les types composites  
# bref, elles sont vraiment utilisables depuis disons la 3.9 - on peut maintenant écrire `dict[str, int]` pour désigner un dictionnaire dont les clés sont des chaines et les valeurs des entiers
#
# du coup il faut les voir comme un trait relativement récent, et une énorme proportion du code Python en reste dépourvu  
# ce n'est pas une raison pour ne pas les utiliser, on peut le faire avec discernement: pas besoin de forcément en mettre partout !
# ````

# %% [markdown]
# ### un objet comme un autre
#
# ````{admonition} pour résumer: des objets normaux
#
# - les noms de fonction sont des variables normales
# - les objets fonction sont des objets comme les autres
# ````
#
# voici à nouveau un exemple biscornu; ce n'est évidemment pas recommandé, mais pour bien comprendre, sachez que c'est légal de faire ceci:
#

# %% slideshow={"slide_type": "slide"} tags=[]
# la fonction est un objet 
times   

# %% tags=[]
# pas du tout recommandé, mais 
# on peut affecter cet objet à une autre variable !
foo = times

# et donc maintenant foo désigne une fonction, je peux donc l'appeler
foo(3, 14)


# %% tags=[]
# et redéfinir `times` pour faire + à la place de * !
def times(x, y):
    # ne vraiment pas faire ça en vrai !!
    return x + y


# %% tags=[]
# maintenant times fait une addition !
times(3, 4)

# %%
# et foo fait bien la multiplication
foo(3, 4)


# %% [markdown]
# ### l'instuction `return`
#
# * un appel de fonction est **une expression**
# * le **résultat** de cette expression est spécifié dans le corps de la fonction par l'instruction `return`
# * le **premier** `return` rencontré provoque **la fin** de l'exécution de la fonction
# * si la fonction se termine **sans rencontrer** un `return`
#   * on retourne `None` - `None` est un mot-clé de Python, qui désigne un objet unique (singleton)
#     
# ````{admonition} return et finally (avancé)
# :class: admonition-small
#
# `return` termine l'exécution de la fonction, sauf si l’expression `return` se trouve à l'intérieur d'un `try` avec une clause `finally`  
# dans ce cas la clause `finally` est exécutée avant de quitter la fonction  
# voir la section sur les exceptions pour comprendre la sémantique de l'instruction `try .. finally`
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les docstrings

# %% [markdown]
# ### où documenter ?
#
# si, dans un objet de type *fonction*, *classe* ou *module*, la **première instruction** est une chaîne de caractères  
# alors c'est le ***docstring*** de cet objet, qui constitue sa documentation
#
# l'idée étant naturellement de pouvoir maintenir en même temps le code et la doc, plutôt que d'avoir la doc dans un système séparé qui du coup n'est jamais à jour

# %%
def hyperbolic(x, y):
    """
    computes xˆ2 - y^2
    """
    return x**2 - y**2


# %% [markdown] slideshow={"slide_type": "slide"}
# c'est ce qui est utilisé pour afficher la doc avec `help(objet)`

# %%
help(hyperbolic)

# %% [markdown]
# ````{admonition} l'attribut spécial __doc__
# :class: info admonition-small
#
# pour information, cette chaine est rangée dans l'espace de nom de l'objet dans un attribut spécial `hyperbolic.__doc__`
# ````

# %% [markdown]
# ### comment documenter ?
#
# c’est une bonne habitude de toujours documenter ! 
#
# * le plus souvent multiligne - avec `"""` comme dans `hyperbolic`
# * pas utile de répéter le nom de l’objet, qui est extrait automatiquement de la signature (DRY)
# * la première ligne décrit brièvement ce que fait l’objet
# * la deuxième ligne est vide
# * les lignes suivantes décrivent l’objet avec plus de détails - notamment les paramètres, etc...

# %% [markdown]
# ### format et exemple
#
# * historiquement le contenu du docstring était basé sur ReST, mais jugé peu lisible
# * du coup pas forcément hyper-bien standardisé - plusieurs conventions existent dans le code disponible
# * recommande personnellement:
#   * styles `google` et/ou `numpy` [voir doc ici](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html)
#
# ````{admonition} un exemple réaliste
#
# voici un exemple sur une librairie réelle, et qui suit un *workflow* assez commun:
#
# - le source est posté sur `github.com`
# - à chaque commit, un *webhook* informe `readthedocs.io` et la doc est recalculée
# - le moteur pour recalculer cette doc est l'outil `Sphinx`
# - voici la doc telle que publiée sur `readthedocs.io`  
#   <https://asynciojobs.readthedocs.io/en/main/API.html#asynciojobs.purescheduler.PureScheduler>
# - et le code source correspondant sur github
#   <https://github.com/parmentelat/asynciojobs/blob/main/asynciojobs/purescheduler.py#L44>
# ````

# %% [markdown]
# ## PEP8
#
# d'après la PEP8, on doit
# * utiliser une (ou plusieurs) ligne(s) vide(s) pour séparer les fonctions, classes et les grands blocs d’instructions
# * rappel: les noms de fonctions sont en minuscules
# * rappel: espace autour des opérateurs et après les virgules  
#   `a = f(1, 2) + g(3, 4)`
# * rappel: des espaces autour de l'`=`, et **pas** après la fonction  
#   `f(1, 2)` et non pas ~~`f (1, 2)`~~ car un espace en trop   
#   `a = f(1, 2)` et non pas ~~`a=f(1, 2)`~~ car manque des espaces 

# %% [markdown]
# ## passage d’arguments et références partagées
#
# * le passage de paramètres se fait par référence
# * ce qui crée donc des références partagées
# * et donc une fonction peut modifier les objets qu'on lui passe

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

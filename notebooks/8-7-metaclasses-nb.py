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
#     title: context managers
#   rise:
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


# %% [markdown] slideshow={"slide_type": ""}
# (label-metaclasses)=
# # métaclasses
#
# on a vu [dans ce chapitre](label-classes-intro), et [spécifiquement ici](label-classes-inheritance) les mécanismes généraux de l'héritage en Python  
# mais ici encore, c'est la version simple des choses, car en bon langae objet qui se respecte,  
# Python nous permet aussi .. de **modifier les règles de base de l'héritage** (entre autres) !  
# c'est le propos des métaclasses, que nous allons étudier maintenant

# %% [markdown]
# ## à quoi ça sert ?
#
# hum, bonne question ! en réalité on peut s'en servir pour énormément de choses! (même si, bien souvent il y a d'autres alternatives, dans la ménagerie de concepts Python, pour faire ces choses sans passer par les métaclasses...)  
# mais bon en tous cas c'est intéressant du point de vue conceptuel !  

# %% [markdown]
# ### un prétexte: le singleton
#
# pour quand même travailler sur une application concrète, nous allons illustrer le concept en implémentant la notion de **singleton**  
#
# c'est quoi ? on parle de singleton lorsqu'on veut qu'une classe **n'existe qu'en un seul exemplaire** dans l'application; comme un espèce d'objet global mais qui serait proprement partagé  
# par exemple: la configuration; ou une classe API pour dialoguer avec un autre programme; ou bien un cache pour ranger des données...
#
# mais avant d'en arriver là nous allons devoir faire un peu de théorie...

# %% [markdown]
# ## `type` et `object`
#
# jusqu'ici nous avons vu que
#
# - tout est objet en Python
# - tout objet a un type
# - une classe est un type - à partir d'ici on ne fera plus la distinction entre ces deux termes
# - une classe a aussi possiblement une ou plusieurs super-classes

# %% [markdown]
# ### relation entre objets et types
#
# du coup on peut s'intéresser à la relation binaire entre les objets:
#
# - $X$ **est une instance de** $Y$ ($Y$ est le type de $X$)

# %%
# et pour ça on va se créer quelques classes et objets

class Class: pass

class SubClass(Class): pass

instance = SubClass()

# %% [markdown]
# pour introspecter la relation "est une instance de", c'est facile, on utilise `type()` !

# %%
# remontons la relation en partant de vector

type(instance), type(SubClass), type(Class), type(type)

# %% [markdown]
# ce qui nous donne un premier élément de réponse:
#
# - un **instance** a comme type la classe qui l'a créée
# - une **classe** a comme type .. `type`
#
# ````{admonition} on peut créer une classe avec type()
# :class: admonition-small warning
#
# si vous êtes attentifs: on a dit qu'un objet est créé par son type (sa classe) considérée comme une usine à objets  
# et donc puisque la classe de `Vector` est `type`, ça signifie qu'on aurait pu créer `Vector` en appelant `type()` ?  
#
# eh bien oui, en effet !  
# on a souvent utilisé `type()` avec un seul paramètre, mais il existe aussi une forme avec 3 paramètres, qui permet de créer une classe !
# ````
#
# ce qui nous donne le diagramme suivant
# ```{image} ../media/objects-types.svg
# :align: center
# :width: 400px
# ```

# %% [markdown]
# ````{admonition} Quiz
# :class: seealso
#
# que donne à votre avis `type(int)` ? et `type(object)`
# ```{admonition} réponse
# :class: dropdown
# `int` et `object` sont tous les deux des types/classes, donc leur type, c'est ... `type` aussi
# ```
# ````

# %% [markdown]
# ### héritage entre classes
#
# maintenant regardons quelle est la relation entre classes et super-classes:
#
# - $X$ **hérite directement** $Y$ ($X$ a comme classe de base $Y$)
#
# la question ne se pose pas à propos de `vector` (seules les classes ont des super-classes)  
# mais pour les autres on obtient ceci - en utilisant l'attribut spécial `__bases__`

# %%
# the base classes of our classes

SubClass.__bases__, Class.__bases__

# %%
# the base classes of the builtin classes

object.__bases__, type.__bases__

# %% [markdown]
# donc on obtient, si on superpose les deux relations:
#
# ```{image} ../media/objects-types-bases.svg
# :align: center
# :width: 500px
# ```

# %% [markdown]
# ## comment les objets sont-ils créés ?
#
# une fois que ceci est bien clair, voyons un peu plus en détail comment les objets sont créés en Python  
# c'est-à-dire quand j'appelle par exemple `Class(0)`: 
#
# - l'objet `Class` est donc un *callable*, on va chercher son attribut `__call__`
# - comme il s'agit d'une utilisation implicite de dunder, on **ne cherche pas** dans l'espace de nom de `Person`,
#   mais dans sa classe
# - or on vient de le voir, sa classe c'est `type`; effectivement il existe une méthode `type.__call__()` qui fait - en gros - ceci ([credits](https://stackoverflow.com/questions/6966772/using-the-call-method-of-a-metaclass-instead-of-new))
#
# ```python
# # the actual code is in C, but a pseudo implementation
# # of the type class in Python could look like this
#
# class type:
#     # when calling Class(0), we will call this method with
#     # cls = Class
#     # args = (0,)
#     # kwargs = {}
#     def __call__(cls, *args, **kwarg):
#
#         # ... a few things could possibly be done to cls here... maybe... or maybe not...
#
#         # then we call cls.__new__() to get a new object
#         # think of this as a class method (the object has not been created yet...)
#         obj = cls.__new__(cls, *args, **kwargs)
#
#         # ... a few things done to obj here... maybe... or not...
#
#         # then we call obj.__init__()
#         obj.__init__(*args, **kwargs)
#
#         # ... maybe a few more things done to obj here
#
#         # then we return obj
#         return obj
# ```
#
# c'est-à-dire en français, on crée un objet en passant par deux étapes, qui sont chacune liée à une *dunder*:
#
# - `__new__()` une méthode de classe (car on n'a pas encore créé l'objet)
#   dans l'esprit, elle est chargée d'**allouer la mémoire**
# - `__init__()`une méthode usuelle chargée d'**initialiser l'objet**
#

# %% [markdown]
# ## le cas d'un objet usuel
#
# on peut donc poursuivre notre analyse, on est toujours en train d'évaluer `Class(0)`
#
# au moment d'appeler `__new__` on la cherche à partir de l'objet `Class`  
# qui en général n'a pas redéfini cette méthode  
# on 

# %% [markdown]
# ````{admonition} WIP
# xxx 
# ````

# %% [markdown]
# ## pour en savoir plus
#
# cette section de la doc officielle donne tous les détails
#
# <https://docs.python.org/3/reference/datamodel.html#customizing-class-creation>

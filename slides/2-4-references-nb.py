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
#     title: "r\xE9f\xE9rences partag\xE9es"
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
# # références partagées

# %% [markdown]
# pour visualiser le comportement de nos programmes  
# et notamment cet aspect de partage de la mémoire

# %%
# %load_ext ipythontutor

# %% [markdown] slideshow={"slide_type": "slide"}
# ## composition des types de base

# %% [markdown]
# * tous ces containers peuvent être imbriqués  
#   liste de dictionnaires de …
#
# * donc ils peuvent être composés sans limite
# * uniquement votre faculté à vous y retrouver  
#   (enfin, vous et ceux qui vous lisent …)

# %% slideshow={"slide_type": "slide"}
# %%ipythontutor heapPrimitives=true curInstr=1 width=900 height=850
# une liste avec une sous-liste qui contient un dict et un tuple
L = ['abc', [ { (1, 2) : 1}, ([3], 4)], 5]

# %% [markdown] slideshow={"slide_type": "slide"}
# ## typage dynamique

# %% [markdown]
# * si on exécute `a = 3`
# * Python va
#   * créer un objet représentant 3
#   * créer une variable `a` si elle n’existe pas encore  
#     (une entrée dans une table)
#
#   * faire de `a` une **référence** de l’objet

# %% slideshow={"slide_type": "slide"}
# %%ipythontutor heapPrimitives=true width=800 curInstr=1
a = 3

# %% [markdown] slideshow={"slide_type": "slide"}
# ## références partagées

# %% [markdown]
# du coup on peut **facilement** avoir  
# **plusieurs variables**  
# qui référencent le **même** objet

# %% slideshow={"slide_type": "slide"}
# %%ipythontutor heapPrimitives=true width=800 curInstr=1

# on aurait pu écrire aussi
# a = b = 3
a = 3
b = a

# %% [markdown] slideshow={"slide_type": "slide"}
# ## rappel : mutable *vs* immutable

# %% [markdown]
# * les entiers, les chaines, les tuples sont `immutables`
#   * ils ne **peuvent pas** être modifiés
#   * il n’y a **pas d’effet de bord** possible  
#     sur un objet immutable
#
#   * il est impossible qu’une modification sur `b` affecte `a`    

# %% [markdown] slideshow={"slide_type": "slide"}
# ### références partagées vers objet immutable

# %% slideshow={"slide_type": "-"}
# %%ipythontutor heapPrimitives=true width=800 curInstr=1

a = 3
b = a
a = a + 2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### idem avec objet mutable

# %% [markdown]
# * comme avant, deux références vers le même objet
# * mais que se passe-t-il si l’objet est mutable ?
#   * il peut **être changé**
# * → impact sur **toutes** les références vers cet objet  
#   * depuis une variable 
#   * ou depuis l'intérieur d'un autre objet

# %% cell_style="center" slideshow={"slide_type": "slide"}
# %%ipythontutor heapPrimitives=true width=800 height=300 curInstr=1
a = [1, 2]
b = a
# en changeant a on change b
a[0] = 'spam'


# %% [markdown] slideshow={"slide_type": "slide"}
# ### types mutables / immutables

# %% [markdown] slideshow={"slide_type": ""}
# | type  | mutable ? |
# |-------|-----------|
# | *int* et autres nombres | immutable       |
# | *list* | **mutable**       |
# | *tuple* | immutable       |
# | *dict* | **mutable**       |
# | *set* | **mutable**       |
# | *frozenset* | immutable       |

# %% [markdown] slideshow={"slide_type": ""}
# <div class="rise-footnote">
#     
# les types `tuple` et `frozenset` permettent notamment  
# de construire des **clés** pour les dictionnaires et autres ensembles
#     
# </div>    

# %% [markdown] slideshow={"slide_type": "slide"}
# ## *shallow* et *deep* copies

# %% [markdown]
# * pour ne pas modifier `b`, faire une **copie** de `a`
# * il y a deux types de copies en Python
# * la *shallow copy* (superficielle)
#   * pour les toutes les séquences, utiliser simplement `a[:]`
#   * pour les dictionnaires utiliser `D.copy()`
#   * sinon, utiliser le module `copy.copy()`
# * la *deep copy* (profonde)
#   * `copy.deepcopy()` pour tout copier de manière récursive

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *shallow* et *deep* copies

# %% [markdown]
# * la différence entre *shallow* et *deep* copy n’existe que pour les  
#   objets composites (les objets qui contiennent d’autres objets)
#
# * shallow copy
#   * crée un nouvel objet composite et y insère  
#     les **références** vers les objets contenus dans l’original
#
# * deep copy
#   * crée un nouvel objet et insère de **manière récursive**  
#     une copie des objets trouvés dans l’original
#
#   * évite les boucles infinies

# %% cell_style="center" slideshow={"slide_type": "slide"}
# %%ipythontutor heapPrimitives=true height=350 width=800 curInstr=1
a = [1, 2]
# cette fois-ci on (shallow) copie d'abord
b = a[:] 
a[0] = 'spam'

# %% [markdown] slideshow={"slide_type": "slide"}
# ## *shallow* et *deep*

# %% [markdown] cell_style="split"
# ### *shallow*
#
# ![](../media/copy-1-shallow.svg)

# %% [markdown] cell_style="split"
# ### *deep*
#
# ![](../media/copy-2-deep.svg)

# %% [markdown] slideshow={"slide_type": "slide"} cell_style="center"
# ## `is` et `==`

# %% [markdown]
# * `obj1 is obj2`
#   * ssi obj1 et obj2 sont **le même objet**
#   * forme inverse: `obj1 is not obj2`

# %% [markdown]
# * `obj1 == obj2`
#   * ssi **les valeurs des objets sont égales**
#   * forme inverse `obj1 != obj2`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `is` et `==`

# %% cell_style="split" slideshow={"slide_type": ""}
a = [0, 1, 2]
b = a[:]
a is b

# %% cell_style="split"



a == b

# %% cell_style="split"
c = d = [0, 1, 2]
c is d

# %% cell_style="split"
c == a

# %% [markdown] slideshow={"slide_type": "slide"}
# ### copie profonde nécessaire ?

# %% cell_style="center" slideshow={"slide_type": "-"}
# %%ipythontutor heapPrimitives=true height=450 width=800 curInstr=1
a = [1, [2]]
# on ne fait qu'une copie 'shallow'
b = a[:]
a[1][0] = 'boom'
print(a)
print(b)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### avec une copie profonde

# %% cell_style="center" slideshow={}
# %%ipythontutor heapPrimitives=true height=500 width=900 curInstr=2
import copy
a = [1, [2]]
# avec une copie profonde on n'a plus de souci
b = copy.deepcopy(a)
a[1][0] = 'boom'
print(a)
print(b)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## autres types de références partagées

# %% [markdown]
# jusqu'ici, références partagées créées par **affectation**  
#
# il existe (plein) d'autres cas de figure :
#
# * appel de fonction  
#   l'objet passé en argument à une fonction  
#   se retrouve affecté au **paramètre** dans la **fonction**
#
# * se méfier aussi des références **entre objets**

# %% [markdown] slideshow={"slide_type": "slide"}
# ### appel de fonction

# %%
# %%ipythontutor
L = [1, 2, 3]

def foo(x):
    x[1] = 'BOOM'

foo(L)
print(L)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### références entre objets

# %% [markdown]
# toutes les parties d'objet qui sont atteignables à partir d'autres objets peuvent devenir des références partagées
#
# pas besoin qu'il y ait nécessairement plusieurs variables dans le paysage
#
# on peut le voir sur l'exemple pathologique suivant

# %% cell_style="center" slideshow={"slide_type": "slide"}
# %%ipythontutor heapPrimitives=true height=400 width=900 curInstr=1

repete = 4 * [[0]]
print(f"repete avant {repete}")

repete[0][0] = 1
print(f"repete après {repete}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### structures cycliques

# %% [markdown]
# ainsi on peut aussi créer des structures cycliques

# %% slideshow={"slide_type": ""}
# %%ipythontutor

L = [None]
L[0] = L
print(L)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## gestion de la mémoire

# %% [markdown]
# * Python sait réutiliser les objets  
#   *e.g.* les petits entiers - slide suivant
#
# * Python sait libérer les objets non utilisés (garbage collector)
#   * un objet sans référence est libéré
#   * contrôle via le module `gc`
# * chaque objet contient deux champs dans l’entête
#   * un champ désignant le typage - cf `type(obj)`
#   * un champ contenant un compteur de références  
#     voir `sys.getrefcount(obj)`      

# %% [markdown] slideshow={"slide_type": "slide"}
# ### optimisation interne à Python

# %% cell_style="split"
# avec cette forme 
# on crée deux objets liste
L = [1, 2]
M = [1, 2] # nouvel objet liste
L is M

# %% cell_style="split"
# ici aussi on pourrait penser
# créer deux objets int
I = 18
J = 18   # nouvel objet entier ?
I is J   # non: partage
         # (optimisation)

# %% [markdown]
# * est-ce que ça pose un problème ?
#   * non ! l’optimisation n’est que pour des types **immutables**

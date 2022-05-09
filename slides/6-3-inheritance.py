# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version, -language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode, -language_info.file_extension, -language_info.mimetype,
#       -toc
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
#     title: "h\xE9ritage"
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
# <span>Thierry Parmentelat</span>
# </div>
#
# <style>
# .smaller {font-size: smaller}
# </style>

# %% [markdown] slideshow={"slide_type": ""}
# # POO & héritage

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour réutiliser du code en python

# %% [markdown]
# * fonctions
#   * pas d'état après exécution
# * modules
#   * garde l'état
#   * une seule instance par programme
# * **classes**
#   * **instances multiples**
#   * **chacune garde l'état**
#   * **héritage**

# %% [markdown] slideshow={"slide_type": "slide"}
# ### programmation orientée objet
#
# pourquoi et comment ?

# %% [markdown] cell_style="split"
# #### deux objectifs
#
# * modularité
# * réutilisabilité

# %% [markdown] cell_style="split"
# #### deux moyens
#
# * espaces de nom
# * héritage

# %% [markdown] slideshow={"slide_type": "slide"}
# ### modularité & réutilisabilité

# %% [markdown] cell_style="split"
# * du code modulaire
#   * grouper le code dans une classe
#   * grouper les données dans un objet
#
# * plus on découpe en petits morceaux
#   * plus on a de chances de pouvoir réutiliser

# %% [markdown] cell_style="split"
# * DRY *don't repeat yourself*
#   * *cut'n paste is evil*
# * code générique
#   * ex: un jeu fait "avancer" une collection d'objets
#   * dès qu'un objet explique comment il avance
#   * il peut faire partie de la simulation
# * c'est là qu'intervient l'héritage

# %% [markdown] slideshow={"slide_type": "slide"}
# ## espaces de nom

# %% [markdown]
# * tous les objets qui sont
#   * un module
#   * une classe
#   * une instance (sauf des classes *builtin*)
# * constituent chacun **un espace de nom**
#   * i.e. une association *attribut* → *objet*

# %% [markdown] slideshow={"slide_type": "slide"}
# ### espaces de nom - pourquoi

# %% [markdown]
# * permet de lever l'ambigüité en cas d'homonymie
#   * si 2 modules utilisent tous les 2 une globale `truc`
#   * elles peuvent coexister sans souci
# * les espaces de nom sont imbriqués (*nested*)
#   * ex. `package.module.classe.methode`
# * on peut accéder à tous les objets
#   * dès qu'on sait le faire à partir d'une variable
#   * par exemple un module importé
# * l'héritage rend cela dynamique
#   * i.e. la résolution des attributs **est faite à *runtime***

# %% [markdown] slideshow={"slide_type": "slide"}
# ### espaces de nom - variables et attributs

# %% [markdown] cell_style="split"
# #### deux mondes étanches
#
# * variables
# * attributs

# %% [markdown] cell_style="split"
# #### se mélangent
#
# * apparemment seulement
# * apprenez à bien lire

# %% [markdown]
# typiquement dans une expression comme `a.b.c`

# %% [markdown] cell_style="split"
# * `a` est une **variable**

# %% [markdown] cell_style="split"
# * `b`, et `c` sont des **attributs**

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ##### résolution des **variables** : statique
#
# * entièrement **lexical**
# * en remontant dans le code
# * avec les règles LEGB  
#   local, englobant, global, *builtin*

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ##### résolution des **attributs** : dynamique
#
# * dans le monde des **objets**
# * en remontant les espaces de nom
# * essentiellement **dynamique**  
#   *i.e.* à *runtime*

# %% [markdown] cell_style="center" slideshow={"slide_type": ""}
# *par ex* dans `a.b.c`
#
# * la variable `a` est identifiée lexicalement  
#   (variable locale, paramètre de fonction,  
#    voir par exemple le cas des clôtures)
# * la variable référence un objet  
#   et `b` est cherché comme un attribut à partir de cet objet

# %% [markdown] slideshow={"slide_type": "slide"}
# ## résolution d'attribut pour la lecture

# %% [markdown] slideshow={"slide_type": ""} cell_style="center"
# * la **résolution des attributs**
# * fournit la **mécanique de base** de la POO
# * et sous-tend notamment (mais pas que)  
#   la mécanique de l'héritage

# %% [markdown]
# ### lecture ou écriture des attributs

# %% [markdown] cell_style="center"
# on distingue deux cas
# * attribut en écriture  
#    `obj.attribute = ...`  
#    (i.e. à gauche d'une affectation)
# * résolution des attributs en lecture  
#     `obj.attribute` 

# %% [markdown] slideshow={"slide_type": "slide"}
# ### lecture: recherche de bas en haut

# %% [markdown]
# **pour la lecture :**  
# la règle pour chercher un attribut en partant d'un objet consiste à
#
# * le chercher dans l'espace de nom de l'objet lui-même
# * sinon dans l'espace de nom de sa classe
# * sinon dans les super-classes  
#   (on verra les détails plus loin)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## ex1. de résolution d'attribut

# %% cell_style="split"
# cas simple sans héritage
# appel d'une méthode
import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length(self):
        return math.sqrt(
            self.x**2 + self.y**2)


# %% cell_style="split"
# quand on cherche vector.length
# on cherche
# 1. dans vector - pas trouvé
# 2. dans Vector - bingo

vector = Vector(3, 4)
vector.length()

# %% cell_style="split"
# on va voir ça en détail 
# dans pythontutor
# %load_ext ipythontutor

# %% [markdown] slideshow={"slide_type": "slide"}
# ### 2 espaces de nom distincts

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# * la classe `Vector` a les attributs
#   * `__init__`
#   * `length`

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# * l'objet `vector` a les attributs
#   * `x` et `y`,
#   * mais pas `length` !

# %% slideshow={"slide_type": "slide"}
# %%ipythontutor width=1000 height=400 curInstr=7
import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

vector = Vector(2, 2)

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### digression : l'attribut spécial `__dict__`

# %% [markdown] slideshow={"slide_type": ""} cell_style="split" tags=["level_intermediate"]
# pour visualiser la même chose sans ipythontutor  
# sachez que les (objets qui sont des) espaces de nom
#
# * ont un **attribut spécial**
# * qui s'appelle `__dict__`
# * qui permet d'inspecter un espace de nom
#
# ce n'est pas une notion à retenir,  
# mais on va s'en servir dans la suite  
# pour regarder le contenu des espaces de nom

# %% tags=["level_intermediate"]
# dans l'instance
list(vector.__dict__)

# %% slideshow={"slide_type": ""} tags=["level_intermediate"]
# les attributs 'intéressants' de Vector
[att for att in Vector.__dict__ if '__' not in att or att == '__init__']

# %% [markdown] slideshow={"slide_type": "slide"}
# ### la  fonction `dir()`
#
# * avec la fonction *builtin* `dir(x)`, on peut accéder  
#   à l'ensemble des attributs qui sont disponibles sur `x`
# * c'est donc la somme des attributs trouvés:
#   * dans l'espace de nom de `x`
#   * dans l'espace de nom de sa classe
#   * et de ses super-classes

# %% cell_style="split"
# sur l'instance

# (on enlève le bruit)
[x for x in dir(vector) if '__' not in x]

# %% cell_style="split"
# sur la classe

[x for x in dir(Vector) if '__' not in x]


# %% [markdown] slideshow={"slide_type": "slide"}
# ### conclusion
#
# dans ce cas simple de la classe `Vector` et de l'instance `vector`:
# * `vector.x` fait référence à l'attribut posé **directement sur l'instance**
# * `vector.length` fait référence à la méthode qui est **dans la classe**

# %% [markdown] slideshow={"slide_type": "slide"}
# ## ex2. résolution d'attribut avec héritage

# %% [markdown] slideshow={"slide_type": ""}
# * jusqu'ici on n'a pas d'héritage  
#   puisque pour l'instant on n'a qu'une classe
# * mais l'héritage  
#   est une **simple prolongation** de cette logique

# %%
# une classe fille sans aucun contenu
class SubVector(Vector):
    pass

subvector = SubVector(6, 8)

# comment fait-on pour trouver subvector.length ?
subvector.length()

# %% slideshow={"slide_type": "slide"}
# %%ipythontutor width=1000 height=400 curInstr=8
import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def length(self):
        return math.sqrt(self.x**2 + self.y**2)
class SubVector(Vector):
    pass

subvector = SubVector(6, 8)

# %% [markdown] slideshow={"slide_type": "slide"}
# * c'est exactement le même mécanisme qui est à l'oeuvre :
# * quand on va vouloir appeler `subvector.length()`  
#   on cherche l'attribut `length` 
#   * dans l'instance `subvector` : non
#   * dans sa classe `SubVector` : non
#   * dans la super-classe `Vector` : ok, on prend ça

# %% [markdown] slideshow={"slide_type": "slide"}
# ## écriture d'attribut: pas de recherche

# %% [markdown] slideshow={"slide_type": ""}
# * le mécanisme de résolution d'attribut qu'on vient de voir  
#   ne fonctionne que **pour la lecture des attributs**
# * quand on **écrit** un attribut dans un objet,  
#   le mécanisme est beaucoup plus simple:  
#   on écrit **directement dans l'espace de nom** de l'objet
# * on considère que c'est une écriture  
#   si le terme `obj.attribute` est **à gauche** d'une affectation  
# * typiquement `self.name = name` dans le constructeur

# %% cell_style="split"
# quand on évalue un attribut en lecture
# on recherche en partant de l'objet
# et donc ici on trouve la méthode
# dans l'espace de noms de la super-classe
subvector.length()

# %% cell_style="split"
# mais quand on écrit un attribut
# c'est une autre histoire complètement
# l'attribut est créé directement dans l'objet
subvector.foo = 12

'foo' in subvector.__dict__


# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### lecture *vs* écriture - cas limites

# %% [markdown] cell_style="split" tags=["level_intermediate"]
# * il y a écriture si  
#   et seulement si il y a **affectation**
# * dans 1. il y a
#   * **lecture** de l'attribut `liste`
#   * même si on modifie l'objet
# * dans 2. il y a
#   * **écriture de l'attribut**
#   * donc écrit dans (l'espace de nom) `obj`

# %% [markdown] cell_style="split" tags=["level_intermediate"]
# * 1. lecture !
#
# ```python
# obj.liste.append('foo')
# ```
#
# * 2. écriture
#
# ```python
# obj.liste += ['foo']
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## héritage

# %% [markdown] slideshow={"slide_type": ""} cell_style="split"
# une classe peut hériter d’une  
#   (ou plusieurs) autre classes
#   
# ```python
# # la syntaxe est
# class Class(Super):
#     pass
#
# # ou 
# class Class(Super1, Super2):
#     pass
# ```

# %% [markdown] slideshow={"slide_type": ""} cell_style="split"
# * si A hérite de B, ont dit que
#   * A est une **sous-classe** de B
#   * et B est la **super-classe** de A
# * de ce qui précède:
#   * la sous-classe hérite  
#     (des attributs)  
#     de sa (ses) super-classe(s)
#   * l’instance hérite de la  
#     classe qui la crée

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `isinstance()` et `issubclass()`

# %% [markdown]
# * `isinstance(x, class1)` retourne `True` si   
#   `x` est une instance de `class1` **ou d’une super classe**
# * `issubclass(class1, class2)` retourne `True` si  
#   `class1` est une sous-classe de `class2`

# %% cell_style="split"
# A est la super-classe
class A:
    pass


class B(A):
    pass


a, b = A(), B()

# %% cell_style="split" slideshow={"slide_type": ""}
isinstance(a, A), issubclass(B, A)

# %% cell_style="split"
isinstance(b, A), isinstance(a, B)

# %% cell_style="split"
# accepte plusieurs types/classes
isinstance(a, (A, B))


# %% [markdown]
# <div class=note>
#    
# * on peut aussi passer à `isinstance` un tuple de classes/types
# * ces fonctions *builtin* sont à privilégier par rapport à l'utilisation de `type()`
#     
#
# </div>
#     

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `super()`

# %% [markdown]
# * utile lorsque la spécialisation  
#   consiste à ajouter ou modifier  
#   par rapport à la classe mère
#
# * le cas typique est d'ailleurs le constructeur  
#   dès qu'on ajoute un attribut de donnée
#
# * permet de ne pas mentionner explicitement  
#   le nom de la classe mère (code + générique)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `super()` dans le constructeur

# %% cell_style="split" slideshow={"slide_type": ""}
# illustration de super() 
# dans le constructeur

class C:
    def __init__(self, x):
        print("init x par superclasse")
        self.x = x

class D(C):
    def __init__(self, x, y):
        # initialiser : la classe C
        super().__init__(x)
        print("init y par classe")
        self.y = y


# %% cell_style="split"
c = C(10)

# %% cell_style="split"
d = D(100, 200)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### `super()` dans une méthode standard

# %% cell_style="split" slideshow={"slide_type": ""}
# super() est souvent rencontrée
# dans __init__ mais s'applique
# partout
class C:
    def f(self):
        print('f dans C')


# %% cell_style="split" slideshow={"slide_type": ""}
class D(C):
    def f(self):
        # remarquez l'absence
        # de self !
        super().f()
        print('f dans D')


# %% cell_style="split"
c = C(); c.f()

# %% cell_style="split"
d = D(); d.f()


# %% [markdown] slideshow={"slide_type": "slide"}
# ## résumé
#
# * les instances et classes sont des objets mutables (sauf classes *builtin*)
# * on utilise `isinstance()` pour tester le type d'un objet
# * chaque instance et chaque classe est un espace de nom
# * lorsqu'on écrit un attribut, on écrit directement dans l'espace de nom de cet objet
# * en lecture, on résoud la référence d'un attribut de bas en haut
# * une méthode peut faire référence à la super-classe avec `super()`
# * en général
#   * les classes ont des attributs de type méthode
#   * les objets ont des attributs de type donnée
#   * mais le modèle est flexible

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## anx1: MRO & graphe d’héritage

# %% [markdown] slideshow={"slide_type": ""} tags=["level_intermediate"]
# ### graphe d'héritage
#
# * on peut donc construire un graphe d’héritage
# * allant des super-classes aux instances

# %% [markdown] cell_style="split" tags=["level_intermediate"]
# ![arbre de classes](media/classes.png)

# %% cell_style="split" tags=["level_intermediate"]
class C1:
    pass
class C2:
    pass
class C(C1, C2):
    def func(self, x):
        self.x = 10
o1 = C()
o2 = C()


# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### MRO: *method resolution order*

# %% [markdown] tags=["level_intermediate"]
# * MRO : method resolution order
# * l’algorithme est le suivant
#   * liste toutes les super-classes en utilisant  
#     un algorithme DFLR (depth first, left to right)
#
#   * si classe dupliquée,  
#     **ne garder que la dernière** occurrence

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ![MRO](media/mro.png)

# %% cell_style="split" tags=["level_intermediate"]
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass


# %% [markdown] tags=["level_intermediate"]
# * parcours DFLR: `D`, `B`, `A`, `object`, `C`, `A`, `object`
# * suppressions : `D`, `B`, ~~`A`~~, ~~`object`~~, `C`, `A`, `object`

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## anx2: attributs de classe

# %% [markdown] tags=["level_intermediate"]
# dans (l'espace de nom d')une classe, on peut mettre 
#
# * des méthodes (on le savait) 
# * et aussi attributs *normaux* - qui référencent des données
#
# rien de nouveau point de vue syntaxe : 
#
# * on écrit juste la déclaration dans la classe,
# * au même niveau d'imbrication que les méthodes
#
# voyons cela sur un exemple

# %% cell_style="split" slideshow={"slide_type": "slide"} tags=["level_intermediate"]
class Factory:
    # un compteur global à la classe
    # dans lequel on va pouvoir mémoriser 
    # tous les labels de toutes les instances
    all_labels = []

    def __init__(self, label):
        self.label = label
        Factory.all_labels.append(label)
        # on aurait pu écrire
        # self.all_labels.append(label)
        # mais c'est dangereux !

Factory.all_labels

# %% cell_style="split" slideshow={"slide_type": ""} tags=["level_intermediate"]
f1 = Factory('premier')
Factory.all_labels

# %% cell_style="split" slideshow={"slide_type": ""} tags=["level_intermediate"]
f2 = Factory('second')
Factory.all_labels

# %% tags=["level_intermediate"]
# on trouve le même objet quel que soit l'endroit d'où on part
f1.all_labels is f2.all_labels is Factory.all_labels

# -*- coding: utf-8 -*-
# ---
# jupyter:
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
#     title: "h\xE9ritage"
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
# # POO & héritage

# %% [markdown]
# ## pour réutiliser du code en python
#
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

# %% [markdown] tags=["gridwidth-1-2"]
# #### deux objectifs
#
# * modularité
# * réutilisabilité

# %% [markdown] tags=["gridwidth-1-2"]
# #### deux moyens
#
# * espaces de nom
# * héritage

# %% [markdown] slideshow={"slide_type": "slide"}
# ### modularité & réutilisabilité

# %% [markdown] tags=["gridwidth-1-2"]
# * du code modulaire
#   * grouper le code dans une classe
#   * grouper les données dans un objet
#
# * plus on découpe en petits morceaux
#   * plus on a de chances de pouvoir réutiliser

# %% [markdown] tags=["gridwidth-1-2"]
# * DRY *don't repeat yourself*
#   * *cut'n paste is evil*
# * code générique
#   * ex: un jeu fait "avancer" une collection d'objets
#   * dès qu'un objet explique comment il avance
#   * il peut faire partie de la simulation
# * c'est là qu'intervient l'héritage

# %% [markdown]
# ## espaces de nom
#
# * tous les objets qui sont
#   * un module
#   * une classe
#   * une instance (sauf des classes *builtin*)
# * constituent chacun **un espace de nom**
#   * i.e. une association *attribut* → *objet*

# %% [markdown]
# ### espaces de nom - pourquoi
#
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

# %% [markdown] tags=["gridwidth-1-2"]
# #### deux mondes étanches
#
# * variables
# * attributs

# %% [markdown] tags=["gridwidth-1-2"]
# #### se mélangent
#
# * apparemment seulement
# * apprenez à bien lire

# %% [markdown]
# typiquement dans une expression comme `a.b.c`

# %% [markdown] tags=["gridwidth-1-2"]
# * `a` est une **variable**

# %% [markdown] tags=["gridwidth-1-2"]
# * `b`, et `c` sont des **attributs**

# %% [markdown] slideshow={"slide_type": "slide"} tags=["gridwidth-1-2"]
# ##### résolution des **variables** : statique
#
# * entièrement **lexical**
# * en remontant dans le code
# * avec les règles LEGB  
#   local, englobant, global, *builtin*

# %% [markdown] slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
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
#
# * la variable référence un objet  
#   et `b` est cherché comme un attribut à partir de cet objet

# %% [markdown] slideshow={"slide_type": ""} cell_style="center"
# ## résolution d'attribut pour la lecture
#
# * la **résolution des attributs**
# * fournit la **mécanique de base** de la POO
# * et sous-tend notamment (mais pas que)  
#   la mécanique de l'héritage

# %% [markdown] cell_style="center"
# ### lecture ou écriture des attributs
#
# on distingue deux cas
#
# * attribut en écriture  
#    `obj.attribute = ...`  
#    (i.e. à gauche d'une affectation)
#
# * résolution des attributs en lecture  
#     `obj.attribute` 

# %% [markdown]
# ### lecture: recherche de bas en haut
#
# **pour la lecture :**  
# la règle pour chercher un attribut en partant d'un objet consiste à
#
# * le chercher dans l'espace de nom de l'objet lui-même
# * sinon dans l'espace de nom de sa classe
# * sinon dans les super-classes  
#   (on verra les détails plus loin)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## ex1. de résolution d'attribut

# %% tags=["gridwidth-1-2"]
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


# %% tags=["gridwidth-1-2"]
# quand on cherche vector.length
# on cherche
# 1. dans vector - pas trouvé
# 2. dans Vector - bingo

vector = Vector(3, 4)
vector.length()

# %% tags=[]
# on va voir ça en détail 
# dans pythontutor
# %load_ext ipythontutor

# %% [markdown] slideshow={"slide_type": "slide"}
# ### 2 espaces de nom distincts

# %% [markdown] slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
# * la classe `Vector` a les attributs
#   * `__init__`
#   * `length`

# %% [markdown] slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
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

# %% [markdown] slideshow={"slide_type": ""} tags=["level_intermediate"]
# ### digression : la fonction `vars()`
#
# pour visualiser la même chose sans ipythontutor  
# sachez que l'on peut inspecter le contenu d'un espace de noms
# avec la fonction `vars(obj)`
#
# <div class=mynote>
#     
# ce n'est pas forcément une notion à retenir, mais on va s'en servir dans la suite  
# pour regarder le contenu des espaces de nom
#     
# </div>    

# %% tags=["level_intermediate"]
# dans l'instance
vars(vector)

# %% slideshow={"slide_type": ""} tags=["level_intermediate"]
# les attributs 'intéressants' de Vector
[att for att in vars(Vector) if '__' not in att or att == '__init__']

# %% [markdown] slideshow={"slide_type": "slide"}
# ### la  fonction `dir()`
#
# * avec la fonction *builtin* `dir(x)`, on peut accéder  
#   à l'ensemble des attributs qui sont disponibles sur `x`
#
# * c'est donc la somme des attributs trouvés:
#   * dans l'espace de nom de `x`
#   * dans l'espace de nom de sa classe
#   * et de ses super-classes

# %% tags=["gridwidth-1-2"]
# sur l'instance

# (on enlève le bruit)
[x for x in dir(vector) if '__' not in x]

# %% tags=["gridwidth-1-2"]
# sur la classe

[x for x in dir(Vector) if '__' not in x]


# %% [markdown] slideshow={"slide_type": "slide"}
# ### conclusion
#
# dans ce cas simple de la classe `Vector` et de l'instance `vector`:
#
# * `vector.x` fait référence à l'attribut posé **directement sur l'instance**
# * `vector.length` fait référence à la méthode qui est **dans la classe**

# %% [markdown] slideshow={"slide_type": ""}
# ## ex2. résolution d'attribut avec héritage
#
# * jusqu'ici on n'a pas d'héritage  
#   puisque pour l'instant on n'a qu'une classe
#
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

# %% [markdown] slideshow={"slide_type": ""}
# ## écriture d'attribut: pas de recherche
#
# * le mécanisme de résolution d'attribut qu'on vient de voir  
#   ne fonctionne que **pour la lecture des attributs**
#
# * quand on **écrit** un attribut dans un objet,  
#   le mécanisme est beaucoup plus simple:  
#   on écrit **directement dans l'espace de nom** de l'objet
#
# * on considère que c'est une écriture  
#   si le terme `obj.attribute` est **à gauche** d'une affectation  
#
# * typiquement `self.name = name` dans le constructeur

# %% tags=["gridwidth-1-2"]
# quand on évalue un attribut en lecture
# on recherche en partant de l'objet
# et donc ici on trouve la méthode
# dans l'espace de noms de la super-classe
subvector.length()

# %% tags=["gridwidth-1-2"]
# mais quand on écrit un attribut
# c'est une autre histoire complètement
# l'attribut est créé directement dans l'objet
subvector.foo = 12

'foo' in vars(subvector)


# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### lecture *vs* écriture - cas limites

# %% [markdown] tags=["level_intermediate", "gridwidth-1-2"]
# * il y a écriture si  
#   et seulement si il y a **affectation**
#
# * dans 1. il y a
#   * **lecture** de l'attribut `liste`
#   * même si on modifie l'objet
# * dans 2. il y a
#   * **écriture de l'attribut**
#   * donc écrit dans (l'espace de nom) `obj`

# %% [markdown] tags=["level_intermediate", "gridwidth-1-2"]
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
# ## héritage - syntaxe

# %% [markdown] slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
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

# %% [markdown] slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
# * si A hérite de B, ont dit que
#   * A est une **sous-classe** de B
#   * et B est la **super-classe** de A
# * de ce qui précède:
#   * la sous-classe hérite  
#     (des attributs)  
#     de sa (ses) super-classe(s)
#
#   * l’instance hérite de la  
#     classe qui la crée

# %% [markdown]
# ## `isinstance()` et `issubclass()`
#
# * `isinstance(x, class1)` retourne `True` si   
#   `x` est une instance de `class1` **ou d’une super classe**
#
# * `issubclass(class1, class2)` retourne `True` si  
#   `class1` est une sous-classe de `class2`

# %% tags=["gridwidth-1-2"]
# A est la super-classe
class A:
    pass


class B(A):
    pass


a, b = A(), B()

# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
isinstance(a, A), issubclass(B, A)

# %% tags=["gridwidth-1-2"]
isinstance(b, A), isinstance(a, B)

# %% tags=["gridwidth-1-2"]
# accepte plusieurs types/classes
isinstance(a, (A, B))


# %% [markdown]
# <div class=mynote>
#    
# * on peut aussi passer à `isinstance` un tuple de classes/types
# * ces fonctions *builtin* sont à privilégier par rapport à l'utilisation de `type()`
#     
#
# </div>
#     

# %% [markdown]
# ## `super()`
#
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

# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
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


# %% tags=["gridwidth-1-2"]
c = C(10)

# %% tags=["gridwidth-1-2"]
d = D(100, 200)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### `super()` dans une méthode standard

# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
# super() est souvent rencontrée
# dans __init__ mais s'applique
# partout
class C:
    def f(self):
        print('f dans C')


# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
class D(C):
    def f(self):
        # remarquez l'absence
        # de self !
        super().f()
        print('f dans D')


# %% tags=["gridwidth-1-2"]
c = C(); c.f()

# %% tags=["gridwidth-1-2"]
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

# %% [markdown] tags=["level_intermediate", "gridwidth-1-2"]
# ![arbre de classes](media/classes.png)

# %% tags=["level_intermediate", "gridwidth-1-2"]
class C1:
    pass
class C2:
    pass
class C(C1, C2):
    def func(self, x):
        self.x = 10
o1 = C()
o2 = C()


# %% [markdown] tags=["level_intermediate"]
# ### MRO: *method resolution order*
#
# * MRO : method resolution order
# * l’algorithme est le suivant
#   * liste toutes les super-classes en utilisant  
#     un algorithme DFLR (depth first, left to right)
#
#   * si classe dupliquée,  
#     **ne garder que la dernière** occurrence

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate", "gridwidth-1-2"]
# ![MRO](media/mro.png)

# %% tags=["level_intermediate", "gridwidth-1-2"]
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass


# %% [markdown] tags=["level_intermediate"]
# * parcours DFLR: `D`, `B`, `A`, `object`, `C`, `A`, `object`
# * suppressions : `D`, `B`, ~~`A`~~, ~~`object`~~, `C`, `A`, `object`

# %% [markdown] tags=["level_intermediate"]
# ## anx2: attributs de classe
#
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

# %% slideshow={"slide_type": "slide"} tags=["level_intermediate", "gridwidth-1-2"]
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

# %% slideshow={"slide_type": ""} tags=["level_intermediate", "gridwidth-1-2"]
f1 = Factory('premier')
Factory.all_labels

# %% slideshow={"slide_type": ""} tags=["level_intermediate", "gridwidth-1-2"]
f2 = Factory('second')
Factory.all_labels

# %% tags=["level_intermediate"]
# on trouve le même objet quel que soit l'endroit d'où on part
f1.all_labels is f2.all_labels is Factory.all_labels

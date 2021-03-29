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
#   notebookname: "h\xE9ritage"
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
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% slideshow={"slide_type": "slide"}
from plan import plan; plan("classes", "avancé")


# %% [markdown] slideshow={"slide_type": "slide"}
# # POO : avancé

# %% [markdown] slideshow={"slide_type": "slide"}
# ## classes et instances

# %% [markdown]
# * les classes et les instances sont des **objets mutables**
#   * on peut donc les modifier après création
#   * même par exemple ajouter des méthodes !
#   * **sauf** pour les classes **`builtin`** !
# * chaque classe et chaque instance
#   * constitue un espace de nommage
# * les classes et les instances : objets presque identiques
#   * par rapport à 'espace de nommage'
#   * et 'résolution des attributs'

# %% [markdown] slideshow={"slide_type": "slide"}
# ### l'instruction `class`

# %% [markdown]
# * une classe est définie par le mot clef `class`
#   * une classe définit des attributs
#   * création à l'évaluation de l'instruction `class`

# %%
# je définis une classe
class Foo:
    def x(self):
        pass


# %%
# ce qui définit la variable Foo
Foo

# %%
# et dans cet objet on trouve un attribut
# qui est une fonction (méthode)
Foo.x

# %% [markdown] slideshow={"slide_type": "slide"}
# ### constructeur

# %% [markdown]
# * une instance (l’objet) est créée lorsqu’une classe est appelée
# * l’instance hérite de tous les attributs de la classe qui l’a créé

# %%
# la classe est une usine à instance
# dit autrement, c'est une fonction
# qu'on peut appeler et qui retourne une instance
foo = Foo()
foo

# %%
# comme on l'a déjà vu, l'instance
# hérite ses attributs de la classe
foo.x


# %% [markdown] slideshow={"slide_type": "slide"}
# ### classe = usine à objets

# %% [markdown] slideshow={"slide_type": ""}
# * une classe est une usine à instances
# * peut créer **plusieurs instances** d’une même classe
# * en cela une classe est **différente d’un module**

# %% [markdown] slideshow={"slide_type": "slide"}
# ## héritage

# %% [markdown] slideshow={"slide_type": ""}
# * une classe peut hériter d’une (ou plusieurs) autre classes
# * si A hérite de B
#   * on dit que A est la sous-classe de B
#   * et B est la super-classe de A
# * la sous-classe hérite des attributs de sa super-classe
# * l’instance hérite de la classe qui la crée

# %% [markdown] slideshow={"slide_type": "slide"}
# ### graphe d'héritage
#
# * on peut donc construire un graphe d’héritage
# * allant des super-classes aux instances

# %% [markdown] cell_style="split"
# ![arbre de classes](media/classes.png)

# %% cell_style="split"
class C1:
    pass
class C2:
    pass
class C(C1, C2):
    def func(self, x):
        self.x = 10
o1 = C()
o2 = C()


# %% [markdown] tags=["level_intermediate"] slideshow={"slide_type": "slide"}
# ## attributs de classe

# %% slideshow={"slide_type": ""} tags=["level_intermediate"]
class Factory:
    # un compteur global à la classe
    all_labels = []

    def __init__(self, label):
        self.label = label
        # ici je pourrais aussi bien écrire
        # Factory.all_labels.append(label)
        # MAIS PAS self.all_labels = self.all_labels + [label]
        # pourquoi ?
        self.all_labels.append(label)

Factory.all_labels

# %% cell_style="split" slideshow={"slide_type": ""} tags=["level_intermediate"]
f1 = Factory('premier')
Factory.all_labels

# %% cell_style="split" slideshow={"slide_type": ""} tags=["level_intermediate"]
f2 = Factory('second')
Factory.all_labels


# %% tags=["level_intermediate"] slideshow={"slide_type": "slide"}
# %load_ext ipythontutor

# %% cell_style="center" slideshow={"slide_type": ""} tags=["level_intermediate"]
# %%ipythontutor width=1000 height=400
class Factory:
    all_labels = []
    def __init__(self, label):
        self.label = label
        self.all_labels.append(label)
f1 = Factory('premier')
f2 = Factory('second')

# %% tags=["level_advanced"]
# %%ipythontutor width=1000 height=400 curInstr=1
class Factory:
    all_labels = []

    def __init__(self, label):
        self.label = label
        # cette forme ne fonctionne pas comme attendu
        self.all_labels = self.all_labels + [label]

f1 = Factory('premier')
f2 = Factory('second')


# %% [markdown] slideshow={"slide_type": "slide"}
# ## référencer un attribut

# %% [markdown]
# * tous les objets ne peuvent pas avoir des attributs
#   * oui pour : packages, modules, classes et instances
#   * mais **pas les (instances de) types de base**
# * pour chercher un attribut dans un objet, deux méthodes
#   * `object.attribut`
#   * `getattr()`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `getattr()`
#
# * il s'agit d'une fonction **builtin**

# %%
class Bar: 
    x = 10
bar = Bar()

# %%
# là il faut que je connaisse le nom de l'attribut
# au moment où j'écris le code
bar.x

# %% cell_style="split"
# ici par contre je passe une chaine
getattr(bar, 'x')

# %% cell_style="split"
# que je pourrais donc **calculer**
attribut = chr(120)
getattr(bar, attribut)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `getattr()`/`setattr()`

# %% [markdown] slideshow={"slide_type": ""}
# * avec `getattr` le nom de l'attribut est un `str`
#   * pas restreint par la syntaxe des identifieurs
#   * de plus on peut le **calculer**
# * la fonction *builtin* `setattr`
#   * fait ce que vous croyez..

# %% cell_style="split"
# un nom d'attribut folklorique
attribut = 'x->y'
setattr(bar, attribut, 42)

# %% cell_style="split"
# on ne peut pas écrire bar.x->y
# mais par contre
getattr(bar, attribut)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### résumé - accès aux attributs

# %% [markdown]
# **en résumé**
#
# * `obj.name` ⇔ `getattr(obj, 'name')`
# * `obj.name = value` ⇔ `setattr(obj, 'name', value)`
#
# **et rappelez-vous également que**
#
# * la lecture fait une **recherche**  
#   de l'instance aux super-classes
#
# * l'écriture (présence d'une affectation)  
#   **écrit directement dans l'objet**
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### lecture *vs* écriture

# %% [markdown] cell_style="split"
# * il y a écriture si  
#   et seulement si il y a **affectation**
# * dans 1. il y a
#   * **lecture** de l'attribut `liste`
#   * même si on modifie l'objet
# * dans 2. il y a
#   * **écriture de l'attribut**
#   * donc écrit dans `obj`

# %% [markdown] cell_style="split"
# * 1. lecture !
# ```python
# obj.liste.append('foo')
# ```
#
# * 2. écriture
# ```python
# obj.liste += ['foo']
# ```
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### remarque

# %% [markdown] cell_style="center" slideshow={"slide_type": ""}
# **comme tous les traits du langage**
#
# * le comportement de `.`
# * est redéfinissable pour une classe
# * par surcharge des méthodes spéciales
# * on en reparlera...

# %% [markdown] slideshow={"slide_type": "slide"}
# ## espace de nommage de l’instance

# %% [markdown]
# * à l'appel de `__init__`:
#   * l’espace de nommage de l’instance est vide
#

# %% cell_style="split"
class MaClasse:
    pass


# %% cell_style="split"
x = MaClasse()

# l'espace de nommage de x est vide
x.__dict__

# %%
# créer un attribut dans l'instance revient
# à ajouter une clé dans l'espace de nommage de l'instance
x.value = 18
x.__dict__


# %% [markdown] slideshow={"slide_type": "slide"}
# ### attributs `__dict__`, `__class__`, `__bases__`

# %% [markdown]
# * valide pour **classes et instances** :
#   * l’attribut `__dict__` est un dictionnaire
#   * qui matérialise les attributs propres à cet objet
# * valide pour **instances seulement** :
#   * l’attribut `__class__`
#   * référence la classe qui a construit l’instance
# * valide pour **classes seulement** :
#   * l’attribut `__bases__` est un tuple
#   * qui contient les super-classes de la classe

# %% cell_style="split" slideshow={"slide_type": "slide"}
class SuperClasse:
    pass
class Classe(SuperClasse):
    pass
o = Classe()
o.__dict__

# %% cell_style="split"
o.value = 12
o.__dict__

# %% cell_style="split"
o.__class__

# %%
Classe.__bases__

# %%
o.__class__.__bases__


# %% [markdown] slideshow={"slide_type": "slide"}
# ## un exemple de classe

# %%
class MaClasse:                # définit la classe MaClasse
    def __init__(self, value): # definit une méthode
        self.value = value     # self est l’instance
    def display(self):
        return(3 * self.value) # self.value: par instance


# %%
x = MaClasse(10)               # on crée 2 instances
y = MaClasse(1000)             # chaque instance a son
                               # propre espace de nommage

# %% cell_style="split"
# MaClasse.display(x)
x.display()

# %% cell_style="split"
# MaClasse.display(y)
y.display()

# %% cell_style="split"
x.__dict__

# %% cell_style="split"
y.__dict__

# %% slideshow={"slide_type": "slide"}
x.value = "bob"      # on peut directement changer les
                     # attributs sans passer par les
                     # méthodes de la classe
x.display()

# %%
x.autre = 15         # on peut également définir de
                     # nouveaux attributs pour
                     # l’instance directement
x.__dict__

# %% cell_style="split"
# pour rappel
x.__class__

# %% cell_style="split"
# uniquement object
# comme super-classe
MaClasse.__bases__


# %% [markdown] slideshow={"slide_type": "slide"}
# ### un exemple d’héritage de classes

# %% cell_style="split"
class MaClasse:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return f"[MC:{self.value}]"
    def square(self):
        return self.value ** 2

# avec __repr__ on a modifié
# la façon de montrer un objet
top = MaClasse(10)
top


# %% cell_style="split"
# voici comment on hérite
class MaSousClasse(MaClasse):
    # ici je redéfinis une méthode
    def __repr__(self):
        return f"[custom: {self.value*2}]"

# et pour tout le reste, on peut manipuler
# un objet MaSousClasse exactement
# comme un objet MaClasse


# %% cell_style="center"
# création
bottom = MaSousClasse(100)

# affichage : customisé par la redéfinition
bottom

# %% cell_style="split"
# on accède à son attribut
# (toujours dans l'instance)
bottom.value

# %% cell_style="split"
# pas besoin de redéfinir: héritée
bottom.square()

# %% [markdown] slideshow={"slide_type": "slide"}
# #### un exemple d’héritage de classes

# %% [markdown] cell_style="split"
# **espace de nommage dans cet exemple**
#
# * `bottom.__repr__` est dans `MaSousClasse`
# * `bottom.square` est dans `MaClasse`
# * `bottom.value` est dans l’instance `bottom`

# %% cell_style="split"
list(MaSousClasse.__dict__.keys())

# %% cell_style="split"
list(bottom.__dict__.keys())

# %% cell_style="split"
list(MaClasse.__dict__.keys())

# %% cell_style="split"
MaSousClasse.__bases__

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `isinstance()` et `issubclass()`

# %% [markdown]
# * `isinstance(x, class1)` retourne `True` si `x` est une instance de `class1` ou d’une super classe
# * `issubclass(class1, class2)` retoune `True` si `class1` est une sous-classe de `class2`
# * ces fonctions *builtin* sont à privilégier à l'utilisation de `type()`

# %% cell_style="split" slideshow={"slide_type": ""}
isinstance(top, MaClasse)

# %% cell_style="split"
isinstance(top, MaSousClasse)

# %% cell_style="split"
isinstance(bottom, MaSousClasse)

# %% cell_style="split"
isinstance(bottom, MaClasse)

# %%
type(bottom) is MaClasse

# %% cell_style="split"
issubclass(MaSousClasse, MaClasse)

# %% cell_style="split"
isinstance(MaSousClasse, MaClasse)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### les classes sont des attributs de modules

# %% [markdown] cell_style="center"
# * on peut avoir une ou plusieurs classes dans un module
# * on ne peut importer qu'un module
# * la classe est un attribut du module (comme n’importe quel attribut)
# * en général
#   * modules en `minuscule`
#   * classe en `ChasseMixte`
# * assez souvent, l'un est dérivé de l'autre

# %% cell_style="split"
# exemple issu de
# la librairie standard
import argparse
argparse.ArgumentParser

# %% cell_style="split"
# un module très utile pour
# l'introspection
import inspect
inspect.ismodule(argparse)

# %% cell_style="split"
inspect.isclass(argparse.ArgumentParser)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### les classes sont des attributs de modules

# %% [markdown]
# les mécanismes d'importation s'appliquent normalement

# %% cell_style="split"
# première forme
import argparse

class MyParser(argparse.ArgumentParser):
    # redéfinissons 'parse'
    def parse(self):
        pass


# %% cell_style="split"
# ou de manière équivalente
from argparse import ArgumentParser

class MyParser(ArgumentParser):
    # redéfinissons 'parse'
    def parse(self):
        pass


# %% [markdown] slideshow={"slide_type": "slide"}
# ### les classes sont des objets mutables

# %% [markdown]
# * créons une classe vide

# %%
class Dummy:
    pass # classe vide, espace de nommage vide


# %%
list(Dummy.__dict__)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### les classes sont des objets mutables

# %% cell_style="split"
# créons deux instances
x = Dummy()
y = Dummy()

# %% cell_style="split"

# on peut ajouter dynamiquement
# un attribut à une classe
Dummy.name = 'Bob'

# %% cell_style="split"
# dès lors on trouve cet attribut
# même en partant de la classe
Dummy.name

# %% cell_style="split"
# et donc a fortiori en partant d'une instance
x.name, y.name

# %% [markdown]
# * `name` est créé après les instances  
#   mais les instances trouvent `name` dans la classe
#
# * la résolution de nom a lieu *à runtime*  
#   le long de l’arbre d’héritage

# %% slideshow={"slide_type": "slide"}
list(x.__dict__)     # l’espace de nommage de x est vide

# %%
x.name = 'Sue'       # on assigne name à x maintenant

Dummy.name, x.name, y.name

# %%
# en résumé, voici les espaces de nommage de `Dummy`, `x`, `y`,
list(Dummy.__dict__)

# %% cell_style="split"
list(x.__dict__)

# %% cell_style="split"
list(y.__dict__)


# %% [markdown] slideshow={"slide_type": "slide"}
# #### les classes sont des objets mutables

# %% [markdown]
# * comme une méthode est un objet, on peut créer et assigner une méthode à une classe après la création de la classe
# * comme la résolution de nom est **faite à chaque appel**, chaque instance verra la nouvelle méthode

# %% cell_style="split"
# on *peut* ajouter des méthodes
# en dehors d'une instruction 'class:'

# on passe self comme pour une méthode
# définie dans une 'class:'
def upperName(self):
    return self.name.upper()

Dummy.upperName = upperName

# %% cell_style="split"
x.upperName()

# %% cell_style="split"
y.upperName()

# %% [markdown] slideshow={"slide_type": "slide"}
# #### les classes sont des objets mutables

# %% [markdown] slideshow={"slide_type": ""}
# pas de différence avec les méthodes usuelles

# %% cell_style="split"
x.upperName()

# %% cell_style="split"
# qui est donc équivalent à
Dummy.upperName(x)

# %% cell_style="split"
# est-ce valable ?
try:
    print(Dummy.upperName())
except Exception as exc:
    print(f"OOPS {exc}")

# %% cell_style="split"
# est-ce valable ?
try:
    print(Dummy.upperName(Dummy))
except Exception as exc:
    print(f"OOPS {exc}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### seules les classes built-in sont immutables

# %% [markdown]
# * l’impact d’une modification d’une classe built-in  
#   serait trop important et pourrait même  
#   casser le fonctionnement de l’interpréteur

# %%
try:
    int.__pow__ = False
except Exception as e:
    import traceback; traceback.print_exc()

# %% [markdown] slideshow={"slide_type": "slide"}
# #### seules les classes built-in sont immutables

# %% [markdown]
# * le `__dict__` d’un built-in est en lecture seule

# %%
try:
    int.__dict__["__pow__"] = False
except Exception as e:
    import traceback; traceback.print_exc()


# %% [markdown] slideshow={"slide_type": "slide"}
# #### seules les classes built-in sont immutables

# %% [markdown]
# * un `mappingproxy` est un objet qui joue le rôle de proxy  
#   pour un `dict` de manière à le rendre en lecture seule
#
# * les classes sont des objets mutables, mais  
#   elles utilisent comme dictionnaire  
#   pour l’espace de nommage un `mappingproxy`  
#   de manière à protéger l’espace de nommage

# %% [markdown] slideshow={"slide_type": "slide"}
# #### seules les classes built-in sont immutables

# %%
class C:
    pass

# en ajoutant un attribut on modifie le __dict__
C.test = 10
list(C.__dict__)

# %%
# mais on ne peut pas modifier le __dict__ directement
try:
    C.__dict__['spam'] = 100
except Exception as e:
    import traceback; traceback.print_exc()


# %% [markdown] slideshow={"slide_type": "slide"}
# ## recherche dans l’arbre d’héritage

# %% [markdown]
# * MRO : method resolution order
# * l’algorithme est le suivant
#   * liste toutes les super-classes en utilisant  
#     un algorithme DFLR (depth first, left to right)
#
#   * si classe dupliquée,  
#     **ne garder que la dernière** occurrence
#
# * chaque classe possède
#   * un attribut `__mro__` (tuple)
#   * et la fonction `mro()` (liste)

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ![MRO](media/mro.png)

# %% cell_style="split"
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass


# %% [markdown]
# * parcours DFLR: `D`, `B`, `A`, `object`, `C`, `A`, `object`
# * suppressions : `D`, `B`, ~~`A`~~, ~~`object`~~, `C`, `A`, `object`

# %% cell_style="split"
D.__mro__

# %% cell_style="split"
C.mro()

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### *Method Resolution Order*

# %% [markdown] tags=["level_intermediate"]
# * l'héritage entre les classes
# * détermine l'ordre dans lequel sont cherchés les attributs
# * en sus de l'instance elle-même
# * en anglais *method resolution order*
# * ou `mro()` (une méthode de la classe)
# * surtout utile avec l'héritage multiple

# %% tags=["level_intermediate"]
C.mro()


# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# #### attributs non fonctionnels (≠ méthode)

# %% [markdown] tags=["level_intermediate"]
# * on peut utiliser les même concepts
# * pour gérer des attributs de donnée (i.e. ≠ méthode)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### pour aller plus loin

# %% [markdown]
# * https://www.python.org/download/releases/2.3/mro/
# * Python utilise l’algorithme C3 qui est légèrement plus compliqué que ce que j’ai expliqué (la différence n’apparaitra que dans des cas très particuliers)
# * https://en.wikipedia.org/wiki/C3_linearization

# %% [markdown] slideshow={"slide_type": "slide"}
# ## appel méthode de super-classe

# %% [markdown]
# * nécessaire lorsque la spécialisation  
#   consiste à ajouter ou modifier  
#   par rapport à la méthode héritée
#
# * le cas typique est d'ailleurs le constructeur  
#   dès qu'on ajoute un attribut de donnée

# %% cell_style="split" slideshow={"slide_type": "slide"}
# sans super()

class C:
    def __init__(self, x):
        print("init x par superclasse")
        self.x = x

class D(C):

    # comme D hérite de C
    # il faut initialiser C correctement
    def __init__(self, x, y):
        # par exemple
        C.__init__(self, x)
        print("init y par classe")
        self.y = y



# %% cell_style="split"
c = C(10)

# %% cell_style="split"
d = D(100, 200)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### deux écoles

# %% [markdown]
# * on peut être **explicite**  
#   dans notre cas la classe `D` sait exactement  
#   (statiquement) qu'elle hérite de `C`  
#   `D.__init__()` appelle `C.__init__()` explicitement
#
# * il est cependant des cas  
#   où on n'a pas forcément cette information
#
# * selon que les super-classes sont  
#   dans la même librairie  
#   ou dans une librairie tierce - qui peut changer

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `super()`

# %% [markdown]
# * la méthode `super()` permet d'adresser ce problème
# * et d’appeler une méthode dans *une* super classe
# * sans avoir à spécifier laquelle
# * c'est l'héritage qui joue

# %% cell_style="split" slideshow={"slide_type": "slide"}
# la même chose que tout à l'heure
# mais avec super()

class C:
    def __init__(self, x):
        print("init x par superclasse")
        self.x = x

class D(C):

    def __init__(self, x, y):
        # c'est qd meme plus simple !
        super().__init__(x)
        print("init y par classe")
        self.y = y



# %% cell_style="split"
c = C(10)

# %% cell_style="split"
d = D(100, 200)


# %% cell_style="split" slideshow={"slide_type": "slide"}
# super() est souvent rencontrée
# dans __init__ mais s'applique
# partout
class C:
    def f(self):
        print('spam')


# %% cell_style="split" slideshow={"slide_type": ""}
class D(C):
    def f(self):
        # remarquez l'absence
        # de self !
        super().f()
        print('beans')


# %% cell_style="split"
c = C(); c.f()

# %% cell_style="split"
d = D(); d.f()


# %% [markdown] slideshow={"slide_type": "slide"}
# ### `super()` a ses limites

# %% [markdown]
# * ça semble très pratique, mais potentiellement dangereux  
#   puisque la résolution est implicite et non explicite
#
# * `super()` suit l’ordre donné par la MRO et risque donc d’appeler une méthode d’une classe sœur
# * `super()` renvoie un objet sur lequel envoyer la méthode  
#   du coup pas besoin de référence à `self` (erreur fréquente au début)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `super()`

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# * `super()` présente l'intérêt marginal de ne pas avoir à répéter la super-classe
#
# * sinon `super()` n’est utile que dans des cas très spécifiques
#   * on change à l’exécution l’arbre d’héritage (donc on ne peut pas spécifier en dur la super classe)
#   * on a des méthodes de même nom dans des super classes (héritage multiple) dans un schéma en losange

# %% cell_style="split" slideshow={"slide_type": ""}
class A:
    def f(self):
        print('A')
class B:
    def f(self):
        print('B')


# %% cell_style="split"
# comme A apparait en premier
# c'est A.f() qui est appelé
# par super().f()

class C(A, B):
    def f(self):
        super().f()
        print('C')


# %% cell_style="split"
c = C()
c.f()


# %% [markdown] cell_style="center"
# * `super()` n’appelle **que la première** méthode  
#   trouvée sur le chemin de la MRO,  
#   et **non les deux** comme on pourrait le croire ou le vouloir

# %% cell_style="split" slideshow={"slide_type": "slide"}
class A:
    def f(self):
        print('A')

class B:
    def f(self):
        print('B')


# %% cell_style="split" slideshow={"slide_type": ""}
# si on les échange
# on change aussi le sens
# de super().f()
class C(B, A):
    def f(self):
        super().f()
        print('C')


# %%
C().f()

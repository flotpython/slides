# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: "m\xE9thodes statiques"
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

# %%
from plan import plan; plan("avancés", "méthodes statiques")


# %% [markdown] slideshow={"slide_type": "slide"}
# # méthodes statiques et de classe

# %% [markdown] slideshow={"slide_type": "slide"}
# ## à quoi ça sert

# %% [markdown]
# * les méthodes statiques et de classe
#   * peuvent travailler sur les arguments d’une classe
#   * sans avoir besoin d’une instance
# * par exemple, pour compter le nombre d’instances d’une classe
# * ou pour fournir des utilitaires qui créent des instances

# %% [markdown] slideshow={"slide_type": "slide"}
# ## méthodes *unbound* et *bound*

# %% [markdown]
# * une méthode *unbound* est une méthode appelée sur la classe
#   * l’instance n’est pas automatiquement passée comme premier argument
#   * c’est un objet fonction classique qui n’a pas besoin d’avoir une instance comme premier argument

# %%
class C:
    def f(self):
        print("demo", self)
C.f

# %% [markdown] slideshow={"slide_type": "slide"}
# ### méthodes *unbound* 

# %%
C.f(1)   # on peut passer n’importe quel objet

# %%
i = C()
C.f(i)   # on peut évidemment passer une instance


# %% [markdown] slideshow={"slide_type": "slide"}
# ### méthodes et *bound*

# %% [markdown]
# * une méthode *bound* est une méthode appelée sur l’instance
#   * l’instance est automatiquement passée comme premier argument de la méthode
#   * c’est un objet *bound method*

# %%
class C:
     def f(self):
         print(self)
i = C()

# un objet 'bound method'
# équivalent si on veut à une currification
# de C.f où on a déja le premier argument self=i
i.f


# %% [markdown] slideshow={"slide_type": "slide"}
# ## comment appeler une méthode sans instance ?
# (bound ou unbound)

# %% [markdown]
# * une méthode appelée sur une instance est *bound*, elle prend automatiquement comme premier argument l’instance (`self`)
# * par contre, une méthode appelée sur une classe est une fonction classique
# * comment appeler une méthode qui travaille sur les arguments de la classe indifféremment d’une classe ou d’une instance
#   * par exemple pour compter le nombre d’instances

# %% [markdown] slideshow={"slide_type": "slide"}
# ### cas 1 : méthode sans argument

# %% cell_style="split"
class C:
    
    numInstances = 0

    def __init__(self):
        C.numInstances += 1
        
    # méthode qui ne prend
    # pas self en argument
    def printNumInstances(): 
        print("Nombre d'instances : {}"
              .format((C.numInstances)))


# %% cell_style="split"
# je peux envoyer la méthode
# à la classe elle-même
C.printNumInstances() 

# %% cell_style="split"
# mais pas sur une instance
i = C()

try:     
    i.printNumInstances()
except TypeError as e:
    print("OOPS", e)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### cas 2 : méthode avec `self` comme argument

# %% cell_style="split"
class C:

    numInstances = 0                         

    def __init__(self):
        C.numInstances += 1

    # méthode habituelle avec self
    def printNumInstances(self): 
        print("Nombre d'instances : {}"
              .format((C.numInstances)))


# %% cell_style="split" slideshow={"slide_type": ""}
# cette fois-ci c'est l'inverse, 
# je peux envoyer 
# la méthode à une instance
i = C()
i.printNumInstances() 

# %% cell_style="split" slideshow={"slide_type": ""}
# mais pas sur la classe
try:
    C.printNumInstances()
except TypeError as e:
    print("OOPS", e)    


# %% [markdown] slideshow={"slide_type": "slide"}
# ### en résumé

# %% [markdown]
# * on ne peut pas appeler uniformément la même méthode depuis la classe et l’instance 
#   * soit on peut l’appeler de l’instance, mais pas de la classe
#   * soit on peut l’appeler de la classe, mais pas de l’instance

# %% [markdown] slideshow={"slide_type": "slide"}
# ## utiliser une fonction

# %% [markdown]
# * la solution naïve à ce problème
#   * sortir la méthode de la classe
#   * en faire en quelque sorte une "une méthode de module"
#   * mais ça n'est vraiment pas très élégant
#   * notamment ça casse l'encapsulation

# %% [markdown] slideshow={"slide_type": "slide"}
# ### méthode de module

# %%
def printNumInstances(): # méthode de module
    print("Nombre d'instances : {} "
          .format((C.numInstances)))

class C:
    numInstances = 0
    def __init__(self):
        C.numInstances = C.numInstances + 1


# %%
printNumInstances()

# %%
a = C()
printNumInstances()


# %% [markdown] slideshow={"slide_type": "slide"}
# ### problème avec les méthodes de module

# %% [markdown]
# * le code travaillant sur la classe n’est pas lié à la classe
#   * maintenance difficile
#   * lecture du code difficile
# * pas de possibilité de customisation par héritage

# %% [markdown] slideshow={"slide_type": "slide"}
# ## méthodes statiques et de classe

# %% [markdown]
# * pour appeler une méthode sans instance (d’une classe ou d’une instance), il y a deux possibilités
# * les méthodes statiques ne prennent pas l’instance en premier argument
#   * indépendante de l’instance
#   * créées avec `staticmethod`
# * les méthodes de classe prennent comme premier argument une classe (et non une instance)
#   * indépendante de l’instance
#   * créées avec `classmethod`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### méthodes statiques

# %% cell_style="split"
class C:

    numInstances = 0                         

    def __init__(self):
        C.numInstances += 1

    def printNumInstances():
        print(f"Nombre d'instances : {C.numInstances}")
    
    # en pratique ici on utilise
    # un décorateur; mais on n'en
    # a pas encore parlé ...
    printNumInstances = staticmethod(
        printNumInstances)


# %% cell_style="split"
# sur la classe
C.printNumInstances()

# %% cell_style="split"
# ou sur l'instance
i = C()
i.printNumInstances()

# %% cell_style="split"
C().printNumInstances()


# %% [markdown] slideshow={"slide_type": "slide"}
# ### digression : décorateur

# %% [markdown]
# pour anticiper un peu, en pratique on remplace
#
# ```python
# def printNumInstances():
#     # blabla
#
# printNumInstances = staticmethod(printNumInstances)
# ```
#
# par plus simplement
#
# ```python
# @staticmethod
# def printNumInstances():
#     # blabla
# ```
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### méthodes statiques et surcharge

# %% [markdown]
# * une méthode statique surchargée dans une sous classe doit être redéfinie comme statique dans la sous classe

# %%
class SousC(C):
    
    # on redéfinit la méthode dans la sous-classe
    def printNumInstances():
        print("depuis sousC")
        C.printNumInstances()

    # il faudrait refaire la déclaration magique
    # comme staticmethod, car voici ce qui se passe 
    # si on ne le fait pas
    #printNumInstances = staticmethod(
    #    printNumInstances)


# %% [markdown] slideshow={"slide_type": "slide"}
# #### méthodes statiques et surcharge

# %%
# avec une sous-classe qui ne redéclare pas 
# sa méthode comme staticmethod
# on se retrouve avec le problème initial
i = SousC()

# %% cell_style="split"
# et du coup on ne peut pas
# appeler la méthode sur une instance
try:     
    i.printNumInstances()
except TypeError as e:
    print("OOPS", e)

# %% cell_style="split"
# ça marche avec les classes par contre
SousC.printNumInstances()

# %% cell_style="split"
C.printNumInstances()


# %% [markdown] slideshow={"slide_type": "slide"}
# #### méthodes statiques et surcharge

# %% cell_style="split"
# si au contraire je redéclare la méthode 
# de la sous-classe comme statique
# en utilisant cette fois-ci un décorateur

class SousC(C):

    @staticmethod
    def printNumInstances():
        print("depuis SousC")
        C.printNumInstances()



# %% cell_style="split"
# maintenant ça marche 
# avec instances et classes
i = SousC()            
i.printNumInstances()  

# %% cell_style="split"
SousC.printNumInstances()


# %% [markdown] slideshow={"slide_type": "slide"}
# #### méthodes statiques et surcharge

# %% cell_style="split"
# une autre sous-classe de C 
# qui ne redéfinit pas la méthode
class AutreSousC(C):
    pass


# %% cell_style="split"
AutreSousC.printNumInstances()

# %% cell_style="split"
j = AutreSousC()
j.printNumInstances()


# %% [markdown]
# * `AutreSousC()` appelle automatiquement le constructeur de la classe `C`, ce qui incrémente le compteur d’instances

# %% [markdown] slideshow={"slide_type": "slide"}
# ### méthodes de classe

# %% cell_style="split"
# imaginons maintenant qu'on veuille toujours
# compter les instances mais classe par classe
class C:

    numInstances = 0                         

    def __init__(self):
        C.numInstances += 1

    @classmethod
    def printNumInstances(cls):
        print(f"nb. instances de {cls.__name__}="
              f"{cls.numInstances}")


# %% cell_style="split"
c = C()

# sur l'instance
c.printNumInstances()

# %% cell_style="split"
# sur la classe
C.printNumInstances()


# %% [markdown] slideshow={"slide_type": "slide"}
# ### premier paramètre `cls`

# %% [markdown]
# * avec une méthode de classe, le premier paramètre 
#   * correspond à **la classe de** l'objet sujet de la méthode
#   * et non **pas à une instance**, comme d'habitude
#   * du coup la convention est de l'appeler `cls` et non pas `self`

# %% cell_style="split"
class SousC(C):
    pass


# %% cell_style="split"
# on crée un objet C et un SousC
# -> 2 instances de plus comptabilisées
c, sousC = C(), SousC()
C.printNumInstances()

# %% cell_style="split"
SousC.printNumInstances()

# %% cell_style="split"
sousC.printNumInstances()


# %% [markdown] slideshow={"slide_type": "slide"}
# ## ex: nombre d’instances par sous classe

# %% cell_style="split"
class C:
    
    numInstances= 0

    def __init__(self):
        self.count()

    @classmethod
    def count(cls):
        print(f'incrementing {cls.__name__}')
        cls.numInstances += 1

    @classmethod
    def printNumInstances(cls):
        print(f"nb. instances de {cls.__name__}="
              f"{cls.numInstances}")

        
class SousC(C):
    numInstances= 0



# %% cell_style="split" slideshow={"slide_type": "fragment"}
c = C()

# %% cell_style="split"
sous1, sous2 = SousC(), SousC()

# %% cell_style="split"
c.printNumInstances()
sous1.printNumInstances()
sous2.printNumInstances()

# %% [markdown] slideshow={"slide_type": "slide"}
# ## quand utiliser `staticmethod` ?

# %% [markdown]
# * la méthode statique est adaptée 
#   * lorsque l’on n'a pas d'instance sous la main
#   * e.g. une usine à objets
# * comme une fonction de module
#   * mais dans l'espace de nom de la classe

# %% [markdown] slideshow={"slide_type": "slide"}
# ## quand utiliser  `classmethod` ?

# %% [markdown]
# * la méthode de classe (puisqu’elle reçoit la classe lors de l’appel) est adaptée si 
#   * on a un comportement spécifique en fonction de la sous classe
#   * on veut travailler sur des attributs de la classe, mais on ne veut pas coder en dur son nom
# * voir [cet exemple intéressant sur SO](http://stackoverflow.com/questions/12179271/python-classmethod-and-staticmethod-for-beginner) d’utilisation de `staticmethod` et `classmethod`

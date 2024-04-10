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
#     title: "attributs revisit\xE9s"
#   rise:
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": ""}
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown] slideshow={"slide_type": ""}
# # attr.. (2/3) - descripteurs
#
# accès aux attributs - second notebook
#
# pour résumer les chapitres précédents, on a vu jusqu'ici:
# - la mécanique "usuelle"
# - les properties
# - l'*attrape-tout* avec `__getattr__`
#
# à présent on va voir encore un autre mécanisme, qui s'appelle les **descriptors**  
# en fait, il s'agit d'un mécanisme de très bas niveau, et il se trouve que c'est grâce à ce mécanisme que l'on peut proposer les *properties*  
#
# ````{admonition} avertissement: très avancé !
# on s'est efforcé d'aborder jusqu'ici des notions qui ont une application dans la vie quotidienne d'un développeur  
# à partir de maintenant par contre, on entre de plain-pied dans les tréfonds du langage, et il est vraiment rare qu'on ait besoin de modifier le langage au point de devoir descendre aussi profond dans les soutes...  
# on s'adresse donc à partir d'ici à un public curieux et très avancé; *you will have been warned* ;-)
# ````

# %% [markdown] slideshow={"slide_type": ""}
# ## pourquoi c'est intéressant ?
#
# la recherche des attributs est **totalement centrale** dans le langage  
# on va le voir, lorsqu'on écrit un code aussi banal que `person = Person("jean")`, il y a déjà plusieurs recherches d'attributs qui entrent en jeu !
#
# de plus pour que le modèle fonctionne, on a dû implémenter deux mécanismes séparés pour les instances et les classes, qui sont voisines mais subtilement différentes; si on veut maitriser à fond le langage, on doit en passer par l'étude de ces mécanismes
#
# mais bon à nouveau, si on s'en tient à une utilisation usuelle du langage, tout ceci est complètement optionnel !

# %% [markdown] slideshow={"slide_type": "slide"}
# ## descripteurs
#
# un descripteur est une classe qui détermine le comportement lors de l’accès, l’affectation et l’effacement d’un attribut
#
# une classe avec **au moins une des méthodes** suivantes est un descripteur
# * `__get__()`
# * `__set__()`
# * `__delete__()`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### caractéristique troublante
#
# la caractéristique assez troublante des descripteurs est la suivante:  
# si pendant la recherche "habituelle"
# * on trouve un attribut
# * **et que celui-ci est une instance de descripteur**
# * **alors on l'évalue** (on l'appelle)
# pour obtenir la valeur finale de l'attribut ou pour écrire/détruire selon le contexte
#
# ça nous rappelle un peu les propriétés (et de fait les propriétés sont implémentées à base de descripteurs)

# %% [markdown]
# ## exemple: un attribut d'instance

# %%
# a helper tool to turn verbosity on or off
VERBOSE = True

def verbose(*args, **kwds):
    VERBOSE and print(*args, **kwds)


# %% slideshow={"slide_type": "slide"}
# ici on implémente un attribut usuel (d'instance)
# il faut être attentif à bien ranger la donnée dans l'instance
# et pas dans le descripteur !!!

# une classe de descripteur pour implémenter l'attribut 'name'
class InstanceAttributeDescriptor:
 
    def __init__(self):
        # ici self est l'instance du descripteur
        # cet espace va être partagé par toutes les instances de la classe
        # ce n'est **pas une bonne idée** d'y ranger
        # le nom des personnes
        pass
 
    def __get__(self, instance, owner):
        # self: l'instance du descripteur (de type Descriptor donc)
        # instance: l'instance de type Person
        # owner: ici ça va être None (pourrait recevoir 
        #        la classe Person dans d'autres use cases)

        # du coup bien faire attention à écrire dans `instance` et pas dans `self` !
        oldname = instance._name
        verbose(f"getter returning {oldname=}\n  -- {self=} {instance=}")
        return oldname
 
    def __set__(self, instance, newname):
        # attention à ne pas utiliser instance.name
        # car on cacherait le descripteur !
        verbose(f"setting: {newname}\n  -- {self=} {instance=}")
        instance._name = newname
 
    def __delete__(self, instance):
        verbose(f"deleting: {instance._name}\n  -- {instance=}")
        del instance._name


class Person:
    # on range une instance de Descriptor dans Person.__dict__['name']
    name = InstanceAttributeDescriptor()


# %%
# avec ce code, c'est comme si on avait ajouté 
# un attribut 'name' à toutes les instances de Person

p1, p2 = Person(), Person()
p1.name = "John"
p2.name = "Doe"

p1.name, p2.name


# %% [markdown]
# ````{admonition} exercice
#
# notre descriptor est spécialisé pour l'attribut `name`, transformez-le pour qu'il puisse servir à n'importe quel attribut
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ## stockage des attributs
#
# le protocole nous expose à la fois les deux instances:
#
# - le descripteur 
# - l'instance sujet de la recherche d'attribut
#
# et comme il y a une instance de descripteur par attribut de la classe,
# on peut choisir de ranger les données
#
# - au niveau de l'instance - comme on vient de le faire;
# - où au niveau de la classe si on écrit dans le descripteur
#
# voyons cette deuxième alternative, pour implémenter un attribut de classe

# %% [markdown]
# ## exemple: un attribut de classe
#
# et ceci avec un tout petit changement:

# %% slideshow={"slide_type": "slide"}
# ici on implémente un attribut de classe
# pour ça on va ranger la valeur .. dans le descripteur (l'instance du)

# c-a-d dans self plutot que dans instance

class ClassAttributeDescriptor:

    # la solution de l'exercice: ranger le nom de l'attribut dans le descripteur
    def __init__(self, attribute):
        self.attribute = attribute
 
    def __get__(self, instance, owner):
        # pas besoin de s'embeter à prendre un nom compliqué
        # il n'y a pas de risque de conflit de nom cette fois
        # le _ c'est juste par sécurité mais ça n'a pas d'importance ici
        return self._value
 
    def __set__(self, instance, newvalue):
        self._value = newvalue
 
    def __delete__(self, instance):
        del self.value


class Person:
    # l'attribut 'normal' 
    name = InstanceAttributeDescriptor()
    # ici du coup toutes les instances partagent l'attribut
    shared = ClassAttributeDescriptor("shared")


# %%
VERBOSE = False

p1, p2 = Person(), Person()

# chacun son nom
p1.name, p2.name = "john", "doe"

# la première affectation est écrasée par la seconde
p1.shared, p2.shared = "useless", "because overwritten"

# la preuve
print("========== name:", p1.name, "<->", p2.name)
print("========== shared:", p1.shared, "<->", p2.shared)


# %% [markdown]
# ````{admonition} read-only
#
# on a vu que pour rendre une propriété *read-only*, il suffisait de ne pas fournir de *setter*  
# ici c'est un peu différent, pour obtenir ce comportement il **faut définir `__set__`** en lui faisant lever `AttributeError`
# ```python
#     def __set__(self, instance, name):
#         raise AttributeError('read-only')
# ```
#
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ## attention aux noms
#
# comme avec les propriétés, il faut soigneusement **éviter** d'utiliser **le même nom** pour le descripteur et pour ranger la donnée dans l'instance (dans le descripteur on s'en moque)
#
# la tradition est d'utiliser
#
# - `name` pour le descripteur
# - `_name` pour la donnée

# %% [markdown] slideshow={"slide_type": ""}
# ## *data descriptors*
#
# maintenant, il se trouve que la logique complète de recherche des attributs, qui est implémentée dans `__getattribute__` et qu'on verra pour conclure dans le 3ème et dernier notebook de cette série, va avoir besoin de traiter un peu différemment les attributs de donnée et les attributs de fonction
#
# pour cette raison, on a choisi à ce stade la définition suivante:
#
# ````{admonition} data descriptor
# un descripteur qui implémente `__set__` ou `__delete__` est considéré comme un ***data descriptor***
#
# les autres sont donc .. des ***non-data descriptors***
# ````
#
# **un *data descriptor* est prioritaire** sur un attribut présent dans `__dict__`  
# ce qui n'est pas le cas pour les fonctions

# %% [markdown]
# ````{admonition} xxx à finir
#
# trouver un exemple un peu parlant
# ````

# %% slideshow={"slide_type": "slide"} tags=[]
class DataDescriptor:

    def __get__(self, instance, owner):
        value = instance._name
        print(f"getting: {value}")
        return value
 
    # en fournissant __set__
    # on devient un *data* descriptor
    def __set__(self, instance, name):
        value = name.title()
        print(f"setting: {value}")
        instance._name = value

class PersonData:
    def __init__(self):
        self._name = None
    name = DataDescriptor()


# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
pd = PersonData()
pd.name

# %% tags=["gridwidth-1-2"]
pd.name = 'john'
pd.name


# %% slideshow={"slide_type": "slide"} tags=[]
class DescriptorNonData:

    # sans __set__ on parle 
    # de *non-data* descriptor
    def __get__(self, instance, owner):
        value = instance._name
        print("Getting: {}".format(value))
        return value
 
class PersonNonData:
    def __init__(self):
        self._name = 'John Doe'
    name = DescriptorNonData()


# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
pnd = PersonNonData()
pnd.name = 'bill'
pnd.name

# %% tags=["gridwidth-1-2"]
del pnd.name
pnd.name

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour en savoir plus
#
# * [la doc sur les descriptors](https://docs.python.org/3/howto/descriptor.html) (qui parle aussi des properties)
#

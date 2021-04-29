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
#   nbhosting:
#     title: "attributs revisit\xE9s"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %%
#from plan import plan; plan("avancé", "attribut")


# %% [markdown] slideshow={"slide_type": "slide"}
# # protocole d'accès aux attributs
#
# ## pour quoi faire ?
#
# * ajouter une couche de logique
# * lorsqu'on accède, modifie ou efface un attribut
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple
#
# * supposons que l'on veuille contrôler/intercepter
# * les accès à un ou des attributs

# %% cell_style="split"
class A: 
    pass

a = A()

# %% cell_style="split"
# accès en écriture
a.value = 10

# accès en lecture
print(a.value)

# nettoyage
del a.value


# %% [markdown] slideshow={"slide_type": "slide"}
# ## deux options
#
# * créer des méthodes (getters/setters)
#   * `getvalue()` et `setvalue()`
#   * implique de modifier tout le code
#   * pas satisfaisant
#   
# * modifier la façon
#   * dont python accède aux attributs

# %% [markdown] slideshow={"slide_type": "slide"}
# ## trois mécanismes
#
# * spécifiques à un attribut
#   * propriétés
#   * descripteurs
#
# * pour toute la classe
#   * méthodes `__getattr__`, `__getattribute__`
#   * (et apparentées)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## propriétés

# %%
class Property:
    def __init__(self):
        self._x = None

    def getx(self):       # getter appelé par c.x
        print('get x')
        return self._x

    def setx(self, value):# setter appelé par c.x = value
        print('set x to {}'.format(value))
        self._x = value

    def delx(self):       # deleter appelé par del c.x
        print('deleting x')
        del self._x

    # ici on déclare que x est une propriété de Property
    x = property(getx, setx, delx, "doctring de 'x'.")


# %% slideshow={"slide_type": "slide"}
# question pour voir ceux qui suivent:
# pourquoi on n'appelle pas l'instance property ?

prop = Property()
prop.x = 10

# %% cell_style="split"
print(prop.x)

# %% cell_style="split"
del prop.x


# %% [markdown] slideshow={"slide_type": "slide"}
# ### les propriétés s'héritent
#
# * définies comme méthodes de la classe
# * sont donc héritées par les sous-classes

# %%
class SubProperty(Property): 
    pass

subproperty = SubProperty()
subproperty.x = 30


# %% [markdown] slideshow={"slide_type": "slide"}
# ### la [*builtin* `property`]

# %% [markdown] slideshow={"slide_type": "slide"}
# * attend 4 arguments
#   * getter, setter, deleter, et doc
# * optionnels, lorsqu'un est manquant
#   * l'opération correspondante est interdite
#   
# voir (https://docs.python.org/3.5/library/functions.html#property)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le décorateur `property`
#
# * il existe une syntaxe alternative
# * avec un décorateur `@property` qui décore le getter
# * on doit alors appeler le getter d'après l'attribut (e.g. `value`)
# * on peut ensuite décorer le setter et le deleter
#   * avec `@value.setter` et `@value.deleter`
# * question de goût...  

# %% cell_style="split" slideshow={"slide_type": "slide"}
class DecoratedProperty:
    def __init__(self):
        self._value = None

    @property
    def value(self):            # getter
        print('get value')
        return self._value

    @value.setter
    def value(self, value):     # setter
        print(f"set value to {value}")
        self._value = value

    @value.deleter
    def value(self):            # deleter
        print('del value')
        del self._value


# %% cell_style="split" slideshow={"slide_type": ""}
decorated = DecoratedProperty()
decorated.value = 10


# %% [markdown] slideshow={"slide_type": "slide"}
# ## descripteurs
#
# * un descripteur est une classe qui détermine le comportement
# * lors de l’accès, l’affectation et l’effacement d’un attribut
# * une classe avec au moins une des méthodes
#   * `__get__()`
#   * `__set__()`
#   * `__delete__()`
#   * est un descripteur
#   
# * commençons par voir une version erronée 
#   * mais [qu'on trouve facilement sur internet](http://www.ibm.com/developerworks/library/os-pythondescriptors/))

# %% [markdown] slideshow={"slide_type": "slide"}
# ### caractéristique troublante
#
# la caractéristique assez troublante des descripteurs est la suivante:
#
# * si pendant la recherche "habituelle" on trouve un attribut
# * **et que celui-ci est un descripteur**
# * **alors on l'évalue** (on l'appelle)
# * pour obtenir la valeur finale de l'attribut
# * ou pour écrire/détruire selon le contexte

# %% slideshow={"slide_type": "slide"}
# # ! ATTENTION ! cette version n'est pas conseillée

class DescriptorBroken:
 
    def __init__(self):
        self._name = ''
 
    def __get__(self, instance, owner):
        value = self._name
        print(f"getting: {value}")
        return value
 
    def __set__(self, instance, name):
        value = name.title()
        print(f"setting: {value}")
        self._name = value
 
    def __delete__(self, instance):
        print(f"deleting: {self._name}")
        del self._name
 
class PersonBroken:
    name = DescriptorBroken()


# %% slideshow={"slide_type": "slide"}
user = PersonBroken()
user.name = 'john smith'

# %% cell_style="split"
user.name

# %% cell_style="split"
del user.name

# %% [markdown] slideshow={"slide_type": "slide"}
# ### mécanisme profond
#
# * très puissant, utilisé pour implémenter 
#   * les propriétés
#   * les méthodes statiques et de classe
#   * les méthodes bound et unbound
#   * `super()`
#   * ...
# * protocole de très bas niveau
#   * utiliser de préférence les properties

# %% [markdown] slideshow={"slide_type": "slide"}
# ## stockage des attributs
#
# * il y a une instance de descripteur par attribut de la classe
#   * cette instance de descripteur peut stocker ses propres attributs
#   * comme on vient de le faire
#   * ils seront partagés par toutes les instances
# * un descripteur peut accéder aux attributs des instances
#   * ainsi on peut modifier les attributs dans l'instance
#   
# C'est ce qui ne va pas avec notre premier essai...

# %% cell_style="split" slideshow={"slide_type": "slide"}
# ça ne va pas du tout, si je modifie pb
# ça modifie **aussi** qb
pb = PersonBroken()
qb = PersonBroken()
pb.name = 'John'

# %% cell_style="split"
qb.name


# %% slideshow={"slide_type": "slide"}
# il faut ranger la donnée dans l'instance
# et non pas dans le descriptor

class Descriptor:
 
    def __init__(self):
        # cet espace est partagé par toutes les instances
        # ce n'est **pas** une bonne idée d'y ranger
        # le nom des personnes, qui seront dans
        # person._name
        pass
 
    def __get__(self, instance, owner):
        # c'est ici que le paramètre instance est utile
        value = instance._name
        print(f"getting: {value}")
        return value
 
    def __set__(self, instance, name):
        # attention à ne pas utiliser instance.name
        # car on écraserait le descripteur !
        value = name.title()
        print(f"setting: {value}")
        instance._name = value
 
    def __delete__(self, instance):
        print(f"deleting: {instance._name}")
        del instance._name
 
class Person:
    name = Descriptor()


# %% cell_style="split" slideshow={"slide_type": "slide"}
# maintenant ça va mieux, 
# on peut toucher à p sans modifier q
p = Person()
q = Person()
p.name = 'John'
q.name = 'Bill'
p.name

# %% cell_style="split"
q.name


# %% [markdown] slideshow={"slide_type": "slide"}
# ### où stocker les attributs

# %% [markdown] slideshow={"slide_type": ""}
# * dans le descripteur
#   * si l'information est partagée 
#   * par toutes les instances de la classe
# * dans chaque instance
#   * sinon

# %% [markdown] slideshow={"slide_type": "slide"}
# ### attention aux noms

# %% [markdown] slideshow={"slide_type": ""}
# * que se passe-t-il si l’attribut de l’instance
#  * a le même nom que le descripteur 
#  * i.e. l'attribut de la classe ?
# * le descripteur doit violer la règle de recherche des attributs
#  * sinon il ne sera jamais appelé dans ce cas
#  * puisque l’attribut d’instance est prioritaire sur l’attribut de classe

# %% slideshow={"slide_type": "slide"}
# cette version choisit maladroitement
# d'utiliser instance.name pour stocker
# la vraie valeur du nom, et provoque une récursion

class DescriptorOverride:
 
    def __get__(self, instance, owner):
        # si on choisit d'utiliser instance.name
        # on va rappeler le descripteur !
        value = instance.name
        print(f"getting: {value}")
        return value
 
    def __set__(self, instance, name):
        value = name.title()
        print(f"setting: {value}")
        instance.name = value
 
class PersonOverride:
    name = DescriptorOverride()


# %% slideshow={"slide_type": "slide"}
po = PersonOverride()
qo = PersonOverride()

## je ne fais pas tourner cette version car elle
# provoque un appel récursif infini..
#po.name = 'John'

# %% [markdown] slideshow={"slide_type": "slide"}
# ### attention aux noms

# %% [markdown] slideshow={"slide_type": "slide"}
# * attention donc à utiliser des noms différents
# * entre l'attribut de la classe
#   * qui référence le descripteur
# * et l'attibut de l'instance
#   * qui référence la vraie donnée
# * mais qui ne peuvent pas porter le même nom
# * préfixer avec  un `_` pour ranger la vraie donnée

# %% [markdown] slideshow={"slide_type": "slide"}
# ## descriptors *data* et *non-data*

# %% [markdown] slideshow={"slide_type": ""}
# * un descriptor qui fournit `__get__` et `__set__`
#   * est dit un *data* descriptor
#   * il est **prioritaire** sur un attribut présent
#     dans `__dict__`
#
# * un descriptor qui ne fournit que `__get__`
#   * est dit *non-data*
#   * orienté pour les méthodes
#   * il n'**est pas prioritaire** sur `__dict__`

# %% cell_style="split" slideshow={"slide_type": "slide"}
class DescriptorData:

    def __get__(self, instance, owner):
        value = instance._name
        print(f"getting: {value}")
        return value
 
    # en fournissant __set__
    # on devient un *data* descriptor
    def __set__(self, instance, name):
        value = name.title()
        print("setting: {value}")
        instance._name = value

class PersonData:
    def __init__(self):
        self._name = None
    name = DescriptorData()


# %% cell_style="split" slideshow={"slide_type": ""}
pd = PersonData()
pd.name

# %% cell_style="split"
pd.name

# %% cell_style="split"
pd.name = 'john'
pd.name


# %% cell_style="split" slideshow={"slide_type": "slide"}
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


# %% cell_style="split" slideshow={"slide_type": ""}
pnd = PersonNonData()
pnd.name = 'bill'
pnd.name

# %% cell_style="split"
del pnd.name
pnd.name


# %% [markdown] slideshow={"slide_type": "slide"}
# ### read-only descriptors

# %% [markdown] slideshow={"slide_type": ""}
# * contrairement aux propriétés
# * l'absence de `__set__`
# * ne rend pas l'objet read-only
# * il faut que `__set__`
#   * lève l'exception `AttributeError`

# %% cell_style="split" slideshow={"slide_type": "slide"}
class DescriptorReadOnly:

    def __get__(self, instance, owner):
        value = instance._name
        print("Getting: {}".format(value))
        return value

    def __set__(self, instance, name):
        raise AttributeError('read-only')

class PersonReadOnly:
    def __init__(self):
        self._name = None
    name = DescriptorReadOnly()


# %% cell_style="split" slideshow={"slide_type": ""}
pro = PersonReadOnly()
try:
    pro.name = 'john'
except AttributeError as e:
    print("OOPS", e)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### méthodes `__getattr__` et apparentées

# %% [markdown] slideshow={"slide_type": ""}
# ##### logique des accès en lecture:
#
# * appel à `__getattribute__`
# * qui par défaut (si pas surchargé)
# * fait la propagation "normale"
#   * i.e. chercher dans `__dict__` et remonter  
# * enfin en cas d'échec
#   on appelle `__getattr__`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### accès en lecture

# %% [markdown] slideshow={"slide_type": ""}
# * 1er niveau de customisation *light*
#   * en redéfinissant `__getattr__`
#   * on peut fournir un mécanisme de *fallback*
#
# * 2ème niveau de customisation *deep*
#   * redéfinir `__getattribute__`
#   * qui alors peut choisir
#   * d'appeler ou pas `__getattr__`
#   * et de contourner les descripteurs/properties

# %% [markdown] slideshow={"slide_type": "slide"}
# ### avertissement

# %% [markdown] slideshow={"slide_type": ""}
# * si `__getattr__` est relativement inoffensif
# * par contre redéfinir `__getattribute__` 
# * doit être utilisé avec parcimonie
# * et a vite fait de vous sauter à la figure !

# %% slideshow={"slide_type": "slide"}
class WithGetAttr:

    # seulement pour les attributs
    # non trouvés
    def __getattr__(self, attrname):
        print("getattr with name {}".format(attrname))
        return 10

gwa = WithGetAttr()
gwa.x

# %%
# ce qui n'empêche pas d'avoir aussi des attributs "normaux"
gwa.y = 20
print(gwa.y)


# %% cell_style="split" slideshow={"slide_type": "slide"}
# vous pouvez toujours écrire ce 
# que vous voulez dans __dict__ 
# ou autre, avec ce code
# un attribut d'instance
# renvoie toujours 100

class WithGetAttribute:

    # le point d'entrée pour la recherche
    def __getattribute__(self, attrname):
        return 100

    # comme notre __getattribute__
    # n'implémente pas la recherche
    # des défauts via __getattr__,
    # cette méthode en réalité
    # est inutile ici
    def __getattr__(self, attrname):
        print("ne passera jamais par ici")

    # inutile d'essayer d'implémenter un
    # descriptor ou une property...
    # en exercice ..

wgu = WithGetAttribute()
wgu.foo

# %% cell_style="split"
# pas la peine d'essayer
wgu.bar = 100
wgu.bar

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ##### ça va très loin

# %% cell_style="split"
# même __dict__ !
wgu.__dict__


# %% [markdown] slideshow={"slide_type": "slide"}
# ### subtilité de `__getattribute__`

# %% [markdown]
# * n'est pas utilisée pour la recherche
#   * des méthodes spéciales en `__*__`
#   * exercice : pourquoi ?

# %% [markdown] slideshow={"slide_type": "slide"}
# ### accès en écriture

# %% [markdown] slideshow={"slide_type": ""}
# * quand on écrit `inst.x = blabla`
# * le défaut cette fois est d'écrire dans `self.__dict__['x']`
# * et redéfinissant `__setattr__` on peut choisir une autre stratégie
# * pour faire appel à la stratégie par défaut
#   * `object.__setattr_`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### écriture

# %% [markdown] slideshow={"slide_type": ""}
# * évidemment `__setattr__` ne peut pas faire
#   * `instance.name = blabla`
#   * ni même `setattr(instance, 'name', blabla)`
#   * sous peine de récursion infinie

# %% slideshow={"slide_type": "slide"}
class WithSetAttr:

    def __setattr__(self, attrname, value):
        print("setting {} to {}".format(attrname, value))
        # appeler la façon par défaut
        # de remplir un attribut
        object.__setattr__(self, attrname, value)

wsa = WithSetAttr()
wsa.name = 'john'
wsa.name

# %% [markdown] slideshow={"slide_type": "slide"}
# ## conclusion

# %% [markdown] slideshow={"slide_type": ""}
# ### lecture
#
# * point d'entrée `__getattribute__`
#   * pas utile dans les utilisations courantes
# * descriptors, mais surtout properties
#   * permettent de traiter un attribut à la fois
# * `__getattr__`, agit sur tous les attributs
#   * qui ne sont pas trouvés autrement

# %% [markdown] slideshow={"slide_type": "slide"}
# ### écriture
#
# * point d'entrée unique `__setattr__`
# * la disymétrie est liée au fait
# * que l'écriture est plus simple 
#   * on écrit toujours dans l'objet
#   * et pas dans la classe ou super-classes

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exercice
#
# * `attr-dynamic-properties`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exercice
#
# * `attr-proxy`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour en savoir plus
#
# * [un bon résumé de l'algorithme de résolution des attributs](https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/)
#
# * [la doc sur les descriptors](https://docs.python.org/3.5/howto/descriptor.html) (qui parle aussi des properties)
#   
# * pour les hard-core: [le code c derrière tout ça](https://github.com/python/cpython/blob/3.6/objects/typeobject.c)
#
# * http://sametmax.com/les-descripteurs-en-python/
#
# * [David Beazley: python 3 metaprogramming](http://www.dabeaz.com/py3meta/index.html)

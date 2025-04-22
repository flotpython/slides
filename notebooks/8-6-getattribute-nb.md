---
celltoolbar: Slideshow
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: "attributs revisit\xE9s"
---

+++ {"slideshow": {"slide_type": ""}}

Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

+++ {"slideshow": {"slide_type": ""}}

# attr.. (3/3) - `__getattribute__`

accès aux attributs - troisième et dernier notebook  
*aka putting it all together*:  
où on essaye de réconcilier toutes ces façons d'accéder aux attributs: *properties*, *`__getattr__`*, et autres *descriptors*

+++ {"slideshow": {"slide_type": "slide"}}

## la mécanique générale: 

- pour les accès en écriture, peu de changement par rapport à ce qu'on a vu jusqu'ici:
  **on écrit toujours directement dans l'objet**
- pour les accès en lecture:
  la logique des accès - on dirait en termes savants le *protocole d'accès aux attributs** - est codée dans la *dunder* `__getattribute__`

+++

````{admonition} to review thoroughly
xxx 
````

+++

## accès en écriture: `__setattr__`

par rapport à la version simpliste qu'on a vue dans les premiers chapitres, il y a peu de différence concernant les accès en écriture  
**on écrit toujours directement dans l'objet** 

il existe toutefois un *hook*: on invoque si elle existe la *dunder* `__setattr__`



+++ {"slideshow": {"slide_type": "slide"}}

## accès en lecture: `__getattribute__`

+++ {"slideshow": {"slide_type": ""}}

* 1er niveau de customisation *light*
  * en redéfinissant `__getattr__`
  * on peut fournir un mécanisme de *fallback*

* 2ème niveau de customisation *deep*
  * redéfinir `__getattribute__`
  * qui alors peut choisir
  * d'appeler ou pas `__getattr__`
  * et de contourner les descripteurs/properties

+++ {"slideshow": {"slide_type": "slide"}}

### avertissement

+++ {"slideshow": {"slide_type": ""}}

* si `__getattr__` est relativement inoffensif
* par contre redéfinir `__getattribute__` 
* doit être utilisé avec parcimonie
* et a vite fait de vous sauter à la figure !

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
class WithGetAttr:

    # seulement pour les attributs
    # non trouvés
    def __getattr__(self, attrname):
        print("getattr with name {}".format(attrname))
        return 10

gwa = WithGetAttr()
gwa.x
```

```{code-cell} ipython3
# ce qui n'empêche pas d'avoir aussi des attributs "normaux"
gwa.y = 20
print(gwa.y)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
tags: [gridwidth-1-2]
---
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
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pas la peine d'essayer
wgu.bar = 100
wgu.bar
```

+++ {"slideshow": {"slide_type": ""}, "tags": ["gridwidth-1-2"]}

##### ça va très loin

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# même __dict__ !
wgu.__dict__
```

+++ {"slideshow": {"slide_type": "slide"}}

### subtilité de `__getattribute__`

+++

* n'est pas utilisée pour la recherche
  * des méthodes spéciales en `__*__`
  * exercice : pourquoi ?

+++ {"slideshow": {"slide_type": "slide"}}

### accès en écriture

+++ {"slideshow": {"slide_type": ""}}

* quand on écrit `inst.x = blabla`
* le défaut cette fois est d'écrire dans `self.__dict__['x']`
* et redéfinissant `__setattr__` on peut choisir une autre stratégie
* pour faire appel à la stratégie par défaut
  * `object.__setattr_`

+++ {"slideshow": {"slide_type": "slide"}}

### écriture

+++ {"slideshow": {"slide_type": ""}}

* évidemment `__setattr__` ne peut pas faire
  * `instance.name = blabla`
  * ni même `setattr(instance, 'name', blabla)`
  * sous peine de récursion infinie

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
class WithSetAttr:

    def __setattr__(self, attrname, value):
        print("setting {} to {}".format(attrname, value))
        # appeler la façon par défaut
        # de remplir un attribut
        object.__setattr__(self, attrname, value)

wsa = WithSetAttr()
wsa.name = 'john'
wsa.name
```

+++ {"slideshow": {"slide_type": "slide"}}

## conclusion

+++ {"slideshow": {"slide_type": ""}}

### lecture

* point d'entrée `__getattribute__`
  * pas utile dans les utilisations courantes
* descriptors, mais surtout properties
  * permettent de traiter un attribut à la fois
* `__getattr__`, agit sur tous les attributs
  * qui ne sont pas trouvés autrement

+++ {"slideshow": {"slide_type": "slide"}}

### écriture

* point d'entrée unique `__setattr__`
* la disymétrie est liée au fait
* que l'écriture est plus simple 
  * on écrit toujours dans l'objet
  * et pas dans la classe ou super-classes

+++ {"slideshow": {"slide_type": "slide"}}

## exercice

* `attr-dynamic-properties`

+++ {"slideshow": {"slide_type": "slide"}}

## exercice

* `attr-proxy`

+++ {"slideshow": {"slide_type": "slide"}}

## pour en savoir plus

* [un bon résumé de l'algorithme de résolution des attributs](https://blog.ionelmc.ro/2015/02/09/understanding-python-metaclasses/)

* [la doc sur les descriptors](https://docs.python.org/3/howto/descriptor.html) (qui parle aussi des properties)

* pour les hard-core: [le code c derrière tout ça](https://github.com/python/cpython/blob/3.6/objects/typeobject.c)

* http://sametmax.com/les-descripteurs-en-python/

* [David Beazley: python 3 metaprogramming](http://www.dabeaz.com/py3meta/index.html)

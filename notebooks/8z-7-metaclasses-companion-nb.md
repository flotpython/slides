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
  title: "m\xE9taclasses (incomplet)"
---

+++ {"slideshow": {"slide_type": ""}}

# avertissement

+++

ce notebook ne contient que des exemples, le corps de la présentation est pour l'instant resté [au format PowerPoint](15-metaclasses.pptx)

+++ {"slideshow": {"slide_type": "slide"}}

# Exemple 1

```{code-cell} ipython3
class MaMetaClasse(type):
    def __new__(meta, name, bases, classdict):
        print("Avant la creation de l'objet classe", name)
        print("metaclasse :", meta)
        print("bases :", bases)
        print("dict :", classdict)
        return type.__new__(meta, name, bases, classdict)

    def __init__(classe, name, bases, classdict):
        type.__init__(classe, name, bases, classdict)
        print("Apres la creation de la classe", name)
        print("classe :", classe)
        print("bases :", bases)
        print("dict :", classdict)

class C(metaclass=MaMetaClasse):
    x = 1
```

+++ {"slideshow": {"slide_type": "slide"}}

# Exemple 2

```{code-cell} ipython3
class UpperAttrMetaclass(type):
    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        # on met les noms des attributs non spéciaux
        # en minuscule (aussi)
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.lower()] = val
            uppercase_attr[name] = val
        # on spécifie une super-classe
        # on aurait pu aussi l'ajouter...
        bases = (BaseOfAll,)
        return type.__new__(cls, clsname, bases, uppercase_attr)

class BaseOfAll:
    def common_func(self):
        return "in common_func"

class C(metaclass=UpperAttrMetaclass):
    def funC_bAd_CAP(self):
        pass
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
c = C()
# une instance a la méthode common_func
# parce qu'on a fait hériter C de BaseOfAll
'common_func' in dir(c)
```

```{code-cell} ipython3
# elle a aussi la méthode 'func_bad_cap'
'func_bad_cap' in dir(c)
```

```{code-cell} ipython3
# qu'on retrouve dans la classe
print(C.__dict__.keys())
```

```{code-cell} ipython3
# et la super classe de C est bien BaseOfAll
# heureusement pour nous BaseOfAll hérite de object
print(C.__bases__)
```

```{code-cell} ipython3
print(c.common_func())
```

+++ {"slideshow": {"slide_type": "slide"}}

# Exemple 3

```{code-cell} ipython3
class meta(type):
    def __new__(meta, name, bases, classdict):
        return type.__new__(meta, name, bases, classdict)

class A(metaclass=meta):
    pass

class B(A):
    pass

print(type(A))
print(type(A()))
```

```{code-cell} ipython3
print(type(B))
print(type(B()))
```

```{code-cell} ipython3
# et bien sûr
type(meta)
```

+++ {"slideshow": {"slide_type": "slide"}}

# Exemple 4

```{code-cell} ipython3
class meta(type):
    x = y = z = "meta"
    def __new__(meta, name, bases, classdict):
        return type.__new__(meta, name, bases, classdict)

class A(metaclass=meta):
    x = y = "A"
    pass

class B(A):
    x = "B"
    pass

b = B()

# sur la classe
print("B.x: {}\nB.y: {}\nB.z: {}\n".format(B.x, B.y, B.z))
```

```{code-cell} ipython3
# sur l'instance: x et y trouvés 
print("B().x: {}\nB().y: {}".format(B().x, B().y))
```

```{code-cell} ipython3
# mais pas z qui n'est que dans la métaclasse
try: 
    print("B().z: {}\n".format(B().z)) # AttributeError
except AttributeError as e:
    print("OOPS", e)
```

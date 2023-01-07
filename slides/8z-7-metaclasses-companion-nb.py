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
#     title: "m\xE9taclasses (incomplet)"
#   rise:
#     autolaunch: true
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
# # avertissement

# %% [markdown]
# ce notebook ne contient que des exemples, le corps de la présentation est pour l'instant resté [au format PowerPoint](15-metaclasses.pptx)

# %% [markdown] slideshow={"slide_type": "slide"}
# # Exemple 1

# %%
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


# %% [markdown] slideshow={"slide_type": "slide"}
# # Exemple 2

# %%
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


# %% slideshow={"slide_type": "slide"}
c = C()
# une instance a la méthode common_func
# parce qu'on a fait hériter C de BaseOfAll
'common_func' in dir(c)

# %%
# elle a aussi la méthode 'func_bad_cap'
'func_bad_cap' in dir(c)

# %%
# qu'on retrouve dans la classe
print(C.__dict__.keys())

# %%
# et la super classe de C est bien BaseOfAll
# heureusement pour nous BaseOfAll hérite de object
print(C.__bases__)

# %%
print(c.common_func())


# %% [markdown] slideshow={"slide_type": "slide"}
# # Exemple 3

# %%
class meta(type):
    def __new__(meta, name, bases, classdict):
        return type.__new__(meta, name, bases, classdict)

class A(metaclass=meta):
    pass

class B(A):
    pass

print(type(A))
print(type(A()))

# %%
print(type(B))
print(type(B()))

# %%
# et bien sûr
type(meta)


# %% [markdown] slideshow={"slide_type": "slide"}
# # Exemple 4

# %%
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

# %%
# sur l'instance: x et y trouvés 
print("B().x: {}\nB().y: {}".format(B().x, B().y))

# %%
# mais pas z qui n'est que dans la métaclasse
try: 
    print("B().z: {}\n".format(B().z)) # AttributeError
except AttributeError as e:
    print("OOPS", e)

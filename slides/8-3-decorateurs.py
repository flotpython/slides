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
#     title: "d\xE9corateurs"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": ""}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% [markdown] slideshow={"slide_type": ""}
# # les décorateurs
#

# %% [markdown]
# *avertissement* : version beta

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemples

# %% [markdown]
# les deux constructions que nous avonc déjà rencontré
#
# * `staticmethod`
# * `classmethod`
#
# sont des décorateurs

# %% cell_style="split" slideshow={"slide_type": "slide"}
# plutôt que d'écrire ceci

class C:

    @classmethod
    def f(c):
        pass

    @staticmethod
    def g():
        pass



# %% cell_style="split"
# on aurait aussi bien pu écrire ceci
# mais en moins lisible

class C:

    def f(c):
        pass

    def g():
        pass

    f = classmethod(f)
    g = staticmethod(g)


# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# Le fragment
#
# ```
# @decorateur
# def f():
#     pass
# ```

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# est en fait équivalent à
#
# ```
# def f():
#     pass
# f = decorateur(f)
# ```

# %% [markdown]
# autrement dit, `f` n'est plus la fonction initiale, mais l'objet retourné par `decorateur(f)`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## c'est quoi un décorateur ?

# %% [markdown]
# c'est un *callable* qui prend en argument un *callable* et retourne un *callable*

# %% [markdown] slideshow={"slide_type": "slide"}
# ## c'est quoi un *callable* ?

# %% [markdown]
# * le terme fait référence à un des nombreux protocoles
#   * comme itérable qui veut dire 'peut être dans un for`
# * ici un *callable* c'est, littéralement, un objet qu'on peut appeler
#   * par exemple une fonction (bien entendu)
#   * mais aussi une instance d'une classe qui implémente `__call__`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### une classe de *callables*

# %%
# une classe dont les instances sont des callables
class Additioneur:

    # on crée une instance en lui passant la valeur à additionner
    def __init__(self, delta):
        self.delta = delta

    # ce qu'il faut faire à l'appel
    def __call__(self, entree):
        return entree + self.delta


# %% slideshow={"slide_type": "slide"}
# ceci crée un callable
ajouter4 = Additioneur(4)
# qu'on peut donc utiliser comme une fonction
# en l'occurrence une fonction qui ajoute 4
ajouter4(10)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## à quoi sert un décorateur ?

# %% [markdown]
# à ajouter une couche de logique à une fonction avec une syntaxe explicite `@decorateur`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## comment implémenter un décorateur

# %% [markdown]
# * un décorateur est donc un *callable* (qui instrumente un *callable*)
# * on peut donc choisir d'implémenter le décorateur comme
#   * une fonction
#   * une classe (avec le protocole `__call__`)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple de décorateur - comme une classe

# %% [markdown]
# * pour qu'une fonction sache compter combien de fois elle est appelée
# * le décorateur lui-même implémenté comme une classe

# %%
class NumberCalls:

    # on aura une instance de NumberCalls
    # pour chaque fonction décorée
    # ceci est appelé à la déclaration de f
    def __init__(self, f):
        self.calls = 0
        self.f = f

    # et ce code est exécuté lors des appels à f
    def __call__(self, *args):
        self.calls += 1
        s = f'{self.f.__name__} : {self.calls} calls'
        print(s)
        return self.f(*args)


# %% slideshow={"slide_type": "slide"}
# maintenant je peux définir une fonction décorée
@NumberCalls
def f(a, b):
    print(f"dans l'appel à f({a}, {b})")


# %% cell_style="split"
f(1, 2)

# %% cell_style="split"
f(3, 4)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### l'exemple décortiqué

# %% [markdown] cell_style="split"
# la **déclaration** de `f`
# ```python
# @NumberCalls
# def f(a, b):
#     print(blabla)
# ```

# %% [markdown] cell_style="split"
# * devient
#   * `f = NumberCalls(f)`
# * qui déclenche
#   * le **constructeur** de `NumberCalls`
#   * avec `f` non décoré comme arg
#   

# %% [markdown] cell_style="split"
# * `f` décoré est une instance de `NumberCalls`
# * qui est callable via `__call__`
# * un **appel** à `f` décoré
# ```
# f(1, 2)
# ```

# %% [markdown] cell_style="split"
# * provoque maintenant 
#   * un appel à **`__call__`** sur `f`
#   * et avec arguments `(1, 2)`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple - suite

# %% [markdown]
# * ce décorateur - implémenté comme une classe
# * fonctionne bien sur des fonctions
# * mais ça se passe moins bien avec des méthodes de classe

# %% cell_style="split"
class C:
    @NumberCalls
    def ma_methode(self, x):
        self.x = x


# %% cell_style="split"
c = C()
try:
    c.ma_methode(10)
except TypeError as e:
    print("OOPS", e)


# %% [markdown] slideshow={"slide_type": "slide"}
# * lors de l'appel à `c.ma_methode(10)`
# * on appelle la méthode `__call__` sur l'instance de `NumberCalls`
# * mais elle reçoit comme premier argument l'instance de `NumberCalls` (et non pas l'instance de `C`)
# * et comme arguments dans `*args` uniquement l'entier `10`
# * du coup `ma_methode` est appelée avec un seul argument `10` par `self.f(*args)`
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple de décorateur - comme une fonction

# %% [markdown]
# * même fonctionnalité 
# * mais cette fois implémenté comme une fonction

# %%
def NumberCalls2(f):

    ### le code exécuté à l'appel de f
    def wrapper(*args, **dargs):
        # on range le nombre d'appels directement
        # dans un attribut 'called' de l'objet fonction
        wrapper.calls += 1
        print(f'calling function {f.__name__}, '
              f'called {wrapper.calls} times')
        return f(*args, **dargs)

    ### le code exécuté à la déclaration de f
    # il faut initialiser cet attribut
    wrapper.calls = 0
    return wrapper


# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple de décorateur - comme une fonction

# %%
class D:
    @NumberCalls2
    def ma_methode(self, x):
        self.x = x


# %%
d = D()
d.ma_methode(10)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemples de décorateurs

# %%
from functools import wraps

def runtime(func):
    """
    Décorateur qui affiche le temps d'exécution d'une fonction
    """
    import time
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print(func.__name__, time.perf_counter()-t)
        return res
    return wrapper



# %% slideshow={"slide_type": "slide"}
def counter(func):
    """
    Décorateur qui affiche le nombre d'appels à une fonction 
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{} was called {} times".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper



# %% slideshow={"slide_type": "slide"}
def logfunc(func):
    """
    Décorateur qui log l'activité d'une fonction.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        s = """
The function *{}* was called with
    positional arguments: {}
    named arguments: {}
The returned value: {}
"""
        print(s.format(func.__name__, args, kwargs, res))
        return res
    return wrapper



# %% slideshow={"slide_type": "slide"}
@logfunc
@counter
@runtime
def test(num, L):
    for i in range(num):
        'x' in L
    return 'Done'

test(100000, range(10))



# %% [markdown] slideshow={"slide_type": "slide"}
# ## les métadonnées de la fonction décorée

# %%
def mon_decorateur(func):
    def wrapper(*args, **kargs):
        print('avant func')
        func(*args, **kargs)
        print('apres func')
    return wrapper

@mon_decorateur
def ma_fonction(a, b):
    'une fonction qui ne fait presque rien'
    print('dans ma Fonction')
    print(a, b)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### les métadonnées de fonction : `__doc__` et `__name__`

# %%
ma_fonction(1, 2)

# %%
print(ma_fonction.__doc__)

# %%
print(ma_fonction.__name__)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### garder les métadonnées

# %% [markdown]
# * pour préserver les métadonnées 
#   * principalement les attributes `__doc__` et `__name_`
#   * on .. décore le wrapper avec `functools.wraps`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `functools.wraps`

# %%
from functools import wraps

def mon_decorateur(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        print('avant func')
        func(*args, **kargs)
        print('apres func')
    return wrapper

@mon_decorateur
def ma_fonction(a, b):
    'une fonction qui ne fait presque rien'
    print('dans ma Fonction')
    print(a, b)


# %% [markdown] slideshow={"slide_type": "slide"}
# #### garder les métadonnées de la fonction décorée

# %% cell_style="split"
print(ma_fonction.__doc__)

# %% cell_style="split"
ma_fonction.__name__

# %% cell_style="split"
ma_fonction(1, 2)

# %% cell_style="split"
help(ma_fonction)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## cascader les décorateurs

# %%
@runtime
@counter 
def f():
    pass


# %%
# Est équivalent à 
f = runtime(counter(f))


# %% [markdown] slideshow={"slide_type": "slide"}
# ### passer des arguments au décorateur

# %% [markdown]
# * on peut passer des argument au **décorateur**
#   * ajouter une couche de logique
# * en général, on utilise une fonction au dessus du décorateur 
#   * dont le seul rôle est de permettre  
#     au décorateur (fonction ou classe)
#
#   * de garder un accès aux arguments par une clôture

# %% cell_style="split" slideshow={"slide_type": "slide"}
def nb_appel(label=''):
    class NumberCalls:
        def __init__(self, f):
            self.calls = 0
            self.f = f
        def __call__(self, *args):
            self.calls += 1
            s = (f'{label} {self.f.__name__} '
                 f': {self.calls} calls')
            print(s)
            return self.f(*args)
    return NumberCalls


# %% cell_style="split" slideshow={"slide_type": ""}
@nb_appel("-->")
def f(a, b):
    print(a, b)

f(1, 2)


# %% cell_style="split" slideshow={"slide_type": "slide"}
def caller_builder(label=''):
    def caller(f):
        def wrapper(*args, **dargs):
            wrapper.calls += 1
            print(f'{label} {f.__name__}, '
                  f'called {wrapper.calls} times')
            return f(*args, **dargs)
        wrapper.calls = 0
        return wrapper
    return caller


# %% cell_style="split" slideshow={"slide_type": ""}
class C:
    @caller_builder('method')
    def ma_methode(self, x):
        self.x = x

@caller_builder('function')
def ma_fonction():
    pass


# %% cell_style="center"
C().ma_methode(1)

# %% cell_style="split"
C().ma_methode(1)

# %% cell_style="split"
ma_fonction()

# %% slideshow={"slide_type": "slide"}
ma_fonction()

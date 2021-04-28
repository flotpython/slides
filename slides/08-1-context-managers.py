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
#     title: context managers
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %%
from plan import plan; plan("avancé", "context")


# %% [markdown] slideshow={"slide_type": "slide"}
# # `with as` et *context manager*

# %% [markdown]
# ```
# with expression [as variable]:
# 	with-block
# ```
#
# * redondant fonctionnellement à la clause `try` .. `finally`
# * évalue l'expression
# * applique sur le résutat le protocole de *context manager*
#   * similaire dans le principe au protocole d’itération
#   * permet d’avoir du code compact au détriment de la lisibilité

# %% [markdown] slideshow={"slide_type": "slide"}
# ## où on trouve des context managers

# %% [markdown]
# * un objet fichier est un *context manager*
# * le fichier OS est fermé automatiquement à la fin du `with`
# ```
# with open("../data/une-charogne.txt") as mon_fichier:
#     for l in mon_fichier:
#         print(l)
# ```
#
# * équivalent à
# ```
# mon_fichier = open("../data/une-charogne.txt")
# try:
#     for l in mon_fichier:
#         print(line)
# finally:
#     mon_fichier.close()
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## protocole *context manager* (1)

# %% [markdown]
# * l’objet résultat de l'expression doit avoir deux méthodes `__enter__` et `__exit__`
# * à l’entrée du contexte, `__enter__(self)` est exécuté;
# * le retour de `__enter__` est assigné à la variable mentionnée dans le `.. as var`
# * le code *with-block* est executé

# %% [markdown] slideshow={"slide_type": "slide"}
# ### protocole *context manager* (2)

# %% [markdown]
# * s’il n’y a pas d’exception
#   * `__exit__(self, none, none, none)` est appelée, toujours sur le c.m.
# * s’il y a une exception
#   * `__exit__(self, exc_type, exc_value, exc_traceback)` est appelé
#   * `exc_type`, `exc_value`, `exc_traceback` sont les type, valeur et *traceback* de l’exception
# * le retour de `__exit__` est utilisé:  
#   si `False` ➔ l’exception est relancée  
#   si `True` ➔ l’exception est supprimée (étouffée)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple avec relance d’exception

# %%
# les instances de C peuvent être utilisées
# dans un `with` 
class C():
    
    def __enter__(self):
        print("dans enter()")
        return self

    def __exit__(self, *args):
        print(f"__exit__: args={args}")
        return False   # relance l'exception

    def div(self, a, b):
        print(a/b)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple avec relance d’exception

# %%
import traceback

try:
    with C() as c:
        c.div(1, 0)
except:
    traceback.print_exc()


# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple sans relance d’exception

# %%
class C():

    def __enter__(self):
        print("dans enter()")
        return self

    def __exit__(self, *args):
        print(f"__exit__: args={args}")
        return True  # étouffe l'exception

    def div(self, a, b):
        print(a/b)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemple sans relance d’exception

# %%
with C() as c:
    c.div(1, 0)
print("life goes on")    

# %% [markdown] slideshow={"slide_type": "slide"}
# ## utilisation originale

# %% [markdown]
# * on peut utiliser un *context manager* pour exécuter du code avant et après une opération
#   * par exemple, pour mesurer le temps d’exécution, même en cas d’exception
#   * c’est proche d’un décorateur

# %% [markdown] slideshow={"slide_type": "slide"}
# ### utilisation originale

# %%
import time

class Timer():    

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        print(f"durée d'exécution = {self.end - self.start:2f}")
        return False


# %% [markdown] slideshow={"slide_type": "slide"}
# #### utilisation originale

# %%
try:
    with Timer() as t:
        [x ** 3 for x in range(1000000)]
        print(1/0)
except:
    traceback.print_exc()

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pour aller plus loin

# %% [markdown]
# * http://sametmax.com/gestion-des-erreurs-en-python/

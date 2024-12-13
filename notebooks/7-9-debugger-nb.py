# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
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
#     title: instructions
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown] slideshow={"slide_type": "slide"}
# ## le debugger Python : `pdb`

# %% [markdown] slideshow={"slide_type": ""}
# ### `breakpoint()`

# %% [markdown]
# pour mettre un point d'arrêt dans un programme on peut utiliser `breakpoint()`

# %% tags=["gridwidth-1-2"]
def fact(n):
    if n<=1:
        breakpoint()
        return 1
    else:
        return n * fact(n-1)


# %% [markdown] tags=["gridwidth-1-2"]
# **raccourcis**
#
# | clavier | quoi |
# |------|---------|
# | l (lowercase L)  | list source |
# | w  | show stack | 
# | n | next statement (stay in same function)|
# | s | step into (dive into function call) |
# | c | continue |
# | p | print |
#

# %% slideshow={"slide_type": "slide"}
# si on exécute, le programme s'arrête 
# et on peut ensuite exécuter pas à pas, 
# inspecter la pile et les variables, ...
# fact(3)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `pdb.run()`

# %% [markdown]
# * le module pdb permet de debugger facilement un programme Python
# ```python
# import pdb 
# import mymodule 
# pdb.run('mymodule.test()') 
# ```
#
# * lance le debugger depuis la console sur la fonction `test()`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `pdb.pm()` - post-mortem

# %% [markdown]
# ```python
# import pdb 
# import mymodule 
# mymodule.test() 
# Traceback (most recent call last): 
# 	File "<stdin>", line 1, in ? 
# 	File "./mymodule.py", line 4, in test 
# 		test2() 
# 	…
# pdb.pm()
# ```
#
# * lance le debugger en post-mortem

# %% [markdown] slideshow={"slide_type": "slide"}
# ### sous IPython
#
# dans `ipython` (ou dans un notebook), vous pouvez utiliser la *magic* `%%debug`  
#
# ````{admonition} magic de cellule
# :class: tip
#
# rappelez-vous que avec **un seul `%`** on a affaire à une *magic* de **ligne**  
# et avec **deux pourcents `%%`** c'est une magique **de cellule** 
#
# donc nous ici on utilise presque toujours le double pourcent
# ````

# %%
def fact(n):
    print(f"in fact with {n=}")
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)


# %%
# %%debug
fact(3)

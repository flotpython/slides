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
#     title: instructions
#   rise:
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
# # leftovers

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## arguments en ligne de commande

# %% [markdown]
# * un programme Python se lance typiquement depuis le terminal
# * on a typiquement besoin de lui passer des paramètres :
#   * nom du fichier d'entrée
#   * options diverses..
# * car sinon :
#   * le programme fait toujours exactement la même chose !
#   * soit il faut le modifier à chaque lancement
# * exemple d'école :
#   * un programme qui calcule la factorielle d'un nombre
#   
# on veut pouvoir faire
# ```console
# python factorielle.py 56
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `sys.argv`
#
# * méthode la plus basique: `sys.argv`

# %% cell_style="center"
# un code source

# %cat samples/command_line_args1.py

# %% cell_style="center"
#  quand on le lance

# !python samples/command_line_args1.py --les arguments du shell

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le module `argparse`

# %% [markdown]
# * parseur de `sys.argv`
#   * module `argparse` : la solution préconisée

# %% [markdown] slideshow={"slide_type": "slide"}
# #### exemple avec `argparse`

# %%
# !cat samples/command_line_args2.py

# %% [markdown] slideshow={"slide_type": "slide"}
# #### `argparse` - suite

# %%
# sans argument, ça coince
# !python samples/command_line_args2.py

# %%
# si on l'utilise correctement
# !python samples/command_line_args2.py fic1

# %%
# ou comme ça
# !python samples/command_line_args2.py -v fic1 fic2

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le debugger Python : `pdb`

# %% [markdown] slideshow={"slide_type": ""}
# ### `breakpoint()`

# %% [markdown]
# depuis la version 3.7, pour mettre un point d'arrêt dans un programme on peut utiliser `breakpoint()`

# %% cell_style="split"
def fact(n):
    if n<=1:
        breakpoint()
        return 1
    else:
        return n * fact(n-1)


# %% [markdown] cell_style="split"
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
# ### *old-school* breakpoints

# %% [markdown]
# * pour mettre un *breakpoint* dans votre code
#   * `import pdb; pdb.set_trace()`
# * rappel: à partir de python-3.7:
#   * `breakpoint()` 
#  
# ---
#
# * documentation de pdb:
#   * https://docs.python.org/3/library/pdb.html
#   
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### sous IPython

# %%
def foo():
    y = x


# %%
# %%debug
foo()

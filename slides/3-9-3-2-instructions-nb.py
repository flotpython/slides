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
# # instructions

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

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exécuter du code

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `exec()` et `eval()`

# %% [markdown]
# * comment exécuter du code dans une chaîne de caractères ?
# * `exec()` est une fonction qui permet l’exécution dynamique de code python
#   * retourne toujours None
# * `eval()` est une fonction qui évalue une **expression** (mais **pas** une instruction)
#   * et retourne le résultat de cette évaluation
# * le code est bien sûr passé dans un `str`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `exec()` pour une instruction

# %% cell_style="split"
# instructions
i1 = """def fact(n):
    return 1 if n <= 1 else n * fact(n-1)"""
i2 = """if fact(2) > 1:
    print('OUI')"""

# %% cell_style="split"
# on peut les exécuter
# ceci ne fait rien que de définir une fonction
print(exec(i1))

# %% cell_style="center"
fact

# %% cell_style="split"
# qu'on peut maintenant utiliser au travers de i2
# l'impression ici est faire dans le code de i2
# et puis None est le retour de exec
print(exec(i2))

# %% cell_style="split"
# par contre exec() ne renvoie rien d'utile
print(exec("fact(3)"))

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `exec()` *vs* `eval()`

# %%
# expressions
e1 = '(2+3)/2.0'
e2 = "{'alice' : 35, 'bob' : 8}"

# %%
# on peut aussi les exécuter (une expression est une instruction)
# mais le retour est None ce qui perd de son intérêt
print(exec(e1))

# %% cell_style="split"
# c'est mieux de les évaluer
print(eval(e1))

# %% cell_style="split"
print(eval(e2)['alice'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `eval()` pour une expression

# %%
# par contre on ne peut pas évaluer une instruction
try:
    res = eval(i1)      # i1 est une instruction
except Exception as e:
    print("Exception {} - {}".format(type(e), e))
    import traceback
    traceback.print_exc()

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *use with care*

# %% [markdown]
# * je recommande de n'utiliser ces deux fonctions
# * que de manière spartiate
# * souvent pas réllement utile
# * **gros trou de sécurité**

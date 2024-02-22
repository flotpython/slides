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
# ---

# %% [markdown] cell_style="center"
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown]
# # structures de controle

# %% [markdown] cell_style="split"
# ## l'instruction `if`
#
# L'instruction conditionnelle en Python:
#
# ```
# if <test1>:
#     <statement1>
# elif <test2>:
#     <statement2>
# ...
# else:
#     <statement4>
# ```
#
# repose sur une évaluation dite ***paresseuse***, c'est-à-dire que l'instruction s'arrête **au premier test qui est vrai** (on n'évalue pas les tests suivants)  

# %% cell_style="split"
def appreciation(note):
    if note >= 16:
        return "félicitations"
    elif note >= 14:
        return "compliments"
    elif note >= 12:
        return "encouragements"
    elif note >= 10:
        return "passable"
    else:
        return "insuffisant" 


# %% cell_style="split"
print(appreciation(15.5))

# %% cell_style="split"
print(appreciation(11.5))

# %% [markdown]
# ````{admonition} il y a aussi un match
# :class: seealso admonition-small
#
# bien que beaucoup plus tardive, il y a également une instruction `match` en Python, on en parle plus bas
# ````

# %% [markdown]
# ````{admonition} rappel: test non booléen ?
# :class: tip admonition-small
#
# l'expression qui détermine le test **peut ne pas renvoyer un booléen** - c'est très souvent le cas en pratique  
# dans ce cas-là on appelle la fonction `bool()` pour le transformer en booléen et ainsi savoir si on doit considérer le test comme vrai ou pas; c'est ainsi que si on doit tester si une liste est vide:
#   ```python
#   # on écrira plutôt
#   if L:
#      print("pas vide")
#
#   # que, c'est jsute aussi, mais vilain
#   if len(L) > 0:
#      print("pas vide")
#   ```   
# ````
#

# %% [markdown]
# ## `if` (l'expression) 
#
# il existe aussi une **expression**  permettant de faire quelque chose comme *if .. then .. else ..*  
# la syntaxe générale est 
#
#   ```
#   <exp_1> if <test> else <exp_2>
#   ```
#
# ````{admonition} opérateur ternaire
# :class: admonition-x-small
#
# cette forme se rapproche de l'opérateur dit *ternaire* en C ou JavaScript  
# `<test> ? <exp_1> : <exp_2>`
# ````

# %%
note = 8

# comme c'est une expression, je peux par exemple
# la passer à une fonction
print("insuffisant" if note < 10 else "ouf !")

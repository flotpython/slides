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
# # instructions
#
# principalement les structures de contrôle, et quelques-unes plus anecdotiques  
# nous laissons intentionnellement de coté le `for` pour le moment, ainsi que le `try..except`

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
# dans ce cas-là on appelle la fonction `bool()` pour le transformer en booléen; c'est ainsi que si on doit tester si une liste est vide:
#   ```python
#   # on écrira plutôt
#   if L:
#      print("pas vide")
#
#   # que, c'est juste aussi, mais vilain
#   if len(L) > 0:
#      print("pas vide")
#   ```   
# ````
#

# %% [markdown]
# ### `if` (l'expression) 
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

# et comme c'est une expression, je peux par exemple
# la passer à une fonction

print("insuffisant" if note < 10 else "ouf !")

# %% [markdown]
# ## boucle `while`
#
# ```python
# while <test>:
#     bloc d_instructions
#     alignés comme on l_a vu
# else:
#     bloc     # exécuté à la sortie de la boucle 
#     aligné   # seulement s’il n’y a pas de break
# ```
#
# ````{admonition} while ou for
# :class: note admonition-small
#
# les boucles en Python sont plus volontiers construites avec un `for`;   
# les itérations avec `for` sont tellement importantes en Python qu'on les traite à part
# ````

# %% [markdown]
# ## `break`, `continue`
#
# deux instructions particulières:
#
# * `continue`: abandonner ce tour de boucle, passer au suivant
# * `break`: sortir complètement de la boucle courante

# %% cell_style="split"
# exemple avec continue
# on veut zapper les nombres pairs

L = [1, 5, 2, 7, 9]

while L:
    n = L.pop()
    if n % 2 == 0:
        continue
    # ... faire des trucs compliqués avec n
    print(f"{n=}", end=" ")

# %% cell_style="split"
# exemple avec break
# dès qu'on trouve un nombre pair on s'arrête

L = [1, 5, 2, 7, 9]

while L:
    n = L.pop()
    if n % 2 == 0:
        break
    # ... faire des trucs compliqués avec n
    print(f"{n=}", end=" ")


# %% [markdown]
# ## `return`
#
# `return` sert tout simplement à indiquer la fin d'une fonction, et ce qu'elle doit renvoyer  
# lorsque le programme atteint cette instruction, la fonction courante s'arrête immédiatement
#
# ````{admonition} enfin presque
# :class: admonition-small
#
# il y a des instructions, notamment `try` et `with`, qui peuvent entrainer un peu de nettoyage avant qu'on sorte vraiment de la fonction
# ````

# %% [markdown] cell_style="split"
# ## `pass`
#
# l'instruction `pass` ne fait rien; elle est en général utilisée lorsque la syntaxe demande une instruction, mais qu’on ne l’a pas encore implémentée
#
#   ```python
#   def ma_fonction():
#       pass
#
#   class Foo:
#       pass
#   ```

# %% [markdown]
# ## libération de variables: `del`
#
# * `del a` 
#   * instruction qui libère la variable `a` (en la supprimant de l’espace de nommage)
#   * et décrémente le compteur de références de l’objet vers lequel pointe `a`
# * `del` fonctionne aussi sur
#   * un slicing de séquence: `del L[i:j:k]`
#   * un dictionnaire: `del D[clef]`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## affichage

# %% [markdown] slideshow={"slide_type": "slide"}
# ### la fonction `print()`

# %% [markdown]
# ```
# print(obj1, .., objn, sep=' ', end='\n',
#       file=sys.stdout, flush=False)
# ```
#
# * affiche les objets *obj*  convertis en chaînes de caractères
# * séparés par `sep` (un espace par défaut)
# * dans le fichier `file` (`sys.stdout` par défaut)  
# * la ligne se termine par `end` (un retour chariot par défaut)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### enlever le *newline*

# %% [markdown]
# * suppression du retour à la ligne automatique

# %%
for i in range(10):
    print(i, end='')

# %% [markdown] slideshow={"slide_type": "slide"}
# #### redirection dans un fichier

# %% [markdown]
# * pour que `print()` écrive sur le disque dur

# %% cell_style="split"
with open('test.txt', 'w') as channel:
    L = list(range(10))
    for item in L:
        print(item, file=channel, end=' + ')
    print("\n", file=channel)

# %% cell_style="split"
# !cat test.txt

# %% [markdown] slideshow={"slide_type": "slide"}
# #### plusieurs paramètres

# %% cell_style="split"
print(1, 'x', True)

# %% cell_style="split"
print(1, 'x', True, sep='_')

# %%
# dans un notebook ce n'est pas très parlant
# mais ici on n'obtiendrait PAS de retour à la ligne
print(1, 'x', True, sep='_', end='FIN')

# %%
# et ici on en obtiendrait deux (soit une ligne blanche)
print(1, 'x', True, sep='_', end='\n\n')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### module logging

# %% [markdown]
# * pour le logging plus évolué qu’un simple print redirigé dans un fichier, on peut utiliser le module de la librairie standard logging
# * documentation du module
#   * https://docs.python.org/3/library/logging.html
# * tutorial
#   * https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
#
# c'est **la bonne façon** de conserver des  
# traces d'exécutionpour un programme en production

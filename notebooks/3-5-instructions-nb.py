# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted,-editable
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -rise, -version
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

# %% [markdown] tags=["gridwidth-1-2"]
# ## l'instruction `if`
#
# L'instruction conditionnelle en Python:
#
# ```python
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

# %% tags=["gridwidth-1-2"]
# par exemple

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


# %% tags=["gridwidth-1-2"]
print(appreciation(15.5))

# %% tags=["gridwidth-1-2"]
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
#   ```python
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
#
# on parle toujours de la boucle **la plus imbriquée**

# %% tags=["gridwidth-1-2"]
# exemple avec continue
# on veut zapper les nombres pairs

L = [1, 5, 2, 7, 9]

while L:
    n = L.pop()
    if n % 2 == 0:
        continue
    # ... faire des trucs compliqués avec n
    print(f"{n=}", end=" ")

# %% tags=["gridwidth-1-2"]
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
# ## `match .. case`
#
# une toute nouvelle instruction `match` permet de définir des alternatives selon:
# - la taille d'une objet
# - la valeur dans un objet
# - et en fait pas mal d'autres choses...

# %% slideshow={"slide_type": "slide"}
# dans une version à-la switch

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case 401 | 403 :
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"

print(http_error(404))


# %%
# mais on peut faire aussi plus complexe
# avec du pattern-matching, ici sur la valeur
# dans un tuple

def on_values(point: tuple[float, float]):
    match point:
        case (0, 0):
            return "Origin"
        case (0, y):
            return f"null-x Y={y}"
        case (x, 0):
            return f"null-y X={x}"
        case (x, y):
            return f"regular X={x}, Y={y}"
        case _:
            raise ValueError("Not a point")

P = (0, 20)
print(on_values(P))


# %%
# ou encore ici sur la taille d'un objet

def on_size(string):
    match string.split():
        case []:
            return "no word"
        case [w]:
            return f"one word {w}"
        case first, *rest:
            return f"multi words starting with `{first}`"

print(on_size(""))
print(on_size("a b c"))

# %% [markdown]
# pour une introduction plus complète, voyez ceci <https://peps.python.org/pep-0636/>

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

# %% [markdown] tags=[]
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
# ## exécuter du code
#
# (avancé)
#
# nous allons voir à présent deux **fonctions**, donc tehcniquement ce ne sont pas des instructions, mais bon ce n'est pas important

# %% [markdown]
# ### `exec()` et `eval()`
#
# * comment exécuter du code dans une chaîne de caractères ?
# * `exec()` est une fonction qui permet l’exécution dynamique de code python
#   * retourne toujours None
# * `eval()` est une fonction qui évalue une **expression** (mais **pas** une instruction)
#   * et retourne le résultat de cette évaluation
# * le code est bien sûr passé dans un `str`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `exec()` pour une instruction

# %% tags=["gridwidth-1-2"]
# instructions
i1 = """def fact(n):
    return 1 if n <= 1 else n * fact(n-1)"""
i2 = """if fact(2) > 1:
    print('OUI')"""

# %% tags=["gridwidth-1-2"]
# on peut les exécuter
# ceci ne fait rien que de définir une fonction
print(exec(i1))

# %% cell_style="center"
fact

# %% tags=["gridwidth-1-2"]
# qu'on peut maintenant utiliser au travers de i2
# l'impression ici est faire dans le code de i2
# et puis None est le retour de exec
print(exec(i2))

# %% tags=["gridwidth-1-2"]
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

# %% tags=["gridwidth-1-2"]
# c'est mieux de les évaluer
print(eval(e1))

# %% tags=["gridwidth-1-2"]
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

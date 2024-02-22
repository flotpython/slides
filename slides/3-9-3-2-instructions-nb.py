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

# %% [markdown] slideshow={"slide_type": "slide"}
# ## boucle `while`

# %% [markdown]
# ```python
# while <test>:
#     bloc d_instructions
#     alignés comme on l_a vu
# else:
#     bloc     # exécuté à la sortie de la boucle 
#     aligné   # seulement s’il n’y a pas de break
# ```

# %% [markdown]
# **remarque**  
# les boucles en Python sont plus volontiers construites avec un `for`  
# on en reparlera un peu plus tard

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `break`, `continue`

# %% [markdown]
# deux instructions particulières:
#
# * `continue`: abandonner ce tour de boucle, passer au suivant
# * `break`: sortir complètement de la boucle courante

# %% cell_style="split"
counter = 0
while counter <= 5:
    counter += 1 
    if counter % 2 == 0:
        continue
    print(f"counter={counter}")

# %% cell_style="split"
counter = 0
while counter <= 100:
    counter += 1 
    if counter %3 == 0:
        break
    print(f"counter={counter}")


# %% [markdown] slideshow={"slide_type": "slide"}
# ### `break`, `continue`

# %% [markdown]
# * `break` et `continue` peuvent  être n’importe où dans une boucle
# * ils ne s’appliquent qu’à la boucle dans laquelle ils sont, 
#   * mais **pas aux boucles supérieures**
#
# ```python
# while <test1>:
#     while <test2>:
#         break  # sort de ‘while <test2>’, mais
#                # pas de ‘while <test1>’
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ## instruction `pass`

# %% [markdown]
# * `pass` ne fait rien
# * il est en général utilisé lorsque la syntaxe demande une instruction, mais qu’on ne l’a pas encore implémentée

# %% cell_style="split"
def ma_fonction():
    pass


# %% cell_style="split"
class Foo:
    pass


# %% [markdown] slideshow={"slide_type": "slide"}
# ## libération de variables: `del`

# %% [markdown]
# * `del a` 
#   * instruction qui libère la variable `a` (en la supprimant de l’espace de nommage)
#   * et décrémente le compteur de références de l’objet vers lequel pointe `a`
# * `del` fonctionne aussi sur
#   * un slicing de séquence: `del L[i:j:k]`
#   * un dictionnaire: `del D[clef]`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `del` sur variable

# %% cell_style="split"
print(liste)

# %% cell_style="split"
del liste

# %%
try:
    print(liste)
except Exception as exc:
    print(f"OOPS - {type(exc)}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `del` sur expression

# %% cell_style="split"
liste = list(range(5))
print(liste)

# %% cell_style="split"
del liste[1:3]

# %%
liste

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

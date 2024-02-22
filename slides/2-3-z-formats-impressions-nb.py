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
# # formatage et impressions

# %% [markdown] slideshow={"slide_type": "slide"}
# ## formatage des chaînes : f-strings

# %% [markdown] cell_style="split"
# pour le formatage des chaines: utilisez les ***f-strings***, qui évitent les répétitions fastidieuses

# %% [markdown] cell_style="split"
# l'idée consiste à
# * faire précéder la chaine par un `f`
# * et embarquer directement dans la chaine des `{}`
# * qui peut contenir une expression Python (un nom de variable, ou plus élaboré)
# * et toute la partie dans le `{}` sera remplacé par le résultat de l'expression

# %% cell_style="split" tags=["gridwidth-1-2"]
import math

# %% cell_style="split" tags=["gridwidth-1-2"]
nom, age = "Pierre", 42

# %% cell_style="split" tags=["gridwidth-1-2"]
f"{nom} a {age} ans"

# %% cell_style="split" tags=["gridwidth-1-2"]
f"360° = {2*math.pi} radians"

# %% [markdown]
# ````{admonition} n'importe quelle expression entre {}
# :class: info
#
# notez qu'entre les `{}`, on peut mettre un **nom de variable** mais aussi, plus généralement, écrire **une expression** (faire un calcul)
#
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *f-string* : expression et format

# %% [markdown] slideshow={"slide_type": ""}
# ![](media/f-string.svg)

# %%
print(f"ᴨ arrondi à deux décimales = {math.pi:.2f}")


# %% [markdown] slideshow={"slide_type": "slide"}
# ### `=` dans une f-string

# %% [markdown]
# grâce au `=` optionnel, on peut obtenir en une seule fois un double affichage:
#
# * le code de l'expression
# * et la valeur de l'expression

# %%
# et c'est très pratique pour le debugging
def add(x, y):
    return x+y

a, b = 10, 30

# c'est ici:      ⬇
print(f"{add(a, b)=}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### formats - scientifiques

# %% [markdown]
# formats scientifiques usuels: `e` `f` et `g`, cf. `printf`

# %%
x = 23451.23423536563
f'{x:e} | {x:f} | {x:g} | {x:010.1f} | {x:.2f}'

# %%
y = 769876.11434
f'{x:e} | {y:f} | {x:g} | {y:010.2f} | {x:.2f}'

# %% [markdown]
# Voir aussi pour plus de détails:  
# <https://mkaz.blog/code/python-string-format-cookbook/>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### justification

# %% [markdown]
# pour faire de la justification, on dispose des formats `<` `ˆ` et `>`

# %%
f"|{nom:<12}|{nom:^12}|{nom:>12}|"

# %%
# on peut aussi préciser avec quel caractère remplir
num = 123
f"|{num:<12}|{num:-^12}|{num:0>12}|"

# %% [markdown] slideshow={"slide_type": "slide"} tags=[]
# ### expression dans le format

# %% [markdown] slideshow={"slide_type": ""} tags=[]
# un peu plus avancé, mais notez qu'on peut également utiliser des expressions dans le format

# %% cell_style="split" tags=[]
from decimal import Decimal
value = Decimal('12.34567')

# %% cell_style="split" tags=["gridwidth-1-2"]
# ici la précision de 4
# signifie 4 chiffres
# significatifs en tout

f"value = >{value:10.4}<"

# %% cell_style="split" tags=["gridwidth-1-2"]
# si nécessaire la précision 
# peut aussi être un paramètre !

width = 10
precision = 4
f"value = >{value:{width}.{precision}}<"

# %% [markdown] slideshow={"slide_type": "slide"}
# ## affichage avec `print()`

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

# %% [markdown]
# ### module logging (avancé)
#
# * pour le logging plus évolué qu’un simple print redirigé dans un fichier, on peut utiliser le module de la librairie standard `logging`
# * documentation du module
#   * https://docs.python.org/3/library/logging.html
# * tutorial
#   * https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
#
# c'est **la bonne façon** de conserver des traces d'exécutionpour un programme en production

# %% [markdown]
# ## formatage : méthodes *old-school*
#
# * avant Python-3.6, il y a eu deux autres méthodes pour formatter
#   * `str.format()`
#   * l'opérateur `%`
# * il est **recommandé** d'utiliser les f-strings
# * mais les deux autres formes existent encore, a minima savoir les lire

# %% [markdown] slideshow={"slide_type": "slide"}
# ### formatage avec `str.format()` (*old-school*)

# %%
# anonyme (dans l'ordre)
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

# %%
# par index
print('{1} and {0} {0}'.format('spam', 'eggs'))

# %%
# par nom
print('This {food} is {adjective}'
      .format(food='spam', adjective='absolutely horrible'))

# %% [markdown]
# ### formatage avec `%` (*very old-school*)
#
# * encore plus ancienne méthode

# %%
nom = "Alice"
"%s dit bonjour" % nom

# %%
d = 3
"%i + %i = %i" % (d, d, d + d)

# %%
"%(food)s is %(adjective)s" % {'food' : 'bacon',
                               'adjective' : 'delicious' }

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# * on peut être parfois tenté d’utiliser la concaténation `+`

# %% tags=["level_intermediate"]
'abc' + 'def'

# %% [markdown] tags=["level_intermediate"]
# * par contre **attention**, on ne peut concaténer que des `str`, il faut convertir explicitement avec `str()`

# %% tags=["level_intermediate"]
age = 35
try: 'alice a ' + age + ' ans'
except Exception as e: print ("OOPS", e)

# %% tags=["level_intermediate"]
'alice a ' + str(age) + ' ans'

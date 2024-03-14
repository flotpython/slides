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


# %% [markdown] slideshow={"slide_type": "slide"}
# # affectations
#
# est-ce vraiment utile d'expliquer les affectations (en anglais *assignment*) ?  
# étonnamment il y a un million de choses à dire sur les multiples formes de l'affectation !

# %% [markdown]
# ## affectation simple
#
# bon à la base c'est simple; cette affectation est une **instruction**

# %%
a = 'alice'
print(a)

# %% [markdown]
# ````{admonition} digression : noms admissibles pour une variable
# :class: note admonition-small
#
# pour fabriquer un nom de variable, prenez une suite illimitée de lettres, chiffres, underscores qui
#
# * doit commencer par une lettre ou un underscore
# * n'est pas un mot-clé
# * est sensible à la casse
#   * `Spam` différent de `spam`
# * on peut aussi utiliser des caractères Unicode (accents et autres lettres grecques)
#   * **MAIS** c'est une pratique à utiliser avec la plus grande modération, car `σ` n'est pas `𝜎` !      
#
# ````{list-table} quelques exemples de noms de variables
# :align: center
# :header-rows: 1
#
# * - nom
#   - légal?
#   - nom
#   - légal?
#   - nom
#   - légal?
#   - nom
#   - légal?
# * - `abc`
#   - oui
#   - `ma_variable`
#   - oui
#   - `Spam_38`
#   - oui
#   - `_`
#   - oui
# * - `_caché`
#   - oui
#   - `while`
#   - non
#   - `2wheels`
#   - non
#   - `ma-variable`
#   - non
# ````  

# %% [markdown]
# ## portée des variables (intermédiaire)
#
# pour faire court, la portée d'une variable est **la fonction** - et non pas, comme dans les langages à la C++, le bloc (c'est d'ailleurs assez cohérent avec le fait qu'il n'y a pas de `{}` en Python, si on veut)
#
# à savoir également, l'affectation sert aussi de **déclaration**: si vous affectez une variable dans une fonction, cela signifie que la variable est **locale à la fonction**
#
# `````{admonition} UnboudLocalError
# :class: attention admonition-small
#
# du coup dans le programme suivant, on observe une erreur; pouvez-vous expliquer pourquoi ?
#
# ```python
# variable = 1
#
# def foo():
#     print(f"{variable=}")
#     variable = 2
#
# foo()
# ```
#
# ````{admonition} réponse
# :class: seealso dropdown
#
# à la première ligne de `foo` on référence `variable`; mais comme elle est **affectée** en ligne 2, elle est considérée comme **locale à `foo`**; aussi cela signifie qu'elle n'a pas encore été initialisée !  
# sa valeur est inconnue - et donc en particulier elle ne vaut pas 1 comme on pourrait le penser
# ````
#
# `````

# %% [markdown]
# ### `global` et `nonlocal`
#
# ces deux mots-clé permettent d'affecter une variable qui justement n'est pas locale à la fonction:  
# `global` pour référencer une variable globale au module,  
# `nonlocal` pour référencer une variable dans une fonction imbriquée entre le module et la fonction courante

# %%
# exemple avec global
variable = 1

def foo():
    global variable
    # no worries this time
    print(f"inside {variable=}")
    variable = 2

print(f"before {variable=}")
foo()
# variable is 2
print(f"outside {variable=}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## affectation par *unpacking*
#
# une forme très fréquente - et très pratique - d'affectation  
# on "déballe" le contenu d'une structure, et on affecte les morceaux à plusieurs variables d'un coup

# %%
a, b, c = ['alice', 'bob', 'charlie']
print(b)

# %% [markdown]
# il y a bien sûr quelques contraintes
# * il faut la même forme à grauche et à droite
# * mais les types peuvent être différents (tuple à gauche, liste à droite, ..)
#
# ````{admonition} un idiome pour échanger deux variables
# :class: admonition-small
#
# sans avoir besoin d'une variable temporaire, on peut échanger les contenus des variables `a` et `b` en faisant simplement
# ```python
# a, b = b, a
# ```
# ça marche parce que les expressions à droite ont évaluées **avant** que les affectations aient lieu
# ````

# %% [markdown]
# ### *extended unpacking*
#
# * on peut utiliser une notation `*` devant une (seule) variable
# * cette variable va référencer une *liste* qui regroupe  
#   tout ce qui n’est pas *unpacké* dans les autres variables
#
# * il ne peut y avoir qu’une seule variable de ce type (sinon ce srait ambigu)

# %% slideshow={"slide_type": "slide"} tags=["gridwidth-1-2"]
L = [1, 2, 3, 4, 5]

# %% slideshow={"slide_type": "fragment"} tags=["gridwidth-1-2"]
a, *b = L
print(f"{a=} {b=}")

# %% slideshow={"slide_type": "slide"} tags=["gridwidth-1-2"]
a, *b, c, d = L
print(f"{a=} {b=} {c=} {d=}")

# %% [markdown]
# ### *unpacking* - ignorer des valeurs avec `_`
#
# * lorsqu’on n'est pas intéressé par certaines valeurs il est d'usage d'utiliser la variable `_`
# * on peut l'utiliser plusieurs fois - ne pas penser que ça induit une égalité entre, par exemple ici, la 2ème et la 4ème valeur

# %%
# je ne garde pas les valeurs à la 2e et 4e position
debut, _, milieu, _, fin = [1, 2, 3, 4, 5] 
print(f"{debut=} {fin=} {_=}")

# %% [markdown]
# ### *unpacking* et imbrications
#
# un peu plus gadget, mais parfois utile:
#
# * le terme de gauche peut être imbriqué autant que nécessaire
# * il faut que les deux termes aient la même *forme* (pattern-matching)
# * on peut utiliser indifféremment un tuple ou une liste

# %% tags=["gridwidth-1-2"]
# le \ c'est juste pour aligner les deux morceaux
obj = \
1, ( (2, 3), (4, [5, 6])), 6
a, ( _,      [b,  c    ]), d = obj

# %% tags=["gridwidth-1-2"]
print(f"{a=} {b=} {c=} {d=}")

# %% [markdown]
# ## affectation multiple
#
# * ici les variables pointent vers le même objet !
#   (ça se voit qu'on ne crée qu'une seule liste)
# * on crée donc une référence partagée

# %%
# une seule liste
a = b = c = [1, 2, 3]
a is b

# %%
# qui donne un résultat très différent de ceci où on crée deux listes
A = [1, 2, 3]
B = [1, 2, 3]
A is B

# %%
# dans la pratique c'est surtout utilisé en conjonction avec le unpacking

L = car, *cdr = [1, 2, 3]
print(f"{L=} {car=} {cdr=}")

# %% [markdown]
# ### affectation et boucle `for`
#
# pour anticiper un peu sur les boucles `for`, l'affectation a lieu aussi à chaque itération de boucle

# %% tags=["gridwidth-1-2"]
liste = [1, 10, 100]

for item in liste:
    print(f"{item=}", end=" ")

# %% tags=["gridwidth-1-2"]
# du coup dans un for on peut aussi faire du unpacking

liste = ([1, 2], [10, 20], [100, 200])

for a, b in liste:
    print(f"{a=}x{b=}", end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## expression d'affectation (*walrus*)
#
# enfin depuis la 3.8 on dispose aussi d'une **expression** qui fait de l'affectation  
# bon c'est un peu plus limité que l'instruction (pas de unpacking, pas de `seq[i]` ou de `var.attribut` dans la partie gauche)  
# mais ça rend parfois service:

# %%
# exemple 1 : lecture d'un fichier par buffer

CHUNK = 20 * 1024

with open("../data/hamlet.txt") as feed:
    while chunk := feed.read(CHUNK):
        print(f"[{len(chunk)}]", end='')


# %% scrolled=true
# exemple 2 : les regexps

import re
pattern = "(\d+)(st|nd|rd|th) edition"

with open("../data/hamlet.txt") as feed:
    for lineno, line in enumerate(feed, 1):
        if match := re.search(pattern, line):
            print(match.group(0))

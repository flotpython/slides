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
#     title: "s\xE9quences et chaines"
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
# # séquences & chaines

# %% [markdown] slideshow={"slide_type": "slide"}
# ## c'est quoi une séquence ?

# %% [markdown] cell_style="split"
# * suite finie et ordonnée d'objets
# * du coup indexable, on peut écrire `S[n]`
#   * en Python, les **indices commencent à 0**
# * peuvent contenir des duplications

# %% [markdown] cell_style="split"
# les séquences dans le langage Python (entre autres):
#
# * mutable
#   * `list`, `bytearray`
# * immutable
#   * `str`, `bytes`, `tuple`, `range`

# %% [markdown]
# ````{admonition} les chaines (str) sont des séquences
# :class: info
#
# nous allons voir pour commencer des choses valables **sur toutes les séquences**,
# et donc en particulier sur les chaines de caractères, puisque les chaines sont des séquences
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fonctions sur toutes les séquences

# %% [markdown]
# ### indexation, longueur
#
# * `S[i]`
#   * retourne l’élément d'indice i
# * `len(S)`
#   * donne la taille en nombre d’éléments

# %% [markdown] slideshow={"slide_type": "slide"}
# ### concaténation, comparaisons

# %% [markdown]
# * `S + T`
#  * retourne une nouvelle séquence qui est la concaténation de S et T
# * `S*n` ou `n*S`
#   * retourne une nouvelle séquence qui est la concaténation de n *shallow* copies de S
# * `sum(S)` (resp. `min(S)` et `max(S)`)
#   * retourne la somme des éléments de S (resp. le plus petit, le plus grand)

# %% [markdown] tags=[]
# ````{admonition} les séquences sont des itérables
#
# un itérable en Python, c'est un objet sur lequel on peut faire un `for`
#
# en fait les fonctions `sum`, `min` et `max` s'appliquent à n'importe quel itérable  
# toutes les séquences sont des itérables, mais tous les itérables ne sont pas des séquences  
# la famille des itérables est donc plus large que les séquences
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ### appartenance, recherches

# %% [markdown] slideshow={"slide_type": ""}
# * `x in S`; selon les types:
#   * `True` si un élément de S est égal à x  
#     (e.g. S est une `list`)
#
#   * `True` si S contient x  
#     (e.g. S est une `str`)
#
# * diverses méthodes (voir docs):
#   * `S.count(a)`
#     * retourne le nombre d’occurrences de a dans S
#   * `S.index(a)`, `S.find(a)`  
#     retourne l’indice de la première occurrence de a dans S
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## slicing

# %% [markdown]
# * `S[i:j]` retourne
#   * une nouvelle séquence de même type
#   * contenant tous les éléments de l’indice i à l’indice j-1
# * `S[i:j:k]` retourne
#   * une nouvelle séquence de même type
#   * prenant tous les éléments de l’indice i à l’indice j-1,
#   * par sauts de k éléments
# * les indices `i`, `j` et `k` peuvent être négatifs
#
# voyons des exemples de tout ceci

# %% [markdown]
# ````{admonition} slicing et numpy
# :class: info
#
# la notion de slicing est **très massivement utilisée** dans toutes les librairies numériques, notamment en `numpy`
# ````

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ![](media/egg-bacon.svg)

# %% [markdown] cell_style="split"
# avec le slicing, on peut
#
# * omettre les bornes
# * compter depuis la fin, avec un indice négatif

# %% cell_style="split" tags=["gridwidth-1-2"]
s = "egg, bacon"
s[0:3]

# %% cell_style="split" tags=["gridwidth-1-2"]
# si on omet une borne
# ce sera le début ..
s[:3]

# %% cell_style="split" tags=["gridwidth-1-2"]
# ... ou la fin:
s[5:]

# %% cell_style="split" tags=["gridwidth-1-2"]
# les indices peuvent être négatifs
s[-3:10]

# %%
# tout entier: une shallow-copy
s[:]

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ![](media/egg-bacon-bornes.svg)

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ### les bornes

# %% [markdown] cell_style="split"
# La convention est choisie pour pouvoir facilement "encastrer" les slices:

# %% cell_style="split" tags=["gridwidth-1-2"]
s[0:3]

# %% cell_style="split" tags=["gridwidth-1-2"]
s[3:6]

# %% cell_style="split" tags=["gridwidth-1-2"]
s[6:]

# %% cell_style="split" tags=["gridwidth-1-2"]
s[0:3] + s[3:6] + s[6:] == s

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ![](media/egg-bacon.svg)

# %% [markdown] cell_style="split"
# ### le pas

# %% [markdown] cell_style="split"
# * on peut préciser un pas
# * qui peut aussi être négatif
# * ou omis (défaut 1)

# %% cell_style="split" tags=["gridwidth-1-2"]
s[0:10:2]

# %% cell_style="split" tags=["gridwidth-1-2"]
s[::2]

# %% cell_style="split" tags=["gridwidth-1-2"]
s[:8:3]

# %% cell_style="split" tags=["gridwidth-1-2"]
s[-2::-3]

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ![](media/egg-bacon.svg)

# %% [markdown] cell_style="split"
# ### pas d'exception

# %% [markdown] cell_style="split"
# les slices ont un comportement plus permissif que l'indexation

# %%
# Si j'essaie d'utiliser un index inexistant
try: s[100]
except Exception as e: print("OOPS", e)

# %% cell_style="split" tags=["gridwidth-1-2"]
# par contre avec un slice, pas de souci
s[5:100]

# %% cell_style="split" tags=["gridwidth-1-2"]
# vraiment..
s[100:200]

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/egg-bacon.svg)

# %% cell_style="split" tags=["gridwidth-1-2"]
s[-1]

# %% cell_style="split" tags=["gridwidth-1-2"]
s[-3:-1]

# %% cell_style="split" tags=["gridwidth-1-2"]
s[:-3]

# %% cell_style="split" tags=["gridwidth-1-2"]
s[::-1]

# %% cell_style="split" tags=["gridwidth-1-2"]
s[2:0:-1]

# %% cell_style="split" tags=["gridwidth-1-2"]
s[2::-1]

# %% [markdown] slideshow={"slide_type": "slide"}
# ### formes idiomatiques

# %% [markdown] tags=[]
# s = [1, 2, 3]

# %% cell_style="split" tags=["gridwidth-1-2"]
# une copie simple
s[:]

# %% cell_style="split" tags=["gridwidth-1-2"]
# copie renversée
s[::-1]

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `str` pour manipuler du texte

# %% [markdown]
# * le type `str` est un cas particuliers de **séquence**
# * qui permet de manipuler **du texte**

# %% [markdown]
# ````{admonition} un caractère ce **n'est pas** un octet
# :class: warning
#
# avec l'encodage le plus répandu aujourd'hui (UTF-8), les caractères ASCII tiennent sur un octet  
# mais **ce sont les seuls**: un `é` par exemple occupe 2 octets; un `‰` occupe 3 octets; un `🚀` occupe 4 octets
#
# si vous avez besoin de manipuler des données brutes - typiquement si vous lisez un fichier binaire - il vous faut utiliser le type `bytes` que nous verrons plus tard
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ### écrire une str de manière littérale

# %% [markdown]
# * une chaîne de caractères est définie de manière équivalente par des simples ou doubles guillemets (`'` ou `"`)
# * on peut ainsi facilement inclure un guillemet

# %% cell_style="split" tags=["gridwidth-1-2"]
# une chaine entre double quotes
# pas de souci pour les accents
print("c'est l'été")

# %% cell_style="split" tags=["gridwidth-1-2"]
# entre simple quotes
print('on se dit "pourquoi pas"')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### sur plusieurs lignes

# %% [markdown]
# * pour écrire une chaîne sur plusieurs lignes on utilise `"""` ou `'''`

# %% cell_style="center"
# bien sûr ici vous pouvez remplacer les """ par '''

print("""et pour entrer plusieurs lignes,
ou bien des chaines avec des " et des '
c'est facile aussi""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### chaînes de caractères accolées

# %% [markdown]
# * lorsque vous voulez entrer une chaine un peu longue
# * vous pouvez **simplement accoler** deux chaines dans votre source:

# %% cell_style="split" tags=["gridwidth-1-2"]
s = "le début" " et la fin"
print(s)

# %% cell_style="split" tags=["gridwidth-1-2"]
s = ("une chaine trop longue"
     " pour tenir sur une ligne")
print(s)

# %% [markdown]
# ````{admonition} les parenthèses sont importantes
# :class: warning
#
# notez bien les parenthèses dans ce deuxième exemple, car sinon c'est une erreur de syntaxe
# ````

# %% [markdown] tags=[]
# ### échappements dans les chaines
#
# * le caractère `\` a un sens particulier dans les chaines écrites de manière littérale dans le programme
# * on écrit un retour chariot avec un `\n`
# * une tabulation avec `\t`
# * les guillemets peuvent être échappés (e.g. pour entrer un `'` dans une chaine délimitée avec un `'`)
# * un backslash avec `\\`
# * enfin on peut aussi entrer des caractères exotiques par leur codepoint avec 
#   * `\x` `\u` `\U`

# %% cell_style="split" tags=["gridwidth-1-2"]
s = "deux\nlignes"
print(s)

# %% cell_style="split" tags=["gridwidth-1-2"]
s = 'des\ttrucs\tespacés'
print(s)

# %% cell_style="split" tags=["gridwidth-1-2"]
# imaginons qu'on ait les deux sortes de guillemets
s = "simple' double\""
print(s)

# %% cell_style="split" tags=["gridwidth-1-2"]
s = 'backslash \\\tquote \''
print(s)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *raw-strings*

# %% [markdown] cell_style="split"
# Voici un problème commun, surtout sous Windows:

# %% cell_style="split"
s = 'C:\Temp\test.txt'
print(s)

# %% [markdown] cell_style="center"
# * `\T` n’existe pas comme échappement; Python interprète correctement `\T`
#
# * mais `\t` est compris comme une tabulation !!

# %% [markdown]
# pour résoudre ce problème, on peut utiliser des double-backslash `\\`, mais ce n'est vraiment pas élégant 
#
# la bonne solution consiste à utiliser une "raw string", dans laquelle les backslash ne sont *pas interprétés*

# %%
# pour créer une raw-string, simplement faire précéder le string d'un 'r'

s = r'C:\Temp\test1.bin'

print(s)


# %% [markdown]
# ````{admonition} préférez le / pour les chemins de fichier
#
# notez que le plus souvent, vous pouvez aussi bien utiliser un `/` au lieu d'un <code>&bsol;</code> dans les chemins de fichiers sous Windows, ce qui résoud tous les problèmes d'échappement
#
# les *raw-strings* restent une feature bien pratique dans d'autres contextes, notamment avec les expressions régulières, que nous n'avons pas pu utiliser comme exemple ici puisqu'on n'en a pas encore parlé..
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *docstrings*

# %% [markdown]
# une *docstring* est une chaine littérale insérée **au tout début** du code d'une fonction (ou classe ou module) et qui sert à la documenter  
# on utilise souvent les triples guillemets pour cela

# %% cell_style="split"
def double(n):
    """
    Returns the double of its input parameter

    The help message usually spans several lines
    """
    return 2*n


# %% cell_style="split"
help(double)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## opérations sur les `str`
#
# ### toutes les opérations des séquences
#
# que l'on a déjà vues :

# %% cell_style="split" tags=["gridwidth-1-2"]
s1 = 'abcdéfg'
s2 = 'bob'
len(s1)

# %% cell_style="split" tags=["gridwidth-1-2"]
# concaténation
s1 + s2
'abcdefbob'

# %% cell_style="split" tags=["gridwidth-1-2"]
# slicing
s1[-1::-2]

# %% cell_style="split" tags=["gridwidth-1-2"]
'=' * 30

# %% cell_style="split" tags=["gridwidth-1-2"]
# est-ce une sous-chaine ?
'cdé' in s1

# %% cell_style="split" tags=["gridwidth-1-2"]
# à quelle position ?
s1.index('cdé')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### objet `str` non mutable

# %% [markdown]
# par contre **ATTENTION** un `str` n'est **pas mutable**

# %%
try:
    s1[2] = 'x'
except TypeError as e:
    print("OOPS", e, type(e))

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

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# ## méthodes sur les `str`

# %% [markdown]
# ### `strip()`

# %%
# j'ai lu une chaine dans un fichier
# je ne sais pas trop s'il y a des espaces à la fin
# et si la chaine contient un newline

dirty = "  des blancs au début et à la fin et un newline  \n"
dirty

# %%
# c'est la méthode la plus simple pour nettoyer
dirty.strip()

# %% [markdown]
# ````{admonition} utilisez rstrip() pour nettoyer les lignes lues dans un fichier
# :class: info smaller-admonition
#
# lorsqu'on nettoie une ligne qu'on a lue dans un fichier, on peut envisager
# d'utiliser `rstrip()` qui ne nettoie qu'à droite, là où se situe le NEWLINE
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `split()` et `join()`

# %% cell_style="split"
# une chaine à découper
s = "une phrase\nsur deux lignes"
s

# %% cell_style="split"
# sans argument, split
# découpe selon les espaces
# et tabulations et newline
liste = s.split()
liste

# %% cell_style="split"
# recoller les morceaux
"".join(liste)

# %% cell_style="split"
# le plus souvent
" ".join(liste)

# %%
# ou n'importe quel autre séparateur
"+++".join(liste)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### remplacements, recherches

# %%
s = "une petite phrase"
s.replace('petite', 'grande')

# %% cell_style="split"
# l'index du premier caractère
s.find('hra')

# %% cell_style="split"
s[12]

# %% [markdown] slideshow={"slide_type": "slide"}
# #### et plein d'autres..

# %% [markdown]
# * de nombreuses méthodes disponibles
# * personne ne retient l'intégralité des méthodes sur les types de base
# * le bon réflexe : chercher dans la dos Python qui est très bien faite
# * google les simples mots clés 'python str', vous trouvez
# * <https://docs.python.org/3/library/stdtypes.html>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## formatage : anciennes méthodes

# %% [markdown]
# * avant Python-3.6, il y a eu deux autres méthodes pour formatter
# * `str.format()`
# * l'opérateur `%`

# %% [markdown]
# * il est **recommandé** d'utiliser les f-strings
# * mais les deux autres formes existent encore
# * a minima savoir les lire

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

# %% [markdown] slideshow={"slide_type": "slide"}
# ### formatage avec `%` (*very old-school*)

# %% [markdown]
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

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_advanced"]
# ## un peu d'introspection (avancé)

# %% [markdown] tags=["level_advanced"]
# disons qu'on voudrait savoir combien de méthodes sont disponibles sur les chaines.

# %% cell_style="split" tags=["level_advanced"]
type("abc")

# %% cell_style="split" tags=["level_advanced"]
str

# %% tags=["level_advanced"]
# 'str' est une variable prédéfinie, qui référence
# le type (la classe) de toutes les chaines
type("abc") is str

# %% tags=["level_advanced"]
# du coup son type, c'est .. le type <type>
type(str)

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_advanced"]
# ### un peu d'introspection...

# %% tags=["level_advanced"]
# peu importe... quoi qu'il en soit, dir(str) retourne la liste
# des noms de méthodes connues sur cette classe;
# regardons par exemple les premiers et les derniers
dir(str)[:2], dir(str)[-2:]

# %% tags=["level_advanced"] cell_style="split"
# avec len() je peux savoir combien il y en a
len(dir(str))

# %% tags=["level_advanced"] cell_style="split"
# mais en fait, pour un décompte significatif
# on enlève celles dont le nom contient `__`
methods = [method for method in dir(str)
           if '__' not in method]
len(methods)

# %% tags=["level_advanced"]
# est-ce que les chaines ont une méthode 'split' ?
'split' in methods

# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   nbhosting:
#     title: "s\xE9quences et chaines"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% [markdown] slideshow={"slide_type": ""}
# # séquences & chaines

# %% [markdown] cell_style="split"
# * suite finie et ordonnée d'objets
# * du coup indexable `seq[n]`
# * indices **commencent à 0**
# * peuvent contenir des duplications

# %% [markdown] cell_style="split"
# * mutable
#   * `list`, `bytearray`
# * immutable
#   * `str`, `bytes`, `tuple`, `range`

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
# * `min(S)` (resp. `max(S)`)
#   * retourne le plus petit (resp. le plus grand) élément de S

# %% [markdown] slideshow={"slide_type": "slide"}
# ### appartenance, recherches

# %% [markdown] slideshow={"slide_type": ""}
# * `x in S`; selon les types:
#  * `True` si un élément de S est égal à x  
#    (e.g. S est une `list`)
#  * `True` si S contient x  
#    (e.g. S est une `str`)
# * `S.index(a)`
#   * retourne l’indice de la première occurrence de a dans S
# * `S.count(a)`
#   * retourne le nombre d’occurrences de a dans S

# %% [markdown] slideshow={"slide_type": "slide"}
# ## slicing

# %% [markdown]
# * `S[i:j]` retourne 
#   * une nouvelle séquence de même type
#   * contenant tous les éléments de l’indice i à l’indice j-1
# * `S[i:j:k]` retourne
#   * une nouvelle séquence de même type
#   * prenant tous les éléments de l’indice i à l’indice j-1, par sauts de k éléments

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ![](media/egg-bacon.png)

# %% [markdown] cell_style="split"
# **slicing**
#
# * on peut compter du début ou de la fin
# * on peut omettre les bornes

# %% cell_style="split"
s = "egg, bacon"
s[0:3]

# %% cell_style="split"
# si on omet une borne 
# ce sera le début ..
s[:3]

# %% cell_style="split"
# ... ou la fin:
s[5:]

# %% cell_style="split"
# les indices peuvent être négatifs
s[-3:10]

# %%
# tout entier: une shallow-copy
s[:]

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ![](media/egg-bacon-bornes.png)

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ### les bornes

# %% [markdown] cell_style="split"
# La convention est choisie pour pouvoir facilement encastrer les slices:

# %% cell_style="split"
s[0:3]

# %% cell_style="split"
s[3:6]

# %% cell_style="split"
s[6:]

# %% cell_style="split"
s[0:3] + s[3:6] + s[6:] == s

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ![](media/egg-bacon.png)

# %% [markdown] cell_style="split"
# ### le pas

# %% [markdown] cell_style="split"
# * on peut préciser un pas
# * peut aussi être négatif
# * ou omis (défaut 1)

# %% cell_style="split"
s[0:10:2]

# %% cell_style="split"
s[::2]

# %% cell_style="split"
s[:8:3]

# %% cell_style="split"
s[-2::-3]

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ![](media/egg-bacon.png)

# %% [markdown] cell_style="split"
# ### pas d'exception

# %% [markdown] cell_style="split"
# les slices ont un comportement plus permissif que l'indexation

# %%
# Si j'essaie d'utiliser un index inexistant
try: s[100]
except Exception as e: print("OOPS", e)

# %% cell_style="split"
# par contre avec un slice, pas de souci
s[5:100]

# %% cell_style="split"
# vraiment..
s[100:200]

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/egg-bacon.png)

# %% cell_style="split"
s[-1]

# %% cell_style="split"
s[-3:-1]

# %% cell_style="split"
s[:-3]

# %% cell_style="split"
s[::-1]

# %% cell_style="split"
s[2:0:-1]

# %% cell_style="split"
s[2::-1]

# %% [markdown] slideshow={"slide_type": "slide"}
# ### formes idiomatiques

# %%
s = [1, 2, 3]

# %% cell_style="split"
# une copie simple
s[:]

# %% cell_style="split"
# copie renversée
s[::-1]

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `str` et `bytes`

# %% [markdown]
# * deux cas particuliers de **séquences**
#   * `str` pour manipuler **du texte**
#   * `bytes` pour manipuler **de la donnée brute**
#   
# * **ATTENTION**
#   * un caractère ce **n'est pas** un octet

# %% [markdown]
# <div class="rise-footnote">
#
# avec l'encodage le plus répandu aujourd'hui (UTF-8), tous les caractères ASCII tiennent sur un octet   
# mais **ce sont les seuls**: un `é` par exemple occupe 2 octets; un `‰` occupe 3 octets; un `🚀` occupe 4 octets
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### chaînes de caractères `str`

# %% [markdown]
# * un cas particulier de séquence
# * une chaîne de caractères est définie de manière équivalente par des simples ou doubles guillemets (`'` ou `"`)
# * on peut ainsi facilement inclure un guillemet

# %% cell_style="split"
# une chaine entre double quotes
# pas de souci pour les accents 
print("c'est l'été")

# %% cell_style="split"
# entre simple quotes
print('on se dit "pourquoi pas"')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### chaîne de caractères sur plusieurs lignes

# %% [markdown]
# * pour écrire une chaîne sur plusieurs lignes on utilise `"""` ou `'''`

# %% cell_style="center"
print("""et pour entrer plusieurs 
lignes avec des " et/ou des ' 
c'est facile""")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### chaînes de caractères accolées

# %% [markdown]
# * lorsque vous voulez entrer une chaine un peu longue
# * vous pouvez **simplement accoler** deux chaines dans votre source:

# %% cell_style="split"
s = "le début" " et la fin"
print(s)

# %% cell_style="split"
s = ("une chaine trop longue"
     " pour tenir sur une ligne")
print(s)

# %% [markdown]
# dans ce deuxième exemple, notez les parenthèses (sinon c'est une erreur de syntaxe)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### échappements dans les chaines

# %% [markdown]
# * on écrit un retour chariot avec un `\n`
# * autres caractères utilisant un backslash
#   * `\\`  `\'` `\"` `\t`
#   * `\x` `\u` `\U` 
#   …

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemples

# %% cell_style="split"
s = "l'hôtel"
print(s)

# %% cell_style="split"
# 
s = 'une "bonne" idée'
print(s)

# %% cell_style="split"
s = """une très longue phrase
avec saut de ligne"""
print(s)

# %% cell_style="split"
s = '  un backslash \\ un quote \' ' 
print(s)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *raw-strings*

# %% [markdown] cell_style="split"
# Voici un problème commun, surtout sous Windows:

# %% cell_style="split"
s = 'C:\Temp\test.txt'
print(s)

# %% [markdown] cell_style="center"
# * `\T` n’existe pas comme échappement  
#   Python interprète correctement `\T`
# * mais `\t` est compris comme une tabulation !!

# %% [markdown] cell_style="split"
# * 1$^{ère}$solution : utiliser `\\`  
#   mais pas très élegant

# %% cell_style="split"
s = 'C:\\Temp\\test1.bin'
print(s)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### *raw-strings* (suite)

# %% [markdown]
# * la bonne solution : "raw string" 
# * chaîne de caractères dans laquelle les backslash ne sont *pas interprétés*

# %%
# pour créer une raw-string, simplement faire précéder le string d'un 'r'
s = r'C:\Temp\test1.bin'
print(s)


# %% [markdown]
# <div class="rise-footnote">
#
# **NB** que le plus souvent, vous pouvez aussi bien utiliser un `/` au lieu d'un <code>&bsol;</code> dans les chemins de fichiers sous Windows
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *docstrings*

# %% [markdown]
# * les triples guillemets sont souvent utilisé pour les *docstrings*  
#   (aides des fonctions)

# %% cell_style="split"
def double(n):
    """
    Returns the double of its input parameter
    
    The help message usually spans several lines
    """
    return 2*n


# %% cell_style="split"
help(double)

# %% [markdown]
# <div class="rise-footnote">
#
# il faut que la chaine littérale soit la première instruction dans le code de la fonction
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ## opérations sur les `str`
#
# ### toutes les opérations des séquences
#
# que l'on a déjà vues :

# %% cell_style="split"
s1 = 'abcdéfg'
s2 = 'bob'
len(s1)

# %% cell_style="split"
# concaténation
s1 + s2
'abcdefbob'

# %% cell_style="split"
s1[-1::-2]

# %% cell_style="split"
'=' * 30

# %% [markdown] slideshow={"slide_type": "slide"}
# ### une chaine est une séquence (suite)

# %% cell_style="split"
s1

# %% cell_style="split"
'x' in s1

# %% cell_style="split"
'cdé' in s1

# %% cell_style="split"
s1.index('cdé')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### objet `str` non mutable

# %% [markdown]
# * par contre **ATTENTION** un `str` n'est **pas mutable**

# %%
try: 
    s1[2] = 'x'
except TypeError as e:
    print("OOPS", e, type(e))    

# %% [markdown] slideshow={"slide_type": "slide"}
# ## formatage des chaînes : f-strings

# %% [markdown] cell_style="split"
# * depuis Python-3.6
# * utilisez les ***f-strings***
# * qui évitent les répétitions fastidieuses

# %% [markdown] cell_style="split"
# * entre `{` et `}` : **du code** 
# * embarqué directement dans le format
# * n'importe quelle **expression**

# %% cell_style="split"
import math

# %% cell_style="split"
#
nom, age = "Pierre", 42

# %% cell_style="split"
f"{nom} a {age} ans"

# %% cell_style="split"
f"360° = {2*math.pi} radians"

# %% [markdown]
# <div class="rise-footnote">
#
# **NB** qu'entre les `{}`, on peut mettre un **nom de variable** mais aussi, plus généralement, écrire **une expression** (faire un calcul)
#
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *f-string* : expression et format

# %% [markdown] slideshow={"slide_type": ""}
# ![](media/f-string.png)

# %%
print(f"ᴨ arrondi à deux décimales = {math.pi:.2f}")


# %% [markdown] slideshow={"slide_type": "slide"}
# ### `=` dans une f-string

# %% [markdown]
# grâce au `=` optionnel, on peut obtenir en une seule fois un double affichage:
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
# https://mkaz.blog/code/python-string-format-cookbook/

# %% [markdown] slideshow={"slide_type": "slide"}
# ### formats pour f-string : justification

# %% [markdown]
# justification: formats `<` `ˆ` et `>`

# %%
f"|{nom:<12}|{nom:^12}|{nom:>12}|"

# %%
# on peut aussi préciser avec quel caractère remplir
num = 123
f"|{num:<12}|{num:-^12}|{num:0>12}|"

# %% [markdown] slideshow={"slide_type": "slide"}
# ### expression dans le format

# %% [markdown] slideshow={"slide_type": ""}
# * même le format peut, à son tour, contenir des expressions

# %% cell_style="split"
from decimal import Decimal
value = Decimal('12.34567')

# %% cell_style="split"
# ici la précision de 4 
# signifie 4 chiffres
# significatifs en tout

f"value = >{value:10.4}<"

# %% cell_style="split"
# la précision aurait pu être 
# un paramètre

width = 10
precision = 4
f"value = >{value:{width}.{precision}}<"

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

# %% [markdown] slideshow={"slide_type": "slide"}
# * on peut être parfois tenté d’utiliser la concaténation `+`

# %%
'abc' + 'def' 

# %% [markdown]
# * par contre **attention**, on ne peut concaténer que des `str`, il faut convertir explicitement avec `str()`

# %%
age = 35
try: 'alice a ' + age + ' ans'
except Exception as e: print ("OOPS", e)

# %%
'alice a ' + str(age) + ' ans'

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

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ## un peu d'introspection (avancé)

# %% [markdown] tags=["level_intermediate"]
# disons qu'on voudrait savoir combien de méthodes sont disponibles sur les chaines.

# %% cell_style="split" tags=["level_intermediate"]
type("abc")

# %% cell_style="split" tags=["level_intermediate"]
str

# %% tags=["level_intermediate"]
# 'str' est une variable prédéfinie, qui référence 
# le type (la classe) de toutes les chaines
type("abc") is str

# %% tags=["level_intermediate"]
# du coup son type, c'est .. le type <type>
type(str)

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_intermediate"]
# ### un peu d'introspection...

# %% tags=["level_intermediate"]
# peu importe... quoi qu'il en soit, dir(str) retourne la liste
# des noms de méthodes connues sur cette classe; 
# regardons par exemple les premiers et les derniers
dir(str)[:2], dir(str)[-2:]

# %% tags=["level_intermediate"]
# avec len() je peux savoir combien il y en a
len(dir(str))

# %% tags=["level_intermediate"]
# mais en fait, pour un décompte significatif
# on enlève celles dont le nom contient `__`
len([method for method in dir(str) if '__' not in method])

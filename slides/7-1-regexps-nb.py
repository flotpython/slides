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
#     title: regexps
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
# # expressions régulières

# %% [markdown]
# il s'agit d'une notion **transverse aux langages de programmation**, et présente dans la plupart d'entre eux  
# et en particulier historiquement dans Perl, qui en avait fait un *first-class citizen* 

# %% [markdown] slideshow={"slide_type": ""}
# ## c'est quoi ?
#
# vous cherchez à trouver toutes les adresses e-mail, ou tous les numéros de téléphone dans un texte ?  
# vous voulez savoir si une chaine pourrait être utilisée comme non de variable Python ?
#
# les expressions régulières sont faites pour ce genre d'application  
# voici pour commencer deux exemples élémentaires:
#
# * `a*` décrit tous les mots composés **de 0 ou plusieurs** `a`
#   * `''`, `'a'`, `'aa'`, …  sont les mots reconnus 
# * `(ab)+` : toutes les suites de **au moins 1 occurrence** de `ab`
#   * `'ab'`, `'abab'`, `'ababab'`, … sont les mots reconnus

# %% [markdown] slideshow={"slide_type": ""}
# ## le module `re`
#
# en Python, les expressions régulières sont accessibles au travers du module `re`

# %% tags=[]
import re

# %% [markdown] slideshow={"slide_type": ""}
# ### `re.match()` 
#
# `re.match()` vérifie si l'expression régulière peut être trouvée **au début** de la chaine

# %% tags=[]
# en anglais on dit pattern, ou regexp
# en français on dit filtre, ou encore parfois motif

pattern = "a*"

# %% tags=["gridwidth-1-2"]
# OUI

re.match(pattern, 'aa')

# %% tags=["gridwidth-1-2"]
# OUI

re.match('(ab)+', 'ab')

# %% tags=["gridwidth-1-2"]
# NON: retourne None

re.match('(ab)+', 'ba')

# %% tags=["gridwidth-1-2"]
# ici seulement LE DÉBUT du mot est reconnu, mais c'est OK

match = re.match('(ab)+', 'ababzzz')
match

# %% tags=["gridwidth-1-2"]
# le détail de ce qui a été trouvé

match.start(), match.end()

# %% tags=["gridwidth-1-2"]
# par contre ici le seul match n'est pas au début, donc NON

re.match('a+', 'zzzaaa')

# %% [markdown]
# ### `re.search()`
#
# * `re.search()` cherche la première occurrence de l'expression régulière  
# * et donc **pas forcément** au début de la chaine

# %%
# match répond non car seulement LE DÉBUT de la chaine est essayé

re.match('abzz', 'ababzzz')

# %%
# un use case pour le "walrus operator"
# i.e. une affectation mais qui est aussi une expression

if (match := re.search('abzz', 'ababzzz')):
    print(f"{match.start()=}, {match.end()=}")

# %% [markdown]
# ````{admonition} et autres...
#
# **notre sujet**: ici nous nous intéressons surtout à la façon de **construire les regexps**  
#
# il existe plusieurs autres fonctions pour utiliser les regexps, et notamment
#
# * `re.findall()` et `re.finditer()` pour trouver toutes les occurences du filtre dans la chaine
# * `re.sub()` pour remplacer …
#
# reportez-vous à [la documentation du module](https://docs.python.org/3/library/re.html) pour ces variantes
# ````

# %% [markdown] slideshow={"slide_type": ""}
# ### les objets `Match` 
#
# le résultat de `re.match()` est ... de type `Match`, qui fournit
# * les détails de ce qui a été trouvé (où et quoi)
# * et aussi les sous-chaines correspondant aux **groupes**, dont on reparlera...

# %%
pattern, string = "(ab)+", "the baba of regexps"
(match := re.search(pattern, string))

# %%
begin, end = match.span()
string[begin:end]


# %% [markdown] slideshow={"slide_type": "slide"}
# #### helper
#
# la fonction suivante va juste nous servir à visualiser les résultats d'un `re.match()` sur plusieurs chaines

# %%
# digression : une fonction utilitaire pour montrer
# le comportement d'un même pattern sur plusieurs chaines

def match_all(pattern, strings):
    """
    match a pattern against a set of strings 
    and display results properly aligned 
    """
    # compute max space
    margin = max(len(x) for x in strings) + 2 # for the quotes
    
    for string in strings:
        string_repr = f"'{string}'"
        print(f"'{pattern}' ⇆ {string_repr:>{margin}} → ", end="")
        
        if not (match := re.match(pattern, string)):
            print("NO")
        elif not (match.start() == 0 and match.end() == len(string)):
            # start() is always 0
            print(f"PARTIAL until char {match.end()}")
        else:
            print("FULL MATCH")


# %% cell_style="center"
# ce qui nous permettra de faire par exemple

match_all('(ab)+', ['ab', 'abab', 'ababzzz', ''])

# %% [markdown] slideshow={"slide_type": "slide"}
# ## construire un pattern
#
# une fois ceci en place, voyons les différents outils - on va dire aussi opérateurs - qui nous permettent de construire ce fameux pattern

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un caractère précis `a`

# %%
# si j'écris dans un pattern un caractère "normal"
# ça signifie que je veux trouver exactement ce caractère dans la chaine
match_all("a", ["a", "ab", "bc"])

# %% [markdown]
# ````{admonition}
#  normal ?
#
# pourquoi on dit un caractère "normal" ?  
# il se trouve que certains caractères, comme par exemple le `'.'` que l'on va voir tout de suite, ont un sens spécial,  
# on les appelle des **méta-caractères**
#
# du coup si je veux écrire un regexp qui filtre '.', je dois alors mettre dans ma regexp `"\."`; et pour ça je pense à l'écrire avec une *raw-string* donc je ferais `regexp = r"\."`
#
# ```{admonition} expression régulières et *raw-strings*
# :class: admonition-small
#
# du coup il est très fréquent qu'on utilise systématiquement une *raw-string* pour définir les filtres
# ```
# ````

# %%
match_all(r"\.", ["a", ".a"])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### n'importe quel caractère : `.`

# %%
# un '.' dans le pattern signifie EXACTEMENT UN un caractère
# mais n'importe lequel, à cet endroit dans la chaine

match_all('.', ['a', 'Θ', '.', 'ab', ''])

# %%
# pour bien comprendre la nécessité du \ devant le .

match_all(r'\.', ['a', 'Θ', '.', 'ab', ''])

# %% [markdown] slideshow={"slide_type": ""}
# ### **un seul** caractère parmi un ensemble: `[..]`
#
# avec les `[]` on peut désigner un **ensemble** de caractères, par exemple
#
# * `[acg]` exactement un caractère parmi `a` ou `c` ou `g`
# * `[a-z]` une lettre minuscule
# * `[a-zA-Z0-9_]` une lettre ou un chiffre ou un underscore

# %% tags=["gridwidth-1-2"]
match_all('[a-z]', ['a', '', '0'])

# %% slideshow={"slide_type": ""} tags=["gridwidth-1-2"]
match_all('[a-z0-9]', ['a', '9', '-'])

# %% cell_style="center"
# pour insérer un '-', on peut par exemple le mettre à la fin
match_all('[0-9+-]', ['0', '+', '-', 'A'])

# %% [markdown] tags=[]
# ### idem mais complémenté : `[^..]`
#
# si l'ensemble de caractères entre `[]` commence par un `^`, alors cela désigne le **complémentaire** dans l'espace des caractères

# %% tags=["gridwidth-1-2"]
# complémentaires
match_all('[^a-z]', ['a', '0', '↑', 'Θ'])

# %% tags=["gridwidth-1-2"]
match_all('[^a-z0-9]', ['a', '9', '-', 'Θ'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### 0 ou plusieurs occurrences : `..*`
#
# en ajoutant `*` après un pattern, cela signifie 0 ou plus occurrences de ce pattern  
# on en a vu un exemple déjà avec `a*`, mais le pattern peut être arbitrairement complexe

# %% tags=["gridwidth-1-2"]
# toutes les lettres au début de la chaine
match_all('[a-z]*', ['', 'abc', 'xyz9'])

# %% tags=["gridwidth-1-2"]
# toutes les suites de 'ab' au début de la chaine

match_all('(ab)*', ['', 'ab', 'abcd', 'abab'])

# %% [markdown]
# ````{admonition} utilisez les parenthèses !
#
# le `*` s'applique au (bout de) pattern immédiatement à sa gauche  
# on peut avoir à **utiliser des parenthèses** si nécessaire
# ````

# %% tags=[]
# ici l'étoile s'applique seulement au 'b'

match_all('ab*', ['a', 'abb', 'abab', 'baba'])

# %% cell_style="center"
# si je veux qu'il s'applique à 'ab', je mets des parenthèses

match_all('(ab)*', ['a', 'abb', 'abab', 'baba'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### 1 ou plusieurs occurrences : `..+`
#
# exactement comme `*`, sauf qu'il faut au moins une occurrence cette fois

# %% tags=["gridwidth-1-2"]
match_all('[a-z]+', ['', 'abc', 'xyz9'])

# %% tags=["gridwidth-1-2"]
match_all('(ab)+', ['', 'ab', 'abcd', 'abab'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### concaténation
#
# ensuite, et de manière très naturelle, quand on concatène deux filtres, la chaine doit matcher l'un puis l'autre, évidemment

# %% tags=["gridwidth-1-2"]
# c'est le seul mot qui matche
match_all('ABC', ['ABC']) 

# %% tags=["gridwidth-1-2"]
match_all('A*B', ['B', 'AB', 'AAB', 'AAAB']) 

# %% [markdown]
# ### groupement : `(..)`
#
# les parenthèses sont très utiles, on l'a déjà vu à l'instant avec notre exemple `(ab)*`  
# il faut savoir aussi que cela définit un **groupe** qui peut être retrouvé dans le match  
# notamment grâce à la méthode `groups()`
#
# ````{admonition} très utile !
# :class: tip
#
# c'est notamment comme ça qu'on peut retrouver des morceaux dans une chaine
# ````
#
# ````{admonition} dans quel ordre ?
#
# dans cette forme simple les groupes sont anonymes, et on les retrouve par leur rang, i.e. l'ordre dans lequel apparaissent les parenthèses ouvrantes
# ````

# %% tags=[]
# ici on a deux groupes
pattern = "([a-z]+)=([a-z0-9]+)"

# cette chaine a bien la bonne forme
string = "foo=barbar99"

# la preuve
match = re.match(pattern, string)
match

# %% tags=[]
# et si on veut ensuite extraire de la chaine
# les deux parties (la variable et la valeur)
# on les a ici, dans l'ordre où apparaissent les groupes
match.groups()

# %% [markdown]
# ````{admonition} on peut aussi nommer les groupes
# :class: admonition-small
#
# en général on n'aime pas trop l'idée de coder avec le rang du groupe (c'est fragile)  
# on verra plus bas comment, pour éviter ça, on peut les nommer
# ````

# %% [markdown]
# ### alternative : `..|..`
#
# pour filtrer avec une regexp **ou** une autre  
# ça se complique un peu, attention à bien lire les choses 

# %% tags=[]
# 'ab' ou 'cd'

match_all('ab|cd', ['ab', 'cd', 'abcd'])

# %% tags=[]
# 'ab' ou 'cd*'

match_all('ab|cd*', ['ab', 'c', 'cd', 'cdd'])

# %% tags=[]
# 'ab' ou '(cd)*'

match_all('ab|(cd)*', ['ab', 'c', 'cd', 'cdd'])

# %% tags=[]
# 0 ou + occurrences de (ab ou cd)

match_all('(ab|cd)*', ['ab', 'c', 'cd', 'cdd', 'abcd'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### 0 ou 1 occurrences : `..?`
#
# très pratique pour les morceaux optionnels

# %% tags=["gridwidth-1-2"]
# 0 ou 1 caractère

match_all('[a-z]?', ['', 'b', 'xy'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### nombre d'occurrences dans un intervalle : `..{n,m}`
#
# * `a{3}` : exactement 3 occurrences de `a`
# * `a{3,}` : au moins 3 occurrences
# * `a{3,6}` : entre 3 et 6 occurrences
#
# ````{admonition} bien sûr
# le `a` peut bien sûr être n'importe quelle regexp compliquée hein
# ````

# %% cell_style="center"
# entre 1 et 3 occurrences de 'ab'

match_all('(ab){1,3}', ['', 'ab', 'abab', 'ababab', 'ababababababab'])

# %% [markdown] slideshow={"slide_type": ""}
# ### classes de caractères `\s` etc..
#
# raccourcis qui filtrent **un caractère** dans une classe  
# définis en fonction de la configuration de l'OS en termes de langue
#
# * `\s` (pour Space) : exactement un caractère de séparation (typiquement Espace, Tabulation, Newline)
# * `\w` (pour Word) : exactement un caractère alphabétique ou numérique
# * `\d` (pour Digit) : un chiffre
# * `\S`, `\W` et `\D` : les complémentaires

# %% tags=["gridwidth-1-2"]
match_all('\w+', ['eFç0', 'été', ' ta98'])

# %% tags=["gridwidth-1-2"]
match_all('\s?\w+', ['eFç0', 'été', ' ta98'])

# %% [markdown] slideshow={"slide_type": ""}
# ### groupe nommé : `(?P<name>..)`
#
# pour obtenir le même effet que les groupes anonymes `(..)`  
# mais en leur donnant un nom pour que la recherche soit moins fragile

# %% cell_style="center"
# la même regexp essentiellement que tout à l'heure 
# mais avec deux groupes nommés cette fois
pattern = "(?P<variable>[a-z]+)=(?P<valeur>[a-z0-9]+)"

string = "foo=barbar99"

match = re.match(pattern, string)
match

# %% tags=[]
# et c'est plus lisible pour aller extraire les morceaux

match.group('variable'), match.group('valeur')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### début et fin de chaine : `^` et `$`
#
# parfois on veut s'assurer qu'on filtre bien toute la chaine, pour cela on peut le préciser avec ces deux marques
#
# ````{admonition} signes équivalents
#
# pour info, on peut aussi utiliser respectivement `\A` et `\Z`
# ````

# %% cell_style="center"
# le comportement par défaut de match()

match_all('ab|cd', ['ab', 'abcd'])

# %%
# pour forcer la chaine à matcher jusqu'au bout
# on ajoute un $ 

match_all('(ab|cd)$', ['ab', 'abcd'])

# %% [markdown] slideshow={"slide_type": ""}
# ### plusieurs occurrences d'un groupe : `(?P=name)`
#
# on peut aussi spécifier que **le même groupe** apparaisse plusieurs fois  

# %%
# la deuxième occurrence de <nom> doit être la même que la première
pattern = r'(?P<nom>\w+).*(?P=nom)'

string1 = 'Jean again Jean'
string2 = 'Jean nope Pierre'

match_all(pattern, [string1, string2])

# %% [markdown]
# ## quelques conseils
#
# * chez certaines personnes, il y a un avant et un après les expressions régulières  
#   je ne veux pas vous refroidir, mais ça n'est très **clairement pas** un outil à utiliser **à tour de bras** !
# * dès que ça devient un tout petit peu compliqué, pensez à utiliser un testeur en ligne, vous gagnerez du temps  
#   <https://pythex.org>  
#   <https://regex101.com/> (bien choisir Python)
#   ... et plein d'autres ...  

# %% [markdown] slideshow={"slide_type": ""}
# ## pour aller plus loin
#
# * un peu de détente, avec ce jeu de mots croisés basé sur les regexps  
#   <https://regexcrossword.com>
# * vous avez de quoi commencer avec un solide bagage; toutefois il y a encore beaucoup d'autres possibilités, notamment les options de compilation (pour ignorer la chasse par exemple, et j'en passe..) n'hésitez pas à lire le guide introductif dans la doc
#   <https://docs.python.org/fr/3/howto/regex.html>
# * enfin il y a aussi un tour complet de la syntaxe des regexps  
#   <https://docs.python.org/fr/3/library/re.html#regular-expression-syntax>

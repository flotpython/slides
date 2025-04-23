---
celltoolbar: Slideshow
jupytext:
  encoding: '# -*- coding: utf-8 -*-'
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
language_info:
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
nbhosting:
  title: "s\xE9quences et chaines"
---

+++ {"slideshow": {"slide_type": ""}}

# séquences & chaines

+++ {"slideshow": {"slide_type": "slide"}}

## c'est quoi une séquence ?

+++ {"tags": ["gridwidth-1-2"]}

* suite finie et ordonnée d'objets
* du coup indexable, on peut écrire `S[n]`
  * en Python, les **indices commencent à 0**
* peuvent contenir des duplications

+++ {"tags": ["gridwidth-1-2"]}

les séquences dans le langage Python (entre autres):

* mutable
  * `list`, `bytearray`
* immutable
  * `str`, `bytes`, `tuple`, `range`

+++

````{admonition} les chaines (str) sont des séquences
:class: info

nous allons voir pour commencer des choses valables **sur toutes les séquences**,
et donc en particulier sur les chaines de caractères, puisque les chaines sont des séquences
````

+++ {"slideshow": {"slide_type": "slide"}}

## fonctions sur toutes les séquences

+++

### indexation, longueur

* `S[i]`
  * retourne l’élément d'indice i
* `len(S)`
  * donne la taille en nombre d’éléments

+++ {"tags": []}

### les séquences sont des itérables

un itérable en Python, c'est un objet sur lequel on peut faire un `for`

```python
for item in S:
    # do something with item
```

+++

### concaténation, comparaisons

* `S + T`
 * retourne une nouvelle séquence qui est la concaténation de S et T
* `S*n` ou `n*S`
  * retourne une nouvelle séquence qui est la concaténation de n *shallow* copies de S
* `sum(S)` (resp. `min(S)` et `max(S)`)
  * retourne la somme des éléments de S (resp. le plus petit, le plus grand)

  ````{admonition} en fait sur tous les itérables
  :class: admonition-small
    
  en fait les fonctions `sum`, `min` et `max` s'appliquent à n'importe quel itérable  
  toutes les séquences sont des itérables, mais tous les itérables ne sont pas des séquences  
  la famille des itérables est donc plus large que les séquences
  ````

+++ {"slideshow": {"slide_type": ""}}

### appartenance, recherches

* `x in S`; selon les types:
  * `True` si un élément de S est égal à x  
    (e.g. S est une `list`)

  * `True` si S contient x  
    (e.g. S est une `str`)

* diverses méthodes (voir docs):
  * `S.count(a)`
    * retourne le nombre d’occurrences de a dans S
  * `S.index(a)`, `S.find(a)`  
    retourne l’indice de la première occurrence de a dans S

+++

## slicing

* `S[i:j]` retourne
  * une nouvelle séquence de même type
  * contenant tous les éléments de l’indice i à l’indice j-1
* `S[i:j:k]` retourne
  * une nouvelle séquence de même type
  * prenant tous les éléments de l’indice i à l’indice j-1,
  * par sauts de k éléments
* les indices `i`, `j` et `k` peuvent être négatifs

voyons des exemples de tout ceci

````{admonition} slicing et numpy
:class: info

la notion de slicing est **très massivement utilisée** dans toutes les librairies numériques, notamment en `numpy`
````

+++ {"tags": ["gridwidth-1-2"]}

### indices omis et négatifs

* omettre les bornes
* compter depuis la fin, avec un indice négatif

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["gridwidth-1-2"]}

```{image} media/egg-bacon.svg
:align: center
:width: 450px
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s = "egg, bacon"
s[0:3]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# si on omet une borne
# ce sera le début ..
s[:3]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ... ou la fin:
s[5:]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# les indices peuvent être négatifs
s[-3:10]
```

```{code-cell} ipython3
# tout entier: une shallow-copy
s[:]
```

+++ {"slideshow": {"slide_type": ""}, "tags": ["gridwidth-1-2"]}

### les bornes

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["gridwidth-1-2"]}

```{image} media/egg-bacon-bornes.svg
:align: center
:width: 450px
```

+++ {"tags": ["gridwidth-1-2"]}

La convention est choisie pour pouvoir facilement "encastrer" les slices:

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[0:3]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[3:6]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[6:]
```

```{code-cell} ipython3
:tags: []

s[0:3] + s[3:6] + s[6:] == s
```

+++ {"tags": ["gridwidth-1-2"]}

### le pas

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["gridwidth-1-2"]}

```{image} media/egg-bacon.svg
:align: center
:width: 450px
```

+++ {"tags": ["gridwidth-1-2"]}

* on peut préciser un pas
* qui peut aussi être négatif
* ou omis (défaut 1)

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[0:10:2]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[::2]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[:8:3]
```

```{code-cell} ipython3
:tags: []

s[-2::-3]
```

+++ {"tags": ["gridwidth-1-2"]}

### pas d'exception

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["gridwidth-1-2"]}

```{image} media/egg-bacon.svg
:align: center
:width: 450px
```

+++ {"tags": []}

les slices ont un comportement plus permissif que l'indexation

```{code-cell} ipython3
# Si j'essaie d'utiliser un index inexistant
try: s[100]
except Exception as e: print("OOPS", e)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# par contre avec un slice, pas de souci
s[5:100]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# vraiment..
s[100:200]
```

+++ {"tags": ["gridwidth-1-2"]}

### exemples

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["gridwidth-1-2"]}

```{image} media/egg-bacon.svg
:align: center
:width: 450px
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[-1]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[-3:-1]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[:-3]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[::-1]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[2:0:-1]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[2::-1]
```

+++ {"slideshow": {"slide_type": "slide"}}

### formes idiomatiques

+++ {"tags": []}

s = [1, 2, 3]

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# une copie simple
s[:]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# copie renversée
s[::-1]
```

## `str` pour manipuler du texte

* le type `str` est un cas particuliers de **séquence**
* qui permet de manipuler **du texte**

````{admonition} un caractère ce **n'est pas** un octet
:class: warning

avec l'encodage le plus répandu aujourd'hui (UTF-8), les caractères ASCII tiennent sur un octet  
mais **ce sont les seuls**: un `é` par exemple occupe 2 octets; un `‰` occupe 3 octets; un `🚀` occupe 4 octets

si vous avez besoin de manipuler des données brutes - typiquement si vous lisez un fichier binaire - il vous faut utiliser le type `bytes` que nous verrons plus tard
````

+++

### écrire une str de manière littérale

* une chaîne de caractères est définie de manière équivalente par des simples ou doubles guillemets (`'` ou `"`)
* on peut ainsi facilement inclure un guillemet

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# une chaine entre double quotes
# pas de souci pour les accents
print("c'est l'été")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# entre simple quotes
print('on se dit "pourquoi pas"')
```

### sur plusieurs lignes

* pour écrire une chaîne sur plusieurs lignes on utilise `"""` ou `'''`

```{code-cell} ipython3
:cell_style: center

# bien sûr ici vous pouvez remplacer les """ par '''

print("""et pour entrer plusieurs lignes,
ou bien des chaines avec des " et des '
c'est facile aussi""")
```

### chaînes de caractères accolées

* lorsque vous voulez entrer une chaine un peu longue
* vous pouvez **simplement accoler** deux chaines dans votre source:

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s = "le début" " et la fin"
print(s)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s = ("une chaine trop longue"
     " pour tenir sur une ligne")
print(s)
```

````{admonition} les parenthèses sont importantes
:class: warning

notez bien les parenthèses dans ce deuxième exemple, car sinon c'est une erreur de syntaxe
````

+++ {"tags": []}

### échappements dans les chaines

* le caractère `\` a un sens particulier dans les chaines écrites de manière littérale dans le programme
* on écrit un retour chariot avec un `\n`
* une tabulation avec `\t`
* les guillemets peuvent être échappés (e.g. pour entrer un `'` dans une chaine délimitée avec un `'`)
* un backslash avec `\\`
* enfin on peut aussi entrer des caractères exotiques par leur codepoint avec 
  * `\x` `\u` `\U`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s = "deux\nlignes"
print(s)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s = 'des\ttrucs\tespacés'
print(s)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# imaginons qu'on ait les deux sortes de guillemets
s = "simple' double\""
print(s)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s = 'backslash \\\tquote \''
print(s)
```

+++ {"slideshow": {"slide_type": "slide"}}

### *raw-strings*

+++ {"tags": ["gridwidth-1-2"]}

voici un problème commun, surtout sous Windows:

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s = 'C:\Temp\test.txt'
print(s)
```

+++ {"cell_style": "center"}

* `\T` n’existe pas comme échappement; Python interprète correctement `\T`
* mais `\t` est compris comme une tabulation !!

````{admonition} Python-3.12
:class: note admonition-small

il semble même qu'en 3.12, un `\T` dans une chaine provoque carrément une erreur de syntaxe - ce qui est sans doute mieux au sens où au moins on détecte l'erreur plus tôt...
````

+++

pour résoudre ce problème, on peut utiliser des double-backslash `\\`, mais ce n'est vraiment pas élégant  
la bonne solution consiste à utiliser une "raw string", dans laquelle les backslash ne sont *pas interprétés*

```{code-cell} ipython3
# pour créer une raw-string, simplement faire précéder le string d'un 'r'

s = r'C:\Temp\test1.bin'

print(s)
```

````{admonition} préférez le / pour les chemins de fichier

notez que le plus souvent, vous pouvez aussi bien utiliser un `/` au lieu d'un `\` dans les chemins de fichiers sous Windows, ce qui résoud tous les problèmes d'échappement

les *raw-strings* restent une feature bien pratique dans d'autres contextes, notamment avec les expressions régulières, que nous n'avons pas pu utiliser comme exemple ici puisqu'on n'en a pas encore parlé..
````

+++

### *docstrings*

une *docstring* est une chaine littérale insérée **au tout début** du code d'une fonction (ou classe ou module) et qui sert à la documenter  
on utilise souvent les triples guillemets pour cela

```{code-cell} ipython3
:tags: [gridwidth-1-2]

def double(n):
    """
    Returns the double of its input parameter

    The help message usually spans several lines
    """
    return 2*n
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

help(double)
```

+++ {"slideshow": {"slide_type": "slide"}}

## opérations sur les `str`

+++ {"slideshow": {"slide_type": "slide"}}

### toutes les opérations des séquences

que l'on a déjà vues :

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s1 = 'abcdéfg'
s2 = 'bob'
len(s1)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# concaténation
s1 + s2
'abcdefbob'
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# slicing
s1[-1::-2]
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

'=' * 30
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# est-ce une sous-chaine ?
'cdé' in s1
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# à quelle position ?
s1.index('cdé')
```

### objet `str` non mutable

par contre **ATTENTION** un `str` n'est **pas mutable**

```{code-cell} ipython3
try:
    s1[2] = 'x'
except TypeError as e:
    print("OOPS", e, type(e))
```

+++ {"cell_style": "center", "slideshow": {"slide_type": "slide"}}

## méthodes sur les `str`

+++

### `strip()`

```{code-cell} ipython3
# j'ai lu une chaine dans un fichier
# je ne sais pas trop s'il y a des espaces à la fin
# et si la chaine contient un newline

dirty = "  des blancs au début et à la fin et un newline  \n"
dirty
```

```{code-cell} ipython3
# c'est la méthode la plus simple pour nettoyer
dirty.strip()
```

````{admonition} utilisez rstrip() pour nettoyer les lignes lues dans un fichier
:class: info admonition-smaller

lorsqu'on nettoie une ligne qu'on a lue dans un fichier, on peut envisager
d'utiliser `rstrip()` qui ne nettoie qu'à droite, là où se situe le NEWLINE
````

+++ {"slideshow": {"slide_type": "slide"}}

### `split()` et `join()`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# une chaine à découper
s = "une phrase\nsur deux lignes"
s
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# sans argument, split
# découpe selon les espaces
# et tabulations et newline
liste = s.split()
liste
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# recoller les morceaux
"".join(liste)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# le plus souvent
" ".join(liste)
```

```{code-cell} ipython3
# ou n'importe quel autre séparateur
"+++".join(liste)
```

+++ {"slideshow": {"slide_type": "slide"}}

### remplacements, recherches

```{code-cell} ipython3
s = "une petite phrase"
s.replace('petite', 'grande')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# l'index du premier caractère
s.find('hra')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s[12]
```

#### et plein d'autres..

* de nombreuses méthodes disponibles
* personne ne retient l'intégralité des méthodes sur les types de base
* le bon réflexe : chercher dans la dos Python qui est très bien faite
* google les simples mots clés 'python str', vous trouvez
* <https://docs.python.org/3/library/stdtypes.html>

+++ {"tags": ["level_advanced"]}

## un peu d'introspection (avancé)

disons qu'on voudrait savoir combien de méthodes sont disponibles sur les chaines.

```{code-cell} ipython3
:tags: [level_advanced, gridwidth-1-2]

type("abc")
```

```{code-cell} ipython3
:tags: [level_advanced, gridwidth-1-2]

str
```

```{code-cell} ipython3
:tags: [level_advanced]

# 'str' est une variable prédéfinie, qui référence
# le type (la classe) de toutes les chaines
type("abc") is str
```

```{code-cell} ipython3
:tags: [level_advanced]

# du coup son type, c'est .. le type <type>
type(str)
```

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_advanced"]}

### un peu d'introspection...

```{code-cell} ipython3
:tags: [level_advanced]

# peu importe... quoi qu'il en soit, dir(str) retourne la liste
# des noms de méthodes connues sur cette classe;
# regardons par exemple les premiers et les derniers
dir(str)[:2], dir(str)[-2:]
```

```{code-cell} ipython3
:tags: [level_advanced, gridwidth-1-2]

# avec len() je peux savoir combien il y en a
len(dir(str))
```

```{code-cell} ipython3
:tags: [level_advanced, gridwidth-1-2]

# mais en fait, pour un décompte significatif
# on enlève celles dont le nom contient `__`
methods = [method for method in dir(str)
           if '__' not in method]
len(methods)
```

```{code-cell} ipython3
:tags: [level_advanced]

# est-ce que les chaines ont une méthode 'split' ?
'split' in methods
```

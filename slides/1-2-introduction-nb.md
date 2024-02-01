---
celltoolbar: Slideshow
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  encoding: '# -*- coding: utf-8 -*-'
  notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
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
  title: "g\xE9n\xE9ralit\xE9s"
rise:
  slideNumber: c/t
  start_slideshow_at: selected
  theme: sky
  transition: cube
---

+++ {"slideshow": {"slide_type": "slide"}}

<div class="licence">
<span>Licence CC BY-NC-ND</span>
<span>Thierry Parmentelat &amp; Arnaud Legout</span>
</div>

+++

# généralités


> *Python3 : des fondamentaux à l'utilisation du langage*

+++ {"cell_style": "center"}

> version de référence: python-3.10

+++ {"slideshow": {"slide_type": "slide"}}

## pourquoi Python ?

+++

* syntaxe simple
  * pas de délimitations  `begin end ; {} `
  * uniquement des indentations
  * aucune ambiguïté
  * une seule façon d’écrire
* portable
  * Windows, Linux, Mac OS, etc.
* typage dynamique
  * pas de perte de temps à l'écriture des programmes

+++ {"slideshow": {"slide_type": "slide"}}

### pourquoi Python ?  : lisible

```{code-cell} ipython3
# le sucre syntaxique réduit au minimum
# c'est un partis-pris de conception
# le code est lisible par construction
def factorielle(n):
    return 1 if n <= 1 else n * factorielle(n-1)
```

```{code-cell} ipython3
factorielle(0)
```

```{code-cell} ipython3
factorielle(8)
```

````{admonition} trop court ?
:class: seealso

bien sûr on peut aussi écrire de façon plus bavarde si on préfère, comme par ex.

```python
def factorielle(n):
    if n <= 1:
        return 1
    else:
        return n * factorielle(n-1)
```

````

+++ {"slideshow": {"slide_type": "slide"}}

### pourquoi Python ? : puissant

+++

* types disponibles très puissants et flexibles
  * entiers non bornés, nombres complexes
  * listes, strings Unicode
  * tables de hash: dictionnaires et ensembles
  * langage orienté objet: définir ses propres types
* énorme base de librairies
  * et s’interface facilement avec C et C++
  * et donc du code **efficace**
* gestion de la mémoire automatique
  * GC

+++ {"slideshow": {"slide_type": "slide"}}

### pourquoi Python ? : pas de compilation

+++

* langage interprété
* script direct en ligne de commande
* REPL: usage interactif (ipython / notebook)
* pré-compilation en byte-code des programmes (.pyc)
  * totalement transparent
  * mais pas optimisé comme du code machine  
    compilé à partir de C

+++ {"slideshow": {"slide_type": "slide"}}

### pourquoi python ? : ouvert et gratuit

+++

## la Python Software Foundation (PSF)

possède les droits sur Python et assure son développement

* essentiellement aucune restriction sur le code Python et son usage, même commercial
* https://docs.python.org/3/license.html

+++ {"slideshow": {"slide_type": "slide"}}

### philosophie python

```{code-cell} ipython3
import this
```

+++ {"slideshow": {"slide_type": "slide"}}

## quand utiliser python ?

+++

* scripts (mais pas **uniquement** ça!)
* programmation système
* Internet
* base de données
* prototypage rapide
* calcul scientifique avec `numpy`
* exploration dans les données avec `pandas` et `scikit-learn`
* backend web avec `Django` / `Flask`
* …

+++ {"slideshow": {"slide_type": "slide"}}

### quand ne pas utiliser Python ?

+++

* Python est **plutôt gourmand en mémoire**
  * tout est objet ➔ surcoût partout
  * exemples sur une machine 64 bits

|      objet     |   octets  | natif C |
|----------------|-----------|---------|
| petit entier   | 28 octets |8 octets|
| chaine 'a'     | 50 octets |1 octet|
| chaine 'é'     | 74 octets |2 octets|

* Python plutôt bon en termes de vitesse
  * fonctions de base implémentées en C optimisé
  * PyPy très rapide par rapport à CPython
  * pensez à utiliser `numpy`

+++ {"slideshow": {"slide_type": "slide"}}

### quand ne pas utiliser python ?

+++

**comment prendre la décision d’utiliser Python ?**

* balancer vitesse de développement avec performance
* Python gagne presque toujours

+++ {"slideshow": {"slide_type": "slide"}}

### comment tester la performance ?

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
---
%%timeit

# on construit la liste des premiers carrés
[x**2 for x in range(10000)]
```

````{admonition} attention
:class: attention

cette construction avec les `%` n'est pas standard Python, c'est une *magic* de IPython  
on ne peut l'utiliser que dans `ipython` ou dans les notebooks
````

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_intermediate"]}

### comment tester la place mémoire ?

```{code-cell} ipython3
---
cell_style: split
slideshow:
  slide_type: ''
tags: [level_intermediate]
---
# retourne le nombre d'octets
# utilisés pour stoker un objet

import sys
sys.getsizeof([10])
```

```{code-cell} ipython3
:cell_style: split
:tags: [level_intermediate]

sys.getsizeof([10, 20])
```

```{code-cell} ipython3
:tags: [level_intermediate]

sys.getsizeof([10, 20, 30])
```

+++ {"slideshow": {"slide_type": "slide"}}

## quelle version de python ?

+++

* version 3.x
  * conseil: ne pas utiliser un trait spécifique à la toute dernière version pour du code à large diffusion
  * minimum recommandé 3.8

* ~~version 2.7~~
  * **surtout ne pas utiliser !**
  * en fin de vie - supporté jusque 1er janvier 2020
  * de moins en moins problématique (mais attention sur MacOS)

+++ {"slideshow": {"slide_type": "slide"}}

## documentation

+++

personnellement, pour un accès rapide à la documentation, je fais très facilement une recherche google genre

> python module datetime

+++

````{admonition} le plus simple: chercher sur google
:class: tip

que l'on peut consulter aussi comme ceci <https://www.google.com/search?q=python+module+datetime>

````

+++ {"slideshow": {"slide_type": "slide"}}

### fourni avec Python

* site officielle de la doc Python
  * <https://docs.python.org/>
  * aussi en français ici <https://docs.python.org/fr/3/>
  * très riche: du tutoriel à la description du langage
* contient notamment le Python tutorial
  * <https://docs.python.org/3/tutorial/>
  * initialement Guido van Rossum
  * niveau débutant à moyen

+++ {"slideshow": {"slide_type": "slide"}}

### des cours

* [MOOC Python : des fondamentaux à l'utilisation du langage](https://www.fun-mooc.fr/fr/cours/python-3-des-fondamentaux-aux-concepts-avances-du-langage/)
  * A. Legout et T. Parmentelat
* [MOOC : apprendre à coder en Python](https://www.fun-mooc.fr/en/cours/apprendre-a-coder-avec-python/)
  un peu plus simple
* http://fr.openclassrooms.com/informatique/cours/apprenez-a-programmer-en-python
* et sans doute des dizaines d'autres

+++ {"slideshow": {"slide_type": "slide"}}

### et aussi

* l'incontournable stackoverflow (SO)
  * <https://stackoverflow.com/questions/tagged/python+python-3.x>
  * on peut directement chercher sur Google

* enfin pour ceux qui aiment les *cheat sheet*
  * <https://perso.limsi.fr/pointal/python:memento>

+++ {"slideshow": {"slide_type": "slide"}}

## comment lancer python ?

+++

### depuis un terminal ...

* taper `python` dans le terminal
  * interpréteur en ligne de commande
* en option, `ipython` en remplacement
  * nécessite une installation supplémentaire
  * `pip install ipython`

+++

````{admonition} pour installer des librairies depuis le web (pypi.org)
:class: tip

dans le terminal toujours:

* `pip install mylibrary` est la façon standard d'installer une librairie externe  
* `python -m pip install mylibrary` est équivalent, et parfois plus approprié, notamment en cas d'installation biscornue

````

+++ {"slideshow": {"slide_type": "slide"}, "cell_style": "center"}

```{image} ../media/python-ipython-in-terminal.png
:width: 600px
```

+++ {"slideshow": {"slide_type": "slide"}}

### ... ou dans un environnement graphique

+++ {"cell_style": "center"}

* **Jupyter notebooks**
  * `pip install jupyterlab`
  * `jupyter lab`
* IDE de votre choix (**vs-code**, PyCharm, SublimeText,  
  atom, eclipse, ... bcp de variantes)

+++ {"cell_style": "split"}

dans tous les cas,  
faites un premier test:

```{code-cell} ipython3
:cell_style: split

100 * 100
```

````{admonition} important
:class: important 

il faut savoir interrompre/redémarrer son interpréteur !  
par exemple dans `jupyter lab` voyez le menu `Kernel`
````

+++ {"slideshow": {"slide_type": "slide"}}

## comment avoir de l'aide: `dir`

+++

* `dir(objet)`
  * retourne les attributs d'un objet
  * utile notamment sur un module

```{code-cell} ipython3
:cell_style: center

import math
dir(math)
```

+++ {"slideshow": {"slide_type": "slide"}}

### comment avoir de l’aide ?

+++ {"slideshow": {"slide_type": "-"}}

* `help(objet)`
  * retourne une aide en ligne sur l’objet
  * utile sur fonctions, méthodes, classes, modules
  * fonctionne dans tous les environnements

```{code-cell} ipython3
:cell_style: split

# sur tout un module
help(math)
```

```{code-cell} ipython3
:cell_style: split

# ou juste une fonction
help(math.factorial)
```

+++ {"slideshow": {"slide_type": "slide"}}

## aide IPython (et notebooks)

+++

* pour obtenir de l'aide dans une fenêtre dédiée avec `?`
* le symbole doit être connu de python

````{admonition} ne marche que avec ipython et les notebooks
:class: attention

comme pour les `%` qu'on a vus un peu plus haut, cette notation avec le `?` ne fonctionne pas dans le python "de base"  
il faut être soit dans IPython, soit dans un notebook
````

```{code-cell} ipython3
:cell_style: split

math?
```

```{code-cell} ipython3
:cell_style: split

math.factorial?
```

+++ {"slideshow": {"slide_type": "slide"}}

### aide IPython (et notebooks) (2)

+++

utiliser `TAB` pour la complétion

```{code-cell} ipython3
# ditto, il faut avoir chargé le module
# **avant** de pouvoir utiliser la complétion
from sklearn import tree
```

utiliser le clavier pour sélectionner

```{code-cell} ipython3
# tree.<taper TAB>
```

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_intermediate"]}

### aide IPython (et notebooks) (3)

+++ {"tags": ["level_intermediate"]}

avec un double `??` on peut avoir accès au code source

```{code-cell} ipython3
:tags: [level_intermediate]

# bien sûr il faut avoir **évalué** l'import
from argparse import ArgumentParser
```

```{code-cell} ipython3
:tags: [level_intermediate]

# avant de pouvoir instrospecter l'objet ArgumentParser
ArgumentParser??
```

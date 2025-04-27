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
  title: "g\xE9n\xE9ralit\xE9s"
---

# généralités

````{admonition} Programmer en Python !

  ```{admonition} Version de référence
:class: attention
Python-3.10
```

ou disons plutôt, c'est le minimum requis pour ce cours :)
````

+++

## pourquoi Python ?

* **conçu pour être lisible**, syntaxe simple
  * pas de délimitations  `begin end ; {} `
  * uniquement des indentations
  * la lisibilité fait partir de l'ADN du langage
* typage dynamique
  * pas de perte de temps à l'écriture des programmes
* portable
  * Windows, Linux, Mac OS, etc.

+++ {"slideshow": {"slide_type": "slide"}}

### pourquoi Python ?  : lisible

```{code-cell} ipython3
# le sucre syntaxique est réduit au minimum
# c'est un partis-pris de conception
# le code est lisible par construction

def factorielle(n):
    if n <= 1:
        return 1
    else:
        return n * factorielle(n-1)
```

```{code-cell} ipython3
factorielle(0)
```

```{code-cell} ipython3
factorielle(8)
```

````{admonition} trop long ?
:class: seealso dropdown

bien sûr on peut aussi écrire de façon plus concise si on préfère, comme par ex.

```python
def factorielle(n):
    return 1 if n <= 1 else n * factorielle(n-1)
```

````

+++

### pourquoi Python ? : puissant (*batteries included*)

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

+++

### pourquoi Python ? : pas de compilation

* langage interprété
* script direct en ligne de commande
* REPL: usage interactif (ipython / notebook)
* pré-compilation en byte-code des programmes (.pyc)
  * totalement transparent
  * mais pas non plus optimisé comme du code machine..

+++ {"slideshow": {"slide_type": "slide"}}

### pourquoi python ? : ouvert et gratuit

notamment toutes les discussions sont en ligne et hébergées sur un site *discourse* ici  
<https://discuss.python.org/>  
notamment, si vous êtes intéressé aux évolutions du langage:  
<https://discuss.python.org/c/ideas/6>

+++

## la Python Software Foundation (PSF)

possède les droits sur Python et assure son développement

* essentiellement aucune restriction sur le code Python et son usage, même commercial
* <https://docs.python.org/3/license.html>  
  adapté à un très vaste spectre d'usages

+++ {"slideshow": {"slide_type": "slide"}}

### philosophie python

```{code-cell} ipython3
# le zen de Python est capturé dans un module idoine

import this
```

## quand utiliser python ?

* scripts (mais pas **uniquement** ça!)
* programmation système
* Internet
* base de données
* prototypage rapide
* calcul scientifique avec `numpy`
* exploration dans les données avec `pandas` et `scikit-learn`
* backend web avec `Django` / `Flask`
* …

+++

### quand ne pas utiliser Python ?

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

+++

### comment prendre la décision d’utiliser Python ?

* balancer vitesse de développement avec performance
* Python gagne presque toujours

+++ {"slideshow": {"slide_type": "slide"}}

### comment tester la performance ?

```{code-cell} ipython3
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
:tags: [level_intermediate, gridwidth-1-2]

# retourne le nombre d'octets
# utilisés pour stoker un objet

import sys
sys.getsizeof([10])
```

```{code-cell} ipython3
:tags: [level_intermediate, gridwidth-1-2]

sys.getsizeof([10, 20])
```

```{code-cell} ipython3
:tags: [level_intermediate]

sys.getsizeof([10, 20, 30])
```

## quelle version de python ?

* version 3.x
  * conseil: ne pas utiliser un trait spécifique à la toute dernière version pour du code à large diffusion
  * minimum recommandé 3.10

* {del}`version 2.7`
  * **surtout ne pas utiliser !**
  * en fin de vie - supporté jusque 1er janvier 2020
  * de moins en moins problématique (mais attention sur MacOS)

+++

## documentation

personnellement, pour un accès rapide à la documentation, je fais très facilement une recherche google genre

> python module datetime

````{admonition} le plus simple: chercher sur google
:class: tip

que l'on peut consulter aussi comme ceci  
<https://www.google.com/search?q=python+module+datetime>

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

````{admonition} pour installer des librairies depuis le web (pypi.org)
:class: tip

dans le terminal toujours:

* `pip install mylibrary` est la façon standard d'installer une librairie externe  
* `python -m pip install mylibrary` est équivalent, et parfois plus approprié, notamment en cas d'installation biscornue

````

```{image} ../media/python-ipython-in-terminal.png
:width: 600px
```

+++ {"slideshow": {"slide_type": "slide"}}

### ... ou dans un environnement graphique

+++

* **Jupyter notebooks**
  * `pip install jupyterlab`
  * `jupyter lab`
* IDE de votre choix (**vs-code**, PyCharm, SublimeText,  
  atom, eclipse, ... bcp de variantes)

+++ {"tags": ["gridwidth-1-2"]}

dans tous les cas,  
faites un premier test:

```{code-cell} ipython3
:tags: [gridwidth-1-2]

100 * 100
```

````{admonition} important
:class: important 

il faut savoir interrompre/redémarrer son interpréteur !  
par exemple dans `jupyter lab` voyez le menu `Kernel`
````

+++ {"slideshow": {"slide_type": "slide"}}

## comment avoir de l'aide

### `dir()`

+++

* `dir(objet)`
  * retourne les attributs d'un objet
  * utile notamment sur un module

```{code-cell} ipython3
import math
dir(math)
```

+++ {"slideshow": {"slide_type": "slide"}}

### `help()`

+++ {"slideshow": {"slide_type": "-"}}

* `help(objet)`
  * retourne une aide en ligne sur l’objet
  * utile sur fonctions, méthodes, classes, modules
  * fonctionne dans tous les environnements

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# sur tout un module
help(math)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ou juste une fonction
help(math.factorial)
```

+++ {"slideshow": {"slide_type": "slide"}}

### complétion

+++

**apprenez à utiliser `<TAB>` pour la complétion!!**  
cela fait ggner un temps fou !  
et d'ailleurs pas que dans jupyter, c'est pervasif: dans le shell/terminal, dans vs-code, etc...

```{code-cell} ipython3
# tapez le début
# math.fac
# puis à ce stade taper <TAB>
# ce qui va vous aider à finir la phrase avec un mot connu
```

si votre début de phrase est trop flou, vous aurez à choisir dans une liste de possibles  
dans ce cas, utilisez le clavier pour sélectionner la bonne

```{code-cell} ipython3
# tapez ceci
# math.
# et là si vous tapez <TAB> on va vous afficher les possibilités
# c'est à dire en gros le contenu de dir(math) comme on l'a vu plus haut
# mais c'est interactif
```

+++ {"slideshow": {"slide_type": "slide"}}

### aide avec `symbol?`

+++

* pour obtenir de l'aide dans une fenêtre dédiée avec `?`
* le symbole doit être connu de python

````{admonition} ne marche que avec ipython et les notebooks
:class: attention

comme pour les `%` qu'on a vus un peu plus haut, cette notation avec le `?` ne fonctionne pas dans le python "de base"  
il faut être soit dans IPython, soit dans un notebook
````

```{code-cell} ipython3
:tags: [gridwidth-1-2]

math?
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

math.factorial?
```

### aide avec `symbol??`

avec un double `??` on peut avoir accès au code source

```{code-cell} ipython3
# bien sûr il faut avoir **évalué** l'import
from argparse import ArgumentParser
```

```{code-cell} ipython3
# avant de pouvoir instrospecter l'objet ArgumentParser
ArgumentParser??
```

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
  title: modules
---

# modules & packages

+++

## pour réutiliser du code en python

**DRY = *don't repeat yourself*** : *cut'n paste is evil*

```{list-table}

* - fonctions
  - pas d'état après exécution

* - **modules**
  - **garde l'état, une seule instance par programme**

* - classes
  - instances multiples, chacune garde l'état, héritage
```

+++

### à quoi sert un module ?

pour réutiliser du code, qui peut venir:

* de la librairie standard, e.g. `import math`
  * voir [la liste complète ici](https://docs.python.org/3/library/index.html)
* d'un package installé depuis `pypi.org` avec `pip install numpy`
  * voir PyPI - the Python Package Index - <https://pypi.org/>
* d'un fichier / dossier de votre propre application  
  de cette façon on peut couper son code en morceaux plus digestes

````{admonition} isolation des noms entre les librairies

un module, c’est principalement juste un espace de noms

c’est grâce à ces différents espaces de noms que deux fichiers `foo.py` et `bar.py` peuvent tous les deux définir la même variable `tutu` sans que ça pose le moindre problème de les utiliser tous les deux dans la même application
````

+++ {"slideshow": {"slide_type": ""}, "tags": []}

### c'est quoi un module ?

* un module est un **objet** Python, correspondant au **chargement en mémoire**  
  du code venant d'un fichier ou dossier source  
  (dans le cas d'un *dossier* on parle alors d'un *package* - on en reparlera)

* les différents composants du code sont alors accessibles **comme un attribut** du module  
  (c'est à dire les variables qui sont définis au *toplevel* dans le fichier source)


regardons ce qu'il y a dans ce fichier `mod.py`

```{literalinclude} mod.py
:linenos:
:emphasize-lines: 5, 9
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
tags: []
---
# pour utiliser ce code, je commence par l'importer

import mod
```

```{code-cell} ipython3
:cell_style: center

# ce qui a pour effet de définir la variable 'mod'
# qui désigne - en Python tout est objet -
# un objet qui est de type .. wait for it ..

mod
```

```{code-cell} ipython3
:tags: []

# et depuis cet objet là, je peux accéder via ses attributs
# aux différents morceaux du code, par exemple

mod.GLOBALE
```

```{code-cell} ipython3
:tags: []

# ou encore 

mod.spam('good')
```

````{admonition} noms de fichiers
:class: attention

puisque le nom de la variable est tiré du nom du fichier (sans le `.py`), cela signifie qu'on ne pourra pas prendre n'importe quoi comme nom de fichier; et notamment **on ne peut pas utiliser le `-`**:

* `truc_v22.py`: **OK** comme pour un module
* {del}`` `truc-bidule.py` ``: **KO** pour un module
````

+++

````{admonition} seulement les variables globales
:class: tip admonition-small

bien entendu, si la fonction `spam` avait une variable locale, elle ne serait pas visible dans le module  
la plupart du temps, ce qui eat visible dans le module, ce sont des fonctions et des classes; et parfois des constantes
````

+++

## rappel: la notion d’attribut

on l'a déjà vu, mais pour rappel

* un attribut est une annotation sur un objet (ici le module `mod`)
* dans l'espace de noms de l'objet, on "attache" un nom (ici `spam`) qui désigne autre objet (ici la fonction)
* pour utiliser (aller chercher) un attribut, la syntaxe est `obj.attribute`  
* un attribut n'est **pas une variable**
  * les variables sont résolues par liaison lexicale
  * les attributs sont résolus à run-time

```{admonition} rappel
tout ce qu'on a vu dans la leçon sur les classes, où a beaucoup parlé d'attributs, s'applique ici
```

+++

````{admonition} objet *vs* dictionnaire
:class: admonition-small

cette association nom → valeur rappelle un peu le dictionnaire  
c'est vrai mais pourtant les deux mécanismes (clés dans un dico, attribut dans un objet)  
sont implémentés et s'utilisent de manière différente: `d['key']` *vs* `o.key`  

il est donc important de bien les distinguer - surtout pour ceux qui font du JS
````

+++

## plusieurs formes d'`import`

la forme `import mod` est la plus basique; il en existe des variantes:

```{list-table}

* - code
  - définit la variable
  - commentaire

* - `import mod`
  - `mod`
  - de type module, avec des attributs

* - `import mod as mymod`
  - `mymod`
  - à part ça, même effet que `import mod`

* - `from mod import spam`
  - `spam`
  - on n'a pas accès au module, seulement un attribut 

* - 
  - 
  - qui est directement accessible via la variable `spam`
```


````{admonition} tout ça se combine
:class: admonition-small tip

on peut aussi importer plusieurs symboles du même module, et/ou les renommer si on veut, bref...  
par exemple que font à votre avis les phrases suivantes

```python

import mod1, mod2 as mymod2, mod3

from mod import var, var2 as myvar2, var3

```
````

````{admonition} import *
:class: admonition-small warning

on peut également écrire `from mod import *`, ce qui définit dans l'environnement courant tous les symboles du module, i.e. dans le cas de notre module `mod` les variables `GLOBALE` et `spam`  
toutefois cette pratique est **très fortement déconseillée** en dehors d'usages très spécifiques, car on brise la traçabilité des variables
````

+++

## package = module pour un dossier

il est possible d’organiser un gros code source dans un dossier, qui peut à son tour contenir d'autres dossiers...

du coup, le package est simplement un module, mais qui correspond à un dossier

dans ce cas-là, les attributs du module/package vont nous permettre de nous y retrouver:

+++ {"tags": ["gridwidth-1-2"]}

**si on a cette arborescence de fichiers**

    pack1/
      pack2/
        mod.py
          class Foo

+++ {"tags": ["gridwidth-1-2"]}

**on retrouve l'équivalent dans l'espace des modules**

    pack1
    pack1.pack2
    pack1.pack2.mod
    pack1.pack2.mod.Foo

+++

````{admonition} le contenu du package

**le fichier `__init__.py`**

le module `pack1` peut aussi avoir d'autres attributs que juste ceux qui correspondent aux fichiers dans le dossier  
il suffit pour cela d'écrire un fichier `__init__.py` (dans le dossier correspondant, bien sûr)  
et alors les variables globales dans ce code sont également ajoutées comme attributs dans le package

**Quiz**: sachant que dans notre contexte le fichier `pack1/__init__.py` contient ceci:
```python
print('pack1 init')

x = 1

from .pack2.mod import FOO
```

quels sera à votre avis la liste de tous les attributs de `pack1` ? la réponse est un peu plus bas
````

+++ {"slideshow": {"slide_type": "slide"}}

### importer un morceau du package

**`import dir.dir2.modulename`**

dans ce genre de contexte on peut avoir envie de ne charger qu'une partie du package, c'est possible avec quasiment la même syntaxe:

```{code-cell} ipython3
:tags: []

# voyons le contenu de cet autre module qui s'appelle aussi mod

!cat pack1/pack2/mod.py
```

```{code-cell} ipython3
:tags: []

# on pourrait l'importer comme ceci
# remarquez que l'on charge bien les packages intermédiaires
# qui sont pack1 et pack1.pack2

import pack1.pack2.mod
```

```{code-cell} ipython3
:tags: []

# et l'utiliser comme cela

pack1.pack2.mod.FOO
```

#### les attributs du package

voici la réponse à la question de tout à l'heure:

```{code-cell} ipython3
# si on fait abstraction des attributs spéciaux, 
# notre package a les attributs suivants

[att for att in vars(pack1) if '__' not in att]
```

on y trouve

* `pack2` qui est là à cause du sous-dossier `pack2`
* `x` qui est initialisé à 1 dans `pack2/__init__.py`
* et `FOO` qui résulte de l'import, et qui est aussi une variable globale dans `pack2/__init__.py`

+++

````{admonition} l'intérêt des espaces de noms
:class: admonition-small

vous remarquez que nous avons à présent deux "trucs" différents qui s'appellent tous les deux `mod`  
c'est le gros avantage des espaces de nom, qui permettent comme cela d'organiser les noms en permettant de gérer les éventuelles homonymies, qui peuvent toujours exister lorsqu'on utilise de nombreuses librairies

````

+++

## que fait une importation ?

principalement deux choses:

1. vérifier si le module est déjà chargé, et sinon:

  * **trouver** le fichier/dossier correspondant au module
    on en reparle un peu plus tard (c'est un sujet délicat)
    *rappel*: on ne met pas le `.py` du fichier lors d’un import

  * **compiler** (si besoin) le module en byte-code  
    cela est *caché* dans les dossiers `__pycache__`
    pas besoin de s'en occuper, on n'en parlera plus

  * **charger** en mémoire le module pour construire les objets qu’il définit  
    typiquement fonctions, classes, variables globales au module  
    et les ranger dans les attributs du module

2. affecter la variable locale - comme on l'a vu plus haut

+++

`````{admonition} les modules sont en cache
:class: important

* comme l’importation est une opération lourde, un module n’est chargé qu’**une seule fois**  
  dit autrement, les imports suivants retrouvent le module **déjà présent en mémoire**

* c'est optimal pour l'exécution du code  
  mais attention **pendant la phase de mise au point** interactive  

  ````{admonition} pour IPython et les notebooks

  voici le setup recommandé; vous pouvez copier-coller ceci dans un terminal de type *bash*, 
  ou alors utiliser un éditeur de texte pour ajouter les 3 lignes dans un fichier qui s'appelle 
  `.ipython/profile_default/ipython_config.py` - créer les dossiers au besoin
  ```bash
  mkdir -p ~/.ipython/profile_default
  cat >> ~/.ipython/profile_default/ipython_config.py << EOF
  c.InteractiveShellApp.exec_lines = []
  c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
  c.InteractiveShellApp.exec_lines.append('%autoreload 2')
  EOF
  ```
  ````
  une fois que ceci est en place, vous pouvez tout simplement modifier vos fichiers, les modules seront rechargés au besoin et vous exécuterez toujours la bonne version du code
`````

+++

## localisation du fichier du module

il est temps d'aborder **le point le plus délicat** avec les modules: comment fait le langage pour trouver le fichier (ou, à nouveau, le dossier) lorsqu'on importe un module ?

c'est un sujet souvent mal compris, c'est pourquoi on va essayer de bien décortiquer...

+++

### objectifs

avant de vous donner l'algorithme utilisé, souvenons-nous bien de l'objectif  
il s'agit de pouvoir importer aussi bien:

- la librairie standard
- les librairies installées avec pip
- les morceaux de code qui viennent avec votre propre application

+++

### l'algorithme

du coup on a choisi de chercher les fichiers dans l'ordre suivant

1. d'abord on cherche dans le dossier où se trouve **le point d'entrée** du programme
2. ensuite, si elle est définie, dans le ou les dossiers configurés dans la variable d'environnement `PYTHONPATH`
3. enfin dans les répertoires des librairies standards, ceci est configuré à l'installation  
   c'est dans ces endroits-là qu'on trouve la lib. standard, et les libs installées avec `pip`

````{admonition} c'est quoi le point d'entrée ?

vous savez que pour lancer un programme Python, on exécute en fait quelque chose comme
```bash
python mon-application.py
```
eh bien ce fichier `mon-application.py` c'est ce qu'on appelle le point d'entrée  
pour ceux qui ont fait du C/C++ ça correspond au `main()`

````

+++

### les fausses bonnes idées

````{admonition} PYTHONPATH

pour commencer, je vous recommande fortement de **ne pas utiliser** `PYTHONPATH` dans la vie de tous les jours, c'est vraiment réservé à des usages très spécifiques, notamment lorsqu'on déploie des solutions hostées à la jupyterhub ou autres
````

````{admonition} sys.path
:class: admonition-small

pour être tout à fait complet, il faut savoir que cette liste est en fait calculée au démarrage de l'interpréteur, et rangée dans la variable `sys.path` ... que vous pouvez tout à fait modifier par programme pour ajouter d'autres endroits  
toutefois cette pratique n'est, ici encore, **pas recommandée** en dehors de quelques cas d'usage très spécifiques
````

+++

### du monolithe au package

pour vos premiers pas, vous allez en général compliquer progressivement:

- en premier, on commence par écrire tout dans un seul fichier; là bien sûr, zéro souci
- dès que ça grossit un peu, on va vouloir couper en **plusieurs fichiers**
  et dans ce cas là, il suffit de les mettre **tous dans un même dossier**, y compris le point d'entrée donc, et grâce à la règle numéro 1, on va trouver facilement nos propres modules

toutefois, cette approche atteint **rapidement sa limite**, car

- pour lancer le programme, on doit, soit se placer dans le bon dossier avant de faire  
  `python mon-application.py`  
  soit donner à python le chemin complet  
  `bash le/chemin/ou/se/trouve/mon-application.py`  
  et ce n'est pas forcément très pratique
- ça oblige à éviter des noms déjà pris; si un de vos fichiers s'appelle `turtle.py`, vous ne pourrez plus utiliser le module `turtle` de la libraries standard ! toujours à cause de la règle 1
- si on veut écrire des tests, il faut les placer dans le même dossier aussi...

bref, si le projet a un peu de substance on est vite amené à vouloir organiser ses sources un peu mieux; pour cela la solution est de **créer un package** pour y mettre votre code, sauf que c'est moins trivial qu'on pourrait le penser ou en tous cas le souhaiter, et c'est précisément le sujet du notebook suivant :)

+++

````{admonition} le reste est pour les avancés
:class: warning

en première lecture vous pouvez vous arrêter ici, la suite couvre des aspects plutôt avancés de l'importation

````

+++ {"slideshow": {"slide_type": "slide"}, "tags": ["level_advanced"]}

## notions avancées

+++

### références partagées

* les instructions `import` et `from` sont des **affectations implicites** de variables
  * on a donc le problème des **références partagées** sur des mutables

voici un exemple (ne pas faire ça dans du vrai code !)

```{code-cell} ipython3
# ne surtout pas faire un truc comme ça...
# car ça modifie le contenu du module
# et donc ça impacte tout le programme !

import math
math.pi = 10.
```

en fait je viens de modifier `math.pi` **pour tout mon programme !!**  

on n’aurait **pas le problème avec `from`** parce que là, ça crée une variable locale

```{code-cell} ipython3
# les autres modules ne sont pas impactés

from math import pi
pi = 10
```

### exécuter un module comme un script

un module peut avoir deux rôles

* un module classique qui doit être importé  
  `import module`

* un script exécutable  
  `$ python module.py`

chaque module a un attribut `__name__` qui est défini par l’import

```{literalinclude} toplevel.py
:linenos:
:emphasize-lines: 1, 3
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

import toplevel
print(toplevel.__name__) 
```

#### l'idiome `if __name__ == "__main__"`

sauf que, si le module est le point d'entrée (on l'a lancé avec `python foo.py`), alors son exécution n’est pas le résultat d’un import  
... et du coup dans ce cas-là on ne trouve pas dans `__name__` ce qu'on pourrait attendre (`foo`) mais la chaine standard `__main__`

ce qui explique un idiome qu'on rencontre fréquemment:

```python
# voici un idiome fréquent à la fin d'un source Python
if __name__ == '__main__':
    test_module()
```

voici un exemple

```{literalinclude} samples/fib.py
:linenos:
:caption: dans le dossier `samples/`
:emphasize-lines: 3
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# À la ligne de commande on a
!python samples/fib.py
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# mais à l'import il ne se passe rien
from samples.fib import fib
```

````{admonition} avertissements

on peut effectivement utiliser cette fonctionnalité pour faire des tests unitaires, mais ce n'est **guère utilisé** en production car beaucoup trop limité

de plus, cette pratique entre en conflit avec l'utilisation d'imports relatifs (voir le notebook suivant), aussi elle a tendance à disparaitre au fil du temps
````

+++

### introspection

on peut accèder aux attributs d’un module en utilisant

* `vars(module)` retourne l’espace de nommage de module  
* `dir(module)` liste les attributs
* `globals()` retourne l’espace de nommage du module courant  

**remarque** `locals()` retourne l’espace de nommage à l’endroit de l’appel

+++ {"slideshow": {"slide_type": "slide"}}

exemple avec `globals()`

```{code-cell} ipython3
:tags: []

# cette variable est globale
foo = 10

# celle-ci aussi 
g = globals()

# globals() envoie un dict
type(g)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et les globales sont dedans
'foo' in g and 'g' in g
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

g['foo']
```

```{code-cell} ipython3
:cell_style: center
:tags: []

# si on n'est pas dans une fonction ou une classe,
# locals() et globals() retournent la même chose
locals() == globals()
```

+++ {"slideshow": {"slide_type": "slide"}}

exemple avec `locals()`

```{code-cell} ipython3
# par contre dans une fonction c'est différent
def f():
    tutu = 12
    print(f"tutu dans globals ? : {'tutu' in globals()}")
    print(f"tutu dans locals ? : {'tutu' in locals()}")
    print(f"foo dans globals ? : {'foo' in globals()}")
    print(f"foo dans locals ? : {'foo' in locals()}")
f()
```

### recharger un module

on a vu plus haut comment configurer IPython pour pouvoir travailler efficacement depuis `ipython` ou un notebook

en général c'est suffisant, mais si nécessaire on peut aussi utiliser le module standard `importlib` pour forcer le rechargement d'un module

voici un exemple complet

```{literalinclude} toplevel.py
:linenos:
:emphasize-lines: 1, 3
```

```{code-cell} ipython3
# je l'importe une première fois
import toplevel

# on y trouve donc
toplevel.eggs
```

```{code-cell} ipython3
# je peux changer l'intérieur du module
# à nouveau ce n'est pas conseillé, mais c'est légal

toplevel.eggs = 2
toplevel.eggs
```

```{code-cell} ipython3
# à ce stade si j'importe à nouveau, il ne se passe rien
# car le module est dans le cache

import toplevel

# notamment on a toujours la valeur modifiée de l'attribut
toplevel.eggs
```

```{code-cell} ipython3
# mais je peux forcer le réimport comme ceci

import importlib
importlib.reload(toplevel)

# et là maintenant je repars d'un module propre
# comme le prouve son attribut
toplevel.eggs
```

````{admonition} sys.modules
:class: admonition-small

pour les hackers curieux, le cache des modules est rangé dans `sys.modules`, sous la forme d'un dictionnaire { nom → *objet module* } de tous les modules chargés  
ce qui vous permet d'entrevoir une méthode plus brutale pour forcer le re-chargement des modules...
````

+++

````{admonition} importer un module depuis une chaine 

avec l'instruction `import` on ne peut importer qu'un nom littéral  
mais comment faire si le nom du module est lui-même dans une variable ?  
pour cela voyez **la fonction `importlib.import_module`**

**note**: `exec` est typiquement déconseillé pour ce genre d'usages
````

```{code-cell} ipython3
:cell_style: center

import importlib
nom_module = "math"
math2 = importlib.import_module(nom_module)
math2.e
```

### attributs privés

il existe une convention de nommage:  
tous les noms globaux qui **commencent par un underscore (`_`)** 
  sont **privés au module**
  
cela signifie qu'ils ne font pas partie de l'API, et qu'il n'est pas sage de les modifier  
ça n’est qu’une convention, mais c’est généralement suffisant

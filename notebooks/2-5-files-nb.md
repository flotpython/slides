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
  title: fichiers
---

# fichiers

* on a très souvent besoin de lire ou d'écrire un fichier par programme  
  notamment bien sûr pour lire les entrées ou sauver les résultats

* pour la lecture en pratique on utilise souvent des librairies  
  e.g. pour lire du ***json*** ou du ***yaml***, ou des formats spécialisés

* toutefois il est bon de savoir utiliser les outils de bas niveau  
  (enfin, aussi bas niveau que ce qu'offre Python…)

+++

## formats et librairies 

si vous devez lire des formats communs, faites-le avec:

- le module standard `json` pour du JSON
- la librairie externe `PyYAML` pour du YAML
- `pandas.read_csv()` pour du csv
- etc...

+++

## mais sinon: `open()` est le point d'entrée

* lire et écrire un fichier est très facile en Python
* ouvrir un fichier pour créer un objet "fichier"
* `open('mon_fichier.txt', 'r')`
  * `'r'` ouvre le fichier en lecture (défaut),
  * `‘w’` en écriture,
  * `‘a’` en écriture à la suite (*append*),
* `open()` retourne un objet de type fichier
* qu'il faut **bien penser à refermer**  
  sans quoi on provoque des fuites de *file descriptors*, et au bout  
  d'un moment l'OS ne nous laisse plus ouvrir de fichiers du tout

+++

## utilisez toujours un `with`

* c'est pourquoi il est **recommandé**
* de prendre l'habitude de **toujours utiliser un context manager**

```{code-cell} ipython3
# on n'a pas encore étudié l'instruction with
# mais je vous conseille de toujours procéder comme ceci

# avec with on n'a pas besoin de fermer le fichier
with open('temporaire.txt', 'w') as writer:
    for i in 10, 20, 30:
        print(f"{i} {i**2}", file=writer)
```

avantage du `with`:

* **pas besoin de fermer**
* même en cas de gros souci (exception)

````{admonition} sans context manager
:class: dropdown

dans du vieux code, ou du code de débutant, vous pourrez voir parfois ce style; c'est à éviter !

```python
writer = open('temporaire.txt', 'w')
for i in 10, 20, 30:
        writer.write(f'{i} {i**2}\n')
writer.close()
```

````

+++

## lecture avec `for`

* l'objet fichier est un **itérable** lui-même
* donc on peut l'utiliser dans un `for` pour traiter une ligne à la fois
* c'est ***la méthode recommandée** pour lire un fichier texte

````{admonition} avec un newline
:class: warning

**attention** toutefois, car chaque ligne va contenir un caractère `"\n"` de fin de ligne (sauf éventuellement la dernière)
````

```{code-cell} ipython3
# pour inspecter ce qu'on vient d'écrire
# dans le fichier qui s'appelle "temporaire.txt"
# dans le répertoire courant

# lire un fichier texte ligne par ligne
# on ne peut pas faire plus compact et lisible !

# remarquez aussi:
# open() sans le mode ⇔ open('r')

with open("temporaire.txt") as reader:
    for line in reader:
        # attention ici line contient déjà le newline
        # c'est pourquoi on demande à print() de ne pas
        # en ajouter un second
        print(line, end="")
```

````{admonition} on peut régler le comportement de print()

sans réglage particulier, la fonction `print()` écrit dans le terminal (ou le notebook), et ajoute automatiquement une fin de ligne  
on peut agir sur ce comportement avec
- `print(..., file=writer)` comme on l'a fait au tout début de ce notebook pour créer le fichier `temporaire.txt`
- `print(..., end="")` comme on vient de le faire pour éviter le saut de ligne automatique
````

+++

````{admonition} lecture en comptant les lignes ?
:class: dropdown

* pour anticiper un peu: si je voulais compter les lignes ?

  ```python
  # ne défigurez pas votre code juste pour avoir un indice de boucle
  # utilisez enumerate !

  with open('temporaire.txt') as reader:
      # les numéros de ligne commencent à 1
      for lineno, line in enumerate(reader, 1):
          print(f"{lineno}: {line}", end='')
  ```

on en reparlera au sujet des itérations...
````

+++

````{admonition} évitez readlines()
:class: dropdown

* `F.readlines()`
  * retourne un itérateur sur les lignes
  * équivalent à itérer sur F directement
  * mais moins performant (charge tout le fichier !)
  * et moins pythonique

  ```python
  # ce code fonctionne, mais c'est à éviter
  # surtout si vous lisez de gros fichiers

  with open('temporaire.txt', 'r') as in_file:
      for line in in_file.readlines():
          print(line, end='')
  ```
````

+++

### autres méthodes en lecture

comme toujours, il y a plein d'autres méthodes disponibles sur les fichiers texte, reportez-vous à la documentation pour des besoins spécifiques

+++

## fichiers ouverts en binaire

+++

### ajouter `b` dans le mode

tous les fichiers ne sont pas des fichiers texte  
par ex. un exécutable, un fichier dans un format propriétaire

pour ouvrir un fichier **en mode binaire**:

* on ajoute `b` au mode d'ouverture,
* on interagit avec l'objet fichier avec un objet **`bytes`** et non `str`
* c'est-à-dire que la lecture retourne un `bytes`  
  et on ne peut que écrire un `bytes`

* il n’y a aucun encodage, décodage,  
  et aucune conversion de fin de ligne (auberge espagnole)

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# pour fabriquer un objet bytes, je peux par exemple 
# encoder un texte qui comporte des accents
# (on reparlera des encodages plus tard)

text = "noël en été\n"
binaire = text.encode(encoding="utf-8")

binaire
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# j'ai bien un objet bytes, 
# et sa taille correspond au nombre d'octets 
# et non pas au nombre de caractères

type(binaire), len(binaire), len(text)
```

```{code-cell} ipython3
:cell_style: center
:tags: [gridwidth-1-2]

# remarquez le 'b' dans le mode d'ouverture

with open('temporaire.bin', 'wb') as out_file:
    # je peux du coup écrire un objet bytes
    out_file.write(binaire)
```

```{code-cell} ipython3
:cell_style: center
:tags: [gridwidth-1-2]

# pareil en lecture, le mode avec un 'b'
# va faire que read() retourne un objet bytes

with open('temporaire.bin', 'rb') as in_file:
    binaire2 = in_file.read()
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et donc on retombe bien sur nos pieds
binaire2 == binaire
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ça aurait été pareil 
# si on avait ouvert le fichier en mode texte
# puisque ce qu'on a écrit dans le fichier binaire,
# c'est justement l'encodage en utf-8 d'un texte

#             sans le b ici ↓↓↓
with open('temporaire.bin', 'r') as feed:
    text2 = feed.read()
    
text2 == text
```

## le module `pathlib`

### objectifs

* simplifier la gestion des noms de fichier
  * pour rendre le code plus concis, et donc plus lisible
* notamment, en remplacement de `os.path` qui est *old-school* (et super vilain)
* le sous-titre pour `pathlib`: *object-oriented filesystem paths*

+++

### présentation du module

* **orienté objet**
* examiner le contenu du disque
  existe ou pas, quel type, *globbing* …

* les calculs sur les noms de fichiers  
  concaténation, suffixes, remonter dans l'arbre …

* métadonnées  
  taille, dates de modification, …

* permet d'ouvrir les fichiers
* ne gère pas les urls
* voir [documentation complète](https://docs.python.org/3/library/pathlib.html)

+++

````{admonition} en remplacement de ...
:class: dropdown

pour les anciens, le module `pathlib` remplace entre autres:  

* le plus gros de `os.path`
* certaines choses de `os`
* `glob.glob`
* `fnmatch`
* enfin il contient un wrapper pour `open()`
````

+++

### un exemple

* **orienté objet**
* le sujet devient plus visible
* **NB**: un objet `Path` est immutable

```{code-cell} ipython3
# savoir si un chemin correspond à un dossier
from pathlib import Path

tmp = Path("temporaire.txt")

if tmp.is_file():
    print("c'est un fichier")
```

```{code-cell} ipython3
# donc on peut l'ouvrir

with tmp.open() as feed:
    for line in feed:
        print(line, end="")
```

```{code-cell} ipython3
# on peut faire des calculs sur les noms de fichier
tmp.suffix
```

```{code-cell} ipython3
# changer de suffixe
tmp.with_suffix(".py")
```

```{code-cell} ipython3
# calculer le chemin absolu
# le couper en morceaux, etc...
tmp.absolute().parts
```

### construire un objet `Path`

```{code-cell} ipython3
# un chemin absolu
prefix = Path("/etc")

# le chemin absolu du directory courant
dot = Path.cwd()

# ou du homedir
home = Path.home()

# un nom de ficher
filename = Path("apache")
```

```{code-cell} ipython3
# par exemple le répertoire courant est

dot
```

### l'opérateur `/`

un exemple intéressant de surcharge d'opérateur: selon le type de ses opérandes, `/` fait .. ce qu'il faut ! par exemple ici on ne fait pas une division !

```{code-cell} ipython3
# Path / Path -> Path bien sûr
type(prefix / filename)
```

```{code-cell} ipython3
# Path / str -> Path
type(prefix / "apache2")
```

```{code-cell} ipython3
# str / Path -> Path
type("/etc" / Path("apache2"))
```

```{code-cell} ipython3
# mais bien sûr str / str -> TypeError
try:
    "/etc" / "apache2"
except Exception as e:
    print("OOPS", e)
```

### calculs sur les chemins

j'ai créé un petite hiérarchie de fichiers dans le dossier `filepath-globbing` qui ressemble à ceci

```{image} media/filepath-globbing.png
:align: center
```

```{code-cell} ipython3
# pour commencer, voilà comment on peut trouver son chemin absolu

globbing = Path("filepath-globbing")
absolute = globbing.absolute()
absolute
```

```{code-cell} ipython3
# si on a besoin d'un str, comme toujours il suffit de faire

str(absolute)
```

```{code-cell} ipython3
# les différents morceaux de ce chemin absolu

absolute.parts
```

```{code-cell} ipython3
# juste le nom du fichier, sans le chemin

absolute.name
```

```{code-cell} ipython3
# le chemin, sans le nom du fichier

absolute.parent
```

```{code-cell} ipython3
# tous les dossiers parent

list(absolute.parents)
```

### pattern-matching

```{code-cell} ipython3
# est-ce que le nom de mon objet Path 
# a une certaine forme ?

absolute.match("**/notebooks/*")
```

```{code-cell} ipython3
absolute.match("**/*globbing*")
```

#### pattern-matching - dans un dossier

```{image} media/filepath-globbing.png
:align: center
```

```{code-cell} ipython3
# à présent c'est plus intéressant
# avec des chemins relatifs
root = Path("filepath-globbing")

# tous les fichiers / répertoires 
# qui sont immédiatement dans le dossier
list(root.glob("*"))
```

```{code-cell} ipython3
# les fichiers/dossiers immédiatement dans le dossier
# et dont le nom se termine par un chiffre
list(root.glob("*[0-9]"))
```

#### pattern-matching - dans tout l'arbre

```{image} media/filepath-globbing.png
:align: center
```

```{code-cell} ipython3
# ce dossier, et les dossiers en dessous
# à n'importe quel étage

list(root.glob("**"))
```

```{code-cell} ipython3
# tous les fichiers/dossiers 
# dont le nom termine par un chiffre

list(root.glob("**/*[0-9]"))
```

+++ {"tags": ["level_advanced"]}

## notions avancées

+++ {"tags": ["level_advanced"]}

### encodages par défaut

* vous remarquez qu'on a souvent appelé `open()` sans préciser l'encodage
* l’encodage par défaut pour un fichier ouvert en mode texte est celui retourné par

```{code-cell} ipython3
:tags: [level_advanced]

import locale
locale.getpreferredencoding(False)
```

+++ {"tags": ["level_advanced"]}

* appeler `open()` sans préciser l'encodage peut être risqué
  * dépend des réglages sur la machine cible
* il vaut mieux toujours être **explicite** et préciser l'encodage

```{code-cell} ipython3
:tags: [level_advanced]

with open('temporaire.txt', 'r', encoding='utf8') as in_file:
    print(in_file.read())
```

+++ {"tags": ["level_advanced"]}

* le problème est toutefois de moins en moins aigü
  * Windows, MacOS et Linux à présent configurés par défaut pour UTF-8
* si vous avez encore du `cp1252` (vieux Windows) ou des ISO-latin15 (Unix)
  * je vous recommande de transcoder tout ça !

+++ {"tags": ["level_advanced"]}

### fichiers système

* `sys.stdout`, `sys.stdin`, `sys.stderr`
  * sortie, entrée et erreur standard
  * accessibles donc au travers du module `sys`

```{code-cell} ipython3
:tags: [level_advanced]

import sys
sys.stdout
```

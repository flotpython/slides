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
#     title: fichiers
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

# %% [markdown] cell_style="center" slideshow={"slide_type": ""}
# # fichiers

# %% [markdown]
# * on a très souvent besoin de lire ou d'écrire un fichier par programme  
#   notamment bien sûr pour lire les entrées ou sauver les résultats
#
# * pour la lecture en pratique on utilise parfois des librairies  
#   e.g. pour lire du JSON ou du XML, ou des formats spécialisés
#
# * toutefois il est bon de savoir utiliser les outils de bas niveau  
#   (enfin, aussi bas niveau que ce qu'offre Python…)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `open()`

# %% [markdown] slideshow={"slide_type": ""}
# * lire et écrire un fichier est très facile en Python
# * ouvrir un fichier pour créer un objet "fichier"
# * `open('mon_fichier.txt', 'r')`
#   * `'r'` ouvre le fichier en lecture (défaut),
#   * `‘w’` en écriture,
#   * `‘a’` en écriture à la suite (*append*),
# * `open()` retourne un objet de type fichier
# * qu'il faut **bien penser à refermer**  
#   sans quoi on provoque des fuites de *file descriptors*, et au bout  
#   d'un moment l'OS ne nous laisse plus ouvrir de fichiers du tout

# %% [markdown] slideshow={"slide_type": "slide"}
# ### utilisez toujours un `with`

# %% [markdown]
# * c'est pourquoi il est **recommandé**
# * de prendre l'habitude de **toujours utiliser un context manager**

# %%
# on n'a pas encore étudié l'instruction with
# mais je vous conseille de toujours procéder comme ceci

# avec with on n'a pas besoin de fermer le fichier
with open('temporaire.txt', 'w') as writer:
    for i in 10, 20, 30:
        writer.write(f'{i} {i**2}\n')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### sans context manager

# %%
# dans du vieux code, ou du code de débutant, vous pourrez voir

writer = open('temporaire.txt', 'w')
for i in 10, 20, 30:
        writer.write(f'{i} {i**2}\n')
writer.close()

# %% [markdown]
# avantage du `with`:
#
# * pas besoin de fermer
# * même en cas de gros souci (exception)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## lecture

# %% [markdown]
# * l'objet fichier est un **itérable** lui-même
# * donc on peut l'utiliser dans un `for`

# %% slideshow={"slide_type": ""}
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

# %% [markdown] slideshow={"slide_type": "slide"}
# ### lecture en comptant les lignes

# %% [markdown]
# * pour anticiper un peu:
#   * si je voulais compter les lignes ?
# * (on en reparlera au sujet des itérations)

# %%
# ne défigurez pas votre code juste pour
# avoir un indice de boucle, utilisez enumerate

with open('temporaire.txt') as reader:
    for lineno, line in enumerate(reader):
        print(f"{lineno+1}: {line}", end='')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### évitez `readlines()`

# %% [markdown]
# * `F.readlines()`
#   * retourne un itérateur sur les lignes
#   * équivalent à itérer sur F directement
#   * mais moins performant (charge tout le fichier !)
#   * et moins pythonique

# %%
# fonctionne, mais à éviter

with open('temporaire.txt', 'r') as in_file:
    for line in in_file.readlines():
        print(line, end='')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### autres méthodes en lecture

# %% [markdown]
# * `F.read(size)` lit `size` octets
#  * si `size` n’est pas spécifié, lit tout le fichier
#  * retourne une chaîne de caractères `str` contenant ce qui a été lu
# * `F.readline()` lit une seule ligne
#   * la chaîne retournée contient `\n` à la fin

# %% [markdown] slideshow={"slide_type": "slide"}
# ## écriture

# %% [markdown]
# ### mode d'ouverture
#
# * `open()` prend en premier paramètre le nom du fichier
# * en second vient **le mode** d'ouverture
# * qui est typiquement
#   * soit absent complètement (ouverture en lecture)
#   * soit la chaine 'r' (pour *read* bien sûr)
#   * soit la chaine 'w' (pour *write*)
#
# on peut aussi créer des modes composites (plusieurs caractères), on y reviendra

# %% [markdown] slideshow={"slide_type": "slide"}
# ### méthodes sur fichiers en écriture

# %% [markdown] slideshow={"slide_type": ""}
# pour utiliser un fichier ouvert en écriture

# %% [markdown]
# * `print("paramètres", "usuels", file=F)`
#   * redirige `print` dans ce fichier
# * `F.write('mon texte\n')`
#   * écrit (ici une ligne) dans le fichier
# * `F.writelines(sequence)`
#   * écrit une séquence dans un fichier, le saut de ligne doit être explicite avec `\n`
# * `F.flush()`
#   * force l’écriture dans le fichier en vidant le cache
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### fichiers texte, type `str` et EOL

# %% [markdown] slideshow={"slide_type": ""}
# un fichier sera dit **en mode texte** si le mode d'ouverture  
# passé à `open()` ne contient pas `b`:
#
# * le décodage et l’encodage sont automatiques  
#   lorsqu’on lit ou écrit dans le fichier
#
# * on obtiendra toujours un objet `str` en lecture  
#   et on ne pourra écrire qu’un objet `str`
#
# * les fins de lignes sont automatiquement  
#   converties en '\n' (un seul caractère)  
#   pour être indépendant de l’OS

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fichiers ouverts en binaire

# %% [markdown] slideshow={"slide_type": ""} cell_style="split"
# ### ajouter `b` dans le mode
#
# avec un fichier Python **en mode binaire**
#
# * en ajoutant `b` au mode d'ouverture,
# * on obtiendra un objet `bytes`  
#   en lecture et on ne pourra écrire  
#   qu’un objet `bytes`
#
# * il n’y aura aucun encodage, décodage,  
#   et aucune conversion de fin de ligne (auberge espagnole)

# %% cell_style="split" slideshow={"slide_type": ""}
# j'ai besoin d'un objet bytes
# rappelez vous la section sur Unicode
text = "noël en été\n"
binaire = text.encode(encoding="utf-8")

binaire

# %% cell_style="split"
type(binaire), len(binaire)

# %% cell_style="center" slideshow={"slide_type": "slide"}
# remarquez le 'b' dans le mode d'ouverture

with open('temporaire.bin', 'wb') as out_file:
    # je peux du coup écrire un objet bytes
    out_file.write(binaire)

# %% cell_style="center" slideshow={"slide_type": ""}
# pareil en lecture, le mode avec un 'b'
# va faire que read() retourne un objet bytes

with open('temporaire.bin', 'rb') as in_file:
    binaire2 = in_file.read()

# %% slideshow={"slide_type": ""}
# et donc on retombe bien sur nos pieds
binaire2 == binaire

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un autre exemple

# %% [markdown]
# dans l'autre sens, si on part d'un fichier texte
# qui n'est pas purement ASCII, on obtient des objets
# de taille différente selon qu'on lit en binaire ou pas
# car **un caractère n'est pas un octet**

# %%
with open('../data/une-charogne.txt') as texte:
   x = texte.read()
type (x), len(x)

# %%
with open('../data/une-charogne.txt', 'rb') as binaire:
   y = binaire.read()
type (y), len(y)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le module `pathlib`

# %% [markdown] slideshow={"slide_type": ""}
# ### objectifs
#
# * simplifier la gestion des noms de fichier
# * pour rendre le code plus concis
# * et donc plus lisible
# * sous-titre: *object-oriented filesystem paths*

# %% [markdown] slideshow={"slide_type": "slide"}
# ### présentation du module
#
# * **orienté objet**
# * examiner le contenu du disque
#   existe ou pas, quel type, *globbing* …
#
# * les calculs sur les noms de fichiers  
#   concaténation, suffixes, remonter dans l'arbre …
#
# * métadonnées  
#   taille, dates de modification, …
#
# * permet d'ouvrir les fichiers
# * ne gère pas les urls
# * voir [documentation complète](https://docs.python.org/3/library/pathlib.html)
#

# %% [markdown]
# ````{admonition} xxx
#
# pour les anciens, le module `pathlib` remplace les modules `os`, `os.path` et assimilés
#
# ````

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un exemple
#
# * **orienté objet**
# * le sujet devient plus visible
# * **NB**: un objet `Path` est immutable

# %%
# avec pathlib
from pathlib import Path

config_path = Path("/etc/apache2")

if config_path.is_dir():
    print(f"{config_path} existe et c'est un dossier")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### les points de départ

# %% cell_style="split"
# un chemin absolu
etc = Path("/etc")
etc

# %% cell_style="split"
# le chemin absolu du directory courant
dot = Path.cwd()
dot

# %% cell_style="split"
# ou du homedir
home = Path.home()
home

# %% [markdown] slideshow={"slide_type": "slide"}
# ### l'opérateur `/`

# %% [markdown]
# pour "naviguer" dans les dossiers et construire des chemins, on utilise l'opérateur `/`

# %%
# par exemple pour désigner /etc/apache2 on peut aussi faire

etc / "apache2"

# %% cell_style="split"
# ou encore: le dossier 'bidule' directement dans mon homedir
home / "bidule"

# %% slideshow={"slide_type": ""} cell_style="center"
# le dossier "machin" dans le dossier courant
dot / "machin"

# %%
# ATTENTION quand même car bien sûr str / str -> TypeError
try:
    "/etc" / "apache2"
except Exception as e:
    print("OOPS", e)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### calculs sur les chemins

# %% slideshow={"slide_type": ""} cell_style="split"
# un chemin vers le dossier 'filepath-globbing'
# dans ce répertoire

here = Path.cwd()
globbing = here / "filepath-globbing"

# retrouver le string
str(globbing)

# %% cell_style="split"
globbing.parts

# %% cell_style="center"
# basename
globbing.name

# %% cell_style="split"
# dirname
globbing.parent

# %% cell_style="split"
list(globbing.parents)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *pattern-matching*

# %% cell_style="split" slideshow={"slide_type": ""}
# est-ce que le nom de mon objet Path
# a une certaine forme ?

globbing.match("**/slides/*")

# %% cell_style="split"
globbing.match("**/*globbing*")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *globbing*

# %% [markdown] cell_style="center"
# recherche dans un répertoire

# %% [markdown]
# Voici le contenu du dossier `filepath-globbing`
#
# ```
# filepath-globbing          dossier
# filepath-globbing/a1       fichier
# filepath-globbing/b        dossier
# filepath-globbing/b/b2     fishier
# filepath-globbing/c        dossier
# filepath-globbing/c/cc     dossier
# filepath-globbing/c/cc/c2  fichier
# ```

# %% slideshow={"slide_type": "slide"}
# j'utilise un chemin relatif, la sortie sera plus claire
globbing = Path(".") / "filepath-globbing"
globbing

# %% slideshow={"slide_type": "slide"} cell_style="split"
# les fichiers immédiatement sous globbing
list(globbing.glob("*"))

# %% cell_style="split"
# pareil, qui en plus
# se finissent
# par un nombre
list(globbing.glob("*[0-9]"))

# %% cell_style="split"
# tous les dossiers sous globbing
list(globbing.glob("**"))

# %% cell_style="split"
# les fichiers qui sont
# dans un sous-dossier
# donc à n'importe quelle profondeur
# et qui se terminent par un nombre
list(globbing.glob("**/*[0-9]"))

# %% [markdown] slideshow={"slide_type": "slide"}
# ### voir aussi
#
# * `exists`, `is_dir`, `is_file` ...
# * `stat` / `lstat` / `owner` pour les détails comme taille, permissions...
# * `rename`, `unlink`, `rmdir`
# * `iterdir` (`os.listdir`, mais pas `os.walk`)
# * `glob` - `rglob`
# * `open` / `{read,write}_{text_bytes}` / : wrappers
# * à nouveau: [documentation complète](https://docs.python.org/3/library/pathlib.html)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le module `pathlib` remplace :
#
# * le plus gros de `os.path`
# * certaines choses de `os`
# * `glob.glob`
# * `fnmatch`
# * contient un wrapper pour `open()`

# %%
# on peut faire open() sur un objet Path
# avec un paramètre en moins que le open() builtin
# puisque le nom du fichier est dans l'objet Path

with Path("temporaire.txt").open() as reader:
    for line in reader:
        print(line, end="")

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_advanced"]
# ## notions avancées

# %% [markdown] slideshow={"slide_type": ""} tags=["level_advanced"]
# ### encodages par défaut

# %% [markdown] tags=["level_advanced"]
# * vous remarquez qu'on a souvent appelé `open()` sans préciser l'encodage
# * l’encodage par défaut pour un fichier ouvert en mode texte est celui retourné par:

# %% tags=["level_advanced"]
import locale
locale.getpreferredencoding(False)

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_advanced"]
# * appeler `open()` sans préciser l'encodage peut être risqué
#   * dépend des réglages sur la machine cible
# * il vaut mieux toujours être **explicite** et préciser l'encodage

# %% tags=["level_advanced"]
with open('temporaire.txt', 'r', encoding='utf8') as in_file:
    print(in_file.read())

# %% [markdown] tags=["level_advanced"]
# * le problème est toutefois de moins en moins aigü
#   * Windows, MacOS et Linux à présent configurés par défaut pour UTF-8
# * si vous avez encore du `cp1252` (vieux Windows) ou des ISO-latin15 (Unix)
#   * je vous recommande de transcoder tout ça !

# %% [markdown] slideshow={"slide_type": "slide"} tags=["level_advanced"]
# ### fichiers système

# %% [markdown] tags=["level_advanced"]
# * `sys.stdout`, `sys.stdin`, `sys.stderr`
#   * sortie, entrée et erreur standard
#   * accessibles donc au travers du module `sys`

# %% tags=["level_advanced"]
import sys
sys.stdout

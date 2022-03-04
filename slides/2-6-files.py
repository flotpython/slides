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
#   enfin aussi bas niveau que ce qu'offre Python

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
# ### utilisez un `with`

# %% [markdown]
# * c'est pourquoi il est **recommandé** 
# * de prendre l'habitude de **toujours utiliser un context manager** 

# %%
# on n'a pas encore étudié l'instruction with
# mais je vous conseille de toujours procéder comme ceci

# avec with on n'a pas besoin de fermer le fichier
with open('temporaire.txt', 'w') as writer:
    for i in 10, 20, 30:
        writer.write('{} {}\n'.format(i, i**2))

# %% [markdown] slideshow={"slide_type": "slide"}
# ### sans context manager

# %%
# dans du (très) vieux code, vous pourrez voir

writer = open('temporaire.txt', 'w')
for i in 10, 20, 30:
    writer.write('{} {}\n'.format(i, i**2))
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
# * `F.write('mon texte\n')`
#   * écrit (ici une ligne) dans le fichier
# * `F.writelines(sequence)`
#   * écrit une séquence dans un fichier, le saut de ligne doit être explicite avec `\n` 
# * `F.flush()`
#   * force l’écriture dans le fichier en vidant le cache
# * `print("paramètres", "usuels", file=F)`
#   * redirige `print` dans ce fichier

# %% [markdown] slideshow={"slide_type": "slide"}
# ### fichiers texte, type `str` et EOL

# %% [markdown] slideshow={"slide_type": ""}
# un fichier sera en mode texte si le mode ne contient pas `b`:
#
# * le décodage et l’encodage sont automatiques lorsqu’on lit ou écrit dans le fichier
# * on obtiendra toujours un objet `str` en lecture et on ne pourra écrire qu’un objet `str`
# * les fins de lignes sont automatiquement converties en '\n' pour être indépendant de l’OS

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fichiers ouverts en binaire

# %% [markdown] slideshow={"slide_type": ""}
# ### ajouter `b` dans le mode
#
# on peut ouvrir un fichier Python **en mode binaire** 
#
# * en ajoutant `b` au mode d'ouverture,
# * on obtiendra toujours un objet `bytes` en lecture et on ne pourra écrire qu’un objet `bytes`
# * il n’y aura aucun encodage, décodate, et aucune conversion de fin de ligne (auberge espagnole)

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

# %% [markdown]
# ## notions avancées

# %% [markdown] slideshow={"slide_type": "slide"}
# ### encodages par défaut

# %% [markdown]
# * vous remarquez qu'on a souvent appelé `open()` sans préciser l'encodage
# * l’encodage par défaut pour un fichier ouvert en mode texte est celui retourné par: 

# %%
import locale 
locale.getpreferredencoding(False)

# %% [markdown] slideshow={"slide_type": "slide"}
# * appeler `open()` sans préciser l'encodage peut être risqué
#   * dépend des réglages sur la machine cible
# * il vaut mieux toujours être **explicite** et préciser l'encodage

# %%
with open('temporaire.txt', 'r', encoding='utf8') as in_file:
    print(in_file.read())

# %% [markdown]
# * le problème est toutefois de moins en moins aigü
#   * Windows, MacOS et Linux à présent configurés par défaut pour UTF-8
# * si vous avez encore du `cp1252` (vieux Windows) ou des ISO-latin15 (Unix)
#   * je vous recommande de transcoder tout ça !

# %% [markdown] slideshow={"slide_type": "slide"}
# ### fichiers système

# %% [markdown]
# * `sys.stdout`, `sys.stdin`, `sys.stderr`
#   * sortie, entrée et erreur standard 
#   * accessibles donc au travers du module `sys`

# %%
import sys
sys.stdout

# %% [markdown] slideshow={"slide_type": ""}
# ## le module `pathlib`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### objectifs
#
# * simplifier la gestion des noms de fichier 
# * pour rendre le code plus concis
# * et donc plus lisible
# * sous-titre: *object-oriented filesystem paths*

# %% [markdown] slideshow={"slide_type": "slide"}
# ### présentation du module
#
# * voir [documentation complète](https://docs.python.org/3/library/pathlib.html)
# * et notamment un diagramme des classes 
#   * `purepath` : manipulation sans le filesystem
#   * `path` : par exemple pour globbing (résoudre '*')
# * dispo dans librairie standard depuis python-3.4
#   * et aussi dans pypi, donc pour 2.7
# * ne gère pas
#   * les objets fichier (s'arrête à `open`)
#   * les urls

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un exemple
#
# * orienté objet
# * le sujet devient plus visible
# * **NB**: un objet `Path` est immutable

# %%
# avec os.path
import os.path

config_dir = "/etc/apache2"
if os.path.isdir(config_dir):
    print("OUI")

# %%
# avec pathlib
from pathlib import Path

config_path = Path("/etc/apache2")
if config_path.is_dir():
    print("OUI")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### l'opérateur `/`

# %% [markdown]
# * la fin de `os.path.join`

# %%
# un chemin absolu
prefix = Path("/etc")
# le chemin absolu du directory courant
dot = Path.cwd()
# ou du homedir
home = Path.home()
# un nom de ficher
filename = Path("apache")

# Path / Path -> Path bien sûr
type(prefix / filename)

# %% slideshow={"slide_type": "slide"}
# Path / str -> Path
type(prefix / "apache2")

# %%
# str / Path -> Path
type("/etc" / Path("apache2"))

# %%
# On peut chainer le tout sans parenthèse 
# si le premier (à gauche) est un Path

type(prefix / "apache2" / "modules.d")

# %%
# mais bien sûr str / str -> TypeError
try:
    "/etc" / "apache2"
except Exception as e:
    print("OOPS", e)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### décorticage

# %% [markdown]
# * remplacement de `basename` et `dirname` et similaires

# %%
# un chemin vers le directory 'filepath-globbing' dans ce répertoire

absolute = Path.cwd()
relative = Path(".")

globbing = absolute / "filepath-globbing"

# retrouver le string
str(globbing)

# %%
globbing.parts

# %%
# basename
globbing.name

# %%
# dirname
globbing.parent

# %%
list(globbing.parents)

# %% slideshow={"slide_type": "slide"}
# parce qu'on l'a construit à partir de cwd() qui est absolu
globbing.is_absolute()

# %%
Path("globbing").is_absolute()

# %%
# ancien abspath()
globbing.resolve()

# %%
list(globbing.parents)[-2]

# %%
# ancien relpath()
# juste pour rendre le notebook utilisable partout (windows?)
level1 = list(globbing.parents)[-2]
print("level1", level1)
# chez moi level1 vaut "/Users"
globbing.relative_to(level1)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### pattern-matching

# %% cell_style="center" slideshow={"slide_type": ""}
# est-ce que le nom de mon objet Path 
# a une certaine forme ?

globbing.match("**/slides/*")

# %%
globbing.match("**/*globbing*")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### pattern-matching

# %% [markdown] cell_style="split"
# recherche dans un répertoire

# %% cell_style="split"
# un répertoire qui contient quelques fichiers
# !ls filepath-globbing/**

# %% slideshow={"slide_type": "slide"}
# à présent c'est plus intéressant
# avec des chemins relatifs
globbing = Path(".") / "filepath-globbing"

list(globbing.glob("*"))

# %%
list(globbing.glob("*[0-9]"))

# %%
list(globbing.glob("**"))

# %%
list(globbing.glob("**/*[0-9]"))

# %%
str(globbing)

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
# ### le module `pathlib`remplace :
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

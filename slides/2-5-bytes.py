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
#     display_name: Python 3
#     language: python
#     name: python3
#   nbhosting:
#     title: str et bytes
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

# %%
#from plan import plan; plan("types", "bytes")

# %% [markdown] slideshow={"slide_type": ""}
# # données brutes : le type `bytes`

# %% [markdown] slideshow={"slide_type": ""}
# ## le type `bytes`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### non mutable

# %% [markdown]
# * le type `bytes` correspond, comme son nom l'indique,  
#   à une séquence d'**octets**
# * le type `bytes` est donc un autre exemple de **séquence** (comme `str`) 
# * c'est également un type **non mutable**

# %% cell_style="split"
b = bytes([65, 66, 67])
b

# %% cell_style="split"
try: 
    b[1] = 68
except Exception as exc:
    print(f"OOPS - {type(exc)}\n{exc}")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### littéral

# %% [markdown] cell_style="center"
# pour construire un `bytes` on peut soit
#
# * utiliser le constructeur `bytes()` - comme slide précédent
# * lire un fichier ouvert en mode binaire - vu plus tard
# * mettre un `b` devant une chaîne de caractères

# %% cell_style="split"
# caractère -> code ASCII
b = b'ABC'
b

# %% cell_style="split" slideshow={"slide_type": ""}
# sinon en hexa
b'\x45\xff'

# %% [markdown] slideshow={"slide_type": "slide"}
# ### affichage comme des caractères

# %% [markdown]
# * comme on le voit dans `b'ABC'` , les octets d'un `bytes`  
#   sont parfois **représentés par des caractères ASCII**
#
# * c'est un usage répandu
# * mais ça peut être **source de confusion**

# %% cell_style="split"
# on peut écrire ceci
b1 = b'ete'
b1

# %% cell_style="split"
b2 = bytes(
    [ord('e'), ord('t'), ord('e')]
)
b1 == b2

# %% [markdown]
# * par exemple ceci ne **marcherait pas**
# ```
# >>> b'été'
#          ^
# SyntaxError: bytes can only contain ASCII literal characters.
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# * en interne, le type `bytes` ne stocke que des entiers
# * la représentation sous forme de caractères est uniquement  
#   pour **faciliter la lecture** de l’ASCII

# %%
s = b'a\xff'
s[0], s[1]

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un `bytes` est une séquence

# %% [markdown]
# * on manipule des objets `bytes` presque comme des objets `str`
# * les bytes sont des séquences (donc indexation, slicing, ...)
# * essentiellement les mêmes méthodes que pour les `str`

# %% [markdown] cell_style="split"
# méthodes dans `str`, mais pas dans `bytes`

# %% [markdown] cell_style="split"
# méthodes dans `bytes`, mais pas dans `str`

# %% cell_style="split"
set(dir(str)) - set(dir(bytes))

# %% cell_style="split"
set(dir(bytes)) - set(dir(str))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## texte, binaire et encodage

# %% [markdown]
# * choisir entre `str` et `bytes`
# * quand et comment convertir 

# %% [markdown] slideshow={"slide_type": "slide"}
# ### le problème

# %% [markdown]
# * dès que vous échangez avec l'extérieur, i.e.
#   * Internet (Web, mail, etc.)
#   * stockage (disque dur, clef USB)
#   * terminal ou GUI, etc..
# * vous devez traiter des flux **binaires**
#   * et donc vous êtes confrontés à l'encodage des chaines
#   * et notamment en présence d'accents
#   * ou autres caractères non-ASCII

# %% [markdown] slideshow={"slide_type": "slide"}
# ### contenus binaires et textuels

# %% [markdown] slideshow={"slide_type": ""}
# * toutes les données ne sont pas textuelles
#   * exemple : fichiers exécutables comme `cmd.exe`
#   * stockage de données propriétaires
# * dès qu'on utilise des données textuelles,
#   * on décode une suite de bits
#   * il faut leur **donner un sens**
#   * c'est l'encodage

# %% [markdown] slideshow={"slide_type": "slide"}
# ### codage et décodage en python

# %% [markdown]
# ![](media/str-bytes.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### de multiples encodages

# %% [markdown]
# * au fil du temps on a inventé plein d'encodages
# * le plus ancien est l'ASCII (années 60!)
# * puis pour étendre le jeu de caractères
#   * iso-latin-*
#   * cp-1252 (Windows)
# * et plus récemment, Unicode et notamment UTF-8
#
# aujourd'hui en 2020
# * **privilégier UTF-8** qui devrait être l'encodage par défaut pour tous vos appareils
# * mais le choix de l'encodage revient toujours en fin de compte au programmeur  
#   même lorsqu'il fait le choix de s'en remettre au paramétrage de l'OS

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Unicode

# %% [markdown]
# * ***une*** liste des caractères 
#   * avec **chacun un *codepoint*** - un nombre entier unique
#   * de l'ordre de 137.000 + en Juin 2018 (*and counting*)
#   * limite théorique 1,114,112 caractères
#
# * ***trois*** encodages:
#     * **UTF-8**: taille variable 1 à 4 octets, **compatible ASCII**
#     * UTF-32: taille fixe, 4 octets par caractère
#     * UTF-16: taile variable, 2 ou 4 octets

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/unicode-table.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/unicode-decode-example.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### UTF-8

# %% [markdown]
# * le nombre d'octets utilisé pour encoder un caractère dépend
#   * du caractère et de l'encodage
#   * texte ASCII : identique en UTF-8    
#   * en particulier, ne prennent qu'un octet

# %% [markdown] slideshow={"slide_type": ""}
# ![](media/unicode-utf8-areas.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Unicode et Python: `chr` et `ord`

# %% [markdown] cell_style="split"
# ![](media/unicode-e-accent.png)

# %% cell_style="split"
# le codepoint du é accent aigu
codepoint = 0xe9
codepoint

# %% cell_style="split"
chr(codepoint)

# %% cell_style="split"
ord('é')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `encode` et `decode`

# %% cell_style="split"
text = 'été\n'
type(text)

# %% cell_style="split"
# on compte les 
# caractères 

len(text)

# %% cell_style="split"
# on sait formatter ;)
octets = text.encode(encoding="utf-8")
for b in octets:
    print(f"{b:02x}", end=" ")

# %% cell_style="split"
# ici par contre on
# compte les octets

len(octets)

# %% [markdown] slideshow={"slide_type": "slide"}
# ####  `encode` et `decode`

# %% cell_style="split"
# attention, la présentation des bytes
# à base de caractères n'est pas très lisible
octets

# %% cell_style="split"
# ici on a bien 6 octets
len(octets)

# %% cell_style="split"
octets.decode(encoding="utf-8")

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Martine Ã©crit en UTF-8

# %% [markdown] cell_style="split"
# ![](../media/martine-ecrit-en-utf8.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### pourquoi l’encodage c’est souvent un souci ?

# %% [markdown]
# * chaque fois qu'une application écrit du texte dans un fichier
#   * elle utilise un encodage
# * cette information (quel encodage?) est **parfois** disponible
#   * dans ou avec le fichier
#   * ex. `# -*- coding: utf-8 -*-`
#   * HTTP headers
# * mais le plus souvent on ne peut pas sauver cette information
#   * pas prévu dans le format
#   * il faudrait des **métadata**

# %% [markdown] cell_style="center"
# * du coup on utilise le  
#   plus souvent des heuristiques
# * comme d'utiliser une  
#   configuration globale de l'ordi
# * sans parler des polices de caractères..

# %% cell_style="center" slideshow={"slide_type": "slide"}
# Jean écrit un mail
envoyé = "j'ai été reçu à l'école"

# %% cell_style="center" slideshow={"slide_type": ""}
# son OS l'encode pour le faire passer sur le réseau
binaire = envoyé.encode(encoding="utf-8")

# %% slideshow={"slide_type": ""}
# Pierre reçoit le binaire
# mais se trompe d'encodage
reçu = binaire.decode(encoding="cp1252")

# %% slideshow={"slide_type": ""}
# Pierre voit ceci dans son mailer
reçu

# %% [markdown] slideshow={"slide_type": "slide"}
# ### mais le plus souvent ça marche !

# %% [markdown]
# * lorsqu’on travaille toujours sur la même machine, 
#   * si toutes les applications utilisent l'encodage de l'OS
#   * tout le monde parle le même encodage
# * le problème se corse
#   * dès qu'il s'agit de données externes

# %% [markdown] slideshow={"slide_type": "slide"}
# ### comment en est on arrivé là ?

# %% [markdown] cell_style="center"
# * le standard définit les 128 premières valeurs
#   * c’est l’ASCII classique
# * du coup pendant longtemps le modèle mental a été
#   * ***un char = un octet***
# * cf. le type `char` en C

# %% [markdown] cell_style="center"
# * pendant les années 1990 on a introduit un patch
#   * encodages comme `iso-latin1`, `cp1252`
#   * préserve l'invariant ***un char = un octet***
#   * au prix .. d'une multitude d'encodages

# %% [markdown] slideshow={"slide_type": "slide"}
# ### comment faire en pratique ?

# %% [markdown]
# * le défaut en Python est d'utiliser UTF-8
#   * pour les sources
#   * pour ouvrir les fichiers
# * on peut préciser l'encodage des sources avec
#   * `# coding: ascii` dans les sources
#   * pas utile donc si en UTF-8 - bien sûr recommandé
# * on peut (devrait) préciser l'encodage avec
#   * `str.encode()`, `bytes.decode()`, et `open()`
#   * le défaut dans ce cas va dépendre de l'OS !

# %% [markdown] slideshow={"slide_type": "slide"}
# #### configurer son éditeur de texte pour supporter Unicode/UTF-8

# %% [markdown]
# * notamment lorsque vous écrivez du code
# * il est important que votre éditeur
# * écrive bien vos fichiers source en **UTF-8**
# * de plus en plus c'est le cas par défaut
# * sinon il y a sans doute un réglage dans l'éditeur pour ça

# %% [markdown] slideshow={"slide_type": "slide"}
# #### configurer son éditeur de texte pour Unicode/UTF-8

# %% [markdown]
# * si votre éditeur sauve en autre chose qu’utf-8, vous devez obligatoirement ajouter la ligne suivante au début de votre fichier
# ```
#     # -*- coding: utf8 -*-
# ```
#
#   En remplaçant utf8 par l’encodage utilisé par votre éditeur

# %% [markdown] slideshow={"slide_type": "slide"}
# #### encodages par défaut

# %% cell_style="split"
# on connait l’encodage du terminal avec
import sys
sys.stdin.encoding

# %% cell_style="split"
# et dans l'autre sens
# 
sys.stdout.encoding

# %% cell_style="split"
# on connait l’encodage du système de fichier avec
sys.getfilesystemencoding()

# %% cell_style="split"
# et le réglage système par défaut
sys.getdefaultencoding()

# %% [markdown]
# en principe, au 21-ème siècle vous devez avoir utf-8 partout !

# %% [markdown] slideshow={"slide_type": "slide"}
# #### comment changer d'encodage ?

# %% [markdown]
# * on passe toujours par le type `bytes`

# %% cell_style="split"
# j'écris un mail
s = 'un été, à noël'
# il se fait encoder
b8 = s.encode()
b8

# %% cell_style="split"
# on envoie les bytes par mail
# si à l'arrivée on utilise le mauvais
s1 = b8.decode('latin1')
s1

# %% [markdown] slideshow={"slide_type": "slide"}
# ## outils annexes utiles

# %% [markdown] slideshow={"slide_type": "slide"}
# ### décodage dégradé

# %% [markdown]
# * pour ***décoder*** avec un encodage qui ne supporte pas tous les caractères encodés
# * `decode()` accepte un argument `error`
#   * `"strict"` (par défaut)
#   * `"ignore"` (jette le caractère non supporté)
#   * `"replace"` (remplace le caractère non supporté)

# %% cell_style="split"
octets = 'un été, à noël'.encode(encoding='utf-8')
octets.decode('ascii', errors='ignore')

# %% cell_style="split"
octets.decode('ascii', errors='replace')

# %% [markdown] slideshow={"slide_type": "slide"}
# ### encodage dégradé

# %% [markdown]
# * comment ***encoder*** avec un encodage qui ne supporte pas tous les caractères Unicode
# * `encode()` accepte un argument `error`, identique i.e.:
#   * `"strict"` (par défaut)
#   * `"ignore"` (jette le caractère non supporté)
#   * `"replace"` (remplace le caractère non supporté)

# %% cell_style="split"
s = 'un été, à noël'
s.encode('ascii', errors='ignore')

# %% cell_style="split"
s.encode('ascii', errors='replace')

# %% [markdown]
# ### Unicode vers ASCII
#
# * je veux convertir une chaîne Unicode en ASCII en convertissant en caractères proches
#   * dans la librairie standard `unicodedata.normalize`
#
#   * en librairie externe unidecode
#   * `pip install unidecode`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *deviner* l'encodage ?

# %% [markdown]
# * formellement : non
# * en pratique : avec des heuristiques
#
#   * par exemple avec la librairie externe chardet
#   * https://pypi.python.org/pypi/chardet

# %%
# !pip install chardet

# %%
# !chardetect ../data/une-charogne.txt

# %% [markdown] slideshow={"slide_type": "slide"}
# ### à savoir : le BOM

# %% [markdown] slideshow={"slide_type": ""}
# * le [`BOM` (byte order mark)](https://en.wikipedia.org/wiki/Byte_order_mark)  
#   est un mécanisme permettant de disambigüer  
#   entre les 3 encodages utf-8, utf-16 et utf-32
#
# * du coup si vous savez qu'un document est en Unicode  
#   mais sans savoir quel encodage au juste  
#   le BOM permet de le trouver

# %% [markdown] slideshow={"slide_type": "slide"}
# le BOM consiste à ajouter un header pour utf-16 et utf-32  
# qui crée une inflation artificielle
#   
#

# %% cell_style="split"
# en UTF-32:  1 char = 4 bytes
# donc on devrait voir 4
len("a".encode('utf32'))

# %% cell_style="split"
# les 4 premiers octets correspondent 
# à la constante 'UTF32-LE'
b = "a".encode('utf32')
b[:4]

# %%
# évidemment ce n'est ajouté qu'une seule fois
s1000 = 1000*'x'
len(s1000.encode('utf32'))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## petit retour sur le type `str`  

# %% [markdown] slideshow={"slide_type": ""}
# ### les chaines littérales

# %% [markdown]
# lorsqu'on veut écrire directement dans le programme  
# une chaine avec des caractères exotiques

# %% cell_style="split"
# entré directement au clavier
accent = 'é'
accent

# %% cell_style="split"
# copié collé
warn = '⚠'
warn

# %% cell_style="split"
# défini à partir de son codepoint
# si petit (un octet), format hexadécimal
'\xe9'

# %% cell_style="split"
# si plus grand, utiliser \u 
# pour les codepoints sur 2 octets
"\u26A0"

# %% [markdown] cell_style="center"
# Enfin `\Uxxxxxxxx` pour 4 octets, si codepoint encore plus grand (pas fréquemment utile)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un exemple

# %%
s = '\u0534\u06AB\u05E7\u098b\u0bf8\u0f57\u2fb6'
print(s)

# %% [markdown] slideshow={"slide_type": "slide"}
# avec ces trois notations '\x` `\u` et `\u` il faut bien sûr utiliser **exactement**, respectivement, 2, 4 ou 8 digits hexadécimaux.

# %%
# le retour chariot a pour code ASCII 10
print('\x0a')

# %% tags=["raises-exception"]
# je ne peux pas faire l'économie du 0 
try:
    print('\xa') # python n'est pas content
except:
    import traceback; traceback.print_exc()

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le type `bytearray` (avancé)

# %% [markdown]
# * c’est un objet similaire au type `bytes`, mais qui est **mutable**
# * on l’utilise lorsque l’on a besoin de modifier un objets `bytes`

# %% cell_style="split"
source = b'spam'
buff = bytearray(source)
buff

# %% cell_style="split"
# remplacer 'a' bar 'e'
buff[2] = ord('e')
buff

# %%
for char in buff:
    print(char, end=" ")

# %% [markdown] slideshow={"slide_type": "slide"}
# ### méthodes sur `bytearray`

# %% cell_style="split"
# méthode dans bytes 
# mais pas dans bytearray
set(dir(bytes)) - set(dir(bytearray))

# %% cell_style="split"
# méthode dans bytearray 
# mais pas dans bytes
set(dir(bytearray)) - set(dir(bytes))

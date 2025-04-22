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
  title: str et bytes
---

Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# données binaires

+++

## le type `bytes`

+++

### non mutable

* le type `bytes` correspond, comme son nom l'indique, à une séquence d'**octets**  
  donc entiers **entre 0 et 255**

* le type `bytes` est donc un autre exemple de **séquence** (comme `str`)
* c'est également un type **non mutable**

```{code-cell} ipython3
:tags: [gridwidth-1-2]

b = bytes([65, 66, 67])
b
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# non mutable !
try:
    b[1] = 68
except Exception as exc:
    print(f"OOPS - {type(exc)}\n{exc}")
```

+++ {"cell_style": "center"}

### littéral

pour construire un `bytes` on peut soit

* utiliser le constructeur `bytes()` - comme slide précédent
* lire un fichier ouvert en mode binaire - vu plus tard
* de manière littérale, mettre un `b` devant une chaîne de caractères

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# caractère -> code ASCII
b = b'AB\n'
b
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# ou sinon en hexa
b'\x41\x42\x0a'
```

+++ {"slideshow": {"slide_type": "slide"}}

````{admonition} les détails sordides
:class: dropdown

comme on le voit dans `b'AB\n'` , les octets d'un `bytes` sont parfois **représentés par des caractères ASCII**

  ```python
  # on peut écrire ceci
  b1 = b'ete'
 
  b2 = bytes(
      [ord('e'), ord('t'), ord('e')]
  )
  b1 == b2
  -> True
  ```

c'est pratique, mais ça peut être **source de confusion**  
car par exemple ceci ne **marcherait pas**
```python
>>> b'été'
         ^
SyntaxError: bytes can only contain ASCII literal characters.
```
````

+++

### un `bytes` est une séquence

* on manipule des objets `bytes` presque comme des objets `str`
* les bytes sont des séquences (donc indexation, slicing, ...)
* essentiellement les mêmes méthodes que pour les `str`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# les méthodes dans `str` mais pas dans `bytes`

set(dir(str)) - set(dir(bytes))
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# les méthodes dans `bytes` mais pas dans `str`

set(dir(bytes)) - set(dir(str))
```

## texte, binaire et encodage

* choisir entre `str` et `bytes`
* quand et comment convertir

+++

### codage et décodage en python

```{image} media/str-bytes.svg
:align: center
```

+++

### le problème

* dès que vous échangez avec l'extérieur, i.e.
  * Internet (Web, mail, etc.)
  * stockage (disque dur, clef USB)
  * terminal ou GUI, etc..
* vous devez traiter des flux **binaires**
  * et le plus souvent on **ne sait pas** si/comment le texte a été encodé
  * notamment crucial en présence d'accents ou autres non-ASCII
  * et donc vous êtes confrontés à l'**encodage** des chaines

+++ {"slideshow": {"slide_type": "slide"}}

### de multiples encodages

* au fil du temps on a inventé plein d'encodages
* le plus ancien est l'ASCII (années 60!)
* puis pour étendre le jeu de caractères
  * iso-latin-*
  * cp-1252 (Windows)
* et plus récemment, Unicode et notamment UTF-8

````{admonition} aujourd'hui en 2024: UTF-8
:class: dropdown

* **privilégier UTF-8** qui devrait être l'encodage par défaut pour tous vos appareils
* mais le choix de l'encodage revient toujours en fin de compte au programmeur  
  même lorsqu'il fait le choix de s'en remettre au paramétrage de l'OS
````

+++

## Unicode

### codepoints et 3 encodages

* ***une*** liste des caractères
  * avec **chacun un *codepoint*** - un nombre entier unique
  * de l'ordre de 150.000 + en Unicode-15.1 - sept. 2023l (*and counting*)
  * limite théorique 1,114,112 caractères

* ***trois*** encodages:
    * **UTF-8**: taille variable 1 à 4 octets, **compatible ASCII**
    * UTF-32: taille fixe, 4 octets par caractère
    * UTF-16: taille variable, 2 ou 4 octets

+++ {"slideshow": {"slide_type": "slide"}}

```{image} media/unicode-table.png
:align: center
:width: 600px
```

+++

### rappels: hexadecimal

```{image} media/hexadecimal.svg
:align: center
:width: 600px
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# an int, entered in hexa, printed in decimal
i1 = 0xe8; i1
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# or printed in binary
bin(i1)
```

```{code-cell} ipython3
# a bytes with one byte
b = b'\xe8'

# and so its only value as an int is
i2 = b[0]

# and there's the same indeed
i1 == i2
```

+++ {"slideshow": {"slide_type": "slide"}}

***

```{image} media/unicode-decode-example.png
:align: center
:width: 600px
```

+++

### UTF-8

* le nombre d'octets utilisé pour encoder un caractère dépend
  * du caractère et de l'encodage
  * texte ASCII : identique en UTF-8
  * en particulier, ne prennent qu'un octet

+++

```{image} media/unicode-utf8-areas.png
:align: center
:width: 600px
```

+++ {"tags": ["gridwidth-1-2"]}

### Unicode et Python: `chr` et `ord`

```{image} media/unicode-e-accent.png
:align: center
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# le codepoint du é accent aigu
codepoint = 0xe9
codepoint
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

chr(codepoint)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

ord('é')
```

+++ {"slideshow": {"slide_type": "slide"}}

## Martine Ã©crit en UTF-8

+++ {"tags": ["gridwidth-1-2"]}

```{image} ../media/martine-ecrit-en-utf8.png
:align: center
```

+++ {"cell_style": "center", "slideshow": {"slide_type": "slide"}}

### pourquoi l’encodage c’est souvent un souci ?

* chaque fois qu'une application écrit du texte dans un fichier
  * elle utilise un encodage
* cette information (quel encodage?) est **parfois** - mais pas toujours - disponible
  * dans ou avec le fichier
  * HTTP header - SMTP header
* mais **le plus souvent** on ne peut pas sauver cette information
  * notamment dans le cas usuel d'un fichier sur le disque dur !
  * il faudrait des **métadata**

* du coup on utilise le plus souvent **des heuristiques**
* comme d'utiliser une **configuration globale** de l'ordi
* sans parler des polices de caractères..

voyons comment on en arrive par exemple à recevoir un mail en gloubli-goulba  

```{code-cell} ipython3
:cell_style: center

# Jean écrit un mail

envoyé = "Martine écrit en UTF-8"
```

```{code-cell} ipython3
:cell_style: center

# son OS l'encode pour le faire passer sur le réseau

binaire = envoyé.encode(encoding="utf-8")
```

```{code-cell} ipython3
# Pierre reçoit le binaire mais son ordi
# est un vieux Windows mal configuré

reçu = binaire.decode(encoding="cp1252")
```

```{code-cell} ipython3
# Pierre voit ceci dans son mailer
reçu
```

### mais le plus souvent ça marche !

* lorsqu’on travaille toujours sur la même machine,
  * si toutes les applications utilisent l'encodage de l'OS
  * tout le monde parle le même encodage
* le problème se corse dès qu'il s'agit de **données externes**

+++ {"cell_style": "center"}

### comment en est on arrivé là ?

* le standard ASCII (1960) définit les 128 premières valeurs
* du coup pendant longtemps le modèle mental a été
  * ***un char = un octet***
* cf. le type `char` en C

* pendant les années 1990 on a introduit un patch
  * encodages comme `iso-latin1`, `cp1252`
  * préserve l'invariant *un char = un octet*
  * au prix .. d'une **multitude** d'encodages distincts

+++ {"slideshow": {"slide_type": "slide"}}

#### encodages par défaut

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# on connait l’encodage du terminal avec
import sys
sys.stdin.encoding
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et dans l'autre sens
#
sys.stdout.encoding
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# on connait l’encodage du système de fichier avec
sys.getfilesystemencoding()
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# et le réglage système par défaut
sys.getdefaultencoding()
```

en principe, au 21-ème siècle vous devez avoir utf-8 partout !

+++ {"slideshow": {"slide_type": "slide"}}

## partie pour les avancés

+++

### décodage dégradé

* pour ***décoder*** avec un encodage qui ne supporte pas tous les caractères encodés
* `decode()` accepte un argument `error`
  * `"strict"` (par défaut)
  * `"ignore"` (jette le caractère non supporté)
  * `"replace"` (remplace le caractère non supporté)

```{code-cell} ipython3
:tags: [gridwidth-1-2]

octets = 'un été, à noël'.encode(encoding='utf-8')
octets.decode('ascii', errors='ignore')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

octets.decode('ascii', errors='replace')
```

### encodage dégradé

* comment ***encoder*** avec un encodage qui ne supporte pas tous les caractères Unicode
* `encode()` accepte un argument `error`, identique i.e.:
  * `"strict"` (par défaut)
  * `"ignore"` (jette le caractère non supporté)
  * `"replace"` (remplace le caractère non supporté)

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s = 'un été, à noël'
s.encode('ascii', errors='ignore')
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

s.encode('ascii', errors='replace')
```

### Unicode vers ASCII

* je veux convertir une chaîne Unicode en ASCII en convertissant en caractères proches
  * dans la librairie standard `unicodedata.normalize`
  * en librairie externe unidecode  
    `pip install unidecode`

+++

### *deviner* l'encodage ?

* formellement : non
* en pratique : avec des heuristiques
* par exemple avec la librairie externe chardet [(voir sur pypi.org)](https://pypi.python.org/pypi/chardet)

```{code-cell} ipython3
!pip install chardet
```

```{code-cell} ipython3
!chardetect ../data/une-charogne.txt
```

### à savoir : le BOM

* le [`BOM` (byte order mark)](https://en.wikipedia.org/wiki/Byte_order_mark)  
  est un mécanisme permettant de disambigüer  
  entre les 3 encodages utf-8, utf-16 et utf-32

* du coup si vous savez qu'un document est en Unicode  
  mais sans savoir quel encodage au juste  
  le BOM permet de le trouver

+++ {"slideshow": {"slide_type": "slide"}}

le BOM consiste à ajouter un header pour utf-16 et utf-32  
qui crée une inflation artificielle

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# en UTF-32:  1 char = 4 bytes
# donc on devrait voir 4
len("a".encode('utf32'))
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# les 4 premiers octets correspondent
# à la constante 'UTF32-LE'
b = "a".encode('utf32')
b[:4]
```

```{code-cell} ipython3
# évidemment ce n'est ajouté qu'une seule fois
s1000 = 1000*'x'
len(s1000.encode('utf32'))
```

+++ {"slideshow": {"slide_type": "slide"}}

### petit retour sur le type `str`

+++

#### les chaines littérales

lorsqu'on veut écrire directement dans le programme  
une chaine avec des caractères exotiques

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# entré directement au clavier
accent = 'é'
accent
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# copié collé
warn = '⚠'
warn
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# défini à partir de son codepoint
# si petit (un octet), format hexadécimal
'\xe9'
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# si plus grand, utiliser \u
# pour les codepoints sur 2 octets
"\u26A0"
```

+++ {"cell_style": "center"}

et enfin, utilisez `\Uxxxxxxxx` pour 4 octets, si codepoint encore plus grand (pas fréquemment utile)

+++ {"slideshow": {"slide_type": "slide"}}

#### un exemple

```{code-cell} ipython3
s = '\u0534\u06AB\u05E7\u098b\u0bf8\u0f57\u2fb6'
print(s)
```

+++ {"slideshow": {"slide_type": "slide"}}

avec ces trois notations '\x` `\u` et `\u` il faut bien sûr utiliser **exactement**, respectivement, 2, 4 ou 8 digits hexadécimaux.

```{code-cell} ipython3
# le retour chariot a pour code ASCII 10
print('\x0a')
```

```{code-cell} ipython3
:tags: [raises-exception]

# je ne peux pas faire l'économie du 0
try:
    print('\xa') # python n'est pas content
except:
    import traceback; traceback.print_exc()
```

### le type `bytearray` (avancé)

* c’est un objet similaire au type `bytes`, mais qui est **mutable**
* on l’utilise lorsque l’on a besoin de modifier un objets `bytes`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

source = b'spam'
buff = bytearray(source)
buff
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# remplacer 'a' bar 'e'
buff[2] = ord('e')
buff
```

```{code-cell} ipython3
for char in buff:
    print(char, end=" ")
```

+++ {"slideshow": {"slide_type": "slide"}}

#### méthodes sur `bytearray`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# méthode dans bytes
# mais pas dans bytearray
set(dir(bytes)) - set(dir(bytearray))
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

# méthode dans bytearray
# mais pas dans bytes
set(dir(bytearray)) - set(dir(bytes))
```

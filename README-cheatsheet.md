# micro cheatsheet Python

- [micro cheatsheet Python](#micro-cheatsheet-python)
  - [nombres et atomes](#nombres-et-atomes)
  - [opérateurs - arithmétique](#opérateurs---arithmétique)
    - [affectation / opérateur](#affectation--opérateur)
    - [opérateurs logiques et comparaisons](#opérateurs-logiques-et-comparaisons)
    - [opérateurs exotiques](#opérateurs-exotiques)
  - [chaines](#chaines)
    - [création](#création)
    - [méthodes](#méthodes)
    - [formattage: f-strings](#formattage-f-strings)
  - [syntaxe](#syntaxe)
    - [`def`](#def)
    - [`class`](#class)
    - [`if`](#if)
      - [remarques](#remarques)
    - [`while`](#while)
    - [`for`](#for)
    - [affectations](#affectations)
  - [containers](#containers)
    - [listes](#listes)
    - [indexation et slicing](#indexation-et-slicing)
    - [tuples](#tuples)
    - [ensembles](#ensembles)
    - [dictionnaires](#dictionnaires)
  - [compréhensions et genexprs](#compréhensions-et-genexprs)
    - [compréhension de liste](#compréhension-de-liste)
    - [imbriquées](#imbriquées)
    - [d'ensemble](#densemble)
    - [de dictionnaire](#de-dictionnaire)
    - [expression génératrice](#expression-génératrice)
  - [import](#import)
  - [fichiers](#fichiers)
    - [open()](#open)
      - [en lecture](#en-lecture)
      - [en écriture](#en-écriture)
    - [`from pathlib import Path`](#from-pathlib-import-path)
      - [création](#création-1)
      - [navigation](#navigation)
      - [existence et type](#existence-et-type)
      - [ouverture](#ouverture)
      - [globbing (e.g. chercher "*.txt")](#globbing-eg-chercher-txt)
      - [métadonnées (taille, dates, etc...)](#métadonnées-taille-dates-etc)

## nombres et atomes

* entiers: précision arbitraire
* flottants: sur 64 bits, précision relative de l'ordre de $10^{15}$
* complexes: par exemple `z = 3+1j`; `z.real` et `z.imag`
* booléens: `True` et `False`
* spéciaux:
  * `None` (pas de résultat)
  * `...` (Ellipsis)

## opérateurs - arithmétique

```python
a + b           # addition de nombres
                # concaténation de séquences
a - b           # soustraction de nombres
                # différence d'ensembles
a * b           # multiplication de nombres
                # concaténation multiple si
                # * un des opérandes une séquence
                # * l'autre opérande un entier
a / b           # division FLOTTANTE sur les nombres
                # ajout d'un chemin sur les Path

a // b          # division entière (quotient)
a % b           # reste de la division entière (modulo)

a ** b          # exponentiation (a puissance b)
```

### affectation / opérateur

```python

a = 10          # affecte 10 à la variable a
                # qui est créée au besoin
a += 10         # a = a + 10
a -= 10         # idem a = a - 10
a *= 10         # ...
a /= 10
a //= 10
a %= 10
a **= 10
```

### opérateurs logiques et comparaisons

```python

a and b         # ET logique entre booléens
a or b          # OU logique entre booléens
not b           # NON logique entre booléens

a == b          # comparaison du contenu
a != b          # négation

a is b          # comparaison des objets
                # (même emplacement mémoire)
a is not b      # négation

a < b           # comparaison
a <= b          # ...
a > b
a >= b
10 <= a < 20    # on peut les chainer sans mettre le 'and'
```

### opérateurs exotiques

ces 3 premiers opérateurs sont assez rares en Python pur  
mais **très utilisés** en numpy/pandas  
pour fabriquer des masques (sélectionner des zones dans les données)

```python
a & b           # bitwise ET logique
a | b           # bitwise OU logique
~ a             # bitwise NOT logique

a << 10         # décalage à gauche bit à bit (division par 2**n)
a >> 10         # décalage à droite bit à bit (multiplication par 2**n)

```

## chaines

### création
```python
s = "du texte"  # avec " ou ' indifféremment
s = 'du texte'  #
s = """du       # multiligne - avec """ ou ''' indifféremment
  texte"""      #
```

### méthodes

```python
s.rstrip()      # supprime les espaces/newline/tab à la droite de la chaine
s.split()       # coupe en morceaux selon les espaces/neline/tab
s.split(';')    # coupe en morceaux selon un caractère
"--".join(L)    # recolle les morceaux de l'itérable L avec ce séparateur

s.replace(a, b) # remplace la chaine a par la chaine b
```

### formattage: f-strings

```python
f"bla {variable} bla"           # calcule l'expression entre {}
                                # (ici une simple variable, mais peut être
                                # n'importe quelle expression Python)
                                # et l'insère à la place des {}

f"bla {variable:.2f} bla"       # entre les deux {}, on peut insérer un :
                                # et dans ce cas-là on peut préciser un format
                                # ici: afficher le résulat avec seulement
                                # deux chiffres après la virgule

f"bla {variable:<15} bla"       # ce format indique de prendre en tout 15 caractères
                                # et de justifier à gauche
f"bla {variable:^15} bla"       # centrer
f"bla {variable:>15} bla"       # justifier à droite

f"bla {variable=} bla"          # si on écrit un '=' juste avant le :
                                # on obtient en sortit l'expression ET le résultat
                                # sous la forme par exemple 'variable=12'
```

## syntaxe

### `def`

```python
def foo(x, y):          # définit la fonction foo
    ...


foo(100, 300)           # appelle la fonction foo
```

### `class`

```python
class Foo:              # définit la class Foo

    def __init__(self, x, y):
        self.x = x
        ...

    def __repr__(self):
        return f"..."

    ...

foo = Foo(100, 300)     # crée un objet (une instance) 
                        # de la classe Foo
```

### `if`

```python
if expression1():           # les expressions sont évaluées seulement
    ...                     # si nécessaire
elif expression2():         # elif est optionnel
    ...                     # et possiblement multiple
else:                       # else est optionnel également
    ...
```

#### remarques

* un objet non booléen est considéré comme
  * `False`: si c'est un container vide (str, list, tuple, dict, set...)
  * `False`: si c'est un nombre nul
  * on lui applique `bool()` si c'est une instance de classe utilisateur

* il existe aussi une expression conditionnelle

```python
resultat = expression1() if some_test() else expression2()
```

### `while`

```python
while expression():
    ...
else:                       # optionnel - on passe par le bloc else
    ...                     # lorsque la boucle sort "proprement"
    ...                     # i.e. sans 'break'
```

### `for`

```python
for item in iterable:       # éviter le recours aux indices
    ...
else:                       # optionnel - on passe par le bloc else
    ...                     # lorsque la boucle sort "proprement"
    ...                     # i.e. sans 'break'
```


### affectations

```python
a = une_expression()        # affectation d'une variable

a = b = une_expression()    # les deux variables désignent le même objet

a, b = une_expression()     # unpacking
                            # affectation de plusieurs variables
                            # ici 2, mais peut être n
                            # le résultat de l'expression
                            # doit être un itérable de n objets

a, *b, c = une_expression() # extended unpacking
                            # un nombre fixe n de variables (ici 2)
                            # et UN attrape-tout (ici b) qui capture
                            # le reste de l'itérable résultat de
                            # l'expression à droite, qui doit donc
                            # contenir au moins n objets
```

## containers

### listes

```python
L = []          # liste vide
L = [0, 1, 2]   # création littérale dans le code

L.append(item)  # ajoute un élément au bout
x = L.pop()     # retourne le dernier élément qui est enlevé

item in L       # test d'appartenance (attention c'est LENT)
item not in L   # négation
```

### indexation et slicing

valable sur toutes les séquences (listes et chaines notamment)

```python
len(S)          # la taille - nombre d'éléments
S[i]            # élément à l'index i
S[i:j]          # slice entre i (inclus) et j (exclus)
S[i:j:k]        # pareil avec un pas

S[:]            # copie (superficielle) de la liste
S[::-1]         # copie renversée de la liste
```

### tuples

```python
T = ()          # tuple vide
T = (0,)        # tuple à un élément
T = 0,          # pareil, tuple à un élément
T = (0, 1, 2)   # création littérale dans le code
```

### ensembles

```python
S = set()       # ensemble vide
S = {0, 1, 2}   # création littérale dans le code
S.add(item)     # ajouter un élément
S.remove(item)  # enlever un élément

item in S       # test d'appartenance

S1 & S2         # intersection de deux ensembles
S1 | S2         # union de deux ensembles
S1 - S2         # différence de deux ensembles
```

### dictionnaires

```python
D = {}                     # dictionnaire vide
D = dict()                 # dictionnaire vide
D = {'un': 1, 'deux': 2}   # création littérale dans le code

D['un']                    # la valeur attachée à la clé `'un'`
D['trois'] = 3             # crée ou modifie la valeur associée
                           # à la clé `'trois'`

D.update(D2)               # ajoute dans D les clés/valeurs de D2

item in D                  # item est-il une clé de D ?

for k, v in D.items():     # parcourt tout le dictionnaire
    ...                    # avec k: la clé et v: la valeur
```

## compréhensions et genexprs

### compréhension de liste

```python
[expression(x) for x in iterable]               # compréhension de liste
[expression(x) for x in iterable if test(x)]    # idem avec filtre
```

### imbriquées

```python
[expression(x, y))
   for x in iter1
       if test1(x)
          for y in var2
              if test2(x, y)]
```

### d'ensemble

```python
{expression(x) for x in iterable}               # compréhension d'ensemble
                                                # mêmes variantes (if / imbrication)
```

### de dictionnaire

```python
{ k(x): v(x) for x in iterable}                 # compréhension de dictionnaire
                                                # mêmes variantes (if / imbrication)
```

### expression génératrice

un itérateur sur ce qui serait dans la compréhension de liste

```python
(expression(x) for x in iterable)               # expression génératrice (*genexpr*)
```

*exemple typique*
```python
# la somme des carrés des éléments de l'iterable
sum(x**2 for x in iterable)                     # pas besoin de doubler les ()
```

## import

```python
import math           # définit la variable math
                      # et après je peux écrire math.pi
                      # ou math.sin(x) etc...
from math import pi   # définit la variable pi

import numpy as np    # définit la variable np
                      # et après j'écris np.ndarray
```

## fichiers

### open()

#### en lecture

```python
#                        ↓↓↓                # le mode d'ouverture 'r'
with open("fichier.txt", "r") as reader:    # ouvrir le fichier
    for line in reader:                     # itérer ligne à ligne
        line = line.rstrip()                # enlever le '\n' éventuel
        ...
# le fichier est automatiquement fermé
# à la fin du with
```

#### en écriture

```python
#                        ↓↓↓                # le mode d'ouverture 'w'
with open("fichier.txt", "w") as writer:    # ouvrir le fichier
    print("une ligne", file=writer)         # tout comme le print() terminal
                                            # donc notamment ajouter un newline
    # -- ou --
    writer.write(chaine)                    # dans ce cas pas d'ajout de newline
# le fichier est automatiquement fermé
# à la fin du with
```

### `from pathlib import Path`

#### création

```python
path = Path("dossier")          # création à partir du nom de fichier
path = Path.cwd()               # le dossier courant
path = Path.home()              # le dossier utilisateur
```

#### navigation

```python
path = otherpath / "chemin"     # l'opérateur / pour naviguer
path.drive                      # utile sur Windows
path.parent                     # un Path qui désigne le dossier père
path.parents                    # un itérateur sur les ancêtres
path.name                       # le nom du fichier dans le dossier père

path.absolute()                 # un Path avec un chemin absolu
                                # pour désigner le même fichier
```

#### existence et type

```python
path.exists()                   # existe-t-il ?
path.is_dir()                   # est-ce un dossier ?
path.is_file()                  # est-ce un fichier ordinaire ?
```

#### ouverture
```python
with path.open('r') as reader:              # on peut ouvrir directement un objet Path
    ...                                     # et là reader s'utilise comme ci-dessus
```

#### globbing (e.g. chercher "*.txt")
```python
for file in path.glob("*.txt"):             # itère sur les fichiers (immédiatement)
    # ici file est un Path                  # dans un dossier

for file in path.glob("**/*.txt"):          # pareil mais sur tous les fichiers
                                            # dans le dossier ou un de ses sous-dossiers
                                            # à n'importe quelle profondeur
```

#### métadonnées (taille, dates, etc...)

```python
path.stat().st_size                         # la taille
path.stat().st_mtime                        # date de dernière modification
```

---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
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
  title: hello world
rise:
  scroll: true
---

# premiers pas

+++

## hello world

+++

notre tout premier programme: éditez un fichier `hello.py` qui contient juste

```python
print("hello world")
```

on l'exécute depuis le terminal avec (ne pas taper le signe `$`, c'est l'invite...)
```bash
$ python hello.py
```

qui va nous afficher dans le terminal
```console
hello world
```

+++

### que retenir ?

* ici le mot `print` désigne une **fonction** - prédéfinie dans Python
* on **appelle** cette fonction - avec la syntaxe `print()`  
  en lui passant un **paramètre** - ici la chaine de caractères `"hello world"`
* on peut construire une chaine de caractères entre deux `"`  
  (et aussi d'ailleurs entre deux `'` si on préfère)

+++

## hello guys

+++

on s'enhardit, on dit bonjour à plusieurs personnes; pour cela on modifie notre code pour y mettre
```
# on peut écrire des commentaires
# après le signe #
# qui ne seront pas exécutés
print("hello Alice")
print("hello Bob")
print("hello Charlie")
```

+++

on le fait tourner:
* comment on fait déjà ?
* il va se passer quoi ?

+++

### que retenir ?

* quand on exécute un fichier `.py` avec Python, toutes les instructions qui y sont présentes sont exécutées dans l'ordre, jusqu'à ce qu'on rencontre la fin du fichier, et à ce moment-là python s'arrête (et on dit qu'il *rend la main* au terminal)
* après le signe `#` le texte du programme est considéré comme un commentaire

+++

## ma première variable

+++

essayons maintenant ceci

```python
name = "Alice"
print(f"hello {name}")
name = "Bob"
print(f"hello {name}")
name = "Charlie"
print(f"hello {name}")
```

qu'est-ce que ça va faire d'après vous ?

+++

### que retenir ?

* on peut définir des **variables** - ici `name` est une variable  
  pas besoin de les déclarer, simplement lui affecter une valeur avec le signe `=`
* on peut fabriquer une chaine qui **contient la valeur** d'une variable  
  c'est la notion de **f-string**:  
  la chaine commence avec `f"`  (ou `f'` si on préfère)  
  se termine avec un `"` (ou `'` si on préfère, vous avez compris l'idée générale..)  
  et peut contenir **entre `{}`** un nom de variable  
  du coup les **`{}`** sont remplacés par la valeur de la variable
* on verra d'ailleurs qu'on peut mettre du code plus compliqué que juste une variable entre les `{}` - mais n'anticipons pas

+++

## ma première fonction

+++

comme on a plusieurs fois la même phrase, on va essayer de *factoriser* le code; et pour ça on va utiliser une **fonction**

+++

```python
def hello_name(name):
    print(f"hello {name}")

hello_name("Alice")
hello_name("Bob")
hello_name("Charlie")
```

+++

### que retenir ?

* on définit une fonction avec `def function_name(...):`  
  pas besoin de begin/else ou autres, c'est l'**indentation** qui définit le bloc de code qui fait partie de la fonction

* l'instruction `def` indique combien elle prend de **paramètres**
* on appelle la fonction avec le bon nombre d'**arguments**
  qui sont passés à la fonction dans le même ordre  
  (en fait c'est bcp + compliqué que ça mais pour l'instant...)
* un paramètre c'est en fait une **variable**  
  qui est **visible** dans tout le corps de la fonction
* donc la chaine `"Alice"` est **passée en paramètre** à `hello_name`
  qui "voit" cette chaine au travers de la variable `name`
* de cette façon on peut **réutiliser**: refaire plusieurs fois le même traitement,
  sur des valeurs différentes, sans avoir à répéter le code

+++

## ma première boucle

+++

continuons à factoriser, on va maintenant écrire ceci qui fait toujours la même chose

+++

```python
def hello_name(name):
    print(f"hello {name}")

for name in ["Alice", "Bob", "Charlie"]:
    hello_name(name)
```

+++

### que retenir ?

* en Python on peut fabriquer des **listes** (entre `[]`)
* une liste peut contenir autant de valeurs qu'on veut, des types qu'on veut (même pas besoin que ce soit homogène)
* on peut **itérer** sur une liste en faisant simplement

  ```python
  for item in une_liste:
     du code
     qui travaille sur item
  ```

+++

### pour vous faire réfléchir

que se passerait-il à votre avis si j'avais écrit ma boucle plutôt comme ceci

```python
for name in ["Alice", "Bob", "Charlie"]:
    hello_name("name")
```

+++

## on coupe en deux fichiers

### naïvement

maintenant on décide que la fonction `hello_name` est tellement intéressante qu'elle pourrait être utile à d'autres projets ou applications; si on la laisse dans ce morceau de programme, on ne pourra pas s'en reservir ailleurs, du coup on coupe notre code en deux

* dans le fichier `separate.py` je mets le corps de la fonction

  ```python
  def hello_name(name):
      print(f"hello {name}")
  ```

* du coup dans `hello.py` il ne me reste plus que

  ```python
  for name in ["Alice", "Bob", "Charlie"]:
      hello_name(name)
  ```

question:

* si j'essaie de faire tourner le programme `hello.py` comme ça, à votre avis il va se passer quoi ?

+++

### la bonne façon: avec `import`

eh oui vous avez trouvé, ce code-là ne fonctionne pas, car Python ne "voit" que `hello.py` et il ne sait pas ce que signifie `hello_name`

il ne va quand même pas regarder dans tous les fichiers `.py` de l'ordinateur pour trouver la définition de cette fonction !

du coup il faut l'aider un peu, et pour ça nous avons l'instruction `import`

modifions `hello.py` pour y mettre

```python
# rappel, on a mis le code de hello_name
# dans le fichier separate.py
import separate

for name in ["Alice", "Bob", "Charlie"]:
    separate.hello_name(name)
```

et cette foi ça fonctionne

+++

### que retenir ?

* il y a des fonctions prédéfinies (comme `print`)
* on peut aussi utiliser des fonctions qui sont écrites dans d'autres fichiers, il faut alors les **importer**
  * en indiquant dans quel fichier (on parle de module) elles se trouvent
* lorsqu'on écrit `import separate` cela a pour effet de définir une variable `separate`
  * ensuite on peut aller "piocher" dans le module en faisant `separate.hello_name`

+++

## `import` d'une librairie système

+++

j'écris ceci dans `hello.py` (indice: ce programme fonctionne très bien)

```python
import math

import separate

for name in ["Alice", "Bob", "Charlie", 3*math.pi]:
    separate.hello_name(name)
```

que pensez-vous que va faire maintenant notre programme ?

+++

### que retenir ?

* avec `import` on peut importer du code venant d'un fichier dans le dossier courant
* **ou aussi** un module qui n'est pas à moi
  * ici le module `math` fait partie de la *librairie standard* (il "vient avec" Python)
  * mais ce serait pareil avec du code installé depuis Internet
* remarquez aussi (pour les geeks) qu'on peut passer à `hello_name`
  un peu ce qu'on veut (une chaine, un nombre...)

+++

## ma première classe

+++

on change complètement de paradigme et maintenant on écrit ceci

```python
# dans separate.py

class Person:

    def __init__(self, name):
        self.name = name
    def hello(self):
        print(self.name)
```

et

```python
# dans hello.py

from separate import Person

for name in ["Alice", "Bob", "Charlie"]:
    person = Person(name)
    person.hello()
```

+++

### que retenir ?

* ici on crée une classe `Person` qui est une usine à fabriquer des objets
* on s'en sert pour fabriquer trois objets de type `Person`  
  lorsqu'on appelle `Person(name)` en fait on appelle `__init__(self, name)`  (le constructeur)
* sur lesquels on peut ensuite appeler une méthode `hello()`

* l'intérêt étant que l'instance `person` a capturé le nom, on n'a plus besoin de le repasser à `hello()`

+++

## une classe un peu plus riche

dans l'exemple précédent, on a utilisé une classe pour ranger une donnée (le nom)  
du coup l'intérêt n'est peut-être pas très manifeste

mais on peut aussi bien sûr utiliser cela pour "grouper" plusieurs données qui "vont ensemble"

```python
# dans separate.py

class Person:

    # le constructeur, pour initialiser
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
       print(f"Hello {self.name}, tu as {self.age} ans")
```

```python
# dans hello.py

persons = []

persons.append(Person("Alice", 25))
persons.append(Person("Bob", 22))
persons.append(Person("Charlie", 20))

for person in persons:
    person.hello()

# et ensuite si on voulait par exemple calculer
# la moyenne d'âge de cette micro-classe

total = 0
for person in persons:
    total = total + person.age
print(f"moyenne d'âge: {total / len(persons}")
```

+++

### que retenir ?

* une classe sert souvent à regrouper plusieurs données qui décrivent une entité
* ces "morceaux" (ici `name` et `age`) sont rangés dans l'objet (`self`) sous la forme d'**attributs**
* on accède à un attribut par la notation **`objet.attribut`**
* un attribut peut désigner une donnée (`self.name`) ou une méthode (`person.hello`)

+++

## conclusion

on a vu des exemples de

* fonction - prédéfinie ou pas
* module - fourni par Python ou pas
* classe - ici seulement une classe définie par nos soins, mais il y en a plein la librairie standard

ces 3 notions sont centrales pour la réutilisabilité du code Python

on a aussi vu des exemples de

* chaine de caractère (aussi appelée *string*)
* nombre - des entiers et des flottants
* liste, et on a pu construire
  * des listes de chaines
  * des listes mélangées (chaines et nombres); les listes en Python peuvent être complètement hétérogènes
  * des objets
  * dans tous les cas on a écrit nos boucles comme faisant

    ```python
    for item in iterable:
       bla
       bla
    ```

    et c'est comme ça comme fait la plupart du temps  
    (plutôt que d'itérer sur un index qui ensuite sert à aller chercher dans la liste)

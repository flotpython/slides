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
  title: variables, objets, types
rise:
  scroll: true
---

# variables, objets et types

+++

## Python est fortement typé (eh oui!)

+++

ce qu'on a pu remarquer d'après le notebook précédent

* on n'a jamais **déclaré** de variable (sauf, d'accord, les paramètres des fonctions)
* a fortiori on n'a pas eu besoin de **donner explicitement un type** à nos variables

+++

## déclaration de variable

en fait ce qui se passe avec Python c'est que

* le simple fait d'affecter une variable, si elle est inconnue à cet endroit-là, constitue une déclaration  
* à partir de là, la variable est connue dans toute la fonction - ou tout le module si elle est définie au *toplevel* du module

+++

## variables non typées

* les **variables** ne sont **pas typées**; on peut parfaitement écrire par exemple
  ```python
  a = "100"  # à ce stade a désigne une chaine
  a = int(a) # maintenant a désigne un entier !
  ```

* bien sûr ce **n'est pas** forcément une pratique **recommandée**, mais c'est tout à fait possible en Python  
  en tous cas c'est un exemple pédagogique pour les gens habitués aux **langages compilés**; il faut retenir que **les variables ne sont pas typées**

+++

## les objets sont tous typés

**par contre**:

* **toutes** les données que vous manipulez dans la mémoire en Python sont **des objets**
* et chaque objet de la mémoire
  * **possède un type** (on peut y accéder avec `type(object)` - dont le retour .. est un objet ;)
  * ce type ne changera plus jamais durant la durée de vie l'objet

```{code-cell} ipython3
# illustration
# je tape ça dans mon notebook
# ceux qui veulent utiliser leur installation locale peuvent faire
# ça dans ipython

a = 10
type(a)
```

```{code-cell} ipython3
b = "une chaine"
type(b)
```

```{code-cell} ipython3
import math
type(math)
```

```{code-cell} ipython3
def hello(n):
    print(f"Hello {n}")
type(hello)
```

```{code-cell} ipython3
class Person:
    def __init__(self, name):
        self.name = name

type(Person)
```

## objets mutables ou pas

```{code-cell} ipython3
%load_ext ipythontutor
```

### non mutable (par ex, un entier)

+++

le type `int` n'est **pas mutable** (immutable donc)  
qu'est-ce que ça signifie ?  
une foix l'objet créé, on ne **peut plus le modifier**

```{code-cell} ipython3
%%ipythontutor heapPrimitives=true

a = b = 1

a += 1
```

que se passe-t-il sur cet exemple ?

* on crée un entier '1', et les deux variables le désignent  
  on dit aussi:
  * `a` "pointe vers" l'objet 1, ou encore 
  * `a` référence l'objet 1
* si je change a, en fait je ne **peux pas changer** l'objet 1, car il se trouve que les entiers ne sont **pas mutables**
* du coup, Python va créer un **autre objet** 2  
  et `a` va désigner ce nouvel objet  
  alors que `b` continue de désigner l'objet initial 1

+++

### mutable (par ex: liste)

+++

le type `list` par contre est mutable; ça veut dire, on peut par exemple ajouter une entrée à la fin d'une liste avec la méthode `append`

du coup on peut faire ceci

```{code-cell} ipython3
%%ipythontutor heapPrimitives=true

a = b = [1]

a.append(2)

print(b)
```

## les *type hints*

+++

* depuis Python 3.5, ***on peut***, si on veut, sous-titrer le ***type attendu*** des variables
* la présence de ces *type hints* **ne change rien** du tout au fonctionnement du programme  
  c'est-à-dire que le programme fonctionnne **exactement** comme si on avait enlevé les *type hints*
* alors "à quoi ça sert ?" me direz-vous ?
  * documentation
  * vérification de cohérence, mais avec des outils externes (`mypy`)
* et pour être honnête, c'est vraiment lisse seulement depuis la 3.9  
  ce qui explique qu'on en trouve encore relativement peu dans la nature

```{code-cell} ipython3
# le type hint est ici
#     ↓↓↓↓↓↓↓↓↓↓↓
names : list[str] = ["Alice", "Bob", "Charlie"]

# et ici           ↓↓↓↓↓  ↓↓↓↓↓↓↓  
def hello_name(name: str) -> None:
    print(f"hello {name}")    
```

```{code-cell} ipython3
# avec ce code on peut toujours faire
hello_name("paul")
```

```{code-cell} ipython3
# mais aussi !
hello_name(100)
```

## que retenir ?

* les **variables** ne sont **pas typées**
* mais tout est objet (même fonctions, modules, classes, ...)  
  (tout = tout ce que vous créez comme donnée dans la mémoire)
* et tous les **objets sont typés**
* certains **types** d'objet sont **mutables** et d'autres non

et aussi à propos des *type hints*

* on **peut** si on veut donner le type **attendu** des variables (et donc des paramètres de fonction, entre autres)
* cela n'a **qu'une valeur indicative**, c'est ignoré par le run-time
* mais c'est utile pour **la documentation** (et plus généralement, la facilité de comprendre / utiliser votre code)
* et aussi, ça **peut** être vérifié par des outils externes

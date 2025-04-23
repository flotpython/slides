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
  title: exceptions
---

# exceptions

+++

## c'est quoi ?

il s'agit d'un mécanisme pour gérer les situations exceptionnelles, comme par exemple

```{code-cell} ipython3
:cell_style: center
:tags: [raises-exception]

# on ne peut pas diviser par 0

1 / 0
```

```{code-cell} ipython3
:tags: [raises-exception]

# on ne peut pas ouvrir un fichier qui n'existe pas

with open("will-not-open.txt") as f:
    pass
```

## pourquoi ?

comme vous le voyez sur ces exemples, on ne peut **pas vraiment** gérer ces situation en **retournant un code d'erreur**:

- à la rigueur dans le premier cas on pourrait imaginer renvoyer `math.nan` ou encore `math.inf`
- mais comment gérer le deuxième exemple ?

idéalement, on veut un mécanisme où le souci peut être réglé, soit par la fonction elle-même, ou sinon par l'appelant de la fonction, ou par l'appelant de l'appelant, etc..  
(un peu comme dans un workflow humain, pensez: une banque; si le souci ne peut pas être réglé par votre conseiller, on va en parler au chef d'agence, à son chef, etc..)

+++

## exception et pile d'exécution (1)

dans ce genre de situations exceptionnelles, le langage va "lever une exception" (en anglais, lever = *raise*)  
ça veut dire quoi ? voici ce qu'il va se passer:  

dans le cas général on est dans une fonction qui a été appelée par une fonction qui a été appelée...  
lorsqu'il y a exception, on commence par **interrompre brutalement** l'exécution

voyons pour commencer le cas où l'on n'a pas *attrapé* l'exception:  

````{admonition} lancé depuis le terminal
:class: admonition-small
ça n'a pas une grande importance, mais pour être bien clair, dans ce qui suit, on suppose qu'on lance depuis le terminal un programme `foo.py` qui lance une fonction `main()` qui appelle `driver()`  
tout ça c'est juste pour simuler une certaine profondeur dans les appels de fonction..
````

```{code-cell} ipython3
:cell_style: center

# une fonction qui va faire raise
# mais pas tout de suite

def time_bomb(n):
    if n > 0:
        return time_bomb(n-1)
    else:
        raise OverflowError("BOOM")
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
tags: [raises-exception, gridwidth-1-2]
---
# si on essaye de l'exécuter
# ça se passe mal

def driver():
    time_bomb(1)
    # 
    print("will never pass here")

driver()     
```

+++ {"tags": ["gridwidth-1-2"]}

```{image} media/except-stack-uncaught.svg
:align: center
:width: 250px
```

+++

## l'instruction `try` .. `except`

comme vous pouvez le voir sur la première figure, on regarde dans la pile des appels, pour voir si à un moment donné on a *attrapé* l'exception; dans ce premier cas de figure, ça n'a pas été fait et le programme s'interrompt totalement (on retourne carrément dans le terminal !)

comment faire alors ?  
c'est là qu'intervient l'instruction `try .. except` qui va nous permettre d'*attraper* l'exception  

dans sa version la plus simple, elle se présente comme ceci:

```{code-cell} ipython3
# une instruction `try except` permet de capturer une exception

def divide(x, y):
    try:
        res  = x / y
        print(f"division OK {res=}")
    except ZeroDivisionError:
        print("zero divide !")
    print("continuing... ")
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

divide(8, 4)
```

```{code-cell} ipython3
:tags: [gridwidth-1-2]

divide(8, 0)
```

## exception et pile d'exécution (2)

voyons maintenant la logique de l'exception dans le contexte d'appels, éventuellement profonds  
si on attrape l'exception, notre premier exemple devient ceci:

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
tags: [gridwidth-1-2]
---
def driver_try():
    try:
        time_bomb(2)
        print("not here")
    except Exception as exc:
        print(f"OOPS {type(exc)}, {exc}")
    # et on passera bien ici
    print("the show must go on")
    
driver_try()    
```

+++ {"tags": ["gridwidth-1-2"]}

```{image} media/except-stack-try.svg
:align: center
:width: 300px
```

+++

## l'instruction `raise`

pour compléter le tableau, on peut aussi signaler une condition exceptionnelle avec l'instruction `raise`

```{code-cell} ipython3
# je veux vérifier qu'on me passe bien ce que j'attends
# j'utilise l'exception prédéfinie 'ValueError', c'est exactement son propos

def set_age(person, age):
    if not isinstance(age, int):
        raise ValueError("a person's age must be an integer")
    person['age'] = age
```

```{code-cell} ipython3
:cell_style: center
:tags: [raises-exception]

person = dict()

set_age(person, '10')
```

## hiérarchie des exceptions

la clause `raise` doit fournir un objet idoine: ce doit être une instance de `BaseException`  
par exemple on ne pourrait pas faire `raise 1`

````{admonition} les sous-classes de BaseException

```{image} media/except-list.png
:align: center
:width: 500px
```

<https://docs.python.org/3/library/exceptions.html#exception-hierarchy>
    
````

+++

## la clause `except`

et du coup on utilise cette hiérarchie pour n'attraper qu'**une partie** des exceptions possibles  
dans sa forme la plus générale, elle ressemble à ceci

```python
# les différentes formes de except
try:
    bloc
    de code
except ExceptionClass:        # les instances de
    bloc                      # ExceptionClass
    de rattrapage           
except (Class1, .. Classn):   # comme avec isinstance
    ...
except Class as instance:     # donne un nom à l'objet 
    ...                       # levé par raise
except:                       # attrape-tout - déconseillé
    ...
```    

où on voit que:

* on peut mettre plusieurs `except` après un `try:` chacune attrape **une partie** seulement des classes
* la **première** qui convient est la bonne, et on retourne à un régime non exceptionnel
* si **aucune** ne convient: l'exception se propage dans la pile - comme si on n'avait pas mis le `try:`

+++

````{admonition} attrape-tout ?
:class: admonition-small

le fait de capturer **toutes** les exceptions - avec `except:` ou `except Exception:`  
est généralement considéré comme une **mauvaise idée**!  

il vaut mieux comprendre ce que l’on capture  
car sinon on risque de **rendre silencieuses** d'autres exceptions qui pourtant méritent d'être traitées

on développe ce sujet un peu plus bas, cherchez "traceback"
````

+++

## comment utiliser l'object exception

l'object exception (celui qu'on a donné à `raise`) contient généralement des informations utiles à mieux comprendre ce qu'il se passe  
c'est pourquoi `except` est généralement utilisée sous sa forme `except .. as` qui permet d'inspecter le contenu

selon le type de l'exception, on va trouver les détails dans des attributs, et toujours au moins l'attribut `args`

+++ {"slideshow": {"slide_type": "slide"}}

### exemple de `except .. as`

```{code-cell} ipython3
# imaginez que l'exception se produise au 4-éme appel dans la pile
# et que nous on n'a aucune idée du fichier qu'on est en train d'essayer d'ouvrir
try:
    with open("inexisting-filename") as f:
        ...
except IOError as exc:
    print(f"le type: {type(exc)}")
    print(f"l'exception elle-même {exc}")
    print(f"les arguments {exc.args}")
    # si on veut aller plus loin on peut faire un peu d'introspection
    # comme d'hab on va ignorer les attributs spéciaux
    attributes = [symbol for symbol in dir(exc) if not '__' in symbol]
    print(f"les attributs {attributes}")
    print(f"du coup {exc.filename=} et {exc.strerror=}")
```

## les exceptions sont efficaces

voici une manière décente pour ouvrir un fichier; le code est beaucoup plus concis et efficace  
que de tester si le fichier existe, si ça n’est pas un répertoire, si on a les droits d’écriture, etc.

```{code-cell} ipython3
try:
    with open('fichier-inexistant', 'r') as feed:
        for line in feed:
            print(line)
except OSError as err:
    print(err)
    print(err.args)
    print(err.filename)
```

````{admonition} le reste est pour les avancés
:class: warning

en première lecture vous pouvez vous arrêter ici, la suite couvre des aspects plutôt avancés de l'importation

````

+++

## notions avancées

+++

### `try` .. `else` 

un peu comme avec `for` et `while`, on peut assortir le `try` d'une clause `else`  
qui est exécutée **uniquement s’il n’y a pas eu d’exception**

````{admonition} xxx

une exception dans la clause `else` n’est pas capturée par les `except` précédents
````

```{code-cell} ipython3
def divide(x,y):
    try:
        res  = x / y
    except ZeroDivisionError:
        print('zero divide !')
    else:
        print('all right, result is', res)
    print('continuing... ')
```

```{code-cell} ipython3
divide(8, 3)
```

```{code-cell} ipython3
divide(8, 0)
```

````{admonition} assez peu utilisé
:class: admonition-small

en pratique toutefois, c'est peu utilisé  
ici par exemple, on obtient exactement le même comportement
si on écrit le `print('continuing...')` à la fin du bloc `try:`
    
```python
def divide(x,y):
    try:
        res  = x / y
        print('all right, result is', res)
    except ZeroDivisionError:
        print('zero divide !')
    print('continuing... ')
```    
````

+++

### `try` .. `finally`

**une instruction `try` peut avoir une clause `finally`**

* cette clause est **toujours** exécutée
  * si il n'y a aucune exception
  * si il y a une exception attrapée
  * si il y a une exception non attrapée
  * et même s'il y a un `return` dans le code !
* elle sert à faire du nettoyage après l’exécution du bloc try
  * par exemple fermer un fichier

```{code-cell} ipython3
def finally_trumps_return(n):
    try:
        return 2 / n
    finally:
        print("finally is invicible !")
```

```{code-cell} ipython3
:tags: [raises-exception]

finally_trumps_return(0)
```

### instruction `raise`

on n'a vu jusqu'ici la que sa forme usuelle `raise instance`  
il existe aussi deux formes plus tarabiscotées:

* `raise` tout court   
  c'est la forme usuelle pour **propager** depuis un `except` l'exception originale, qui reste **intacte**

* `raise new_instance from original_exc`
  pour **propagation** avec modification

+++

### exception personnalisée

on peut bien souvent utiliser une des exceptions prédéfinies (comme `ValueError` ci-dessus)  
mais parfois c'est intéressant de se définir ses propres exceptions

pour cela rien de plus simple:

* dans la majorité des cas, on a uniquement besoin
  * d’un nom d’exception explicite finissant par `Error`
  * d’un message d’erreur
* il suffit d'hériter de la classe `Exception` (ou une de ses sous-classes bien entendu)
  * par défaut, tous les arguments passés au constructeur  
    sont mis dans un attribut `args` (un tuple)

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
class SplitError(Exception):
    pass

x, y = 1, 'a'

try:
    raise SplitError('split error', x, y)
except SplitError as exc:
    print(exc.args)
```

### le module `traceback`

en production, on devrait normalement s'astreindre à ne pas du tout utiliser d'attrape-tout  

toutefois en développement, ce n'est pas évident de tout envisager du premier coup  
aussi on trouve une forme assez répandue: attrape-tout avec instrumentation

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
import traceback

try:
    # un gros code; difficile de dire 
    # a priori toutes les exceptions
    # qui peuvent se produire
    pass
except OSError as exc:
    print(f"pour celle-ci je sais quoi faire {exc}")
except KeyboardInterrupt:
    print("pour celle-ci aussi")
except:
    # je suis tout près du main(), je ne veux pas laisser 
    # passer l'exception car ça se terminerait mal
    import traceback
    traceback.print_exc()
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# la même chose avec le module logging
# en vrai on ne fait jamais print()
import logging

logging.basicConfig(level=logging.INFO)


try:
    # un gros code; difficile de dire 
    # a priori toutes les exceptions
    # qui peuvent se produire
    logging.info("in the code")
    1/ 0
except OSError as exc:
    logging.error(f"pour celle-ci je sais quoi faire {exc}")
except KeyboardInterrupt:
    logging.info("pour celle-ci aussi: bye")
except:
    # je suis tout près du main(), je ne veux pas laisser 
    # passer l'exception car ça se terminerait mal
    logging.exception("exception inattendue")
```

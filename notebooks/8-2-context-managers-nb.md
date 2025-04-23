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
  title: context managers
---

+++ {"slideshow": {"slide_type": ""}}

# *context managers*

l'instruction `with .. as` s'utilise exclusivement avec des objets qui sont des ***context managers***
dans ce notebook on va approfondir cette notion

+++

Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

## déjà rencontré

où trouve-t-on des context managers ?  
eh bien par exemple, un objet fichier est un *context manager*

nous avons déjà vu qu'on peut utiliser un objet *fichier* - tel que renvoyé par `open()` - comme ceci
```python
with open("../data/une-charogne.txt") as mon_fichier:
    for l in mon_fichier:
        print(l)
```

ce qui garantit que le fichier OS est fermé automatiquement à la fin du `with` **quoi qu'il arrive** - qu'il se produise des exceptions ou non à l'intérieur du `with`

+++

## un peu plus formellement

lorsqu'on exécute un `with` qui a la forme générale suivante

```python
with expression [as variable]:
	with-block
    ...
```

* bien sûr on commence par évaluer l'expression
* puis on applique sur l'objet résutat le protocole de *context manager*

c'est-à-dire:

+++

### protocole *context manager* 

l’objet résultat de l'expression doit avoir deux méthodes `__enter__` et `__exit__`

* entrée dans le `with`:
    * à l’entrée du contexte, `__enter__(self)` est exécuté;
    * le retour de `__enter__` est assigné à la variable mentionnée dans le `.. as var`
* à ce stade le code *with-block* est executé
* sortie sans exception
  * `__exit__(self, None, None, None)` est appelée, toujours sur le *context manager*
* sortie en cas d'exception:
  * `__exit__(self, exc_type, exc_value, exc_traceback)` est appelé avec  
    `exc_type`, `exc_value`, `exc_traceback` sont les type, valeur et *traceback* (pile) de l’exception

  * le retour de `__exit__` est utilisé:  
    si `False` ➔ l’exception est relancée  
    si `True` ➔ l’exception est supprimée (étouffée)

  
````{admonition} un protocole ?
:class: attention

comme on le voit, c'est similaire dans le principe au protocole d’itération  
dans le sens où on avait également décortiqué [le comportement de la boucle `for`](label-for-under-the-hood) en faisant appel à des méthodes spéciales, avec des conventions spécifiques; c'est ce que Python appelle un *protocole*
````

````{admonition} try .. finally
:class: admonition-small

le lecteur attentif aura remarqué que ce meécanisme est une peu redondant fonctionnellement à la clause `try` .. `finally`  
en effet on pourrait aussi écrire notre ouverture de fichier comme ceci
```python
mon_fichier = open("../data/une-charogne.txt")
try:
    for l in mon_fichier:
        print(line)
finally:
    mon_fichier.close()
```
````

+++ {"slideshow": {"slide_type": "slide"}}

### exemple avec relance d’exception

```{code-cell} ipython3
# a context manager class that will raise the exceptions

class Raises():
    
    def __enter__(self):
        print("in enter()")
        return self

    def __exit__(self, *args):
        print(f"in exit: args={args}")
        return False   # relance l'exception
```

```{code-cell} ipython3
# because of that we still need to use a try .. except

import traceback

try:
    # we do not need the result, so no need for an 'as' clause
    with Raises():
        # purposefully triggering an exception
        1 / 0
except:
    print("OOPS - we catch the exception")
    traceback.print_exc()
```

```{code-cell} ipython3
# note that the exit phase is always called
with Raises():
    # no exception here
    pass
```

+++ {"slideshow": {"slide_type": "slide"}}

### exemple sans relance d’exception

```{code-cell} ipython3
# a context manager class that will block the exceptions

class Blocks():

    def __enter__(self):
        print("in enter()")
        return self

    def __exit__(self, *args):
        print(f"in __exit__: args={args}")
        return True  # this is how we say we want to block this exception
                     # of course in real code we could decide this depending
                     # on the exception itself
```

```{code-cell} ipython3
with Blocks():
    1 / 0
print("life goes on")    
```

## utilisations classiques

le plus souvent on va utiliser cette notion pour toutes les opérations un peu *transactionnelles*, où on doit proprement refermer les choses, ce qui correspond en pratique:
- à l'allocation / libération de ressources
- au temps long en terme d'OS, c'est à dire par exemple les accès réseau

typiquement, un *handle* d'accès à une **base de données** sera souvent exposé comme un *context manager*  
pareillement, les **protocoles réseau** offriront souvent une API de *context manager*, à la différence toutefois que dans ce cas ils seront *asynchrones*; mais là c'est encore un autre dossier complètement ...

+++

## `contextlib`

sachez enfin que la librairie `contextlib` expose un décorateur qui simplifie l'implémentation d'un *context manager*  
grâce à ce décorateur on s'économise la définition d'une classe, et obtenir un *context manager* **en décorant un générateur**, comme par exemple

```python
import contextlib

@contextlib.contextmanager
def custom_database_connector(url):
    session = ...   # how to connect to the DB
    yield session
    session.close()

with custom_database_connector("https://database.example.com/") as session:
    ... # do the DB black magic using session
```

+++

## utilisation originale

citons enfin un usage moins académique, mais intéressant aussi  
on peut utiliser un *context manager* pour **exécuter du code avant et après une opération**  
par exemple, pour mesurer le temps d’exécution, même en cas d’exception  
dans cet usage, c’est proche d’un décorateur

```{code-cell} ipython3
import time

class Timer():    

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        print(f"durée d'exécution = {self.end - self.start:2f}")
        return False
```

```{code-cell} ipython3
try:
    with Timer() as t:
        # do some stuff 
        [x ** 3 for x in range(100000)]
        # trigger an exception
        1 / 0
except:
    traceback.print_exc()
```

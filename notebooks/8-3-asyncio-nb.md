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
  title: asyncio / async / await
---

+++ {"slideshow": {"slide_type": ""}}

# `asyncio`

ou *la programmation asynchrone en Python*  
un sujet qui mériterait, ici encore, une formation à soi tout seul... donc ici on va se contenter d'un tout petit vernis

+++

## objectifs

faciliter l'écriture "de code parallèle de manière séquentielle":

* parallèle: on fait **plusieurs choses** en même temps
* séquentielle: ça se passe dans **un seul thread**

````{admonition} avertissement

le *runtime* des notebooks Jupyter utilise **aussi** la programmation asynchrone  
aussi il va arriver que l'on ne puisse **pas utiliser ici exactement le même code** que celui qu'on écrirait en pur Python, et on signalera alors la version à utiliser en pur Python 
````

+++

## *use cases*

on a coutume de ranger les applications en deux familles

* *CPU bound*: le programme fait exclusivement du calcul, la vitesse d'exécution est liée aux performances du processeur
* *I/O bound*: le programme fait principalement des entrées-sorties, la fait d'utiliser un processeur plus rapide ne se répercute pas sur les performances du programme

dans ce référentiel, la programmation asynchrone est **très adaptée** à la deuxième famille (d'où le `io` dans `asyncio`)

en effet, pour augmenter les performances d'une application *CPU bound*, on ne peut s'en tirer qu'en mettant en jeu plusieurs coeurs en même temps - d'où le recours au *multiprocessing* ou au *multithreading*  
par contre dans le cas des applications *I/O bound*, l'essentiel du temps le CPU ne fait rien que d'attendre que les I/O se terminent; du coup il est possible d'**accélérer très sensiblement** les performances, en se tournant vers un modèle *mono-threadé* mais qui *schedule* intelligemment les différents traitements, qui peuvent ainsi se dérouler en parallèle - en apparence au moins - tout en maximisant l'utilisation du CPU, et sans les risques de contamination liées au *multi-threading*

+++ {"slideshow": {"slide_type": "slide"}}

## un exemple

imaginons qu'on ait besoin de récupérer plusieurs URLs en parallèle

+++ {"slideshow": {"slide_type": "slide"}}

### version asynchrone

voici comment on pourrait s'y prendre avec `asyncio`

````{admonition} librairies spécialisées

le modèle de programmation est très différent du modèle impératif usuel; aussi on a besoin d'utiliser des **librairies idoines**  
par exemple ici, au lieu d'utiliser `requests` comme on le ferait avec du code "classique", on va utiliser pour les accès HTTP la librairie `aiohttp`, spécialement conçue pour fonctionner en asynchrone - comme le laisse entendre le préfixe `aio`  
d'autres librairies comme `asyncssh` ont choisi un nom encore plus explicite
````

```{code-cell} ipython3
# fait partie de la librairie standard
import asyncio

# pip install aiohttp
import aiohttp

# une fonction définie avec `async` est une 'coroutine'

async def asynchroneous(url):
    """
    a coroutine that fetches a URL and prints the number of bytes received
    """
    # un context manager peut être asynchrone lorsque les opérations
    # de 'enter' et 'exit' sont elles-mêmes asynchrones
    async with aiohttp.ClientSession() as session:
        print(f"fetching {url}")
        # idem ici, un autre CM asynchrone
        async with session.get(url) as response:
            print(f"{url} returned status {response.status}")
            # à l'intérieur d'une coroutine on peut - et
            # lorsqu'on appelle une autre coroutine, on doit
            # utiliser le mot clé 'await'
            raw = await response.read()
            print(f"{url} returned {len(raw)} bytes")
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# voici par exemple comment on peut lancer
# plusieurs coroutines en parallèle

async def main(urls):
    """
    Creates a group of coroutines and waits for them to finish
    """
    # the '*' thingy is just because gather expects all the futures
    # to be passed individually, rather than in a containers
    return await asyncio.gather(* (asynchroneous(url) for url in urls))
```

```{code-cell} ipython3
# the collection of URLs that we'll be fetching in parallel

urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]
```

````{admonition} notebook *vs* pur Python

pour appeler une fonction asynchrone depuis le code synchrone (typiquement depuis le point d'entrée de votre programme), 
en Python pur on écrirait ici

```python
asyncio.run(main(urls))
```

mais ici dans l'environnement des notebooks, comme on l'a signalé plus haut, on doit s'y prendre un peu autrement
````

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# mesurons la performance

import time
begin = time.time()

# dans un vrai programme on écrirait
# asyncio.run(main(urls))
# mais ici dans un notebook, on peut/doit faire simplement ceci
await main(urls)

print("Durée totale {}s".format(time.time() - begin))
```

+++ {"slideshow": {"slide_type": "slide"}}

### en séquence, pour comparer

voici pour comparer le même travail, mais fait séquentiellement, avec donc cette fois la librairie habituelle `requests`

```{code-cell} ipython3
# en version purement séquentielle
import requests

def synchroneous(url):
    print(f"fetching {url} synchroneously (blocking)")
    response = requests.get(url)
    print(f"{url} returned status {response.status_code}")
    print(f"{url} returned {len(response.text)} chars")
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# et si on on lit les 4 de cette manière:

import time
begin = time.time()

for url in urls:
    synchroneous(url)

print("Durée totale {}s".format(time.time() - begin))
```

la différence de performance va varier d'un environnement à l'autre, mais dans la plupart des cas on observe que la version asynchrone est de l'ordre de 4 fois plus rapide !

+++ {"slideshow": {"slide_type": ""}}

### bien remarquer

* le code de la version asynchrone a un flux de contrôle 'normal':  
  pas besoin de créer des callbacks, qui auraient nécessité de découper le traitement en morceaux

* nous n'avons pas non plus eu besoin de créer/manipuler un *thread*
* on pourrait faire tourner en parallèle n'importe quelle tâche réactive
  * comme réagir à une entrée clavier
  * faire tourner un processus séparé
  * lire un fichier local...

+++ {"slideshow": {"slide_type": ""}}

## les outils

### syntaxe:

* `async def` pour définir une fonction asynchrone (une coroutine)
* `await <expr>` pour attendre un résultat asynchrone
* `await for` pour un itérateur qui attend à chaque tour
* `await with` ditto pour un context manager

### librairie `asyncio`

* une boucle d'événement, par exemple `asyncio.run()`
* le coeur de la librairie est collé à l'OS et tire parti du framework

+++ {"slideshow": {"slide_type": ""}}

## pourquoi c'est mieux que des threads

le gros souci avec les *threads*, c'est qu'on n'a pas le contrôle sur le moment où a lieu le *context switching* entre threads  
ce qui crée le problème bien connu de zones critiques, de protection par verrous, etc..

en fait dans le paradigme asynchrone, (tout se passe comme si) avec l'instruction `await` on indique les points où on peut changer de contexte  
du coup on n'**utilise pas le *scheduler* de *threads* de l'OS**, et c'est la boucle d'événements de `asyncio`, qui tourne **dans un seul *thread***, qui se charge du *switching*

la contrepartie par contre, c'est qu'une tache asynchrone doit s'abstenir de "garder la main" trop longtemps, sinon les autres coroutines sont en situation de famine.

+++ {"slideshow": {"slide_type": "slide"}}

## un autre exemple

voyons maintenant un exemple encore plus basique: pour simuler des traitements parallèles qui auraient des durées variables, et qui retournent quelque chose, nous définissons ceci:

```{code-cell} ipython3
import asyncio
# quelque chose de plus basique

async def mysleep(duration):
    print("Entrée dans {duration}".format(**locals()))
    await asyncio.sleep(duration)
    print("Sortie de {duration}".format(**locals()))
    return duration**2
```

et on met en parallèle 3 pseudo-tâches comme ceci

```{code-cell} ipython3
# de nouveau, dans un vrai programme ce serait
# async def main():
#     return asyncio.gather(mysleep(1), mysleep(0.5), mysleep(1.5))
# results = asyncio.run(main())

# mais ici on peut faire + rapidement
results = await asyncio.gather(mysleep(1), mysleep(0.5), mysleep(1.5))
```

```{code-cell} ipython3
# et du coup on retrouve les résultats ici, dans le même ordre que les entrées
results
```

+++ {"slideshow": {"slide_type": ""}}

## librairies disponibles

* toutes les librairies réseau sont disponibles: http, telnet, ssh, ...
* idem pour la gestion de bases de données
* tout pour gérer les subprocess (natif dans `asyncio`)

**préférez cette solution**: dès que vous devez faire quelque chose de réactif, et  
**restez loin des *threads*** autant que vous pouvez !

+++ {"slideshow": {"slide_type": "slide"}}

## comment ça marche

à l'origine il y a les générateurs (*aka* fonctions génératrices - souvenez-vous, celles qui contiennent un `yield`)  
on a vu que le fonctionnement des générateurs imposait de "*mettre au freezer*" l'état d'avancement (la pile) du générateur  

avec ce mécanisme on a tout ce qu'il faut pour faire un *scheduler* soft !  
d'ailleurs avant l'arrivé de `asyncio` dans la 3.5, il y a eu dans la 3.4 une version où les coroutines étaient implantées comme des générateurs...

+++ {"slideshow": {"slide_type": ""}}

### coroutine

* une coroutine (`async def`) est une généralisation de fonction génératrice
* historiquement `await` s'appelait `yield from`

+++

### pour en savoir plus

je vous renvoie vers le chapitre 8 du MOOC "Python : des fondamentaux aux concepts avancés du langage" sur <https://fun-mooc.fr>, où je développe tout ceci beaucoup plus avant

+++

## *cheatsheet*

vous pouvez {download}`télécharger une *cheatsheet* ici<../media/cheat-sheet-for-python-asyncio.pdf>`

+++

## ce qu'il faut retenir

si vous avez à faire des traitements qui sont massivement *I/O bound*, vous avez intérêt à utiliser ces technologies de préférence à une programmation *multi-thread*, qui passera moins bien à l'échelle, et pourra s'avérer plus difficile à mettre en oeuvre proprement

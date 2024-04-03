# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted,-editable
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
#   language_info:
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#   nbhosting:
#     title: asyncio / async / await
#   rise:
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": ""}
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown] slideshow={"slide_type": ""}
# # `asyncio`

# %% [markdown]
# ## objectifs
#
# * faciliter l'écriture "de code parallèle de manière séquentielle"
# * parallèle: on fait **plusieurs choses** en même temps
# * séquentielle: ça se passe dans **un seul thread**
# * défini dans [pep3156](https://www.python.org/dev/peps/pep-3156/)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### historique

# %% [markdown] slideshow={"slide_type": ""}
# * défini comme une convergence 
# * de différentes approches similaires
# * développées dans les frameworks web (tornado notamment)
# * dispo sous cette forme depuis python-3.5
# * et aussi en 3.4 avec une syntaxe différente

# %% [markdown] slideshow={"slide_type": "slide"}
# ## un exemple
#
# * récupérer plusieurs urls en parallèle

# %%
import asyncio
import aiohttp
 
async def asynchroneous(url):
    async with aiohttp.ClientSession() as session:
        print(f"fetching {url}")
        async with session.get(url) as response:
            print(f"{url} returned status {response.status}")
            raw = await response.read()
            print(f"{url} returned {len(raw)} bytes")

# %% slideshow={"slide_type": "slide"}
async def main(urls):
    """
    Creates a group of coroutines and waits for them to finish
    """
    return await asyncio.gather(* (asynchroneous(url) for url in urls))

# %%
urls = ["http://www.irs.gov/pub/irs-pdf/f1040.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040ez.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040es.pdf",
        "http://www.irs.gov/pub/irs-pdf/f1040sb.pdf"]

# %% slideshow={"slide_type": "slide"}
import time
begin = time.time()

# dans un vrai programme on écrirait
#event_loop = asyncio.get_event_loop()
#event_loop.run_until_complete(main(urls))

# mais ici dans un notebook, on peut/doit faire simplement ceci
await main(urls)
print("Durée totale {}s".format(time.time() - begin))

# %% [markdown] slideshow={"slide_type": "slide"}
# ### en séquence, pour comparer

# %%
# en version purement séquentielle
import requests

def synchroneous(url):
    print(f"fetching {url} synchroneously (blocking)")
    response = requests.get(url)
    print(f"{url} returned status {response.status_code}")
    print(f"{url} returned {len(response.text)} chars")


# %% slideshow={"slide_type": "slide"}
import time
begin = time.time()
for url in urls:
    synchroneous(url)
print("Durée totale {}s".format(time.time() - begin))

# %% [markdown] slideshow={"slide_type": "slide"}
# ### bien remarquer

# %% [markdown] slideshow={"slide_type": ""}
# * dans notre exemple nous n'avons défini aucune callback
# * ni aucun *thread*
# * le code de la version `asyncio` 
#   * a un flux de contrôle 'normal'
#   * même si on découpe un peu plus finement l'algorithme
# * on pourrait faire tourner en parallèle n'importe quelle tâche réactive
#   * comme réagir à une entrée clavier
#   * faire tourner un processus séparé
#   * lire un fichier local...

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les morceaux

# %% [markdown] slideshow={"slide_type": ""}
# ##### syntaxe:
#
# * `async def` pour définir une fonction asynchrone
# * `await <expr>` pour attendre un résultat asynchrone
# * `await for` pour un itérateur qui attend à chaque tour
# * `await with` ditto pour un context manager
#
# ##### librairie `asyncio`
#
# * une boucle d'événement, par exemple `asyncio.get_event_loop()`
# * le coeur de la librairie est collé à l'OS et tire parti du framework

# %% [markdown] slideshow={"slide_type": "slide"}
# ## pourquoi c'est mieux que des threads

# %% [markdown] slideshow={"slide_type": ""}
# * l'instruction `await`
#   * pour indiquer les points où on peut changer de contexte
# * contrairement à ce qui se passe en multi-thread
#   * où on passe d'un thread à l'autre de manière non controlée
# * pas (beaucoup moins) de **section critiques**
#   * moins de charge sur le programmeur
# * globalement plus efficace

# %% [markdown] slideshow={"slide_type": "slide"}
# ## un autre exemple

# %%
import asyncio
# quelque chose de plus basique

async def mysleep(duration):
    print("Entrée dans {duration}".format(**locals()))
    await asyncio.sleep(duration)
    print("Sortie de {duration}".format(**locals()))

# %%
# de nouveau, dans un vrai programme ce serait
# loop = asyncio.get_event_loop()
# loop.run_until_complete(
#    asyncio.gather(mysleep(1), mysleep(0.5), mysleep(1.5)))

# mais ici
await asyncio.gather(mysleep(1), mysleep(0.5), mysleep(1.5))


# %% [markdown] slideshow={"slide_type": "slide"}
# ## ce qu'il faut retenir

# %% [markdown] slideshow={"slide_type": ""}
# * quasi totalité des librairies réseau disponibles
#   * http, telnet, ssh, ...
# * et pour subprocess (natif dans `asyncio`)
# * préférez cette solution 
#   * dès que vous devez faire quelque chose de réactif
#   * de préférence aux threads

# %% [markdown] slideshow={"slide_type": "slide"}
# ## comment ça marche
#
# * à l'origine il y a les fonctions génératrices

# %%
def gen_range(n):
    i = 0
    while i <= n:
        yield i
        i += 1


# %%
def enumerer():
    for x in gen_range(2):
        print(x)

enumerer()

# %% [markdown] slideshow={"slide_type": "slide"}
# ### fonctions génératrices 

# %% [markdown] slideshow={"slide_type": ""}
# * déjà à ce stade il se passe quelque chose de *magique*
# * ou en tous cas de pas simple à implémenter avec un pc et une pile
# * python 'séquentiel' a déjà un mécanisme 
#   * pour mettre au freezer une fonction et son contexte

# %% [markdown] slideshow={"slide_type": "slide"}
# ### coroutine

# %% [markdown] slideshow={"slide_type": ""}
# * une coroutine (`async def`) est une généralisation de fonction génératrice
# * historiquement `await` s'appelait `yield from`

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
#     title: "fonction g\xE9n\xE9ratrice et it\xE9rateur"
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

# %% [markdown] slideshow={"slide_type": ""}
# # générateur

# %% [markdown] slideshow={"slide_type": "slide"}
# ## c'est quoi un générateur ?

# %% [markdown]
# * une **fonction génératrice**, ou générateur, est une fonction qui retourne un itérateur
# * le code d'un générateur ressemble à un code normal
# * mais qui utilise le mot clé `yield` au lieu de `return`
# * tout se passe donc comme si à l'exécution: 
#   * on `yield` une valeur, on suspend,
#   * puis plus tard à l'itération suivante  
#     on restaure l'état, 
#
#   * et on recommence
#   * jusqu'à rencontrer un `return`  
#     auquel cas l'itération se termine

# %% [markdown] slideshow={"slide_type": "slide"}
# ## générateurs en pratique

# %%
# un générateur
def func(n):
    for i in range(n):
        yield i**2


# %%
# retourne un objet itérable
# qui donc peut etre le sujet d'un for
for i in func(10):
    print(i, end=' ') 


# %% [markdown]
# ## comment ça marche

# %% [markdown] slideshow={"slide_type": "slide"}
# ### fonction usuelle

# %% [markdown]
# * lors de l’appel d’une fonction standard
#   * un espace de nommage est créé  
#     pour les variables locales à la fonction
#
#   * l’espace de nommage est détruit au `return`  
#     c’est-à-dire à la sortie de la fonction

# %% [markdown] slideshow={"slide_type": "slide"}
# ### fonction génératrice

# %% [markdown]
# * lors de l’appel d’une fonction générateur
#   * un espace de nommage est créé  
#     pour les variables locales à la fonction
#
#   * cet espace de nommage est **conservé**  
#     jusqu’à la fin de l’itération
#
#   * ce qui peut nécessiter une pile d'exécution  
#     de plusieurs stackframes en cas de `yield from`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### illustration

# %%
def f():
    yield 2


# %%
f()

# %%
for i in f():
    print(i)

# %% cell_style="split"
# si on veut le manipuler directement
# on peut l'appeler une fois
it = f()
next(it)

# %% cell_style="split"
# mais pas la seconde dans ce cas précis
try:
    next(it)
except StopIteration as e:
    print("OOPS", e)


# %% [markdown] slideshow={"slide_type": "slide"}
# #### illustration

# %%
def func(n):
    for i in range(n):
        yield i**2


# %%
for i in func(10):
    print(i, end=' ') 

# %% [markdown]
# * la boucle `for` appelle le générateur, 
# * qui renvoie un itérateur,
# * sur lequel `for` appelle `next()` comme d'habitude

# %% [markdown] slideshow={"slide_type": "slide"}
# ### protocole

# %% [markdown]
# * la logique de l'itérateur
# * consiste à ce que son `__next__()`
#   * retourne le prochain `yield` 
#   * ou à lever `StopIteration` en cas de `return`
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### illustration

# %%
x = func(3)
next(x)

# %%
next(x)

# %%
next(x)

# %%
try:
    next(x)
except StopIteration as e:
    print("OOPS", e)

# %% [markdown] slideshow={"slide_type": "slide"}
# #### illustration

# %%
x = func(2)
x

# %%
y = iter(x)
y

# %%
z = iter(y)
z

# %%
# l'itérateur d'un itérateur est lui-même, donc:
y is z

# %% [markdown] slideshow={"slide_type": "slide"}
# #### illustration

# %%
# ces trois objets sont les mêmes exactement
next(x)

# %%
# ils suivent la même itération !
next(y)

# %%
# du coup la troisième fois ...
try:     
    next(z)
except StopIteration as e:
    print("OOPS", e)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## `return` et `yield`

# %% cell_style="split"
def f():
    yield 1
    yield 2
    return 3
    yield 4


# %% cell_style="split"
for i in f():
    print(i)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### `return` et `yield`

# %% [markdown] slideshow={}
# * l'instruction `yield exp` dans le générateur
#   * correspond à un `return exp` dans (le `next` de l') itérateur
# * l'instruction `return exp` dans le générateur
#   * correspond dans l'itérateur à un `raise StopIteration(exp)`
# * la fin naturelle du générateur 
#   * correspond dans l'itérateur à un `raise StopIteration(None)` 
# * **ne pas lever** `StopIteration` dans le générateur 

# %% [markdown] slideshow={"slide_type": "slide"}
# ## fonction générateur et itérateur

# %% [markdown]
# * une fonction génératrice renvoie un itérateur
# * c'est donc une manière pratique de rendre un objet itérable
# * que d'implémenter sa spéciale `__iter__` 
# * comme une fonction génératrice

# %% cell_style="split"
# une version avec classe 
# du parcours précédent
class IterSquares:
    """les carrés de 0 à top**2"""
    def __init__(self, top):
        self.top = top
    def __iter__(self):
        i = 0
        while i <= self.top:
            yield i**2
            i += 1


# %% cell_style="split" slideshow={}
for i in IterSquares(3):
    print(i)


# %% [markdown] slideshow={"slide_type": "slide"}
# ##  un itérateur pour une classe `Mots` 

# %% [markdown]
# * on veut implémenter une classe `Mots`
#   * créée à partir d'une phrase
#   * permette d'itérer sur tous les mots dans la phrase
#   

# %% [markdown]
# ##### cas 1 : `Mots` est son propre itérateur
#
# * `Mots` a les méthodes `__iter__()` et `__next__()`
# * `__iter__()` retourne `self`
# * l’instance est l’itérateur, donc au maximum  
#   un unique itérateur par instance
#
# * `__next__()` implémente l’itération

# %% slideshow={"slide_type": "slide"}
class Mots():
    def __init__(self, phrase):
        self.phrase = phrase.split()
        self.count = 0

    # en faisant ce choix, une instance
    # est son propre itérateur, avec la
    # limite qu'on a déjà vue plusieurs fois
    # sur les boucles imbriquées notamment
    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.phrase):
            raise StopIteration
        self.count = self.count + 1
        return self.phrase[self.count - 1]


# %% slideshow={"slide_type": "slide"}
m = Mots("une grande phrase")
[x for x in m]

# %%
# il n’y a qu’un itérateur par instance 
[x for x in m] 


# %% [markdown] slideshow={"slide_type": "slide"}
# ###  un itérateur pour une classe `Mots` 

# %% [markdown]
# ##### Cas 2 : l'itérateur dans une classe séparée
#
# * `Mots` a la méthode `__iter__()` qui retourne une instance 
# * d’une nouvelle classe `IterMots` qui sera un itérateur pour notre classe `Mots`
# * `IterMots` a les méthodes `__iter__()`, qui retourne `self`,  
#   et `__next__()` qui implémente l’itération
#
# * chaque itération sur une instance de `Mots` crée un nouvel itérateur

# %% slideshow={"slide_type": "slide"}
class Mots():
    def __init__(self, phrase):
        self.phrase = phrase.split()

    def __iter__(self):
        return IterMots(self.phrase)

class IterMots():
    def __init__(self, phrase):
        self.phrase = phrase
        self.count = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count == len(self.phrase):
            raise StopIteration
        self.count = self.count + 1
        return self.phrase[self.count - 1]


# %% cell_style="split" slideshow={"slide_type": "slide"}
m = Mots("une grande phrase")
[x for x in m]

# %% cell_style="split"
# maintenant plus de problème
[x.upper() for x in m] 

# %%
# on peut itérer autant qu'on veut
[x.upper() for x in m if 'a' in x]


# %% [markdown] slideshow={"slide_type": "slide"}
# ####  un itérateur pour une classe `Mots` 

# %% [markdown]
# ##### Cas 3 : le plus simple
#
# * on implémente dans `Mots` uniquement `__iter__()` 
# * sous forme d’une fonction générateur
# * chaque itération sur une instance crée une nouvelle fonction génératrice, donc un nouvel itérateur
# * c’est la solution la plus compacte à écrire

# %% cell_style="split" slideshow={"slide_type": "slide"}
class Mots():
    def __init__(self, phrase):
        self.phrase = phrase.split()

    def __iter__(self):
        for i in self.phrase:
            yield i


# %% cell_style="split"
m = Mots("une grande phrase")
[x for x in m]

# %% cell_style="split"
[x for x in m]

# %% cell_style="split"
[x.upper() for x in m if 'a' in x]

# %% [markdown] slideshow={"slide_type": "slide"}
# ## retour sur les générateurs

# %% [markdown]
# * l’utilisation des générateurs 
#   * pour rendre facilement une classe itérable
#   * n’est qu’une toute petite partie de leur utilité
# * les générateurs sont à la base de presque tout en Python 3
#   * permet d’abstraire la difficulté d’un traitement
#   * très performant
#   * s’utilise avec tout ce qui itère 
#   * à la base des coroutines et de la programmation asynchrone

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple : analyse de code Python

# %% [markdown]
# * je veux extraire toutes les entêtes 
#   * de fonctions python
#   * contenues dans tous les fichiers Python d'un répertoire

# %%
# !grep -n 'def ' *.py /dev/null

# %% slideshow={"slide_type": "slide"}
from pathlib import Path

def generator(dossier):
    for file in Path(dossier).glob("*.py"):
        try:
            with file.open() as feed:
                for lineno, line in enumerate(feed, 1):
                    if line.strip().startswith('def '):
                        yield lineno, feed.name, line.strip()[4:]
        except OSError as exc:
            print(f"oops with {file} - {type(exc)} {exc}")


# %% slideshow={"slide_type": "slide"}
# on peut l'utiliser dans tout ce qui attend un itérable

# un for
for lineno, file, line in generator("."):
    print(f"{lineno}:{file}:{line}")


# %% cell_style="split"
# dans un autre generateur
def generator2():
    for (_, filename, _) in generator('.'):
        yield filename

list(generator2())


# %% cell_style="split"
# ou une expression génératrice :)

gen_exp = (filename for (_, filename, _) 
           in generator('samples'))

for x in gen_exp:
    print(x)


# %% [markdown] slideshow={"slide_type": "slide"}
# ## on n'a pas besoin de classes alors ?
#
# * si, mais uniquement pour les cas les plus sophistiqués
#   * traitement très complexe 
#   * besoin d’héritage
#   * etc.
# * les générateurs fournissent une solution légère et élégante
#   * pour abstraire des traitements itératifs

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `yield from`

# %% [markdown]
# ou comment factoriser les générateurs

# %%
def sum_numbers(num):
    """
    retourne la somme de tous les chiffres d'un nombre
    récursivement jusqu'à obtenir un chiffre entre 0 et 9
    """
    _sum = 0
    for n in str(num):
        _sum = _sum + int(n)
    if _sum > 10:
        return sum_numbers(_sum)
    else:
        return _sum



# %%
sum_numbers(11236786578)


# %% slideshow={"slide_type": "slide"}
# comment factoriser du code qui contient un yield ?

def gen(size):
    # if size is even: make it odd
    if size % 2 == 0:
        size = size - 1
        for i in range(size):         # le même 
            if sum_numbers(i) == 7:   # fragment 
                yield i               # de code
    else:
        for i in range(size):         # utilisé
            if sum_numbers(i) == 7:   # deux fois
                yield i               # mais avec un yield


# %% slideshow={"slide_type": "slide"}
# première solution, qui marche mais peu élégante

# le code factorisé
def gen_sum_is_7(size):
    for i in range(size):
        if sum_numbers(i) == 7:
            yield i

def gen(size):
    # if size is even: make it odd
    if size % 2 == 0:        
        size = size - 1      
        # on ne peut utiliser le code factorisé
        # que via un for, du coup c'est lourd
        for i in gen_sum_is_7(size):
            yield i
    else:
        # ditto
        for i in gen_sum_is_7(size):
            yield i


# %% slideshow={"slide_type": "slide"}
# deuxième solution: yield from

# le code factorisé (inchangé p/r solution 1)
def gen_sum_is_7(size):
    for i in range(size):
        if sum_numbers(i) == 7:
            yield i

def gen(size):
    # if size is even: make it odd
    if size % 2 == 0:        
        size = size - 1      
        # on ne peut utiliser le code factorisé
        # que via un for, du coup c'est lourd
        yield from gen_sum_is_7(size)
    else:
        # ditto
        yield from gen_sum_is_7(size)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### `yield from`
#
# * beaucoup plus puissant que cela
# * on en reparlera avec les coroutines et `asyncio`
#   * c'est de la délégation

# %% [markdown] slideshow={"slide_type": "slide"}
# ## chaîne de traitements

# %% [markdown]
# * un usage classique des générateurs est de les chaîner
#   * pour faire une chaîne de traitements
# * l’idée est de cascader plusieurs traitements
#   * sans jamais générer une grande structure de données temporaire

# %% slideshow={"slide_type": "slide"}
# ces trois fonctions utilisent yield et sont donc des générateurs 
def cat_on_file(filename):
    print("ouverture de {}".format(filename))
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip()

# ces deux fonctions attendent un itérable 'lines'
# et peuvent donc travailler 
# sur (le résultat d')un générateur
def remove_comments(lines):
    for line in lines:
        if not line.startswith('#'):
            yield line


def get_func_headers(lines):
    for line in lines:
        if line.startswith('def') and line.endswith(':'):
            yield line


# %% slideshow={"slide_type": "slide"}
# all_lines est l'itérateur rendu par cat_on_files
all_lines = cat_on_file('samples/closures.py')

# %%
# on peut donc appeler remove_comments dessus
all_lines_no_comment = remove_comments(all_lines)

# %%
# et à nouveau
all_functions = get_func_headers(all_lines_no_comment)

# %% [markdown]
# * remarquez bien qu'à ce stade on n'a toujours pas ouvert le fichier !

# %% cell_style="split" slideshow={"slide_type": "-"}
for i in all_functions:
    print(i)

# %% cell_style="split"
# si on recommence il ne se passe plus rien
for i in all_functions:
    print(i)

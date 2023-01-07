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
#     title: fonctions
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")


# %% [markdown] slideshow={"slide_type": ""}
# # passage de paramètres

# %% [markdown] slideshow={"slide_type": "slide"}
# ## paramètres multiples

# %% [markdown]
# pour **définir** aussi bien que pour **appeler** une fonction,  
# Python propose une large gamme de mécanismes pour le passage de paramètres
#
# chacun de ces mécanismes est assez simple pris individuellement,
# mais un peu de soin est nécessaire pour bien expliquer le mécanisme général

# %% [markdown] slideshow={"slide_type": "slide"}
# ### paramètres multiples : use case, un *wrapper*

# %% [markdown]
# * écrire un wrapper autour de `print()`
# * c'est-à-dire une fonction `myprint()`
# * qui ajoute `HELLO` au début de chaque impression
# * mais sinon l'interface de `myprint()`  
#   est exactement celle de `print()`, i.e.  
#
#   * nb. variable de paramètres
#   * réglages inchangés - e.g. `myprint(..., file=f)`
#   
# ```python
# >>> myprint(1, 2, 3, sep='+')
# HELLO 1+2+3
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### *use case : variante* 
#
# * dans une variante de `myprint`, 
# * on veut imposer un premier argument obligatoire pour remplacer `HELLO`,…
#
# ```python
# >>> myprint2('HEY', 1, 2, 3, sep='==')
# HEY 1==2==3
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# nous allons expliquer tout ceci, mais pour l'instant voyons comment se comporterait une fonction `myprint()`idéale :

# %% cell_style="split" slideshow={"slide_type": ""}
# la première variante
def myprint(*args, **kwds):
    print("HELLO", end=" ")
    print(*args, **kwds)


# %% cell_style="split"
# ajout automatique de 'HELLO'
# et on peut utiliser tous
# les paramètres spéciaux 
# de print()
myprint(1, 2, 3, sep='+')


# %% cell_style="split"
# la seconde avec le premier
# paramètre obligatoire
def myprint2(obligatoire, 
             *args, **kwds):
    print(obligatoire, end=" ")
    print(*args, **kwds)    


# %% cell_style="split"
# le premier paramètre
# sert à remplacer 'HELLO'
myprint2('HEY', 1, 2, 3, sep='==')


# %% [markdown] slideshow={"slide_type": "slide"}
# ## paramètres et arguments

# %% [markdown]
# précisons le vocabulaire  
# lorsqu'il peut y avoir ambiguïté :
#
# * `paramètre`: le nom qui apparaît dans le `def`
# * `argument`: l'objet réellement passé à la fonction

# %% cell_style="split" slideshow={}
# ici x est un PARAMÈTRE
def foo(x):
    print(x)


# %% cell_style="split"
# et ici a est un ARGUMENT
a = 134 + 245
foo(a)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### typologie

# %% [markdown]
# * il y a 4 manières de déclarer des paramètres 
# * et 4 manières d’appeler une fonction avec des arguments
# * les deux familles se ressemblent un peu
# * mais il y a tout de même des différences
#
# * le sujet que nous abordons ici est celui qui consiste  
#   à **lier les arguments à des paramètres**
#
# * de façon à ce que tous les arguments soient exposés à la fonction

# %% [markdown] slideshow={"slide_type": "slide"}
# ## déclaration des paramètres

# %% [markdown] slideshow={"slide_type": "slide"}
# * paramètre positionnel ou ordonné ou usuel/normal
#  * `def foo(x):`
# * paramètre nommé ou avec valeur par défaut
#   * `def foo(x=10):`
# * paramètre de forme `*args`
#   * `def foo(*args):`
#   * correspond aux arguments non nommés "en plus"
# * paramètre de forme `**kwds`
#   * `def foo(**kwds):`
#   * correspond aux arguments nommés "en plus"

# %% [markdown] slideshow={"slide_type": "slide"}
# ### (I) paramètre positionnel

# %% [markdown]
# * obtiennent un rang de gauche à droite
# * le mécanisme le plus simple et le plus répandu

# %%
# on s'intéresse ici à la déclaration des paramètres
def agenda(nom, prenom, tel, age, job):
    # pour afficher quel argument est attaché
    # à quel paramètre
    D = dict(nom=nom, prenom=prenom, tel=tel,
             age=age, job=job)
    print(D)


# %% [markdown] slideshow={"slide_type": "slide"}
# #### (I) paramètre positionnel

# %% [markdown]
# * comment on peut alors appeler la fonction ?

# %%
# appel usuel, sans nommage
# c'est l'ordre des arguments qui compte
agenda('doe', 'alice', '0404040404', 35, 'medecin')

# %%
# par contre en nommant les arguments lors de l’appel
# on peut les mettre dans n’importe quel ordre
agenda(prenom='alice', nom='doe', age=35,
       tel = '0404040404', job = 'medecin')


# %% [markdown] slideshow={"slide_type": "slide"}
# ### (II) paramètre nommé / avec valeur par défaut

# %%
# ici les 3 premiers paramètres sont obligatoires
# et les deux suivants optionnels (ils ont une valeur par défaut)
def agenda(nom, prenom, tel,
           age = 35, job = 'medecin'):
    # comme tout à l'heure, pour afficher 
    # ce qui correspond aux paramètres
    D = dict(nom=nom, prenom=prenom, tel=tel,
             age=age, job=job)
    print(D)


# %% [markdown] slideshow={"slide_type": "slide"}
# #### (II) paramètres nommés

# %% [markdown]
# * comment on peut alors appeler la fonction ?

# %%
# appel en suivant la signature
# il manque deux arguments, on utilise les valeurs par défaut
agenda('Dupont', 'Jean', '123456789')

# %%
# on peut aussi nommer les arguments, et à nouveau 
# ça permet de mélanger l'ordre des paramètres imposés
# ici aussi job est manquant, on utilise la valeur par défaut
agenda(prenom = 'alice', nom = 'doe',
       age = 25, tel = '0404040404')

# %%
# on peut mixer les deux approches
# ici les trois premiers sont liés dans l'ordre
agenda('Dupont', 'Jean', '123456789', age = 25, job = 'avocat')


# %% [markdown] slideshow={"slide_type": "slide"}
# #### (II) paramètres nommés

# %% [markdown]
# * **attention** à ne pas confondre la forme `name=value` dans une entête de fonction et lors d’un appel
# * **dans un entête** c’est une déclaration de paramètre (avec valeur) par défaut
# * **lors d’un appel**
#   * c’est une désignation explicite d’arguments par nom (et non par ordre de déclaration)
#   * l'argument nommé est affecté au paramètre de même nom

# %% [markdown] slideshow={"slide_type": "slide"}
# ### (III) paramètre multiple, forme `*args`

# %% [markdown]
# * Python collecte tous les arguments non nommés restants 
#   (non liés à un paramètre) sous forme d’un tuple
#
# * et assigne le paramètre `args` à ce tuple
# * du coup avec cette forme, la fonction peut être appelée 
#   * avec un nombre variable d'arguments

# %% [markdown] slideshow={"slide_type": "slide"}
# #### (III) paramètre multiple, forme `*args`

# %% cell_style="split"
# définition
def variable(*args):
    print(f"args={args}")

# utilisation
variable()

# %% cell_style="split"
# appel
variable(1)

# %% cell_style="split"
variable(1, 2, 3, 4, 5, [2,3])


# %% [markdown]
# ****

# %% cell_style="split"
# définition
def variable2(one, two, *args):
    print(f"one={one}, two={two}, args={args}")

# utilisation
variable2(1, 2)

# %% cell_style="split"
# appel
variable2(1, 2, 3)

# %% cell_style="split"
variable2(1, 2, 3, 4, 5, [2,3])


# %% [markdown] slideshow={"slide_type": "slide"}
# #### (III) paramètre multiple, forme `*args`

# %% [markdown]
#   
# * `args` est un nom de paramètre quelconque,  
#   même si c'est souvent `args` (comme `self` est souvent appelé `self`)  
#   lorsqu'on se contente de passer cela à une autre fonction
#
# * `*args` **ne peut apparaître qu'une fois**   
#   bien sûr, car sinon il y aurait ambiguïté
#   
# ```python
# def variable(*args1, *args2):
#     pass
# # où finit args1 et où commence args2 ?
# variable(1, 2, 3, 4)
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### (IV) paramètre multiple, forme `**kwds`

# %% [markdown]
# * python collecte tous les arguments nommés restants  
#   i.e. non liés à un paramètre
#
# * et les met dans **un dictionnaire**
# * dont les clés sont les noms et les valeurs les arguments
# * qui est affecté au paramètre `kwds`
# * ici encore le nombre d’arguments peut être quelconque
# * c'est le même mécanisme d'*attrape-tout* que pour `*args`  
#   mais avec les arguments nommés

# %% [markdown] slideshow={"slide_type": "slide"}
# #### (IV) paramètre multiple, forme `**kwds`

# %% cell_style="split" slideshow={"slide_type": ""}
# définition
def named_args(**kwds):
    print(f"kwds={kwds}")
    
# var_named
named_args()

# %% cell_style="split"
named_args(a = 1)

# %% cell_style="split"
named_args(a = 1, b = 2)


# %% [markdown]
# ****
#

# %% cell_style="split" slideshow={"slide_type": ""}
# définition
def named_args1(a=0, **kwds):
    print(f"a={a} kwds={kwds}")
    
# var_named
named_args1(a=1)

# %% cell_style="split"
named_args1(1, b=2)

# %% cell_style="split"
named_args1(a = 1, b = 2)


# %% [markdown] slideshow={"slide_type": "slide"}
# #### (IV) paramètre multiple, forme `**kwds`

# %% [markdown]
# * ici encore cette forme de paramètre **ne peut apparaître qu'une fois**
# * car sinon, comme avec `*args`, la liaison serait ambigüe

# %% [markdown] slideshow={"slide_type": "slide"}
# ## *unpacking* des arguments

# %% [markdown]
# ### **dans l'autre sens**

# %% [markdown]
# * c'est-à-dire à l'**appel** d'une fonction
# * nous avons déjà vu deux formes d'appel
#   * `func(x)`
#   * `func(x=10)`
# * python propose également deux formes spéciales
#   * `func(*x)`
#   * `func(**x)`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### (III) appel avec la forme `*x`

# %% [markdown] slideshow={"slide_type": ""}
# * on peut utiliser un paramètre de la forme `*x`
# * où `x` désigne **un itérable**
# * Python va transformer `*x` en une suite de paramètres à passer à la fonction
# * dans ce sens par contre on peut utiliser la forme `*x` **plusieurs fois** dans le même appel

# %% cell_style="split" slideshow={"slide_type": "slide"}
# une définition classique
def f4(a, b, c, d):
    print(a, b, c, d)


# %% cell_style="split"
# appel avec la forme *x
L = [1, 2, 3, 4]
f4(*L)

# %% cell_style="split"
# n'importe quel itérable
f4(*"abcd")

# %% cell_style="split"
L1, L2 = (1, 2), (3, 4)

# 2 *params dans le même appel
# ne posent pas problème
f4(*L1, *L2)

# %% cell_style="split"
# on peut utiliser * avec une expression
f4(*range(1, 3), *range(10, 12))


# %% [markdown] slideshow={"slide_type": "slide"}
# ### (IV) appel avec la forme `**x`

# %% [markdown]
# * cette fois `x` est supposé être **un dictionnaire**
# * Python va transformer ce dictionnaire en une suite de paramètres nommés

# %%
def f3(a, b, c):
    print(a, b, c)

D = {'a':1, 'c':3, 'b':2}

# équivalent à func(a=1, b=2, c=3)
f3(**D)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## piège fréquent avec les arguments par défaut

# %% [markdown]
# * les valeurs par défaut sont évaluées à l’endroit de la déclaration de la fonction

# %%
i = 5
def f(arg = i):  # i vaut 5 au moment de la déclaration
    print(arg)
i = 6            # i est mis à 6 après la déclaration, ça
                 # n’est pas pris en compte
f()


# %% [markdown] slideshow={"slide_type": "slide"}
# ### piège fréquent avec les arguments par défaut

# %% [markdown]
# * les valeurs par défaut de f ne sont évaluées **qu’une fois** à la création de l’objet fonction et mises dans **f.__defaults__**
#   * si la **valeur par défaut est mutable**  
#     elle pourra être modifiée dans la fonction
#
#   * et dans ce cas, la valeur par défaut  
#     **est modifiée pour l'appel suivant**
#
# du coup
#
# * ➔ **ne jamais utiliser un mutable comme valeur par défaut !!!**

# %% [markdown] slideshow={"slide_type": "slide"}
# #### piège fréquent avec les arguments par défaut

# %% cell_style="split"
# on pourrait penser en lisant ceci 
# que sans préciser L on devrait 
# toujours retourner une liste [a]
def f(a, L = []):
    L.append(a)
    return L


# %% cell_style="split"
# la valeur par défaut est
# évaluée par l'instruction def:
f.__defaults__



# %% cell_style="split"
# OK ici ça fait ce qu'on attend
f(1)

# %% cell_style="split"
# sauf que ATTENTION
# on a modifié ceci
f.__defaults__

# %%
# si bien qu'à l'appel suivant il se passe ceci !
f(2)


# %% [markdown] slideshow={"slide_type": "slide"}
# #### piège fréquent avec les arguments par défaut

# %% [markdown]
# * solution 

# %% cell_style="split"
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    print(L)
f(1)
f(2)
f(3)


# %% cell_style="split"
# ou si on préfère
def f(a, L=None):
    L = L if L is not None else []
    L.append(a)
    print(L)
f(1)
f(2)
f(3)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## ordre des paramètres et arguments

# %% [markdown] slideshow={"slide_type": ""}
# ### paramètres

# %% [markdown] cell_style="split"
# * dans un `def` 
#   * on peut combiner les différentes  
#     formes de déclarations de paramètres
#
#   * tous les ordres ne sont pas autorisés
#   * on recommande *l’ordre suivant*  
#     (voir aussi plus loin…)

# %% [markdown] cell_style="split"
# 1. paramètres positionnels (`name`),
# 1. paramètres par défaut (`name=value`),
# 1. forme `*name` (une au maximum)
# 1. forme `**name` (une au maximum)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### arguments

# %% [markdown] cell_style="split"
# * dans un appel de fonction
# * on recommande de matérialiser deux groupes

# %% [markdown] cell_style="split"
# en premier les non-nommés
#
# * arguments positionnels (`name`), 
# * forme(s) `*name`,
# * dans l'ordre qui va bien
#
# puis ensuite les arguments nommés
#
# * arguments nommés (`name=value`),
# * forme(s) `**name`
# * pareil, dans le bon ordre

# %% [markdown] cell_style="center" slideshow={"slide_type": ""}
# <div class="rise-footnote">
# contrairement aux paramètres, on peut mentionner plusieurs `*` ou `**`
# et on les met dans l'ordre où ça fait du sens
# </div>

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exemples

# %% slideshow={"slide_type": ""}
# une fonction passe-partout qui affiche juste ses paramètres 
# pour nous permettre d'illustrer les appels 


# pour rappel également
# dans la définition de la fonction
# on ne peut pas mentionner plusieurs * ou **
def show_any_args(*args, **kwds):
    print(f"args={args} - kwds={kwds}")


# %% cell_style="split"
show_any_args(1)

# %% cell_style="split"
show_any_args(x=1)

# %% slideshow={"slide_type": "slide"}
# exemple 1
# on recommande de mettre les arguments non-nommés en premier
show_any_args(1, 4, 5, 3, x = 1, y = 2)

# %% slideshow={"slide_type": ""}
# exemple 1 (suite)
# car ceci est illégal et déclenche une SyntaxError
# foo(1, x=1, 4, 5, 3, y = 2)

# %%
# exemple 2
l1 = [1, 2]
l2 = [3, 4]
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}

# on peut appeler avec plusieurs * et **
show_any_args(*l1, *l2, 1000, **d1, **d2)


# %% [markdown] slideshow={"slide_type": ""}
# * attention aux mélanges, ça devient vite incompréhensible
#   * en cas de doute
#   * n'hésitez pas à tout nommer 
#   * ou en tous cas plus que nécessaire
# * dans le reste de cette section
#   * tenter de voir le cas général

# %% [markdown] slideshow={"slide_type": "slide"}
# ## associer arguments et paramètres (avancé)

# %% [markdown]
# * dans le cas général
#   * où les paramètres et les arguments sont complexes
# * il faut un mécanisme 
#   * pour associer paramètres et arguments
# * si on reste raisonnamble
#   * cela fonctionne de bon sens
# * mais attention aux mélanges trop hardis
#   * cela devient vite inextricable

# %% [markdown] slideshow={"slide_type": "slide"}
# ### 2 groupes : positionnels et nommés

# %% [markdown] slideshow={"slide_type": ""}
# * **attention**
# * les arguments ne sont pas pris dans l’ordre de l’appel !
#   * en premier on résoud les arguments positionnels et `*args`
#   * puis les arguments nommés et `**kwds`
# * ce qui est assez logique si on se souvient que
#   * `*args` concerne les arguments non nommés  
#     qui vont dans un tuple
#
#   * et `**kwds` concerne les arguments nommés  
#     qui vont dans un dictionnaire
#
# * voyons ça sur un exemple

# %% [markdown] slideshow={"slide_type": "slide"}
# #### associer les arguments aux paramètres

# %% cell_style="split"
def show_abcd(a, b, c, d):
    print(dict(a=a, b=b, c=c, d=d))

# pas de souci ici
show_abcd(1, c = 3, *(2,), **{'d':4})

# %% cell_style="split"
# par contre ici on dit en fait 
# b=2 mais aussi b=3 
# à cause du *(3,)
try:
    show_abcd(1, b = 2, *(3,), 
              **{'d':4})
except TypeError as exc:
    print("OOPS", exc)

# %% [markdown]
# * l’argument nommé `b` est mis à `2`,  
#   mais le tuple `*(3,)` assigne également `3` à `b`
#
# * pour comprendre, regardons l’exemple suivant

# %% [markdown] slideshow={"slide_type": "slide"}
# #### associer les arguments aux paramètres

# %%
show_any_args(1, b = 3, *(2,), **{'d':4})


# %% [markdown]
# * l’intérêt des arguments nommés est de ne pas avoir à se souvenir de l’ordre de la déclaration
# * combiner des arguments nommés et une forme `*args` supprime ce bénéfice 
# * puisqu’il faut se souvenir de l’ordre pour éviter des collisions
# * comme dans l’exemple précédent; **c’est à éviter !**

# %% [markdown] slideshow={"slide_type": "slide"}
# ### arguments *keyword-only*

# %% [markdown]
# **rappel** les 4 familles de paramètres qu'on peut déclarer dans une fonction :
#
# 1. paramètres positionnels (usuels)
# 1. paramètres nommés (forme *name=default*)
# 1. paramètre **args* qui attrape dans un tuple le reliquat des arguments positionnels 
# 1. paramètre ***kwds* qui attrape dans un dictionnaire le reliquat des arguments nommés
#

# %% slideshow={"slide_type": "slide"}
# une fonction qui combine les différents 
# types de paramètres
def ab_etc(a, b=100, *args, **kwds):
    print(f"a={a}, b={b}, args={args}, kwds={kwds}")


# %% cell_style="split"
ab_etc(1)

# %% cell_style="split"
ab_etc(1, 2)

# %% cell_style="split"
ab_etc(1, 2, 3)

# %% cell_style="split"
ab_etc(1, 2, 3, bar=1000)

# %%
ab_etc(1, 2, 3, bar=1000)


# %% [markdown] slideshow={"slide_type": "slide"}
# #### ordre des déclarations

# %% [markdown]
# * l'ordre dans lequel sont déclarés les différents types de paramètres est imposé par le langage
# * historiquement à l'origine, on **devait déclarer dans cet ordre** :
#
# > positionnels, nommés, forme `*`, forme `**`
#

# %% [markdown] slideshow={"slide_type": ""}
# * ça reste une bonne approximation
# * mais en Python-3 on a introduit [les paramètres *keyword-only*](https://www.python.org/dev/peps/pep-3102/)
# * on peut ainsi définir un paramètre qu'il **faut impérativement** nommer lors de l'appel
# * et également en 3.8 [les paramètres *positional-only*](https://docs.python.org/3/whatsnew/3.8.html#positional-only-parameters)
# * qui introduit des paramètres usuels qu'on **ne peut pas nommer** lors de l'appel

# %% slideshow={"slide_type": "slide"}
# on peut déclarer un paramètre nommé **après** l'attrape-tout *args
# du coup ici le paramètre nommé `b` devient un *keyword-only* parametter
def a_etc_b(a, *args, b=100, **kwds):
    print(f"a={a}, b={b}, args={args}, kwds={kwds}")


# %% [markdown]
# avec cette déclaration, je **dois nommer** le paramètre `b`

# %% cell_style="split"
# je peux toujours faire ceci
a_etc_b(1)

# %% cell_style="split"
# mais si je fais ceci l'argument 2 
# va aller dans args
a_etc_b(1, 2)

# %%
# pour passer b=2, je **dois** nommer mon argument
a_etc_b(1, b=2)


# %% [markdown] slideshow={"slide_type": "slide"}
# ### arguments *positional-only*

# %% cell_style="split" slideshow={"slide_type": "slide"}
# en général on peut toujours nommer
# des arguments même si le paramètre 
# est positionnel
def f(a, b, c, d):
    print(dict(a=a, b=b, c=c, d=d))
    
f(a=1, b=2, c=3, d=4)

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ```python
# # un exemple de paramètre *positional-only* 
# # introduit dans Python-3.8
# def f(a, b, /, c, d):
#     print(a, b, c, d, e, f)
#
# # ceci cause un exception 
# # car on ne PEUT PAS nommer a ni b
# f(a=1, b=2, c=3, d=4)
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### retombées sur la syntaxe de base

# %% [markdown]
# sachez qu'on peut également faire ceci  
# (indépendamment des appels de fonction):

# %%
# le extended-unpacking consiste à extraire un morceau
# de taille inconnue dans un itérable
# on ne peut mettre qu'une seule fois * à un étage de l'affectation

a, *b, c = [1, 2, 3, 4, 5, 6]
print(dict(a=a, b=b, c=c))

# %% cell_style="split"
# construire une liste avec *args
l1 = [3, 4]
l2 = [5, 6]
[1, 2, *l1, *l2]

# %% cell_style="split"
# pareil avec un dictionnaire
d1 = {3: 'c', 4: 'd'}
d2 = {5: 'e', 6: 'f'}
{1: 'a', 2: 'b', **d1, **d2}

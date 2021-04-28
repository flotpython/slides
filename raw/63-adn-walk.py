# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 2
#     language: python
#     name: python2
#   notebookname: Promenade le long de l'ADN
#   version: '1.0'
# ---

# %% [markdown]
# <span style="float:left;">Licence CC BY-NC-ND</span><span style="float:right;">François Rechenmann &amp; Thierry Parmentelat&nbsp;<img src="media/inria-25.png" style="display:inline"></span><br/>

# %% [markdown]
# # Promenade le long de l'ADN

# %% [markdown]
# Nous allons voir dans ce complément une version exécutable de l'algorithme de la promenade le long de l'ADN.

# %% [markdown]
# Il s'agit donc de dessiner le parcours d'une séquence d'ADN, si chaque nucléotide `C`,  `A`, `G`, et `T` correspond à une direction dans le plan, pour rappel&nbsp;:

# %% [markdown]
# ![Extrait du transparent](media/directions.png)

# %% [markdown]
# Mais dans l'immédiat, commençons par notre séquence habituelle

# %%
# la formule magique pour utiliser print() en python2 et python3
from __future__ import print_function
# pour que la division se comporte en python2 comme en python3
from __future__ import division

# %% [markdown]
# ### La librairie `matplotlib`

# %% [markdown]
# La librairie que nous allons utiliser pour dessiner le chemin s'appelle `matplotlib`, principalement parce qu'elle est d'un usage très répandu pour mettre en forme des résultats de calcul.

# %%
# pour que les graphiques apparaissent dans le notebook
# %matplotlib inline
# importation de la librairie
import matplotlib.pyplot as pyplot

# enfin: la taille à utiliser pour les figures
import pylab
pylab.rcParams['figure.figsize'] = 8., 8.

# %% [markdown]
# `matplotlib` va pouvoir très facilement dessiner le chemin qui nous intéresse, si on lui fournit deux listes de valeurs, qu'on appelle en général simplement `X` et `Y`, de même taille, et qui vont contenir les coordonnées des points par lesquels on passe.
#
# Voyons cela tout de suite sur un exemple construit "à la main": imaginons que l'on veuille dessiner un chemin qui passe par&nbsp;:
#
# * premier point (0, 0)
# * deuxième point (2, 1)
# * troisième point (1, 0)
# * quatrième point (3, 4)

# %%
# on construit la liste des abscisses
X = [0, 2, 1, 3]
# et la liste des ordonnées
Y = [0, 1, 0, 4]

# %% [markdown]
# Et pour dessiner il nous suffit alors d'appeler la fonction `plot` comme ceci&nbsp;:

# %%
pyplot.plot(X, Y)
pyplot.show()


# %% [markdown]
# ### Des fonctions qui renvoient deux valeurs

# %% [markdown]
# Donc pour dessiner un fragment d'ADN, le problème revient simplement à calculer les coordonnées des points du chemin, sous la forme d'une liste d'abscisses et une liste d'ordonnées.

# %% [markdown]
# Nous sommes donc confrontés au besoin d'écrire une fonction, mais qui doit renvoyer deux choses (la liste des abscisses et la liste des ordonnées), et idéalement en une seule passe pour être aussi efficace que possible. 

# %% [markdown]
# Il est très facile en python de renvoyer plusieurs valeurs dans une fonction. Souvenez-vous, dans le calcul des fréquences des bases, nous calculions déjà en un seul parcours les nombres d'occurrences des 4 bases. 
#
# Revoyons ça à nouveau sur un premier exemple très simple&nbsp;: une fonction qui calcule le carré et le cube d'un nombre.

# %%
# une fonction qui renvoie deux valeurs
def square_and_cube(x):
    carre = x * x
    cube = x ** 3
    # techniquement : on construit un tuple avec ces deux valeurs
    return carre, cube


# %% [markdown]
# Pour utiliser les deux résultats de la fonction, on utilise tout simplement cette syntaxe&nbsp;:

# %%
a, b = square_and_cube(5)
print("a=", a)
print("b=", b)

# %% [markdown]
# ### Utiliser un dictionnaire

# %% [markdown]
# Avant de voir le parcours de l'ADN à proprement parler, il nous reste à décider comment représenter l'association entre d'une part les 4 lettres de notre alphabet `C`, `A`, `G` et `T`, et les déplacements correspondants dans le plan.

# %% [markdown]
# Pour cela, il est naturel en python d'utiliser un dictionnaire. Comme on l'a vu dans le complément sur les rudiments de python, un dictionnaire en python permet d'associer des valeurs à des clés comme ceci&nbsp;:

# %%
moves = {
    'C' : [1, 0],
    'A' : [0, 1],
    'G' : [-1, 0],
    'T' : [0, -1],
    }

# %% [markdown]
# De sorte que par exemple on pourra facilement calculer le déplacement à faire lorsqu'on voit passer un `C`&nbsp;:

# %%
moves['C']

# %% [markdown]
# Ce qui signifie pour nous que lorsqu'on rencontre un `C`, il faut&nbsp;:
#
#  * faire `+1` en x, 
#  * et ne rien faire (ajouter `0`) en y.

# %% [markdown]
# Que l'on peut écrire, en utilisant la même syntaxe que tout à l'heure&nbsp;:

# %%
delta_x, delta_y = moves['C']
print("a ajouter en x", delta_x)
print("a ajouter en y", delta_y)


# %% [markdown]
# ### Le parcours à proprement parler

# %% [markdown]
# Nous avons à présent tous les éléments pour écrire une fonction, qui
#
# * prend en entrée un fragment d'ADN codé comme une chaine de caractères contenant les 4 abbréviations,
# * et qui retourne deux listes, correspondant aux X et aux Y respectivement, des points du chemin.

# %%
# un algorithme qui calcule les deux chemins en x et y
# en partant et en se deplaçant le long de la chaine
def path_x_y(adn):
    # initialise les résultats
    path_x, path_y = [], []
    # on commence au centre
    x, y = 0, 0
    # le point de départ fait partie du chemin
    path_x.append(x)
    path_y.append(y)

    # pour tout l'ADN
    for nucleotide in adn:
        # quel deplacement faut-il faire
        delta_x, delta_y = moves[nucleotide]
        # on l'applique
        x += delta_x
        y += delta_y
        # on range le point courant
        # dans les listes resultat
        path_x.append(x)
        path_y.append(y)

    return path_x, path_y


# %% [markdown]
# Voyons ce que cela nous donne sur un tout petit brin d'ADN pour commencer&nbsp;:

# %%
small_adn = "CAGACCACT"
X, Y = path_x_y(small_adn)
print("les abscisses", X)

# %%
pyplot.plot(X, Y)
pyplot.show()


# %% [markdown]
# ### Un raccourci

# %% [markdown]
# Si on veut tout mettre ensemble dans une seule fonction plus pratique à appeler&nbsp;:

# %%
def walk(adn):
    print("longueur de la séquence d'entrée", len(adn))
    X, Y = path_x_y(adn)
    pyplot.plot(X, Y)
    pyplot.show()


# %%
walk(small_adn)

# %% [markdown]
# ### Des données plus grosses

# %% [markdown]
# Si on prend par exemple le brin d'ADN qui est illustré dans le transparent de la séquence 7&nbsp;:

# %%
from adn_samples import sample_week1_sequence7
print(sample_week1_sequence7)

# %% [markdown]
# On peut le dessiner tout simplement comme ceci&nbsp;:

# %%
walk(sample_week1_sequence7)

# %% [markdown]
# ### Le résultat sur de vraies séquences

# %% [markdown]
# Si vous allez vous promener sur http://www.ebi.ac.uk/ena, vous pouvez faire toutes sortes de recherches pour travailler sur des données réalistes. 

# %% [markdown]
# ##### Un point de rebroussement très visible : Borrelia 

# %% [markdown]
# Pour le premier exemple nous allons regarder le résultat de notre visualisation avec *Borrelia*, que vous [pouvez consulter ici](http://www.ebi.ac.uk/ena/data/view/CP000013), ou retrouver en entrant dans [http://ebi.ac.uk/ena]() et en cherchant la clé `CP000013`. Nous l'avons chargé pour vous (voir plus loin comment vous pouvez charger d'autres spécimens à partir d'une autre clé)&nbsp;:

# %%
from adn_samples import borrelia
print("taille de borrelia", len(borrelia))

# %% [markdown]
# Avec cet échantillon vous allez voir très distinctement un point de rebroussement apparaître&nbsp;:

# %%
walk(borrelia)

# %% [markdown]
# ##### Un contrexemple : Synechosystis

# %% [markdown]
# A contrario, voici ce qu'on obtient avec *Synechosystis* (clé `BA000022`). Soyez patient car ce brin contient environ 3.5 millions de bases.

# %%
from adn_samples import synechosystis
walk(synechosystis)

# %% [markdown]
# ### Des données réelles

# %% [markdown]
# Pour illustrer ce qu'il est possible de faire très simplement aujourd'hui, je suis allé [sur le site du Eureopan Nucleotide Archive](http://www.ebi.ac.uk/ena) j'ai cherché "Borrelia burgdorferi B31" et je suis arrivé à cette page&nbsp;:

# %% [markdown]
# [http://www.ebi.ac.uk/ena/data/view/AE000783]()

# %% [markdown]
# Nous vous fournissons un petit utilitaire (très sommaire) qui permet d'aller chercher de telles séquences pour les manipuler directement dans ce notebook&nbsp;:

# %%
import adn_fetch

# %% [markdown]
# Que vous pouvez utiliser comme ceci à partir de la clé de la séquence qui vous intéresse&nbsp;:

# %%
burgdorferi = adn_fetch.fetch('AE000789')

# %%
# et que maintenant on peut donc dessiner aussi
walk(burgdorferi)

# %% [markdown]
# ### Explorer le chemin de manière interactive

# %% [markdown]
# `matplotlib` a été conçu au départ pour produire des courbes sur du papier. Nous concluons ce complément pour vous signaler une autre possibilité qui peut s'avérer intéressante dans certains cas. Dans le contexte d'un écran où on dispose d'une souris pour interagir, et notamment ici à l'intérieur d'un notebook, on va pouvoir "explorer" les détails du dessin.

# %% [markdown]
# Pour cela nous allons utiliser une librairie supplémentaire au dessus de `matplotlib`, qui s'appelle `mpld3`, voici comment cela se présente&nbsp;:

# %%
# pour pouvoir utiliser la librairie
import mpld3


# %% [markdown]
# Avec ce nouvel outil on va pouvoir afficher les même graphiques&nbsp;:

# %%
def zoomable_walk(adn):
    print("longueur de la séquence d'entrée", len(adn))
    X, Y = path_x_y(adn)
    pyplot.plot(X, Y)
    # au lieu d'afficher le dessin avec pyplot.show()
    # on retourne un objet HTML qui est rendu par le notebook
    return mpld3.display()


# %%
zoomable_walk(sample_week1_sequence7)

# %% [markdown]
# Mais avec en plus la possibilité de "zoomer" et de se déplacer dans le graphique avec les 3 petits outils qui apparaissent en bas à gauche lorsque votre souris survole le dessin&nbsp;:
#
# * Home: pour revenir à l'échelle de départ,
# * Déplacement: pour déplacer le point de vue et garder la même échelle,
# * Zoom: désignez un rectangle pour zoomer dans la figure.

# %% [markdown]
# Nous ne montrons toutefois cette possibilité plus à des fins ludiques que réellement utiles, car en pratique bien entendu on n'a guère le temps de se livrer à une inspection fine. On préfèrera adapter l'algorithme, comme on le verra dans une leçon ultérieure.

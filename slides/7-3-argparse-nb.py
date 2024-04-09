# -*- coding: utf-8 -*-
# ---
# jupyter:
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
#     title: "\xE9crire un lanceur"
# ---

# %% [markdown] slideshow={"slide_type": "-"} tags=[]
# Licence CC BY-NC-ND, Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown]
# # écrire un point d'entrée
#
# quand on écrit un projet en Python, on peut publier uniquement une librairie : un paquet de classes, de fonctions, destinées à être utilisées depuis une autre application.
#
# il est parfois aussi utile de publier un vrai "lanceur", c'est-à-dire un programme complet, destiné à être lancé en tant que tel avec une commande dans le terminal, genre
#
# ```bash
# $ python script.py
# ```
#
# on appelle alors ce fichier `script.py` un **lanceur**, une **commande**, ou encore un **point d'entrée**

# %% [markdown]
# ## lire les arguments
#
# souvent on veut pouvoir passer à ce lanceur **des paramètres**
#
# par exemple si vous avez écrit un programme qui calcule la factorielle, on veut pouvoir écrire
#
# ```bash
# $ python factorielle.py 6
# factorial(6)=720
# ```

# %% [markdown]
# il nous faut donc trouver un moyen de "faire passer" ce paramètre `6` depuis le terminal jusqu'à l'application Python; pour cela on dispose de deux mécanismes :
#
# * `sys.argv`
# * le module `argparse`
#
# de manière générale, sauf dans les cas simplissimes, il est préférable d'utiliser le second, bien qu'un tout petit peu plus complexe que le premier; voyons cela

# %% [markdown]
# ## `sys.argv`
#
# Python permet de retrouver la commande de lancement du point d'entrée au travers de l'attribu `sys.argv`, sous la forme d'une liste de chaines (la commande initiale est découpée selon les espaces)
#
# considérons pour commencer le programme suivant

# %%
# # %cat est une 'magic' de IPythion
# qui permet d'afficher le contenu de fact_sysargv.py

# %cat samples/fact_sysargv.py

# %%
# avec le ! je fais comme si je tapais ça dans le terminal

# !python samples/fact_sysargv.py 6

# %% [markdown]
# cette mécanique fonctionne mais présente **de gros défauts** :
#
# * principalement, on ne fait **aucun contrôle** sur les paramètres; si vous appelez le programme avec trop ou pas assez d'arguments, il se passe des trucs pas forcément très nets
# * et si vous ne vous souvenez plus de comment il faut appeler le programme, vous en êtes quittes pour retrouver et relire le code...

# %%
# par exemple si on essaie de lancer le programme sans le paramètre
# on obtient une erreur - c'est normal - 
# mais franchement ce n'est pas très clair de comprendre ce qu'on a mal fait

# ! python samples/fact_sysargv.py

# %%
# et avec deux paramètres, le second est simplement ignoré...

# ! python samples/fact_sysargv.py 6 20

# %% [markdown]
# ## les options
#
# en plus de tout cela, il arrive fréquemment qu'on ait envie de passer des **options**; par exemple, notre programme pourrait avoir deux modes d'affichage, bavard ou pas (c'est juste un exemple hein..)
#
# traditionnellement, les options **commencent par un tiret haut**, comme ceci :

# %%
# le -v est une option (v pour verbose)
# du coup le programme fonctionne en mode bavard

# ! python samples/fact_sysargv2.py -v 6

# %%
# sans option il marche en mode silencieux, pas de baratin

# ! python samples/fact_sysargv2.py 6

# %% [markdown]
# ````{admonition} c'est sous-optimal
# :class: admonition-small
#
# vous pouvez regarder le code de `fact_sysargv2.py` pour voir comment on a implémenté cela; notez surtout que le code devient vite un peu torturé, même pour traiter ce cas hyper-simple où on n'a qu'une seule option
# ````

# %% [markdown]
# ## `argparse`
#
# `argparse` est un module de la librairie standard, conçu spécialement pour traiter de manière plus lisible ce genre de cas
#
# on ne va pas ici entrer dans les détails, mais simplement montrer le code qui se comporterait comme `fact_sysargv2`.py

# %%
# %cat samples/fact_argparse.py

# %% [markdown]
# ce code peut sembler un peu plus bavard que tout à l'heure; mais d'abord il donne un programme plus agréable à utiliser

# %%
# si on ne passe pas les paramètres imposés, 
# le programme ne fait rien, 
# mais il nous explique comment on aurait dû l'appeler

# ! python samples/fact_argparse.py

# %%
# on peut avoir de l'aide
# ! python samples/fact_argparse.py --help

# %%
# et les options sont disponibles en version courte 
# (-v comme tout à l'heure)
# mais aussi en version longue

# ! python samples/fact_argparse.py --verbose 6

# %% [markdown]
# mais fondamentalement, le plus gros avantage c'est la lisibilité, et la simplicité de maintenance, car analyser les options "à la main" devient rapidement compliqué, fouillis, et donc peu lisible et peu maintenable...
#
# pour tous les détails sur `argparse`, [reportez-vous à ce tutoriel](https://docs.python.org/3/howto/argparse.html)

# %% [markdown]
# ````{admonition} le reste est pour les avancés
#
# en première lecture vous pouvez vous arrêter ici
# ````

# %% [markdown]
# ## packaging
#
# on va conclure ce notebook sur une note plus avancée
#
# si maintenant vous avez besoin que votre lanceur s'installe en même temps que le reste de votre librairie, vous allez utilisez `setup.py` et écrire une clause comme ceci :

# %% [markdown]
# ```python
# setup(
#     ...,
#     entry_points={
#         'console_scripts': [
#             'lanceur = monpackage.fact_argparse:main',
#         ]
# )
# ```

# %% [markdown]
# et de cette façon, après avoir installé le package avec `pip install` (localement ou pas), vous ou votre utilisateur pourra lancer la commande `bidule`, qui sera branchée sur la fonction `main` du module `monmodule` dans le package `monpackage`
#
# ```bash
# # une fois installé, on peut faire ceci dans le terminal
# $ bidule 6
# 720
# ```
#
# pour davantage de détails, [reportez-vous à la documentation de `setuptools` à ce sujet](https://setuptools.readthedocs.io/en/latest/userguide/quickstart.html#entry-points-and-automatic-script-creation)

# %% [markdown]
# ## conclusion
#
# on vient de voir l'essentiel des techniques qui permettent d'écrire un lanceur en Python
#
# comme vous l'avez compris on recommande d'utiliser `argparse`, de préférence à l'accès direct à `sys.argv`, qui donne un code plus lisible, plus maintenable, et beaucoup plus court dans la plupart des cas réels
#
# enfin pour installer de tels lanceurs, il est préférable de sous-traiter le travail à `setuptools`, qui se chargera de tous les détails - souvent sordides - pour une installation propre sur tous les OS de vos éventuels utilisateurs
#
# ````{admonition} autres librairies
# :class: seealso admonition-small
#
# pour être tout à fait exhaustif, sachez qu'il existe une foultitude de librairies qui peuvent vous rendre la vie encore plus facile, notamment si la librairie est assez riche; dans cette famille on peut citer entre autres [`click`](https://github.com/pallets/click), mais [il en existe plein d'autres !](https://github.com/shadawck/awesome-cli-frameworks?tab=readme-ov-file#python)
# ````

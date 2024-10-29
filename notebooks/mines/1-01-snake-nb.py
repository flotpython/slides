# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     custom_cell_magics: kql
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
#     title: des jeux en Python
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown]
# # écrire un petit jeu
#
# aujourd'hui pour le premier cours du module "AP: Apprentissage de la Programmation en Python",
# nous allons coder un petit jeu 

# %% [markdown]
# ## objectifs
#
# ce qu'on veut faire aujourd'hui principalement, c'est :
#
# * vérifier les installations de tout le monde
# * installation et utilisation d'une librairie
# * pratiquer en vraie grandeur la boucle
#   * écriture de code
#   * lancement de programme
#   * debugging éventuellement
# * de préférence avec
#   * vs-code pour l'édition de programme
#   * le terminal pour le lancement du programme  
# * écriture de **code simple**
#   * pas nécessairement besoin de structures de données compliquées
# * priorité à la pratique
#   * utiliser git et faire un commit à chaque étape
#   * bien utiliser vs-code et la palette
#   * bref, mieux utiliser son environnement
# * en plus c'est ludique !

# %% [markdown]
#
# ```{admonition} un repo pour rendre vos devoirs
# :class: important
#
# pour rendre vos devoirs, vous allez
# - créer un repo **privé** sur github,
# - appelez-le `ap-homework`
# - et vous allez **ajouter votre prof comme collaborateur**
# - le TP vous indique de créer un dossier `mysnake`, du coup assurez-vous de le créer **dans le repo `ap-homework`**
# - de cette façon vous n'aurez plus qu'à faire vos *commit*, puis un (ou plusieurs si nécessaire) *push*, pour exposer votre travail au prof
# ```

# %% [markdown]
# ## avertissement
#
# il y a dans vs-code une fonction de *terminal intégré* qui peut être pratique  
# ça évite de basculer sans cesse entre deux applications (vs-code / terminal)
#
# **toutefois**  
# par expérience c'est plus compliqué à faire marcher correctement  
# c'est pourquoi **commencez par** faire marcher votre programme dans le **terminal natif**  
# surtout si vous rencontrez des problèmes dans le terminal intégré de vs-code
#
# notez qu'on peut facilement **basculer entre les applications**  
# sans passer par la souris avec la touche `⌘-Tab` (et une clé similaire sur Windows)

# %% [markdown]
# ## le TP
#
# ````{admonition} TP snake
#
# Voyez le TP qui se trouve ici
#
# <https://flotpython-exos-python.readthedocs.io/en/main/tps/snake/README-snake-nb.html>
# ````

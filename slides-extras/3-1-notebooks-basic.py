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
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: introduction aux notebooks
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown] slideshow={"slide_type": ""}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# </div>

# %% slideshow={"slide_type": "slide"}
from plan import plan_extras; plan_extras("notebooks")

# %% [markdown] slideshow={"slide_type": "slide"}
# # introduction aux notebooks

# %% [markdown]
# ## c'est quoi un notebook ?

# %% [markdown]
# un document hybride qui mélange:
#
# * du texte formatté,
# * des équations et illustrations,
# * avec des fragments de code exécutable,
# * possiblement interactifs.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## un exemple en ligne

# %% [markdown]
# la revue Nature a publié en janvier 2015 un exemple de notebook interactif
#
# * longtemps en ligne [sur nature.com](http://www.nature.com/news/ipython-interactive-demo-7.21492)
# * sources dans github <https://github.com/jupyter/nature-demo/>
#
# c'est un exemple très parlant de ce qu'on peut en faire.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## les grandes lignes

# %% [markdown]
# * le notebook est une suite de cellules
# * chacune typée 'Markdown' ou 'Code'
# * *Shift+Enter*: pour évaluer une cellule et passer à la suivante

# %% [markdown]
# * le code est exécuté par le lecteur - qui peut donc **le modifier**
# *  par exemple pour **faire varier** interactivement les paramètres

# %% [markdown] slideshow={"slide_type": "slide"}
# # pourquoi c'est intéressant ?

# %% [markdown]
# ## applications assez immédiates
#
# dans les domaines de
#
# * publication scientifique,
# * éducation,
# * ingénierie...

# %% [markdown] slideshow={"slide_type": "slide"}
# ## publication

# %% [markdown]
# * plus adapté au monde du 21-ème siècle
# * que le papier - fût-il en pdf -  
#   qui est un format … de la fin du 15-ème !

# %% [markdown]
# * début de réponse à l'idéal du *runnable paper*
# * ouvre la voie à une recherche plus reproductible
# * et à l'exploration autour des conditions originales

# %% [markdown] slideshow={"slide_type": "slide"}
# ## éducation

# %% [markdown]
# * idéal pour assembler le cours et les TPs qui vont avec
# * sans que l'étudiant ait son attention dispersée 
# * par d'incessants changements de contexte

# %% [markdown] slideshow={"slide_type": "slide"}
# ## autres intérêts

# %% [markdown]
# * communication entre professionels
# * assembler explications, données et code
# * ...

# %% [markdown] slideshow={"slide_type": "slide"}
# # un peu d'histoire

# %% [markdown]
# * tout début 2001-2005 : premiers essais infructueux (Perez + Kern)
# * 2-ème essai 2007-2011 : première release de IPython fin 2011
# * 2014: Jupyter - spin-off de IPython
#   * IPython est maintenant le nom du kernel Python
#   * autres kernels disponibles (R, Julia, ...)
# * 2017: JupyterLab - environnement tout-en-un

# %% [markdown] slideshow={"slide_type": "slide"}
# ## histoire (suite)
#
# * similitudes avec le modèle de notebook de sage a.k.a. <sagemath.org>
# * et aussi semble-t-il avec un google notebook (service fermé en 2012)
# * tous inspirés des notebooks mathematica (1988!) et des worksheets maple
#

# %% [markdown]
# ## sources
#
# * [Fernando Perez (IPython)](http://blog.fperez.org/2012/01/ipython-notebook-historical.html)
# * [William Stein (Sage)](https://groups.google.com/forum/#!topic/sage-devel/uc9HIMREh9Y)
# * [Une bonne synthèse](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook#gs.aOP5gG0)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## situation actuelle
#

# %% [markdown]
# * projet en pleine effervescence
# * connu d'abord sous le nom de ipython (jusque 2014)
# * renommé en Jupyter (Julia - Python - R)  
#   plus ouvert aux autres langages
# * nouvel outil disponible sous le nom jupyterlab
# * il serait vain de vouloir enseigner ces outils
# * détails modifiés en permanence
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## le format notebook
#

# %% [markdown]
# il reste cependant - heureusement ! - que :
#
# * le format du notebook est stable, bien documenté,
# * avec des outils de conversion 'command-line' simples
# * et des APIs maintenues.

# %% [markdown] slideshow={"slide_type": "slide"}
# # premiers pas jupyter notebook
#

# %% [markdown]
# * je conseille de démarrer par  
#   une **installation locale** de jupyter
# * on peut aussi envisager une approche hébergée  
#   (jupyterhub, nbhosting, sagemath)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### installation (1) Jupyter avec anaconda
#
# * si vous avez installé anaconda, vous avez déjà Jupyter :)
#

# %% [markdown]
# ### installation (2) jupyter avec pip
#
# * sinon avec `pip`
#
# ```
# pip install jupyter jupyterlab
# ```
#

# %% [markdown] slideshow={"slide_type": "slide"}
#
# les sous-commandes disponibles
#
# ```
# $ jupyter --help
# usage: jupyter <snip> [subcommand]
#
# jupyter: interactive computing
#
# positional arguments:
#   subcommand     the subcommand to launch
#
# <snip>
# available subcommands: console kernelspec lab labextension migrate
# nbconvert nbextension notebook qtconsole <snip>
# ```
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## sous commandes
#
# | *commande* | *objet*                          |
# |------------|----------------------------------|
# | **notebook**   | interface traditionnelle jupyter |
# | lab        | nouvelle interface jupyterlab    |
# | &nbsp; | &nbsp; |
# | **nbconvert**  | conversions diverses             |
# | &nbsp; | &nbsp; |
# | kernelspec | gestion des noyaux disponibles   |
# | nbextension | gestion de plugins jupyter      |
# | labextension | gestion de plugins jupyterlab  |
# | &nbsp; | &nbsp;|
# | console    | cli pour interagir avec noyau    |
# | qtconsole  | idem sous interface qt           |
#
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## utilisation typique
#
# ```
# $ jupyter notebook
# ```
#
# va faire plusieurs choses:
#
# * lance un serveur (web) de notebooks
#   * `the jupyter notebook is running at: http://localhost:8888/?token=blabla`
# * crée une fenêtre/tab dans un browser (selon vos réglages)
# * qui se connecte au service de notebooks
#
#

# %% [markdown] slideshow={"slide_type": "slide"}
# # mon premier notebook
#
# ![](media/notebooks-001-run.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-002-welcome.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-003-creating-py3.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-004-renaming.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-005-named.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-006-saved.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### contenu
#
# * suite de cellules
# * chacune typée 'markdown' ou 'code'
# * (ou aussi d'ailleurs 'raw' mais j'en déconseille l'usage)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-007-markdown.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-008-insert-cell.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-009-code-cell.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### la logique édition / commande
#
# * la couleur de la cellule sélectionnée indique le mode

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-010-edit-mode.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-011-cmd-mode.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### commandes utiles
#
# * les commandes clavier avec *Entrée*
#   * Control-Entrée : évaluer la/les cellule(s)
#   * Maj-Entrée : évaluer et passer à la suite
#   * Alt-Entrée : évaluer et insérer une cellule vide
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### et dans les menus
#
# voir surtout
#
# * *File -> Save*
#   * note: checkpoints : pas disponible
#
# * *File -> Download as ...*
#   * par exemple obtenir le notebook comme un `.py`
#
# * *Kernel -> Restart & Clear output*
# * *Kernel -> Restart & Run all*
#

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# ### raccourcis clavier
#
# pour visualiser :
#
# * menu : *Help -> Keyboard Shortcuts*
# * command-mode : tapez `H`
# * edit-mode: tapez `Control-M H`

# %% [markdown] cell_style="split" slideshow={"slide_type": ""}
# ![](media/notebooks-020-keyboard-shortcuts.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## à retenir:
#
# * mode 'édition' : `control-m` + clé
# * mode 'commande' : clé directement
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## raccourcis **très utiles**
#
# | raccourci | effet |
# |-----------|---------|
# | `y` | cellule(s) de type code |
# | `m` | cellule de type markdown |
# | `1`..`6` | markdown + titre |
#
# #### et aussi
#
# | raccourci | effet |
# |-----------|---------|
# | `a` | insère une cellule au dessus |
# | `b` | insère une cellule au dessous |
# | `f` | find & replace |
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## sélection de plusieurs cellules
#
# * Maj-Flêche (haut/bas)
# * Maj-J/K

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-030-sel-mult.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-031-sel-moved-down.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### les cellules de texte

# %% [markdown]
# les deux composantes pour la partie texte:
#     
# * le format [`markdown`](https://en.wikipedia.org/wiki/Markdown)
# * le langage [`mathjax`](https://www.mathjax.org/) pour les équations à la $\LaTeX$

# %% [markdown] slideshow={"slide_type": "slide"}
# ### markdown

# %% [markdown] slideshow={"slide_type": ""}
# * popularisé notamment grâce à github
#   * README.md
#   * usage pervasif sur tout le site
# * commence à être très répandu
# * déployé par exemple sur les forums FUN

# %% [markdown] slideshow={"slide_type": "slide"}
# ## sections
#
# ```
# # titre 1
# ## titre 2
# ### etc.
# ```
#
# # titre 1
# ## titre 2
# ### etc.
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### listes à bulles

# %% [markdown] slideshow={"slide_type": "slide"}
# ```
#
# * une liste à bulles
# * avec d'autres bulles
#   * et s'il le faut
#   * des sous-bulles
# ```
#
# * une liste à bulles
# * avec d'autres bulles
#   * et s'il le faut
#   * des sous-bulles

# %% [markdown] slideshow={"slide_type": "slide"}
# ### listes à numéros

# %% [markdown] slideshow={"slide_type": "slide"}
# ```
# 1. une liste à numéros
# 1. avec d'autres bulles
#   1. et s'il le faut
#   1. des sous-bulles
# ```
#
# 1. une liste à numéros
# 1. avec d'autres bulles
#   1. et s'il le faut
#   1. des sous-bulles

# %% [markdown] slideshow={"slide_type": "slide"}
# ### styles (1)

# %% [markdown] slideshow={"slide_type": ""}
# ```
#
# * le plus utile `pour montrer du code`
# * ou du texte **en gras**
# * ou *en italique*
# * ou ***en gras italique***
# ```
#
# * le plus utile `pour montrer du code`
# * ou du texte **en gras**
# * ou *en italique*
# * ou ***en gras italique***

# %% [markdown] slideshow={"slide_type": "slide"}
# ### styles (2)

# %% [markdown] slideshow={"slide_type": ""}
#     ```
#     Un long fragment qu'on veut laisser tel quel
#     e.g. une sortie de terminal
#     ```
#
# ```
# Un long fragment qu'on veut laisser tel quel
# e.g. une sortie de terminal
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### liens

# %% [markdown] slideshow={"slide_type": ""}
# ```
# l'url telle quelle https://github.com ou <https://github.com>
# ```
#
# l'url telle quelle https://github.com ou <https://github.com>

# %% [markdown] slideshow={"slide_type": "-"}
# ```
# [le texte qui apparait](http://github.com/)
# ```
#
# [le texte qui apparait](http://github.com/)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### image

# %% [markdown] slideshow={"slide_type": "-"}
# sans changement de taille
#
# ```
# ![une légende](media/markdown-cheatsheet-online-1.png)
# ```
#
# ![une légende](media/markdown-cheatsheet-online-1.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# et la suite..
# ![une légende](media/markdown-cheatsheet-online-2.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### block quotes

# %% [markdown] slideshow={"slide_type": ""}
# ```
# > anecdotique, mais parfois on a besoin de citer quelqu'un,
# > comme pour les messages électroniques
# > > les citations peuvent être emboitées
# ```
#
# > anecdotique, mais parfois on a besoin de citer quelqu'un,
# > comme pour les messages électroniques
# > > les citations peuvent être emboitées

# %% [markdown] slideshow={"slide_type": "slide"}
# ### remarques

# %% [markdown] slideshow={"slide_type": ""}
# * markdown pas extrêmement bien standardisé
# * notamment pour les tables
# * mais beaucoup plus compact et pratique
# * que des versions plus lourdes comme notamment reST
# * accepter la philosophie (simpler is better)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### Mathjax

# %% [markdown] slideshow={"slide_type": "slide"}
# * [mathjax](https://github.com/mathjax/MathJax)
# * supporte une grosse partie des équations $\LaTeX$
# * principalement il suffit d'insérer 
#   * entre deux `$` (inline)
#   * entre deux `$$` (paragraphe)
#
# * exemples tirés de [wikipedia](https://en.wikibooks.org/wiki/LaTeX/Mathematics)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### équations (1)

# %% [markdown] slideshow={"slide_type": ""}
# ```
# on peut sans souci insérer $f(n) = n^5 + 4n^2 + 2 |_{n=17}$
# au beau milieu d'une ligne
# ```
#
# on peut sans souci insérer $f(n) = n^5 + 4n^2 + 2 |_{n=17}$ 
# au beau milieu d'une ligne
#
# ou simplement utiliser $\bigotimes$ un seul symbole de la ménagerie $\LaTeX$
#
# ou mettre des caractères Unicode → bien entendu

# %% [markdown] slideshow={"slide_type": "slide"}
# ### équations (2)
#
# mais si l'équation est un peu plus grosse, sur sa propre ligne

# %% [markdown] cell_style="split"
# ```
# $ x = a_0 + \cfrac{1}{a_1 
#           + \cfrac{1}{a_2 
#           + \cfrac{1}{a_3 + \cfrac{1}{a_4} } } } $
# ```

# %% [markdown] cell_style="split" slideshow={"slide_type": "-"}
# $ x = a_0 + \cfrac{1}{a_1 
#           + \cfrac{1}{a_2 
#           + \cfrac{1}{a_3 + \cfrac{1}{a_4} } } } $

# %% [markdown] slideshow={"slide_type": "slide"}
# ### équations (3)

# %% [markdown] cell_style="split"
# ```
# $
# A_{m,n} = 
#  \begin{pmatrix}
#   a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
#   a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
#   \vdots  & \vdots  & \ddots & \vdots  \\
#   a_{m,1} & a_{m,2} & \cdots & a_{m,n} 
#  \end{pmatrix}
# $
# ```

# %% [markdown] cell_style="split" slideshow={"slide_type": "-"}
# $
# A_{m,n} = 
#  \begin{pmatrix}
#   a_{1,1} & a_{1,2} & \cdots & a_{1,n} \\
#   a_{2,1} & a_{2,2} & \cdots & a_{2,n} \\
#   \vdots  & \vdots  & \ddots & \vdots  \\
#   a_{m,1} & a_{m,2} & \cdots & a_{m,n} 
#  \end{pmatrix}
# $

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exercice
#
# objectifs
#
# * pour créer votre premier notebook
# * lancez `notebook jupyter`
# * préférablement dans un dossier vide
#

# %% [markdown] slideshow={"slide_type": ""}
# et surtout, familiarisez vous avec **les raccourcis** clavier
#
# * `esc` et `entrée` pour alterner commande / édition
# * `control-m` `1`..`6` pour les titres
# * `shift-entrée` pour passer à la cellule suivante
# * `control-m` `m` / `control-m` `y` pour alterner markdown/code
# * flêches haute et basse
# * shift-flêche : sélection multiple
# * déplacement vers le haut et bas

# %% [markdown] slideshow={"slide_type": "slide"}
# ### voir aussi

# %% [markdown] slideshow={"slide_type": ""}
# voyez le menu 'home'
#
# * correspond au répertoire où vous avez lancé jupyter
# * vous permet de renommer les notebooks
# * et les supprimer

# %% [markdown] slideshow={"slide_type": "slide"}
# ## nouvelle interface: jupyterlab
#
# * disponible en 1.0 depuis Juillet 2019
# * multiples outils
# * dans *un seul tab* du browser
#
# ```
# $ pip show jupyterlab
# Name: jupyterlab
# Version: 1.1.1
# ...
# ```
#

# %% [markdown] slideshow={"slide_type": "slide"}
#
# ```
# $ jupyter lab
# ```
#
# ![](media/notebooks-041-lab-welcome.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-042-lab-3tabs.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-043-lab-commands.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-044-lab-multi-tools.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-045-lab-terminal.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-046-lab-console.png)
#

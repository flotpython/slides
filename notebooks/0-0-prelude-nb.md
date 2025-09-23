---
celltoolbar: Slideshow
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  cell_metadata_json: true
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
  title: "pr\xE9lude"
---

# Programmer en Python

> *Des fondamentaux à l'utilisation du langage*


[![Published](https://img.shields.io/badge/Published-Website-green)](https://python.info-mines.paris)
[![MyST Build Status](https://img.shields.io/github/actions/workflow/status/flotpython/slides/myst-to-pages.yml?branch=main&label=MyST%20Build%20Status)](https://github.com/flotpython/slides/actions/workflows/myst-to-pages.yml)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/flotpython/slides)
[![nbhosting (requires login)](https://img.shields.io/badge/nbhosting-(requires%20login)-blueviolet)](https://nbhosting.inria.fr/auditor/notebook/python-slides)

[![License: CC BY-NC-ND](https://img.shields.io/badge/License-CC%20BY--NC--ND-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/4.0/) `thierry.parmentelat@inria.fr` - `arnaud.legout@inria.fr`

+++

## plateformes et liens

### exercices

[![exos Python](https://img.shields.io/badge/exos-Python-darkgreen)](htps://python-exos.info-mines.paris)
[![exos mooc autocorrigés (requires login)](https://img.shields.io/badge/exos%20mooc-autocorrigés%20(requires%20login)-blueviolet)](https://nbhosting.inria.fr/auditor/notebook/exos-mooc)
[![exos Data Science](https://img.shields.io/badge/exos-Data%20Science%20(accessoirement)-darkgreen)](htps://numerique-exos.info-mines.paris)


### support pour installations

[![Extrait du cours des Mines](https://img.shields.io/badge/Extrait%20du%20cours%20des%20Mines-online-blue)](https://ue12-p25.github.io/intro/1-1-installations/)
[![Vidéo de démo des outils](https://img.shields.io/badge/Vidéo%20de%20démo%20des%20outils-YouTube-red?logo=youtube)](https://www.youtube.com/watch?v=i_ZcP7iNw-U)



````{admonition} pour cloner ce cours

```bash
git clone https://github.com/flotpython/slides.git
```

````

+++

### et aussi le MOOC

en ligne sur France Université Numérique:  
le MOOC "Python 3 : des fondamentaux aux concepts avancés du langage"  
<https://www.fun-mooc.fr/en/cours/python-3-des-fondamentaux-aux-concepts-avances-du-langage/>

+++

## outils et notebooks

on peut suivre le cours sans installation locale (plateforme nbhosting, jupyterlite)  
par contre si vous optez pour une installation locale, il vous faut idéalement (cette liste figure dans la doc d'installation ci-dessus)

- un terminal avec `git` (sur Windows: "git for windows" vient avec un terminal "bash")
- un éditeur de code - (vs-code)
- une installation Python - évidemment - (miniconda)
- IPython, et Jupyter pour les notebooks
  qui s'installe - comme tous les outils Python - avec
  ```bash
  pip install jupyter
  ```

````{admonition} suivez bien les instructions
:class: admonition-small

c'est utile de se souvenir que `pip install` est la commande magique qui permet d'installer de nouveaux modules  
dans notre cas toutefois, on a besoin d'un peu plus que jupyterlab, veillez à bien suivre les instructions d'installation et [**notamment cette partie**](https://ue12-p25.github.io/intro/1-1-installations/#-les-librairies-num%C3%A9riques)
````

+++

### cloner le repo

```bash
$ cd le/bon/dossier
$ git clone https://github.com/flotpython/slides
$ cd slides/notebookes
$ ls
```

+++

### IPython

```bash
# depuis le terminal
$ cd le/bon/dossier/slides/notebooks

$ ipython
Python 3.12.2 | packaged by conda-forge | (main, Feb 16 2024, 21:00:12) [Clang 16.0.6 ]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.23.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: print("hello world")
hello world

In [2]: exit()
$ 
```

+++

### Jupyter

```bash
# depuis le terminal
$ cd le/bon/dossier/slides/notebooks

$ jupyter lab
... qui va ouvrir une fenêtre dans le navigateur
... il vous faut alors laisser ce terminal tranquille, il est occupé...
```

* double-cliquez sur un nom de fichier pour l'ouvrir  
* terminez votre session avec *File* -> *Shut Down*: votre terminal redevient disponible

````{admonition} jupytext

avec les notebooks sauvés au format texte, (`*-nb.md` ou `*-np.py`), si le double clic ouvre un fichier texte, c'est que vous n'avez pas bien suivi les consignes d'installation, et [**notamment cette partie**](https://ue12-p25.github.io/intro/1-1-installations/#-les-librairies-num%C3%A9riques)
````

+++

### naviguer dans les cellules

pour naviguer dans les cellules :

si nécessaire au début : sélectionner avec la souris, puis

````{admonition} utiliser ***Maj-Entrée* / *Shift-Enter***
:class: tip

pour

* **évaluer la cellule courante** (le dernier résultat s'affiche)
* et **passer à la cellule suivante**
````

on peut aussi utiliser la flêche triangulaire dans la menubar,
mais c'est beaucoup moins pratique, car en fait on passe son temps à faire essentiellement ça !

à vous d'essayer; bien sûr vous pouvez revenir en arrière et modifier une cellule, mais il faut bien penser à toujours l'évaluer

```{code-cell} ipython3
X = 10 * 30
X
```

```{code-cell} ipython3
L = [1, X]
L
```

````{admonition} exercice
:class: seealso

* modifiez la première cellule ci-dessus pour faire en sorte que X vaille 400
* regardez maintenant la valeur de `L`
* et évaluez la seconde cellule, vérifiez que la valeur de `L` a bien changé
````

+++

### nbhosting

sur nbhosting vous avez sans installation: jupyter + le cours  
utilisez les boutons pour cacher / afficher la structure du cours

```{image} media/nbhosting-buttons.png
:align: center
:width: 500px
```

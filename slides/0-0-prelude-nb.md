---
celltoolbar: Slideshow
ipub:
  sphinx:
    toggle_input: true
    toggle_input_all: true
    toggle_output: true
    toggle_output_all: true
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted,-editable
  cell_metadata_json: true
  encoding: '# -*- coding: utf-8 -*-'
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,-language_info.version,
    -language_info.codemirror_mode.version, -language_info.codemirror_mode,-language_info.file_extension,
    -language_info.mimetype, -toc, -version
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
rise:
  slideNumber: c/t
  start_slideshow_at: selected
  theme: sky
  transition: cube
---

+++ {"slideshow": {"slide_type": "slide"}}

Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# Cours Python

##### *Des fondamentaux à l'utilisation du langage*

+++ {"cell_style": "split"}

Thierry Parmentelat - Inria  

`thierry.parmentelat@inria.fr`

+++ {"slideshow": {"slide_type": "slide"}}

## plateformes et liens

* notebooks
  * <https://nbhosting.inria.fr/>
* contenu de ce cours en version HTML statique
  * <https://flotpython-slides.readthedocs.io/>
* les sources des notebooks :
  * <https://github.com/flotpython/slides>

* exercices autocorrigés
  * <https://nbhosting.inria.fr/auditor/notebook/exos-mooc>

+++ {"slideshow": {"slide_type": "slide"}}

### et aussi le MOOC

en ligne sur France Université Numérique

* le MOOC "Python 3 : des fondamentaux aux concepts avancés du langage"  
  <https://www.fun-mooc.fr/en/cours/python-3-des-fondamentaux-aux-concepts-avances-du-langage/>

+++ {"slideshow": {"slide_type": "slide"}, "cell_style": "split"}

## notebooks

* introduction très rapide au fonctionnement de la plateforme

+++ {"slideshow": {"slide_type": ""}, "cell_style": "split"}

  * utilisez les boutons pour cacher / afficher  
    la structure du cours

+++ {"cell_style": "split"}

![](media/nbhosting-buttons.png)

+++ {"slideshow": {"slide_type": "slide"}, "cell_style": "split"}

### notebooks - naviguer dans les cellules

+++ {"slideshow": {"slide_type": ""}, "cell_style": "split"}

pour naviguer dans les cellules :

si nécessaire au début : sélectionner avec la souris, puis

````{admonition} utiliser ***Maj-Entrée* / *Shift-Enter***
:class: tip

pour

* **évaluer la cellule courante** (le dernier résultat s'affiche)
* et **passer à la cellule suivante**
````

on peut aussi utiliser la flêche triangulaire dans la menubar, mais c'est beaucoup moins pratique, car en fait on passe son temps à faire essentiellement ça !

à vous d'essayer; bien sûr vous pouvez revenir en arrière et modifier une cellule, mais il faut bien penser à toujours l'évaluer

```{code-cell} ipython3
:cell_style: split

X = 10 * 30
X
```

```{code-cell} ipython3
:cell_style: split

L = [1, X]
L
```

````{admonition} exercice
:class: seealso

* modifiez la première cellule ci-dessus pour faire en sorte que X vaille 400
* regardez maintenant la valeur de `L`
* et évaluez la seconde cellule, vérifiez que la valeur de `L` a bien changé

````
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

```{image} media/inria-50-alpha.png
:align: right
:width: 100px
```
Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

# Cours Python

> *Des fondamentaux à l'utilisation du langage*

+++

Thierry Parmentelat - Arnaud Legout - Inria  

`thierry.parmentelat@inria.fr` - `arnaud.legout@inria.fr`

+++

## plateformes et liens

| contenu | url |
|-:|:-|
| HTML statique | <https://flotpython-slides.readthedocs.io/> |
| sources des notebooks | <https://github.com/flotpython/slides> |
| notebooks live (nécessite un login) | <https://nbhosting.inria.fr/> |
| exercices autocorrigés (idem) | <https://nbhosting.inria.fr/auditor/notebook/exos-mooc> |

+++

### et aussi le MOOC

en ligne sur France Université Numérique:  
le MOOC "Python 3 : des fondamentaux aux concepts avancés du langage"  
<https://www.fun-mooc.fr/en/cours/python-3-des-fondamentaux-aux-concepts-avances-du-langage/>

+++

## notebooks

* introduction très rapide au fonctionnement de la plateforme
* utilisez les boutons pour cacher / afficher la structure du cours

```{image} media/nbhosting-buttons.png
:align: center
:width: 500px
```

+++

### notebooks - naviguer dans les cellules

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

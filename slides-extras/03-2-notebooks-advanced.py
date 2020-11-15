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
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: "notebooks avanc\xE9s"
# ---

# %% [markdown] cell_style="split" slideshow={"slide_type": "slide"}
# # `nbdime`
#
# ## *notebook diff and merge*
#
# * `pip install nbdime`
#   * `nbdime config-git --enable`
# * sortie sur terminal ou sur browser
#   * et connectable à git
# * [exemples](https://github.com/jupyter/nbdime)

# %% [markdown] cell_style="split"
# ### Sous-commandes:
#
# * `diff`
# * `merge`
# * `diff-web`
# * `merge-web`
# * `mergetool`
# * `config-git`

# %% [markdown] slideshow={"slide_type": "slide"}
# # architecture
#
# [schéma sur http://jupyter.readthedocs.io](http://jupyter.readthedocs.io/en/latest/architecture/how_jupyter_ipython_work.html)
#
# ![](media/notebooks-040-architecture.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## acteurs
#
# imaginons que vous avez créé deux notebooks:
#
# * votre browser web - probablement 3 tabs (home, nb1, nb2)
# * un service http (notebook server)
# * et pour chaque notebook ouvert:
#   * un kernel ipython
#   * un fichier ipynb (json)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## console / qt-console
#
# * outils plus orientés 'command-line'
# * pour interagir avec un kernel aussi
# * [sur `readthedocs.io`](https://jupyter-console.readthedocs.io/en/latest/)
#
# ```
# jupyter console 
# jupyter qtconsole 
# ```
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## multiples acteurs / un kernel
#
# * Ainsi **plusieurs acteurs**
# * peuvent interagir avec **un seul kernel**
# * les deux voient alors **une seule variable**
#
# Voir par exemple `jupyter console --existing`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### format des notebooks

# %% [markdown] slideshow={"slide_type": ""}
# * format `.ipynb`
# * en réalité json
# * contient tout y compris résultats
# * et autres métadonnées (notebook + cellule)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `nbconvert`
#
# * un utilitaire pour convertir dans tous les sens
# * à retrouver sur [`readthedocs.io`](https://nbconvert.readthedocs.io/en/latest/)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### mise en forme
#
# * format par défaut html
#
# ```
# $ jupyter nbconvert foo.ipynb
# [nbconvertapp] converting notebook foo.ipynb to html
# [nbconvertapp] writing 251635 bytes to foo.html
# ```
#
# * ou en python
#
# ```
# $ jupyter nbconvert --to python foo.ipynb
# [nbconvertapp] converting notebook foo.ipynb to python
# [nbconvertapp] writing 114 bytes to foo.py
# ```
#

# %% [markdown] slideshow={"slide_type": "slide"}
# * autres formats disponibles au travers de
#   * $\LaTeX$ 
#   * et/ou [pandoc](https://github.com/jgm/pandoc)
# * requiert une installation séparée
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### exécution
#
# ```
# $ jupyter nbconvert --to notebook --execute foo.ipynb
# [nbconvertapp] converting notebook foo.ipynb to notebook
# [nbconvertapp] executing notebook with kernel: python3
# [nbconvertapp] writing 1364 bytes to foo.nbconvert.ipynb
# ```
#
# * le notebook a été entièrement exécuté avant d'être sauvé dans une copie.
# * ajouter `--inplace` pour modifier le notebook.
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### nettoyage
#
# ```
# pip install nbstripout
# nbstripout foo.py
# ```
#
# * enlève les résultats de l'évaluation des cellules
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### API
#
# * une API python complète est disponible pour écrire ses propres traitements.
# * si intérêt : [un exemple ici](https://github.com/flotpython/tools/blob/master/tools/nbnorm.py) 
#   * une moulinette pour nos notebooks du MOOC
#   * pas très élégant mais fait le job:
#   * vérifie la présence d'une première cellule auteur/licence
#   * efface les sorties
#   * vérifie/normalise certains traits markdown
#   * ...

# %% [markdown] slideshow={"slide_type": "slide"}
# # astuces

# %% [markdown]
# ## Command Palette
# `Cmd-Shift-P`
# ![](media/notebooks-047-command-palette.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## docstring
# `?`
# ![](media/notebooks-048-docstring.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### magics

# %% [markdown]
# * les *magics* sont des annotations spéciales
# * qui commencent par un '%'
# * il s'agit le plus souvent de commodités
# * qu'on ne pourrait pas faire directement en python

# %% [markdown]
# * [voir une liste complète ici](https://ipython.org/ipython-doc/3/interactive/magics.html)
# * `%lsmagic`
#

# %%
# ou bien sûr
# %lsmagic

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `%matplotlib`
#
# * `inline`
# * `notebook`
# * `nbagg`

# %%
import numpy as np

# %%
# %matplotlib inline
import matplotlib.pyplot as plt 
plt.ion()

# %% slideshow={"slide_type": "slide"}
x = np.linspace(0, 4*np.pi, 100)
y = 2*np.cos(x+2) + np.sin(2*x)
plt.plot(x, y);

# %% [markdown] slideshow={"slide_type": "slide"}
# ## supprimer l'affichage
#
# * finir une cellule de code par `;`
# * supprime l'impression automatique
# * (en fait, revient à ajouter une dernière expression `None`)

# %%
# %matplotlib inline
from matplotlib import pyplot as plt
plt.ion()

# %% slideshow={"slide_type": "slide"}
# %matplotlib inline

import numpy
x = 1 - numpy.linspace(0, 1, 100)**1.5
plt.hist(x)

# %% slideshow={"slide_type": "slide"}
x = 1 - numpy.linspace(0, 1, 100)**2.
plt.hist(x);

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `autoreload`

# %% [markdown]
# il s'agit d'une extension (chargée avec `load_ext`), très pratique lorsqu'un notebook importe un module qui est modifié en même temps - sous un éditeur comme spyder ou autre.
#
# le module est alors **rechargé automatiquement** à chaque modification du fichier.

# %%
# %load_ext autoreload
# %autoreload 2

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `%run`
#
# * permet d'exécuter un fichier python
# * **ou un autre notebook**
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-049-included-code.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-050-included-run.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## commandes shell

# %%
# %cd ..
# %ls
# %cd -

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `!` pour exécuter une commande

# %%
mots_de_passe = !cat /etc/passwd

# %%
for line in mots_de_passe[:6]:
    print(line)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## génération de html

# %%
from IPython.display import HTML
from itertools import product


# %%
def table_generator(xs, ys):
    html = "<table>"
    for x in xs:
        html += "<tr>"
        for y in ys:
            html += "<td>({}, {})</td>".format(x, y)
        html += "</tr>"
    html += "</table>"
    return HTML(html)


# %% slideshow={"slide_type": "slide"}
lines = [ 'a', 'b', 'c', 'd']
columns = range(1, 5)
table_generator(lines, columns)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## sélection de magics - python
#
# * `%%time` - `%timeit` - mesures de performance
# * `%prun` - `%lprun` - profiling 
# * `%debug` et `%pdb` - debugging
# * `%who` - liste les variables connues
# * je vous renvoie à [cet excellent article](https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## multiples kernels
#
# * on peut même semble-t-il mélanger plusieurs langages dans le même notebook
# * comme python2 / python3
# * ou python + r

# %% [markdown] slideshow={"slide_type": "slide"}
# # `interact`
#
# * souvenez-vous : le notebook de *Nature*
# * partie du projet `ipywidgets`
# * [voir sur `readthedocs.io`](http://ipywidgets.readthedocs.io/en/latest/examples/Using%20Interact.html)
#
# ```
# from ipywidgets import interact, fixed
# ```
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ## use case
#
# * visualisation de la fréquence:
# * partant de la fonction $sin_f: x \longrightarrow sin(f.x)$
#

# %% cell_style="split"
# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
plt.ion()


# %% [markdown] cell_style="split" slideshow={"slide_type": "-"}
# on veut créer 
#
# * une visualisation interactive
# * qui permette de *voir* l'effet du paramètre $f$

# %% slideshow={"slide_type": "slide"}
def sinus(freq):
    X = np.linspace(0., 10., 200)
    Y = np.sin(freq*X)
    plt.plot(X, Y)


# %% cell_style="split"
sinus(1)

# %% cell_style="split"
sinus(0.5)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `interact`
#
# grâce à interact on va pouvoir explorer ça de manière plus complète et plus interactive.

# %%
from ipywidgets import interact

# %%
interact(sinus, freq=(0.5, 10., 0.5));


# %% [markdown] slideshow={"slide_type": "slide"}
# ## appel à `interact`

# %% [markdown]
# * premier argument: une fonction `f`
# * +: autant d'arguments supplémentaires
#   * que de paramètres attendus par `f`
# * chacun est un `Slider`

# %% [markdown]
# par exemple
#
# * si `f` prend deux aguments `foo` et `bar`
# * `interact(f, foo=.., bar=..)`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## bouche-trou: `fixed`

# %% [markdown]
# * quand un des paramètres reste fixe

# %%
# la fonction x**omega entre phi et phi + 1
def histo2(omega, phi):
    plt.hist(np.linspace(phi, phi+1, 100)**omega, alpha=0.3)


# %%
from ipywidgets import fixed
interact(histo2, omega=(0., 2.), phi=fixed(0.))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## sliders

# %% [markdown]
# * en fait cet appel à interact
#   * `interact(histo2, omega=(0., 2.))`
# * est un raccourci pour
#   * `interact(histo2, omega=Floatslider(min=0., max=2.))`

# %% [markdown] slideshow={"slide_type": "slide"}
# ce qui permet un peu plus de réglages:
#
# * `min`, `max`, `step`
# * et `value` - valeur initiale

# %%
from ipywidgets import FloatSlider
interact(histo2, 
         omega=FloatSlider(min=0., max=2., value=1.83), 
         phi=fixed(0.));

# %% [markdown] slideshow={"slide_type": "slide"}
# ## sliders (ctd)

# %% [markdown]
# plusieurs types disponibles
#
# * booléen (checkbox)
# * texte (saisie utilisateur)
# * liste ou dict (choix multiples)

# %% slideshow={"slide_type": "slide"}
# une liste ou un dictionnaire est transformé(e) en un Dropdown
interact(histo2,
         omega={'petit': 0.1, 'moyen': 0.5, 'plat': 1.0}, 
         phi=fixed(0.));

# %% [markdown] slideshow={"slide_type": "slide"}
# * [liste complète des widgets](http://ipywidgets.readthedocs.io/en/latest/examples/widget%20list.html)
# * et [notamment sur dropdown](http://ipywidgets.readthedocs.io/en/latest/examples/widget%20list.html#dropdown)

# %%
from ipywidgets import Dropdown
interact(histo2, 
         omega=Dropdown(options={'petit': 0.1, 'moyen': 0.5, 'plat': 1.0}),
         phi=fixed(0.))

# %% [markdown] slideshow={"slide_type": "slide"}
# ## calculs lourds
#
# * créer un slider avec `continuous_update=false`
# * pour éviter mises à jour trop fréquentes

# %% [markdown] slideshow={"slide_type": "slide"}
# # extensions
#
# * notebook : `nbextension`
# * server : `serverextension`
# * jupyterlab: `labextension`

# %% [markdown] slideshow={"slide_type": "slide"}
# ```
# $ jupyter nbextension --help
# <snip>
# Examples
# --------
#
#     jupyter nbextension list                          # list all configured nbextensions
#     jupyter nbextension install --py <packagename>    # install an nbextension from a Python package
#     jupyter nbextension enable --py <packagename>     # enable all nbextensions in a Python package
#     jupyter nbextension disable --py <packagename>    # disable all nbextensions in a Python package
#     jupyter nbextension uninstall --py <packagename>  # uninstall an nbextension in a Python package
#
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ```
# parmentelat ~/git/cours-python/cstb $ jupyter serverextension list
# config dir: /Users/parmentelat/.jupyter
#     jupyter_nbextensions_configurator  enabled
#     - Validating...
#       jupyter_nbextensions_configurator  OK
# config dir: /Library/Frameworks/Python.framework/Versions/3.5/etc/jupyter
#     jupyterlab  enabled
#     - Validating...
#       jupyterlab  OK
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### `jupyter_nbextensions_configurator`
#
# * [sur github](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator)
#
# ```
# pip install jupyter_nbextensions_configurator
# jupyter nbextensions_configurator enable --user
# ```
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/notebooks-051-nbextensions-configurator.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ### infrastructure
#
# * mybinder.org
# * jupyterhub

# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Slideshow
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
#   notebookname: "outils de g\xE9n\xE9ration de doc"
#   rise:
#     autolaunch: true
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown] slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# </div>

# %%
from plan import plan_extras; plan_extras("doc", "outils")

# %% [markdown] slideshow={"slide_type": "slide"}
# # génération de documentation

# %% [markdown] slideshow={"slide_type": "-"}
# * PEPs
# * outils de génération de documents
#   * [doxygen](http://www.stack.nl/~dimitri/doxygen/) (non détaillé)
#   * [sphinx](http://www.sphinx-doc.org/en/stable/)
#   * [mkdocs](http://www.mkdocs.org/): plus orienté markdown (non détaillé)
# * langages de markup : reST, markdown et doctest
# * styles de docstrings : reST, google et numpy
# * readthedocs.io (infra / présentation séparée)

# %% [markdown] slideshow={"slide_type": "slide"}
# # PEPs
#
# * [PEP8](https://www.python.org/dev/peps/pep-0008/#documentation-strings)
#
# pas très bavard sur le sujet, mentionne simplement
#
# * quels objets doivent avoir un docstring 
#   * correspond à l'interface publique / visible de l'extérieur
#   * l'utilisation de `"""` plutôt que `'''`
#   * et renvoie pour l'essentiel à PEP 257

# %% [markdown] slideshow={"slide_type": "slide"}
# * [PEP257](https://www.python.org/dev/peps/pep-0257/)
# qui se dépêche de préciser les contours:
#
# > The aim of this PEP is to standardize the high-level structure of docstrings: what they should contain, and how to say it (without touching on any markup syntax within docstrings). The PEP contains conventions, not laws or syntax.

# %% [markdown]
# et heureusement sans doute !
#
# * imaginez à quoi ressemblerait le markup si on l'avait décidé en 2001
# * une époque où on pensait que le wiki est une idée géniale..

# %% [markdown] slideshow={"slide_type": "slide"}
# > If you violate these conventions, the worst you'll get is some dirty looks. But some software (such as the Docutils [3] docstring processing system [1] [2] ) will be aware of the conventions, so following them will get you the best results.

# %% [markdown] slideshow={"slide_type": "slide"}
# # génération de documents: `sphinx`
#
# * outil d'extraction et mise en forme doc
# * en provenance
#   * de parties écrites directement dans un markup
#   * et une partie en provenance du code (autodoc)
# * de nombreux *plugins* (extensions)
#   * qui implémentent les différents styles de docstring
#   * et autres themes..
# * [doc officielle](http://www.sphinx-doc.org/en/stable/)  

# %% [markdown] slideshow={"slide_type": "slide"}
# ### conseil
#
# * l'autodoc en provenance des méthodes et fonctions
#   * est certes utile et nécessaire
#   * mais ça ne *devrait pas* être la partie prépondérante
# * il est souvent **très utile**
#   * de donner des exemples simples (readme/tuto)
#   * et autres (install/changelog)

# %% [markdown]
# ### installation
#
# * requise sur l'ordi de chaque collaborateur
# * susceptible de travailler sur la doc
# * pour pouvoir tester le résultat en local
#
# ```
# pip3 install sphinx
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### démarrage
#
# * à faire une seule fois sur le projet
# * puis poussé sur git (essentiellement `conf.py`et `index.rst`)
#
# ```
# sphinx-quickstart
# ```
#
# et répondre aux questions
#
# ```
# > autodoc: automatically insert docstrings from modules (y/n) [n]: y
# > doctest: automatically test code snippets in doctest blocks (y/n) [n]: y
# > mathjax: include math, rendered in the browser by mathjax (y/n) [n]: y
# > viewcode: include links to the source code of documented python objects (y/n) [n]: y
# > create makefile? (y/n) [y]: y
# > create windows command file? (y/n) [y]: y
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### structure usuelle

# %% [markdown] slideshow={"slide_type": "slide"}
# ```
# Creating file ./conf.py.
# Creating file ./index.rst.
# ```
#
# #### point d'entrée `index.rst`
#
# * typiquement inclut d'autres morceaux
# * dont généralement par exemple un API.rst
# * contient un TOC
#
# #### configuration `conf.py`
#
# * définit les extensions à **importer**
#   * ATTENTION: ne fait **pas** d'installation automatique
# * pour ajouter du markdown (setup readthedocs)
#
# ```
# source_parsers = {
#     '.md': CommonMarkParser,
# }
# source_suffix = ['.rst', '.md']
# ```

# %% [markdown] slideshow={"slide_type": "slide"}
# ### inclusion

# %% [markdown] slideshow={"slide_type": "-"}
# * inclure d'autres morceaux de documentation
#
# ```
# $ cat index.rst
# Contents:
#
# .. toctree::
#    :maxdepth: 3
#
#    README
#    API
# ```
#
# * a pour effet d'inclure `README.md` et `API.rst`

# %% [markdown] slideshow={"slide_type": "slide"}
# ## autodoc
#
# ```
# .. autofunction:: io.open
#
# .. automodule:: io
#     :members:
# ```
#
# * voir [ici pour plus de détails](http://www.sphinx-doc.org/en/stable/ext/autodoc.html)
#
# * comme par exemple les clauses 
#   * `autoclass`
# * ou d'autres clauses reconnues dans `automodule`
#   * `:inherited-members:`
#   * `:show-inheritance:`
#   * etc...

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un exemple simple avec reST + markdown
#
# * [source](https://github.com/parmentelat/asynciojobs/tree/master/sphinx/source)
# * [résultat sur readthedocs](http://asynciojobs.readthedocs.io/en/latest/)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### un exemple plus élaboré
#
# * [source](https://github.com/ronf/asyncssh/tree/master/docs)
# * [résultat sur readthedocs](http://asyncssh.readthedocs.io/en/latest/)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## génération *per se*
#
# ### raccourcis
#
# * `make html`
# * `make help`
#
# ### ou
#
# * `sphinx-build -b html sourcedir builddir`

# %% [markdown] slideshow={"slide_type": "slide"}
# ### langages de markup

# %% [markdown] slideshow={"slide_type": "-"}
# ## markdown
#
# * très répandu et en plein boom
# * natif dans **github** notamment
# * dans **notebooks**
# * et de très nombreux outils sociaux (e.g. FUN)
#
# * impact du markup aussi léger que possible 
# * le source **reste lisible**

# %% [markdown] slideshow={"slide_type": "slide"}
# ### outils
#
# * e.g. atom
# * librairie python `markdown2`
# * etc etc...

# %% [markdown]
# * exemple d'un site web
#   * qui en partant [de ceci](https://raw.githubusercontent.com/parmentelat/r2lab/public/r2lab.inria.fr/markdown/tools.md)
#   * affiche [cela](https://r2lab.inria.fr/tools.md)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## reST
#
# * historiquement assez répandu
# * mais en train de passer de mode 
# * avantages
#   * syntaxe non floue
#   * très complet
#   * très utilisé
# * inconvénients
#   * **pas très lisible**
# * [un cheat sheet](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
# * librairie python `docutils`
#   * et binaires comme e.g. rst2html.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ## doctest
#
# * l'outil qui permet de reconnaitre des snippets comme
# ```
#    >>> une_expression()
#    le_resultat_attendu
# ```
#
# * peut apparaître au milieu d'un docstring typiquement
# * donc pas un format à part entière comme les deux précédents
# * [un exemple](https://github.com/django/django/blob/master/django/utils/text.py#L223)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### usages de doctest
#
# les snippets doctest servent à la fois
#
# * à des fins de **documentation**
#   * si on le met dans le docstring
# * et aussi de test
#   * grâce à l'outil `doctest`

# %% slideshow={"slide_type": "slide"}
# !cat samples/pgcd.py

# %% slideshow={"slide_type": "slide"}
# !python3 -m doctest -v samples/pgcd.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ### limitations de doctest
#
# * limité à comparer les sorties
# * impossible d'écrire des scénarii compliqués

# %% [markdown] slideshow={"slide_type": "slide"}
# ### mon opinion
#
# * utile sur un (très) **petit** projet pour
#   * donner des exemples simples
#   * dont on peut vérifier qu'ils sont à jour
# * mais fait double emploi avec par exemple
#   * un notebook de readme
#   * de vrais tests unitaires

# %% [markdown] slideshow={"slide_type": "slide"}
# # styles de docstring

# %% [markdown] slideshow={"slide_type": "slide"}
# ## SO
#
# Un bon résumé dans [ce post sur stackoverflow](http://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format) qui dit par ailleurs
#
# > @sorin, I also would like to know what markup, if any, is most common. But I think the answer is that none of them is really all that common: people tend to prefer to look at the Python source directly, rather than converted to html. So, it's most useful to just be consistent but in a way that's optimized for human readability, and no explicit markup. – poolie Oct 21 '12 at 7:31

# %% [markdown] slideshow={"slide_type": "slide"}
# ## reST
#
# * [exemple](http://thomas-cokelaer.info/tutorials/sphinx/_modules/template.html)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## google style
#
# > ReStructuredText is great, but it creates visually dense, hard to read docstrings. 
#
# * [extension sphinx](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html) `sphinx.ext.napoleon`
# * [exemple](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## numpy style
#
# * [même extension sphinx](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/index.html) `sphinx.ext.napoleon`
# * [exemple](http://www.sphinx-doc.org/en/stable/ext/example_numpy.html)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## `napoleon`
#
# * la même extension sphinx
# * supporte les deux styles
# * et est [décrite en détail ici](http://www.sphinx-doc.org/en/stable/ext/napoleon.html)

# %% [markdown] slideshow={"slide_type": "slide"}
# # micro-exemples

# %% [markdown] slideshow={"slide_type": "-"}
# ## micro-exemple reST

# %%
# !cat samples/random_rest.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ## micro-exemple numpy

# %%
# !cat samples/random_numpy.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ## micro-exemple numpy + typehints

# %%
# !cat samples/random_numpy_typehints.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ## micro-exemple google

# %%
# !cat samples/random_napo.py

# %% [markdown] slideshow={"slide_type": "slide"}
# ## micro-exemple google + typehints

# %%
# !cat samples/random_napo_typehints.py

# %% [markdown] slideshow={"slide_type": "slide"}
# # `readthedocs.io`
#
# * infra publique d'hébergement de la doc produite
# * facile à connecter aux webhooks de gitlab/github
# * supporte aussi [`mkdocs`](http://www.mkdocs.org/) pour markdown en sus de sphinx
# * présentation séparée..

# %% [markdown] slideshow={"slide_type": "slide"}
# # exercice
#
# * choisir un (ou 2) des 3 styles proposés
# * créer une branche dans le projet
# * adapter les docstrings
# * faire tourner sphinx  en local
# * committer / pousser / merger dans master

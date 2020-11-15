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
#   notebookname: readthedocs.io
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

# %% slideshow={"slide_type": "slide"}
from plan import plan_extras; plan_extras("doc", "readthedocs")

# %% [markdown] slideshow={"slide_type": "slide"}
# # `readthedocs.io`

# %% [markdown]
# * système communautaire
# * pour héberger la documentation
# * mode 'on installe et on oublie'
#   * connecté aux *webhooks* de gitlab/github
#   * i.e. regénère la documentation à chaque commit
# * possiblement pour plusieurs branches / tags

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple
# ![](media/readthedocs-example-01.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ## exemple
# ![](media/readthedocs-example-02.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# # Exemple de création de projet

# %% [markdown]
# ![](media/readthedocs-setup-01.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/readthedocs-setup-02.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/readthedocs-setup-03.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/readthedocs-setup-04.png)
#

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/readthedocs-setup-05.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/readthedocs-setup-06.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/readthedocs-setup-08.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/readthedocs-setup-09.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/readthedocs-setup-10.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/readthedocs-setup-11.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/readthedocs-setup-12.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# # Troubleshooting

# %% [markdown]
# Allons voir https://readthedocs.org/projects/apssh/builds

# %% [markdown] slideshow={"slide_type": "slide"}
# ![](media/readthedocs-troubleshot.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# Une fois qu'on en a terminé
#
# ![](media/readthedocs-view-doc.png)

# %% [markdown] slideshow={"slide_type": "slide"}
# ### rebase
#
# * ça peut être un peu fastidieux naturellement
# * et on n'a pas d'autre choix que de committer/pousser
# * aussi il peut être utile de créer une branche spécifique
# * pour pouvoir rebaser le tout une fois que c'est terminé

# %% [markdown] slideshow={"slide_type": "slide"}
# # documentation

# %% [markdown]
# * Bien évidemment elle est sur `readthedocs`
# * à cette adresse https://docs.readthedocs.io/en/latest/

# %% [markdown] slideshow={"slide_type": "slide"}
# # les points principaux

# %% [markdown] slideshow={"slide_type": ""}
# ## formats
#
# * reStructuredText
# * markdown
# * https://docs.readthedocs.io/en/latest/getting_started.html#write-your-docs
#
#
# ## outils
#
# * sphinx
# * mkdocs
# * https://docs.readthedocs.io/en/latest/builds.html#build-process

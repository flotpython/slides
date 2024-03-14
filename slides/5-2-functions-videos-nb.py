# -*- coding: utf-8 -*-
# ---
# jupyter:
#   celltoolbar: Edit Metadata
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -rise, -version
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
#     title: 'cours 8/9: les fonctions'
# ---

# %% [markdown]
# Licence CC BY-NC-ND, Thierry Parmentelat & Aurélien Noce

# %% [markdown]
# # fonctions : intro en 4 vidéos

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown]
# ## objectifs
#
# le programme pour cette partie
#
# * étudier les objets de type fonction, et notamment
#   * le passage de paramètre
#   * les fonctions comme citoyen de niveau 1
#   * la visibilité des variables  

# %% [markdown]
# ## vidéos

# %% hide_input=false
# les vidéos sur youtube
parts = (
    ("le passage des arguments", "8hLlyUbXZ3U", "12:53"),
    ("les clôtures", "msoWN4wSplM", "5:45"),
    ("la syntaxe lambda", "Rsu9O1soTsA", "2:32"),
    ("les générateurs", "DqYM_XMVtKw", "7:22"),
)

# %% [markdown]
# ***évaluez la cellule suivante*** pour faire apparaitre le sommaire des vidéos, en 4 parties

# %% hide_input=false scrolled=false
from IPython.display import display, HTML, IFrame

def index_as_embedded():
    for index, (title, stem, duration) in enumerate(parts, 1):
        display(HTML(f"<h3>{index}. {title} ({duration})</h3>"))
        display(IFrame(f"https://www.youtube.com/embed/{stem}", width=800, height=450))

index_as_embedded()

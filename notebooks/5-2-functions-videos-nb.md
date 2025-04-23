---
celltoolbar: Edit Metadata
jupytext:
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
  title: 'cours 8/9: les fonctions'
---

# fonctions : sommaire vidéos

+++

Licence CC BY-NC-ND, Thierry Parmentelat & Aurélien Noce

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

## vidéos

+++

***évaluez la cellule suivante*** pour faire apparaitre le sommaire des vidéos, en 4 parties

```{code-cell} ipython3
:tags: [remove-input]

# les vidéos sur youtube
parts = (
    ("le passage des arguments", "8hLlyUbXZ3U", "12:53"),
    ("les clôtures", "msoWN4wSplM", "5:45"),
    ("la syntaxe lambda", "Rsu9O1soTsA", "2:32"),
    ("les générateurs", "DqYM_XMVtKw", "7:22"),
)

from IPython.display import display, HTML, IFrame

def index_as_embedded():
    for index, (title, stem, duration) in enumerate(parts, 1):
        display(HTML(f"<h3>{index}. {title} ({duration})</h3>"))
        display(IFrame(f"https://www.youtube.com/embed/{stem}", width=800, height=450))

index_as_embedded()
```

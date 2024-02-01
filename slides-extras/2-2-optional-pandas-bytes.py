# -*- coding: utf-8 -*-
# ---
# jupyter:
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
#   notebookname: pandas & bytes (optionnel)
#   rise:
#     slideNumber: c/t
#     start_slideshow_at: selected
#     theme: sky
#     transition: cube
#   version: '1.0'
# ---

# %% [markdown] cell_style="center" slideshow={"slide_type": "slide"}
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat</span>
# </div>

# %%
import pandas 

# %%
columns = ['a','b', 'c', 'd', 't']
df = pandas.read_csv("https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv", 
                     names = columns, header=1)


# %%
df.head()
print(type(df['t'][0]))

# %%
print("values ->", type(df.values))
line1 = df.values[0]
print("line1 ->", type(line1))

# %%
line1.dtype

# %%
import sys
sys.version_info

# %%
i = 'été'

# %%
type(i)

# %%
b = i.encode(encoding='utf-8')

# %%
type(b)

# %%
b

# %%
len(b)

# %%
b.decode(encoding='utf-8') == i

# %%
b2 = i.encode(encoding='cp1252')
len(b2)

# %%
with open('windows', 'w') as f:
    f.write(b.decode(encoding='cp1252'))

# %%
# !pwd

# %%
pandas.read_csv('windows')

# %%
with open('windows', 'rb') as f:
    print(f.read())


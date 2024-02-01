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
#   notebookname: pandas
#   rise:
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

# %% slideshow={"slide_type": "-"}
from plan import plan_extras; plan_extras("pandas")

# %% [markdown] slideshow={"slide_type": "slide"}
# # pandas

# %% [markdown]
# from `Python for data analysis`, Wes McKinney

# %% [markdown]
# # objectives
#
# * data structures with labeled axes
#   * automatic or explicit data alignment
# * integrated time series functionality
# * same data structure for time series or non-time series
# * arithemtic operations and reductions (on a whole column)
# * flexible handling of missing data
# * merge and other relation operations as found in popular db systems, e.g. sql-based

# %%
import pandas as pd

# %% slideshow={"slide_type": "slide"}
from pandas import Series, DataFrame

# %% [markdown] slideshow={"slide_type": "slide"}
# # `Series`

# %% [markdown]
# a `Series` corresponds roughly to a column (values) in an excel spreadsheet, with names (index) attached to lines

# %% cell_style="split"
# by default lines are numbered
ser = Series([4, 7, -5, 3])
ser

# %% cell_style="split"
ser.values

# %% cell_style="split"
list(ser.index)

# %% slideshow={"slide_type": "slide"}
# attaching names to lines
ser2 = Series([4, 7, -5, 3],
              index = ['d', 'b', 'a', 'c'] )
ser2

# %% cell_style="split"
ser2['a']

# %% cell_style="split"
ser2['d'] = 6
ser2

# %% cell_style="split"
# extract a list of lines
ser2[ ['c', 'a', 'b'] ]

# %% cell_style="split"
# numpy operations
ser2[ser2 > 0]

# %% cell_style="split" slideshow={"slide_type": "slide"}
ser2 * 2

# %% cell_style="split"
# looking for keys (lines)
'b' in ser2

# %%
'e' in ser2

# %%
# creating from a regular python dict
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}

ser3 = Series(sdata)
ser3

# %%
# providing a dict *and* an index 
# may lead to discarding data or undefined data
states = ['California', 'Ohio', 'Oregon', 'Texas']

ser4 = Series(sdata, index = states)
ser4

# %%
ser4.isnull()

# %% [markdown] slideshow={"slide_type": "slide"}
# ### combining 2 `Series` (here, addition)
#
# a notion called **data alignment**

# %% cell_style="split"
ser3

# %% cell_style="split"
ser4

# %%
ser3 + ser4

# %% [markdown] slideshow={"slide_type": "slide"}
# ### the `name` attribute

# %%
ser4.name = 'population'
ser4.index.name = 'state'

# %%
ser4

# %% [markdown] slideshow={"slide_type": "slide"}
# ### altering the index in place

# %%
ser

# %%
ser.inde = ['Bob', 'Steve', 'Jeff', 'Ryan']

# %%
ser

# %% [markdown] slideshow={"slide_type": "slide"}
# # `DataFrame`

# %% [markdown]
# a data frame corresponds roughly to a full spreadsheet with
#
# * cells can be accessed by row or by column
# * 2 dimensions mostly symmetrical

# %% slideshow={"slide_type": "slide"}
data = {'state' : ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year' : [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

# %%
# providing data as a dict
frame = DataFrame(data)
frame

# %%
# ordering the columns
DataFrame(data, columns=['year', 'state', 'pop'])

# %%
# specifying undefined column to make space
# and names for rows (in index like for Series)
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index = ['one', 'two', 'three', 'four', 'five'])

# %%
frame2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### retrieving columns
#
# one can retrieve each column as a `Series` object, note the `name` attribute is set properly.

# %% cell_style="split"
# accessing a column
# returns a Series
frame2['state']

# %% cell_style="split"
# ditto throuh an attribute 
frame2.year

# %%
# all series share the same index
frame2['state'].index is frame2['pop'].index

# %% [markdown] slideshow={"slide_type": "slide"}
# ### retrieving rows
#
# this also returns a `Series` !

# %% cell_style="split"
frame2.loc['three']

# %% cell_style="split"
type(frame2.loc['three'])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### modifying columns by assignment

# %%
import numpy as np

# %%
# this uses numpy broadcasting
frame2['debt'] = 16.5
frame2

# %%
# from a numpy array
frame2['debt'] = np.random.randint(0, 10, 5)
frame2

# %%
# ditto from a Series
# missing data will be marked as NaN
newdebt = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = newdebt
frame2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### creating a new column

# %%
# just assign as if it was existing
frame2['eastern'] = frame2.state == 'Ohio'
frame2

# %%
# deleting 
del frame2['eastern']
frame2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### columns are shared data

# %%
pop = frame2['pop']
pop

# %%
pop['three'] = 5
frame2

# %% [markdown] slideshow={"slide_type": "slide"}
# ### creating from a dict of dicts

# %%
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

# %%
frame3 = DataFrame(pop)
frame3

# %% [markdown] slideshow={"slide_type": "slide"}
# ### transposing

# %%
# like with numpy
frame3.T

# %% [markdown] slideshow={"slide_type": "slide"}
# ### specifyng the index

# %%
#  like with Series, one can set `index`
DataFrame(pop, index=[2001, 2002, 2003])

# %% [markdown] slideshow={"slide_type": "slide"}
# ### ` values` returns a ndarray

# %%
frame3.values

# %% [markdown] slideshow={"slide_type": "slide"}
# ### numpy type

# %%
# here we have a homogeneous array
frame3.values.dtype

# %%
# when several types are mixed: using numpy wildcard object type
frame2.values

# %%
frame2.values.dtype

# %% [markdown] slideshow={"slide_type": "slide"}
# # ` Index`  objects

# %%
ser = Series(range(3), index=['a', 'b', 'c'])
index = ser.index
index

# %%
# slicing
index[1:]

# %%
# cannot write through the index
try:
    index[0] = 'x'
except TypeError as e:
    print(" OOPS", e)

# %%
# sharing of indexes
index = pd.Index(np.arange(3))

# %%
ser11 = Series([1.5, -2.5, 0], index=index)

# %%
ser11.index is index

# %% [markdown] slideshow={"slide_type": "slide"}
# ### index like a fixed size set

# %%
frame3

# %%
'Ohio' in frame3.columns

# %%
2000 in frame3.index

# %% [markdown] slideshow={"slide_type": "slide"}
# # essential functionality

# %% [markdown]
# ## reindexing

# %% cell_style="split"
ser21 = Series([4.5, 7.2, -5.3, 3.6],
               index = ['d', 'b', 'a', 'c'])
ser21

# %% cell_style="split"
# create a new Series
ser22 = ser21.reindex(['a', 'b', 'c', 'd', 'e'])
ser22

# %% cell_style="split"
ser21.reindex(['a', 'b', 'c', 'd', 'e'], fill_value=0)

# %% cell_style="split"
ser21

# %%
ser21.values is ser2.values

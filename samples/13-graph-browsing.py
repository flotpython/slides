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
# ---

# %% [markdown]
# # graph browsing

# %% [markdown]
# ## depth-first or breadth-first scanning
#
# given a non-valued directed graph G, and a start vertex V, there are 2 famous algorithm to walk the graph from V
#
# * depth-first (DF) browsing, and
# * breadth-first (BF) browsing
#
# intuitively :

# %%
from simpletree import tree

tree

# %% [markdown] cell_style="split"
# DF browsing from v would scan
# ```
# v v1 v11 v111 v112 
# v12 v121 v122 
# v2 v21 v211 v212 
# v22 v221 v222
# ```

# %% [markdown] cell_style="split"
# BF browsing would scan
# ```
# v 
# v1 v2 
# v11 v12 v21 v22
# v111 v112 v121 v122 v211 v212 v221 v222
# ```

# %% [markdown]
# ## objectives

# %% [markdown]
# we want to write a **generator** that implements these 2 browsing policies from a a graph and vertex.
#
# of course only the nodes reachable from the entry vertex will be browsed.

# %% [markdown]
# ## algorithms
#
# the algorithms used to perform these scans are, interestingly, very close to one another
#
# in both cases we need a STORAGE object, where we can store things and retrieve them later on

# %% [markdown]
# ### FIFO / FILO

# %% cell_style="split"
from collections import deque
class Fifo:
    def __init__(self):
        self.line = deque()
    def store(self, item):
        self.line.append(item)
    def retrieve(self):
        if self.line:
            return self.line.popleft()
    def __len__(self):
        return len(self.line)


# %% cell_style="split"
from collections import deque
class Filo:
    def __init__(self):
        self.line = deque()
    def store(self, item):
        self.line.append(item)
    def retrieve(self):
        if self.line:
            return self.line.pop()
    def __len__(self):
        return len(self.line)        


# %% cell_style="split"
fifo = Fifo()
for i in range(1, 4):
    fifo.store(i)
while fifo:
    print(f"retrieve → {fifo.retrieve()}")

# %% cell_style="split"
filo = Filo()
for i in range(1, 4):
    filo.store(i)
while filo:
    print(f"retrieve → {filo.retrieve()}")


# %%
# assumptions:
# vertices reachable from a vertex are 
# stored in a 'neighbours' attribute
def scan(start, storage):
    """
    scan all vertices reachable from start vertex
    in an order that is DF or BF depending on the 
    storage policy (fifo or filo)
    storage should have store() and retrieve() methods
    and be testable for emptiness (if storage: ...)
    also it should be empty when entering the scan
    """

    storage.store(start)
    # keep track of what we've seen
    scanned = set()
    
    while storage:
        current = storage.retrieve()
        # skip vertices already seen
        if current in scanned:
            continue
        yield current
        scanned.add(current)
        for neighbour in current.neighbours:
            storage.store(neighbour)


# %%
class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = set()
        
    def __repr__(self):
        return self.name


# %%
# rebuild sample graph
def tree_vertex(name, depth):
    if depth == 0:
        return Vertex(name)
    elif depth > 0:
        result = Vertex(name)
        result.neighbours.add(tree_vertex(name+'1', depth-1))
        result.neighbours.add(tree_vertex(name+'2', depth-1))
        return result


# %%
g = tree_vertex('v', 3)
g

# %% [markdown] cell_style="split"
# ### FILO = DF - depth first

# %% [markdown] cell_style="split"
# ### FIFO = BF - breadth first

# %% cell_style="split"
for vertex in scan(g, Filo()):
    print(vertex)

# %% cell_style="split" inputHidden=false outputHidden=false
for vertex in scan(g, Fifo()):
    print(vertex)

# %% [markdown]
# ### applications

# %% [markdown]
# being a generator, we can combine it with all the `itertools` and the like

# %%
import itertools

# %% [markdown]
# for example, if we need to print every other vertex in a DF scan

# %% cell_style="split"
df_scan = scan(g, Filo())

for v in itertools.islice(df_scan, 0, None, 2):
    print(v)

# %% cell_style="split"
# notice that df_scan is now exhausted !

for v in itertools.islice(df_scan, 0, None, 2):
    print(v)

# %% [markdown]
# or skip the first 3..

# %%
df_scan = scan(g, Filo())

for v in itertools.islice(df_scan, 3, None):
    print(v)

# %% [markdown] cell_style="center"
# ***

# %% [markdown]
# applied on the graph from 'game of thrones' 
#

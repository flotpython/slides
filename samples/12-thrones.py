# -*- coding: utf-8 -*-
# ---
# jupyter:
#   ipub:
#     sphinx:
#       toggle_input: true
#       toggle_input_all: true
#       toggle_output: true
#       toggle_output_all: true
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
#   notebookname: pagerank on a graph
#   version: '1.0'
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% [markdown]
# # pagerank on a graph

# %% [markdown]
# *pagerank* is a graph metric made famous by Google, who has been using it - at its beginning - to sort pages found in an Internet search, so as to show most relevant pages first.

# %% [markdown]
# ## what is pagerank

# %% [markdown]
# in a valued and directed graph, each edge in the graph has an integer value attached to it
#
# for such graphs [pagerank](https://en.wikipedia.org/wiki/PageRank) aims at describing something akin "popularity" for each vertex
#
# ### no damping
# the original **(no damping)** model roughly goes as follows
#
# * all vertices (pages in the case of the Web) have an equal likelihood to be your starting point
# * at each step, you consider the outgoing links, and randomly pick one as your next step, with relative probabilities based on the outgoing weights  
#   that is to say, if for instance your current vertex has three outgoing links, with weighs 20, 40 and 60, then the first neighbor has 1/6 likelihood to be the next one, and second and third neighbors have 1/3 and 1/2 respectively.
#
# pagerank is then defined on each vertex as the relative number of times that you'll have visited that vertex after an infinite random walk that follows those rules

# %% [markdown]
# ### with damping
#
# the above model has a flaw, as it does not account for people actually restarting from scratch their path in the web; 
# for that reason, in practice the following model **(with damping)** is more widely used 
#
# * all vertices (pages in the cas of the Web) have an equal likelihood to be your starting point
# * at each step, you would either
#   * with a **0.15** probability restart from a randomly picked vertex (with an equal likelihood) 
#   * or otherwise pick your next vertex like in the original model, using outgoing weight relative probability
#   
# in this example, we used a standard **damping factor** value of 85% (usually named $d$) 

# %% [markdown]
# ## overview
#
# we are going to compute this measure on a graph
#
# instead of dealing with web pages, we will use a dataset that describes the graph of weighed **relationships between characters** in a novel related to the ***Game of Thrones*** saga;  
# but since a graph is a graph, we can apply the same algorithm to this one, and give each character a rank, that may be perceived as some sort of popularity.
#
# so in a nutshell we need to build a graph in memory, and use this to simulate the logic of the random walk described above; theory has proven that the measure should converge to a stable value, provided that simulation is long enough, and we will verify this experimentally.
#
#
# here are the steps that we will take to this end :
#
# 1. **aquisition**  
#   1. get raw data over http, it is located here  
#     https://raw.githubusercontent.com/pupimvictor/NetworkOfThrones/master/stormofswords.csv  
# 1. **parsing**  
#   1. understand what this data represents
#   1. design a data structure that can capture this information in a way that is convenient for the simulation that we want to run on the graph
#   1. build that data structure from the raw data obtained during first step
# 1. **simulation**
#   1. pagerank can be computed by linear algebraic methods - using a stochastic matrix to model the relative likelyhood to go to vertex $j$ knowning you're on $i$; however in this exercise we want to do a simulation
#   1. so once this graph is ready, we can write a simulation tool that walks the graph randomly following the *rules of the game* explained above
# 1. **observation** 
#   1. running the simulation several times with different lifespans rangin from several hops to a few thousands, we can experimentally check if we indeed obtain consistent results, i.e. constant results for all characters

# %% [markdown]
# *****

# %% [markdown]
# ## hints

# %% [markdown]
# ### for step **acquisition**
#
# * loading a csv as a pandas dataframe is a one-liner when using [pandas.read_csv](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html)
#
# * once you have a dataframe you will need to iterate on its rows  
#   this can be done like so (image the dataframe has columns LastName and FirstName)
#   
#   ```python
#   for i, line in df.iterrows():
#         print(f"line number {i}, {line.FirstName} {line.LastName}")
#   ```

# %% [markdown] tags=["level_intermediate"]
# Note that it is also possible to use [the `requests` library](https://requests.readthedocs.io/en/master/) to download the remote csv file right into memory
#
# Sine it is not part of the standard library, you need to install it with `pip install requests` 
#
# so it all comes down to using `requests.get` to create a request object, and then read this object's `text` attribute to download the data
#
# it is an alternative approach that takes more steps to do the job (at you will need to load the file yourself) but may be more flexible in other similar situations

# %% [markdown]
# ### for **parsing**
#
# the crucial part here is to imagine a data structure that depicts the graph; 
# we will need to model 'vertices' in the graph in a way that can be easily walked.
#
# many data structures can do the job, and our suggestion here is to use a dictionary of dictionaries; like in the following example
#
# ```
# test graph:
#    'A'   -- 10 ->  'B'
#    'A'   -- 20 ->  'C' 
#    'B'   -- 30 ->  'C' 
#    'B'   -- 40 ->  'D'
#    'D'   -- 20 ->  'A'
# ```
#
# would then be represented by a dictionary that looks like this
#

# %%
graph = {'A': {'B': 10, 'C': 20}, 
         'B': {'C': 30, 'D': 40},
         'D': {'A': 20}}

# %% [markdown]
# so to put it another way :
# * our graph's keys are the graph's vertices
# * the value attached (in the dictionary sense) to a vertex represents the outgoing links of that vertex
#
# so, because there is a link weighed 20 going from 'D' to 'A', we have

# %%
graph['D']['A'] == 20

# %% [markdown] tags=["level_intermediate"]
# if you'd rather go for using `requests` than `pandas`, one last word of warning about parsing:
# * you will start from a single `str` object (the raw data) that needs to be cut into lines first;  
#   for that, `str.split()` can do the job very well
# * however some of the lines obtained by this method may be either useless (there is often a first line with column names, and it is the case here too); the last line may be empty as well, so pay attention
# * for cutting a line into pieces, `str.split()` here again can do the job very nicely

# %% [markdown]
# ### for **simulating**
#
# of course you will need to [use the `ramdom` module](https://docs.python.org/3.7/library/random.html), and in particular `random.choice()` to pick in a list of choices. 
#
# one way to think about this problem is to create a class `RandomWalker`:
#
# * initialization (`__init__` method)
#   * we create an instance from a graph-dictionary and a damping factor
#   * we also want to model the current vertex, so a `current` instance attribute comes in handy
# * initialization (continued) - `init_random()` method
#   * this is optional, but in order to speed up simulation, we may want to prepare data structures that are ready for that purpose; in particular, each time we run a simulation step (move the current vertex), we want to randomly pick the next vertex with relative probabilities in line with the outgoing weighs
#   * as a suggestion, these data structures could be (a) a list of all vertices in the graph, so that one can be picked randomly using `random.choice()` and (b) a dictionary of similar structures for each vertex when it comes to picking a neigh bour
# * pick a start vertex - `pick_start_vertex()` method
#   * returns a starting vertex with a uniform probability
# * pick a neighbour vertex - `pick_neighbor_vertex()` method
#   * from the current vertex, return a neighbour picked randomly with the probabilities defined by their outgoing weighs.
# * simulate the graph for some number of steps - `walk()` method
#   * from all the above, it is easy to write the simulation
#   * result is a dictionary with vertices as key, and as value 
#     the number of steps spent in that vertex during the simulation
#   

# %% [markdown]
# ## YOUR CODE

# %% [markdown]
# ### data acquisition

# %%
URL = "https://raw.githubusercontent.com/pupimvictor/NetworkOfThrones/master/stormofswords.csv"

# %%
# your code here
# insert new cells with Alt-Enter

# %%
# your code here

# %% [markdown]
# ### parsing

# %%
# your code here

# %%
# your code here

# %% [markdown]
# ### simulation

# %%
import random

class PageRankWalker:
    

    def __init__(self, graph, damping=0.85):
        self.graph = graph
        self.damping = damping
        # current vertex
        self.current = None
        self.init_random()
        

    def init_random(self):
        """
        initialize whatever data structures 
        you think can speed up simulation
        """
        ...
        

    def pick_start_vertex(self):
        """
        randomly picks a start vertex
        with equal choices
        """
        ...

    def pick_next_vertex(self):
        """
        randomly picks a successor from current vertex
        using the weights
        """
        ...
        
        
    def walk(self, nb_steps):
        """
        simulates that number of steps
        result is a dictionary with 
        vertices as key, 
        and as value number of steps spent in that vertex
        """
        ...

# %% [markdown]
# ## running it

# %% [markdown]
# *** 
# RUNNING IT

# %%
# create a walker object from the graph obtained above
walker = PageRankWalker(graph)

# %% cell_style="split"
STEPS = 1000
frequencies = walker.walk(STEPS)

# %%
# the sum of all values should be STEPS
raincheck = sum(frequencies.values())
raincheck == STEPS 

# %%
raincheck, STEPS

# %%
# dicts are not so good at sorting
# let's use a list instead

tuples = [ (vertex, count) for vertex, count in frequencies.items() ]
tuples.sort(key = lambda tupl: tupl[1], reverse=True)

tuples[:4]

# %% [markdown]
# ***

# %% [markdown]
# make it reproducible

# %% [markdown]
# #### def monte_carlo(graph, steps):
#     """
#     run a simulation over that number of steps
#     """
#     walker = PageRankWalker(graph)
#     # simulate
#     frequencies = walker.walk(steps)
#     # retrieve result
#     tuples = [ (vertex, count) for vertex, count in frequencies.items() ]
#     # sort on highest occurrences first
#     tuples.sort(key = lambda tupl: tupl[1], reverse=True)
#     # display 5 most items
#     for character, count in tuples[:5]:
#         print(f"{character} was visited {count} times i.e. {count/steps:02%}")

# %%
# show top winners with a 1000-steps simu
for _ in range(5):
    print(f"{40*'-'}")
    monte_carlo(graph, 1000)

# %%
# same with a tenfold simulation
for _ in range(5):
    print(f"{40*'-'}")
    monte_carlo(graph, 10000)

# %% [markdown]
# ***

# %% [markdown]
# ### visualization (optional)

# %% [markdown]
# using [the graphviz library](https://graphviz.readthedocs.io/en/stable/examples.html) 
#
# installing dependencies is a 2-step process
#
# * the binary tool; for that [see the project's page](https://graphviz.gitlab.io/download/);  
#   also be aware that most common linux distros do support *graphviz*,  
#   so you can install them with either `dnf` or `apt-get`;  
#   or `brew` if on MacOS
#
# * the Python wrapper that you can install with (surprise !)
# ```bash
# pip install graphviz
# ```

# %%
# DiGraph stands for Directed Graph
# that's what we need since our graph is directed indeed

from graphviz import Digraph

# %%
gv = Digraph('Characters of the Thrones', filename='thrones.gv')

for source, weighted_dict in graph.items():
    for target, weight in weighted_dict.items():
        gv.edge(source, target, label=f"{weight}")

# %% cell_style="split"
gv.attr(rankdir='TB', size='12')
gv

# %% [markdown]
# # variants

# %% [markdown]
# * use the csv library to parse input
# * for scalability: the weights in a real graph can be much higher;  
#   a smarter implementation would remove the need for allocating the potentially large / huge lists in `weighted_dispatcher`

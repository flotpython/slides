# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: metro parisien
#   version: '1.0'
# ---

# %% [markdown]
# # le réseau du métro parisien

# %%
# %load_ext autoreload
# %autoreload 2

# %% [markdown]
# ![](metro.png)

# %%
from pathlib import Path
import numpy as np
import pandas as pd 

# %% [markdown]
# ## introduction

# %% [markdown]
# ### les données

# %% [markdown]
# on vous a préparé deux jeux de données qui décrivent le métro parisien

# %%
# a few constants
DATA = Path("DATA")

# %%
# load data
stations  = pd.read_csv(DATA/"stations.txt", index_col="station_id")
hops =      pd.read_csv(DATA/"hops.txt")

# %%
stations.head()

# %%
hops.head()

# %% [markdown]
# **SOURCE :** à l'origine [la source de ces données est la RATP](https://dataratp2.opendatasoft.com/explore/dataset/offre-transport-de-la-ratp-format-gtfs/information/) et [plus précisément ceci](http://dataratp.download.opendatasoft.com/RATP_GTFS_LINES.zip), prétraité par nos soins
#
# **DISCLAIMER** comme vous le verrez ces données ne sont pas parfaites, mais dans l'ensemble c'est un niveau de qualité suffisant pour notre propos d'aujourd'hui.

# %% [markdown]
# ### ce qu'on veut en faire
#
# 1. dessiner le réseau sur une carte
# 1. s'en servir de support pour visualiser deux algorithmes de parcours de graphe
#   * DFS : *depth-first-search*
#   * BFS : *breadth-first-search*

# %% [markdown]
# ### comment on se propose de le faire
#
# 1. construire une structure de données pour 
#   * ranger le graphe,
#   * pouvoir le parcourir rapidement/efficacement
# 2. afficher la carte avec la librairie `folium`
# 3. parcours :
#   1. implémenter les 2 parcours de graphe
#   1. numéroter les stations (en partant de Chatelet) selon les deux parcours
#   1. afficher les résultats  

# %% [markdown]
# ## structures de données

# %% [markdown]
# On va représenter le graphe avec plusieurs classes d'objet :
# * `Station` : contient les détails de l'arrêt ; ici on n'a gardé, parmi tous les détails exposés par la RATP, que les coordonnées latitude et longitude, mais dans un exemple plus réaliste on pourrait avoir ici plein de détails...
# * `Node` : modélise un noeud (sommet) dans le graphe, et ses noeuds voisins ;
# * `Graph` : contient l'ensemble des noeuds du réseau.

# %% [markdown]
# ![](data-structures.png)

# %% [markdown]
# ### le type `Station`

# %%
# le type Station correspond à une ligne 
# dans la dataframe chargée à partir de stations.txt
# ce serait assez redondant d'avoir à se redéfinir un type pour cela

# et grâce à la dataframe - que l'on a indexée par station_id
# on peut trouver la station correspondant à un station_id
# par accès direct (comme dans un dictionnaire)

# si je cherche par exemple la station dont l'id vaut 2152
station_sample = stations.loc[2152]
station_sample

# %%
try:
    station_sample['station_id']
except Exception as exc:
    print(f"OOPS - {type(exc)} : {exc}")

# %%
station_sample['latitude']

# %%
station_sample.name

# %%
# quel est le type de cet objet
type(station_sample)

# %%
# définissons un type
Station = pd.Series


# %% [markdown]
# ### le type `Node`
#
# Pour modéliser les relations entre stations, on *enrobe* le type `Station` avec un objet `Node` qui possède une référence vers une station, et aussi vers les noeuds voisins.
#
# La première idée consisterait à garder dans un attribut `self.neighbours` un `set` d'objets `Node`; mais comme on veut également attacher à chaque lien une information sur le numéro de ligne, on va plutôt utiliser un dictionnaire dans les clés sont les voisins et les valeurs les numéros de ligne.
#
# Ce qui nous donne :

# %%
class Node:
    """
    a node is part of a graph; it has a reference to a unique Station object
    and also to a set of Node's that are its immediate neighbours
    finally it has an optional 'label' attribute that we will use when 
    drawing the graph on a map
    """
    def __init__(self, station: Station):
        self.station = station
        # use a dictionary to attach a value to each link (here the line number)
        self.line_by_neighbour = dict() # type: Dict[Node -> str]
        self.label = None
        
    def __repr__(self):
        return str(f"[Node {self.station.name}]")
    
    def add_edge(self, neighbour: "Node", line):
        self.line_by_neighbour[neighbour] = line
        
    def nb_edges(self):
        return len(self.line_by_neighbour)
    
    def iter_neighbours(self):
        "iterates (neighbour, line) over neighbours"
        for neighbour, line in self.line_by_neighbour.items():
            yield neighbour, line

    @property
    def latitude(self):
        return float(self.station['latitude'])

    @property
    def longitude(self):
        return float(self.station['longitude'])        


# %%
class Graph:
    """
    the toplevel object that models the complete graph
    as essentially a set of nodes (thus of stations)
    for efficiency we also maintain an index of those hashed by station_id
    """
    def __init__(self):
        self.nodes = set()
        self.nodes_by_station_id = {}
        
    def add_node(self, station):
        """
        insert a station in graph; duplicates are simply ignored
        """
        # this is how to retrieve the 'index' column 
        # in an indexed dataframe (must not be indexed with inplace=True)
        station_id = station.name

        # don't add it if already there
        if station_id in self.nodes_by_station_id:
            return
        node = Node(station)
        self.nodes.add(node)
        self.nodes_by_station_id[station_id] = node
        
    def find_node_from_station_id(self, station_id):
        return self.nodes_by_station_id[station_id]

    def add_edge(self, from_station_id, to_station_id, line):
        """
        insert an edge - both ends must exist already
        """
        # locate both ends that MUST be present already
        node_from = self.find_node_from_station_id(from_station_id)
        node_to = self.find_node_from_station_id(to_station_id)
        if not node_from or not node_to:
            print(f"OOPS - cannot add edge {from_station_id}->{to_station_id}")
            return
        node_from.add_edge(node_to, line)
        
    def __len__(self):
        return len(self.nodes)
    
    def nb_edges(self):
        return sum(node.nb_edges() for node in self.nodes)
    
    def nb_nodes(self):
        return len(self.nodes)
    
    def iter_nodes(self):
        """
        an iterator on nodes
        """
        return iter(self.nodes)
    
    def iter_edges(self):
        """
        iterates over triples (node_from, node_to, line)
        """
        for node in self.iter_nodes():
            for neighbour, line in node.iter_neighbours():
                yield node, neighbour, line


# %% [markdown]
# ## construction du graphe

# %%
def build_graph(stations, hops):
    graph = Graph()
    for index, station in stations.iterrows():
        node = graph.add_node(station)
    for index, hop in hops.iterrows():
        graph.add_edge(hop['from_station_id'], hop['to_station_id'], hop['line'])
    return graph


# %%
metro = build_graph(stations, hops)

print(f"notre graphe a {metro.nb_nodes()} stations et {metro.nb_edges()} liens")

# %%
# exercice: calculer le nombre de lignes
lines = set()
for node, neighbour, line in metro.iter_edges():
    lines.add(line)

print(lines)

# %% [markdown]
# ## dessiner le graphe sur une carte

# %%
import folium

STATION_RADIUS = 100
MARKER_DIAMETER = 20

LINE_WIDTH = 7.5
STATION_COLOR = '#d22'

# %% [markdown]
# ### les couleurs des lignes

# %%
from nuancier import nuancier
nuancier

# %% [markdown]
# ### afficher les labels
#
# pour mettre en évidence une station (un peu fastidieux en folium)

# %%
from labelicon import label_icon

# %% [markdown]
# ### Chatelet au centre de la carte

# %%
chatelet_station_id = 2221
chatelet_station = stations.loc[chatelet_station_id]

# %%
map_center = [chatelet_station['latitude'], chatelet_station['longitude']]

# %% [markdown]
# ### ma première carte en folium

# %%
autre_station = stations.loc[2122]
autre_position = [autre_station['latitude'], autre_station['longitude']]

une_couleur = nuancier["1"]

# %% [markdown]
# On n'aura besoin que des classes suivantes
#
# * `folium.map`
# * `folium.map.Marker` pour attacher un label à chaque station
# * `folium.Circle`
# * `folium.PolyLine` pour tracer un trait

# %%
map = folium.Map(location=map_center, zoom_start=13)

folium.map.Marker(map_center, icon=label_icon('0')).add_to(map)
folium.Circle(map_center, STATION_RADIUS,
              fill=True, fill_color=une_couleur).add_to(map)

folium.map.Marker(autre_position, icon=label_icon('100')).add_to(map)
folium.Circle(autre_position, STATION_RADIUS,
              fill=True, fill_color=une_couleur).add_to(map)

folium.PolyLine([map_center, autre_position], 
                weight=LINE_WIDTH, color=une_couleur).add_to(map) 

map


# %% [markdown]
# ### contruire une `folium.Map` à partir du graphe

# %% [markdown]
# Nous voulons visualiser les stations, et les lignes. En option (si `show_labels=True`), on affichera aussi l'attribut `label` des objets `Node` lorsqu'il est défini.

# %%
def build_map(metro, show_labels=True):

    map = folium.Map(location=map_center, zoom_start=13)
    
    for node in metro.iter_nodes():
        if show_labels and node.label:
            folium.map.Marker(
                [node.latitude-0.0001, node.longitude-0.0001],
                icon=label_icon(node.label)
            ).add_to(map)
        folium.Circle(
            [node.latitude, node.longitude],
             STATION_RADIUS,
             fill=True,
             fill_color=STATION_COLOR,
        ).add_to(map)
    for node, neighbour, line in metro.iter_edges():
        line_color = nuancier[line]
        locations = [(node.latitude, node.longitude),
                     (neighbour.latitude, neighbour.longitude)]
        folium.PolyLine(locations=locations, 
                        weight=LINE_WIDTH, color=line_color).add_to(map)
            
    return map


# %%
# on met au moins un label pour voir l'effet
metro.find_node_from_station_id(chatelet_station_id).label = '0'

build_map(metro)

# %% [markdown]
# *****
# *****
# *****

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

# %% [markdown]
# DF browsing from v would scan
# ```
# v v1 v11 v111 v112 
# v12 v121 v122 
# v2 v21 v211 v212 
# v22 v221 v222
# ```

# %% [markdown]
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
# we want to write a **generator** that implements the 2 browsing policies from a vertex in a graph :
# * depth first search (DF or DFS)
# * breadth first search (BF or BFS)
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

# %%
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


# %%
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


# %%
fifo = Fifo()
for i in range(1, 4):
    fifo.store(i)
while fifo:
    print(f"retrieve → {fifo.retrieve()}")


# %%
filo = Filo()
for i in range(1, 4):
    filo.store(i)
while filo:
    print(f"retrieve → {filo.retrieve()}")


# %%
# assumptions:
# vertices reachable from a vertex are 
# stored in a 'neighbours' attribute
def scan(start_node, storage):
    """
    scan all vertices reachable from start vertex
    in an order that is DF or BF depending on the 
    storage policy (fifo or filo)
    storage should have store() and retrieve() methods
    and be testable for emptiness (if storage: ...)
    also it should be empty when entering the scan
    """

    storage.store(start_node)
    # keep track of what we've seen
    scanned = set()
    
    while storage:
        current_node = storage.retrieve()
        # skip vertices already seen
        # station.name is actually station['station_id']
        # but it is now indexed
        if current_node.station.name in scanned:
            continue
        yield current_node
        scanned.add(current_node.station.name)
        for neighbour, line in current_node.iter_neighbours():
            storage.store(neighbour)


# %%
def DFS(metro, station):
    node = metro.find_node_from_station_id(station.name)
    storage = Filo()
    yield from scan(node, storage)


# %%
def BFS(metro, station):
    node = metro.find_node_from_station_id(station.name)
    storage = Fifo()
    yield from scan(node, storage)


# %% [markdown]
# ## illustration

# %% [markdown]
# ### depth-first scan

# %%
# labelling all stations according to a DFS scan
for index, node in enumerate(DFS(metro, chatelet_station)):
    node.label = str(index)
print(f"index={index}")
build_map(metro)

# %% [markdown]
# ### breadth-first scan

# %%
# same with a BFS
for index, node in enumerate(BFS(metro, chatelet_station)):
    node.label = str(index)
print(f"index={index}")
build_map(metro)

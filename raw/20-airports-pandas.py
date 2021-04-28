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
#   notebookname: airports again, w/ pandas
#   version: '1.0'
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% [markdown]
# # Ditto - avec pandas

# %%
import pandas as pd

# %%
pd.options.display.max_rows = 8

# %% [markdown]
# # digression

# %% [markdown]
# À titre expérimental, nous importons un notebook comme un module python

# %%
# un loader personnalisé pour charger un notebook comme un module
from notebookloader import NotebookFinder

# %%
import sys
sys.meta_path.append(NotebookFinder())

# %%
# avec ce bidule on peut directement charger un notebook comme un module
from airports import distance_degrees

# %% [markdown]
# # airports

# %%
airports_url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"

# %%
airports = pd.read_csv(airports_url, header=None)

# %%
# si on n'en dit pas plus on obtient les données mais les noms laissent à désirer
airports

# %%
# on peut donner des noms aux colonnes
airports.columns = ["airport_id", "name", "city", "country", "iata", "icao", "latitude", "longitude", "altitude", "timezone", "dst", "tz", "airport", "source"]

# %%
# ne voir que le début
airports.head()

# %% cell_style="split"
# un échantillon
airport1 = airports.iloc[0]; airport1

# %% cell_style="split"
# pour information
type(airport1['airport_id'])

# %%
# airports.loc?

# %% [markdown]
# # airlines

# %% [markdown]
# pareil...

# %%
airlines_url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat"

# %%
airlines = pd.read_csv(airlines_url, header=None)

# %%
airlines.columns = ["airline_id", "name", "alias", "iata", "icao", "callsign", "country", "active"]

# %%
airlines.head(20)

# %%
# un échantillon
airline1 = airlines.iloc[2]; airline1

# %% [markdown]
# # routes

# %% [markdown]
# et encore une fois

# %%
routes_url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat"

# %%
routes = pd.read_csv(routes_url, header=None)

# %%
routes.columns = ["airline", "airline_id",
                  "src_airport", "src_airport_id", "dst_airport", "dst_airport_id",
                  "codeshare", "stops", "equipment"]

# %%
routes.tail(20)

# %% [markdown]
# ### un peu de nettoyage
#
# **attention** certaines ces lignes contiennent un `airline_id` - entre autres - non renseigné
#
# comme avec *numpy* on peut faire des opérations de comparaison, pour ne retenir par exemple ici que les lignes qui utilisables

# %%
valid_series = (routes['airline_id'] == r'\N')

# %% cell_style="split"
# cette expression renvoie une Series (colonne)
valid_series

# %% cell_style="split"
type(valid_series)

# %%
# comme la colonne est faite de booléens, 
# on peut s'en servir pour indexer dans la table
unusable_routes = routes[(routes['airline_id'] == r'\N')]
unusable_routes.iloc[0]

# %%
# le nombre d'entrées inutilisables 
# par rapport à airline_id
len(unusable_routes)

# %%
# le nombre total de routes exposées dans l'URL
nb_total_routes = len(routes)

# %% cell_style="center"
# pour filtrer, c'est à dire ne garder 
# que les lignes qui vérifient une condition
# ici on étend un peu le critère de validité
routes = routes[(routes['airline_id'] != r'\N') 
              & (routes['src_airport_id'] != r'\N') 
              & (routes['dst_airport_id'] != r'\N')]

# %%
# on prend une colonne, on la traduit en nombre
# car sinon on n'a que des chaines de caractères
routes['airline_id'] = pd.to_numeric(routes['airline_id'])

# %% cell_style="split"
# maintenant on a bien un entier
route1 = routes.iloc[0]
type(route1['airline_id'])

# %%
# en fait, plusieurs colonnes sont dans ce cas
# et ont besoin d'être traduites en nombres
for column in ('airline_id', 'src_airport_id', 'dst_airport_id'):
    routes[column] = pd.to_numeric(routes[column])

# %%
# sauf qu'à ce stade on a encore un souci de nettoyage
# car pour certaines routes, un des deux aéroports est inconnu
routes.iloc[170].dst_airport_id

# %%
airports[airports['airport_id'] == 7163]


# %%
# il faut donc nettoyer davantage
# XXX here...

# %% [markdown]
# ### distance

# %%
# rappel: on a importé distance_degrees du notebook 'airports'

# ici route est une ligne dans routes
def distance_route(route):
    src_airport = airports[airports['airport_id'] == route['src_airport_id']].iloc[0]
    dst_airport = airports[airports['airport_id'] == route['dst_airport_id']].iloc[0]
    return distance_degrees(
        src_airport['latitude'], src_airport['longitude'],
        dst_airport['latitude'], dst_airport['longitude'])


# %%
# on peut maintenant appliquer cette fonction à une route 
# c'est à dire une ligne de la table
route0 = routes.iloc[0]
distance_route(route0)

# %% cell_style="split"
route0

# %% [markdown]
# ### un histogramme

# %% [markdown]
# pour représenter la répartition des longueurs de routes

# %%
lengths = routes.apply(distance_route, axis=1)

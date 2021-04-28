# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernel_info:
#     name: python3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: airports et airlines
#   nteract:
#     version: 0.12.3
#   version: '1.0'
# ---

# %% [markdown]
# <div class="licence">
# <span>Licence CC BY-NC-ND</span>
# <span>Thierry Parmentelat &amp; Arnaud Legout</span>
# </div>

# %% [markdown] cell_style="split"
# # airports & airlines

# %% [markdown] cell_style="split"
# ### mise en forme de données depuis https://openflights.org/data.html

# %% [markdown]
# ### aller chercher une URL

# %%
# commençons par la liste des aéroports
airports_url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat"

# %% [markdown]
# pour aller chercher une url comme celle-ci, on utilise typiquement le module `requests`

# %%
import requests

# %% [markdown]
# qui s'utilise en deux temps

# %%
# la réponse donne juste le code http
response = requests.get(airports_url)

response

# %%
# pour obtenir le contenu 
dat = response.text

# %% [markdown]
# un aperçu du début

# %%
dat.split('\n')[:3]

# %% [markdown]
# regardons un échantillon à la fin de la chaine

# %%
dat[-200:]

# %% [markdown]
# ### découpage

# %% [markdown]
# on voit que les lignes sont séparées par des `\n`, on découpe donc

# %%
# le nom de variable nous indique qu'il s'agit d'une liste de chaines, 
# chacune correpondant à un aéroport
airport_strs = dat.split("\n")

# %% [markdown]
# **attention**: comme le texte contient un dernier `\n`, `split()` nous renvoie du coup un **dernier élément** qui est une **chaine vide**, il faudra s'en souvenir

# %%
airport_strs[-3:]

# %% [markdown]
# si on regarde un échantillon, un aéroport est décrit par une chaine qui ressemble à ceci

# %%
airport_line = airport_strs[100]
airport_line


# %% [markdown]
# ### digression: `sanitize`

# %% [markdown]
# on voit que chaque ligne a des champs séparés par une virgule, et que certains de ces champs - les chaines - commencent et finissent par un guillemet
#
# première idée pour ne pas trop s'embêter:
#
# * on découpe la ligne avec les `,`
# * et on enlève les guillemets de début et de fin de chaque champ

# %% [markdown]
# **risque** ce qu'on risque, ce serait qu'il y ait des vraies virgules à l'intérieur des quotes; dans ce cas-là il faudra écrire une expression régulière; mais c'est compliqué, alors on fait vite et sale

# %%
def sanitize(string):
    """
    enleve les " s'ils sont présents au début
    et à la fin de la chaine
    """
    # par prudence
    if len(string) <= 1:
        return string
    if string[0] == '"' and string[-1] == '"':
        return string[1:-1]
    return string


# %% cell_style="split"
# cas de coin : un seul caractère
print(sanitize('"'))

# %% cell_style="split"
# une chaine normale
print(sanitize("abc"))

# %% cell_style="split"
# là on doit enlever les quotes
print(sanitize('"abc"'))

# %% cell_style="split"
# seulement au début: on ne touche pas
print(sanitize('"abc'))

# %% [markdown]
# ### airports - suite

# %% [markdown]
# on peut maintenant créer une structure adaptée pour modéliser chaque aéroport

# %%
from dataclasses import dataclass

@dataclass
class Airport:
    city: str
    airport_id: int
    iata: str
    latitude: float
    longitude: float



# %% [markdown]
# et écrire une fonction qui transforme une des lignes d'entrée en une instance de cette classe

# %%
# rappel
airport_line


# %%
def airport_from_line(line):
    try:
        airport_id, _, city, _, iata, _, lat, lon, *_ = [sanitize(x) for x in line.split(',')]
        return Airport(city, int(airport_id), iata, float(lat), float(lon))
    except Exception as exc:
        # arrive assez souvent en fait
        # print(f"OOPS can't do airport from {line}: {type(exc)}, {exc}")
        pass


# %%
airport_from_line(airport_line)


# %% [markdown]
# ### index

# %% [markdown]
# pour stocker toute la table dans une structure efficace, on va créer **un index** (dictionnaire) pour hacher *airport_id* → *instance*, de façon à pouvoir faire des recherches efficaces par la suite

# %%
# ici j'utilise une fonction
# ça me permet de ne pas pouller l'espace de noms global
# avec la variable temporaire `all_airports`
# dont je n'aurai plus besoin une fois l'index créé
def airport_index():
    # souvenez-vous qu'on avait une dernière ligne vide
    all_airports = [airport_from_line(line) for line in airport_strs if line]
    # si une exception se produit dans airport_from_line
    # on va avoir un élément de all_airports qui est None
    all_airports = [airport for airport in all_airports if airport is not None]
    # pour hacher, une simple compréhension de dictionnaire fait le job
    return {airport.airport_id: airport for airport in all_airports}


# %%
# apparemment quelques entrées ont des problèmes de cohérence
airport_by_id = airport_index()

# %%
# combien d'aéroports
len(airport_by_id)

# %% [markdown]
# ## airlines

# %% [markdown]
# on peut reproduire exactement la même démarche pour les routes et les compagnies aériennes

# %%
airlines_url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airlines.dat"

# %%
airlines_dat = requests.get(airlines_url).text
airline_strs = airlines_dat.split("\n")


# %%
@dataclass
class Airline:
    airline_id: int
    name: str
    code2: str


# %%
airline_strs[137]


# %%
def airline_from_line(line):
    try:
        airline_id, name, _, code2, *_ = [sanitize(x) for x in line.split(",")]
        return Airline(int(airline_id), name, code2)
    except Exception as exc:
        print(f"OOPS can't do airline from {line}: {type(exc)}, {exc}")    


# %%
# une autre stratégie pour conserver un espace de nom propre
all_airlines = [airline_from_line(line) for line in airline_strs if line]
all_airlines = [airline for airline in all_airlines if airline]
airline_by_id = {airline.airline_id: airline for airline in all_airlines}
del all_airlines

# %%
# combien 
len(airline_by_id)

# %% [markdown]
# ## routes

# %%
routes_url = "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat"

# %%
# apparemment celui-ci a des fins de ligne à la windows
# d'un autre coté c'est un .dat ..

routes_dat = requests.get(routes_url).text
route_strs = routes_dat.split("\r\n")
route_strs[100]


# %%
@dataclass
class Route:
    airline_id: int
    # these 2 of course are airport_ids
    src_id: int
    dst_id: int


# %%
def route_from_line(line):
    try:
        _, airline_id, _, src_id, _, dst_id, *_ = line.split(',')
        return Route(int(airline_id), int(src_id), int(dst_id))
    except Exception as exc:
        print(f"OOPS can't do route from {line}: {type(exc)}, {exc}")    


# %% [markdown]
# ici par contre on ne peut plus hacher car les routes n'ont pas d'index; contentons-nous pour l'instant d'une grande liste

# %%
all_routes = [route_from_line(line) for line in route_strs]
all_routes = [route for route in all_routes if route]

# %% cell_style="split"
len(route_strs)

# %% cell_style="split"
len(all_routes)

# %%
len(route_strs) - len(all_routes)

# %% [markdown]
# ### distance beween 2 airports

# %%
# shamelessly copied from 
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
# thank you Michael0x2a !

from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6373.0

def distance(lat1, lon1, lat2, lon2):
    """
    all incoming values in radians
    """
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c


# %%
def distance_degrees(lat1, lon1, lat2, lon2):
    """
    all incoming values in degrees
    """
    return distance(radians(lat1), radians(lon1),
                    radians(lat2), radians(lon2))


# %% cell_style="split"
# testing
lat1 = 52.2296756
lon1 = 21.0122287
lat2 = 52.406374
lon2 = 16.9251681

print("Result:", distance_degrees(
    lat1, lon1, lat2, lon2))
print("Should be:", 278.546, "km")

# %% cell_style="split"
# testing
lat1 = 43.65
lon1 = 7.21
lat2 = 49.01
lon2 = 2.55

print("Result:", distance_degrees(
    lat1, lon1, lat2, lon2))
print("Should be about 700 km")


# %% [markdown]
# ### un opérateur sur la classe `Airport`

# %%
def airport_minus(self, other):
    lat1, lon1 = self.latitude, self.longitude
    lat2, lon2 = other.latitude, other.longitude
    return distance_degrees(lat1, lon1, lat2, lon2)

Airport.__sub__ = airport_minus    

# %%
# un index par code iata
airport_by_iata = {airport.iata: airport for airport in airport_by_id.values()}

# %%
nice = airport_by_iata['NCE']; nice

# %%
roissy = airport_by_iata['CDG']; roissy

# %% cell_style="split"
nice - roissy

# %% cell_style="split"
roissy - nice

# %% [markdown]
# ### mapping

# %%
import folium
map_center = [nice.latitude, nice.longitude]

# %%
map = folium.Map(location=map_center, zoom_start=3)

# c'est trop long si on affiche tout, 
# prenons pour commencer les 300 premiers
airport_300samples = [
    airport for (counter, airport) in 
    zip(range(300), airport_by_id.values())
]
for airport in airport_300samples:
    folium.CircleMarker([airport.latitude, airport.longitude],
                        radius=3,
                        weight=2,
                       ).add_to(map)
map

# %% [markdown]
# ### on peut maintenant élaguer un peu

# %%
# rappel sur la structure d'une route
all_routes[10]

# %% [markdown]
# on décide de filtrer sur disons deux compagnies parce sinon on ne voit rien

# %%
# pour localiser les compagnies par leur petit nom (code2)
# on va créer un nouvel index

airline_by_code2 = {airline.code2: airline for airline in airline_by_id.values()}

# maintenant les recherches sont rapides
air_france = airline_by_code2['AF']
british_airways = airline_by_code2['BA']
delta = airline_by_code2['DL']
air_canada = airline_by_code2['AC']
air_france, british_airways, delta, air_canada

# %%
# on sélectionne deux compagnies
selected_airline_ids = {137, 330}

# %% [markdown]
# ### un ensemble d'aéroports

# %% [markdown]
# on a maintenant envie de construire un ensemble d'aéroports, ceux qui ont au moins une ligne aérienne opérée par AF ou BA; mais à ce stade on ne peut pas le faire

# %%
try: 
    dummy_set = set((nice, roissy))
except Exception as exc:
    print(f"OOPS {type(exc)} {exc}")


# %% [markdown]
# c'est un peu ballot, car chaque aéroport a un `airport_id` unique sur lequel on peut hasher; du coup il suffit de faire

# %% cell_style="split"
# là franchement on pourrait utiliser
# le paramètre airport plutôt que self
def airport_hashing_method(self):
    return hash(self.airport_id)

def airport_eq_method(self, other):
    return self.airport_id == other.airport_id    


# %% cell_style="split"
Airport.__hash__ = airport_hashing_method
Airport.__eq__ = airport_eq_method

# %%
# maintenant c'est OK
dummy_set = set((nice, roissy))

# %% [markdown]
# ### back to business: seulement les aéroports concernés

# %% [markdown]
# on peut maintenant construire l'ensemble des aéroports qui sont connectés à l'une ou l'autre de nos deux compagnies

# %%
selected_airports = set()

for route in all_routes:
    if route.airline_id not in selected_airline_ids:
        continue
    try:
        src_airport = airport_by_id[route.src_id]
        dst_airport = airport_by_id[route.dst_id]
        # c'est ici qu'on ajoute les instances
        # de Airport dans un ensemble
        selected_airports.add(src_airport)
        selected_airports.add(dst_airport)
    except KeyError:
        # pas tout à fait complet apparemment
        pass
    
len(selected_airports)

# %%
map = folium.Map(location=map_center, zoom_start=1)

for airport in selected_airports:
    folium.CircleMarker([airport.latitude, airport.longitude],
                        radius=3,
                        weight=.8,
                        fill=True,
                        fill_color="#88f",
                       ).add_to(map)
map


# %% [markdown]
# ### avec les routes

# %% cell_style="split" slideshow={"slide_type": ""}
# ditto pour rendre les objets 
# Airline hashables
def airline_hashing_method(self):
    return hash(self.airline_id)

def airline_eq_method(self, other):
    return self.airline_id == other.airline_id    


# %% cell_style="split"
Airline.__hash__ = airline_hashing_method
Airline.__eq__ = airline_eq_method

# %%
# avec les routes

# le début bien sûr c'est le même
map = folium.Map(location=map_center, zoom_start=2)

AIRPORT_COLOR = '#88f'
AIRLINE_COLOR = {
    air_france: '#88f',
    air_canada: '#f88',
}

for airport in selected_airports:
    folium.CircleMarker([airport.latitude, airport.longitude],
                        radius=3,
                        weight=1,
                        fill=True,
                        fill_color=AIRPORT_COLOR,
                       ).add_to(map)

for route in all_routes:
    if not route.airline_id in selected_airline_ids:
        continue
    try:
        src_airport = airport_by_id[route.src_id]
        dst_airport = airport_by_id[route.dst_id]
        locations = [(src_airport.latitude, src_airport.longitude),
                     (dst_airport.latitude, dst_airport.longitude)]
        # use neutral gray in case it'd be not found
        color = AIRLINE_COLOR.get(airline_by_id[route.airline_id], "#aaa")
        folium.PolyLine(locations=locations, 
                        weight=0.2, color=color).add_to(map)
    except Exception as exc:
        print(f"oops, {route} {type(exc)} {exc}")
map

# %% [markdown]
# ### construire un graphe

# %% [markdown]
# On veut construire un graphe avec toutes les routes entre deux aéroports, en se limitant à quelques compagnies spécifiques.
#
# Pour cela on va ajouter un attribut `remotes` aux aéroports concernés (ceux qui opèrent au moins un vol d'au moins une des compagnies choisies)

# %%
selected_airline_ids

# %%
len([route for route in all_routes if route.airline_id in selected_airline_ids])

# %%
for airport in airport_by_id.values():
    airport.remotes = dict()

for route in all_routes:
    if route.airline_id not in selected_airline_ids:
        continue
    try:
        src = airport_by_id[route.src_id]
        dst = airport_by_id[route.dst_id]
        src.remotes[dst] = src - dst
        dst.remotes[src] = src - dst
    except Exception as exc:
        print(f"ignoring route {route} {type(exc)} {exc}")

# %%
selected_airports = [airport for airport in airport_by_id.values() if airport.remotes]
len(selected_airports)

# %%
nice.remotes

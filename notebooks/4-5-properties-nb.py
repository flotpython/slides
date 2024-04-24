# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted,-editable
#     notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version,
#       -jupytext.text_representation.format_version,-language_info.version, -language_info.codemirror_mode.version,
#       -language_info.codemirror_mode,-language_info.file_extension, -language_info.mimetype,
#       -toc, -version
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
#     title: properties
# ---

# %% [markdown] slideshow={"slide_type": "-"}
# Licence CC BY-NC-ND, Thierry Parmentelat

# %%
from IPython.display import HTML
HTML(filename="_static/style.html")

# %% [markdown] slideshow={"slide_type": ""}
# (label-properties)=
# # properties

# %% [markdown]
# niveau intermédiaire/ avancé
#
# en guise de complément, ce notebook introduit la notion de *property*

# %% [markdown]
# ## propos
#
# on a vu qu'en général, une classe expose
#
# * des **attributs**, pour accéder directement aux différents 'morceaux' de **données** qui constituent une instance
# * et des **méthodes**, qui sont des **fonctions**
#
# il arrive qu'on se trouve dans une situation un peu mixte, où on voudrait 
#
# * pouvoir **accéder aux données**, mais **au travers d'une fonction**  
#   qui puisse, par exemple, faire des contrôles sur la validité des valeurs  
#   ou simplement parce que l'accès en question se fait au travers d'une indirection

# %% [markdown]
# ## digression
#
# ### langages dogmatiques: getter & setter
#
# commençons par une digression: on a dit que Python était un langage *pragmatique*  
# dans des langages *dogmatiques* comme C++ ou Java, ce qui est considéré comme une bonne pratique, ça va être de
#
# - définir les attributs comme des champs privés de la classe
# - fournir des méthodes - dites *getter* et *setter* pour manipuler les attributs
#
# par exemple une classe `Gauge` - qui modélise une valeur confinée dans un certain intervalle - serait dans cette optique exposée au travers de deux méthodes
#
# - `obj.get_value()` qui renvoie la valeur courante
# - `obj.set_value(new_value)` qui permet de modifier la valeur - et qui n'autorisera pas de valeur en dehors de l'intervalle de la jauge
#
# ici on prend volontairement un exemple où ces méthodes d'accès sont relativement simples, mais ce formalisme est très général et souvent poussé à son extrême: le code qui utilise la classe ne fait **jamais** directement référence aux attributs, mais **toujours** au travers de ces méthodes d'accès; et de cette façon on assure l'encapsulation, on peut garantir les invariants, etc...

# %% [markdown]
# ### en Python
#
# sauf que, il faut bien le reconnaitre, le code qui résulte de cette approche est .. vraiment vilain  
# on se retrouve avec plein de parenthèses, et de `get_` et de `set_`, ça rend le programme beaucoup moins lisible
#
# c'est pourquoi on tient beaucoup à pouvoir accéder directement aux attributs  
# ce qui ne veut pas dire qu'on va renoncer à l'idée de pouvoir contrôler ces accès !  
#
# c'est exactement notre sujet: les *properties*, c'est le mécanisme qui va nous permettre:
#
# - d'avoir un code utilisateur qui peut accèder directement aux attributs
# - alors qu'en réalité on passe bel et bien par une couche de logique !
#
# on va voir ceci sur deux exemples

# %% [markdown]
# ## exemple 1 : indirection
#
# dans cet exemple, on a une classe `Station` (de métro); elle veut exposer un attribut `latitude`  
# sauf que, en fait cette donnée n'est **pas directement** un attribut de `Station`, elle est incluse dans un autre objet qui est lui-même un attribut..
#
# imaginez par exemple que vous avez lu une dataframe, qui contient la liste des stations de métro

# %%
import pandas as pd

stations = pd.read_csv("../data/stations.txt")
stations.head(2)


# %% [markdown]
# et maintenant, on veut définir une classe `Station` pour manipuler ce contenu

# %%
class Station:
    def __init__(self, indice):
        self.row = stations.iloc[indice]


# %% [markdown]
# on a donc une classe qui "emballe" un objet de type `pandas.Series`  
# ce serait bien d'exposer un attribut `latitude`, pour pouvoir écrire par exemple
#
# ```python
# # ce code ne marche pas
#
# class Station:
#     def __init__(self, indice):
#         self.row = stations.iloc[indice]
#     def __repr__(self):
#         # ici self.latitude ne veut rien dire
#         return f"[Station {self.latitude:.2f}]"
# ```
#
# mais bien entendu, ça ne fonctionne pas dans l'état, puisque l'attribut `latitude` n'est pas présent dans l'objet `station`

# %% [markdown]
# ça oblige à écrire plutôt `station.row.latitude`, mais ça n'est pas du tout pratique, il va falloir se souvenir de cette particularité à chaque fois qu'on aura besoin d'accéder à `latitude`  
# (ou, encore pire, à copier les colonnes de la dataframe sous forme d'attributs - une très mauvaise idée); 
#
# c'est l'idée derrière la notion de ***property***: on va créer ici une *property* qui s'appelle `latitude`  
# ça se présente comme un attribut "normal", mais en fait lorsqu'on accède à cet attribut on le fait au travers de fonctions
#
# voici ce que ça donnerait dans ce premier exemple:

# %%
# maintenant ça fonctionne

class Station:
    def __init__(self, indice):
        self.row = stations.iloc[indice]
    def __repr__(self):
        # maintenant plus de problème
        return f"[Station {self.latitude:.2f}]"
    
    # car grâce à cette property, on peut accéder à l'attribut self.latitude
    @property
    def latitude(self):
        return self.row.latitude


# %%
station0 = Station(0)
station0


# %% [markdown]
# ## exemple 2 : une jauge
#
# deuxième cas d'usage, on veut une classe qui manipule une valeur, mais on veut en plus être sûr qu'elle appartient à un certain intervalle; disons entre 0 et 100
#
# sans les properties, on serait obligé de définir une méthode `set_value`, qui va pouvoir faire des contrôles
#
# ```python
# # en définissant un setter
# # ça marche mais c'est vraiment moche comme approche
#
# class Gauge:
#     def __init__(self, value):
#         self.set_value(value)
#     def __repr__(self):
#         return f"[Gauge {self._value}]"
#         
#     def set_value(self, newvalue):
#         # on force la nouvelle valeur à être dans l'intervalle
#         self._value = max(0, min(newvalue, 100))
#
#     # et pour être cohérent on fournit aussi un getter
#     def get_value(self):
#         return self._value
# ```

# %% [markdown]
# mais à nouveau ce n'est pas du tout pratique :
#
# * d'abord il faut "cacher" l'attribut pour éviter que l'on fasse accidentellement `gauge.value = 1000`
# * ensuite du coup il faut aussi exposer une autre méthode `self.get_value()` pour lire la valeur
# * et une fois qu'on a fait tout ça, on se retrouve à devoir écrire un code bavard et pas très lisible, bref c'est super moche
# * enfin, ça change l'API, et s'il y a déjà du code qui utilise l'attribut `.value`, il faut tout changer...
#
# pour information, cette technique est celle employée dans les langages comme C++ et Java, on appelle ces méthodes des *getters* et *setters*  
# inutile de dire que ce n'est pas du tout pythonique comme pratique !
#
# à nouveau dans cette situation les properties viennent à la rescousse; voici comment ça se présenterait

# %%
# version avec une property

class Gauge:
    
    def __init__(self, value):
        # on écrit .. au travers de la property
        self.value = value
        
    def __repr__(self):
        # on lit .. aussi au travers de la property
        return f"[Gauge {self.value}]"

    # la property se présente ici comme une paire de méthodes
    # d'abord le getter
    @property
    def value(self):
        """
        the docstring
        """
        return self._value
    
    # la syntaxe pour définir le 'setter' correspondant 
    # à la property 'value'
    # et c'est pour ça bien sûr qu'on écrit '@value'
    @value.setter
    def value(self, newvalue):
        self._value = max(0, min(newvalue, 100))


# %% [markdown]
# avec ce code, on peut manipuler les objets de la classe "normalement", 
# et pourtant on contrôle bien la validité de la valeur
#
# ````{admonition} value ou _value ?
# :class: attention
#
# c'est important de bien faire la différence 
#
# - entre l'attribut `_value` qui est un attribut "normal" dans lequel on range la donnée, 
# - et l'attribut `value` qui est la propriété pour y accéder; gare aux récursions infinies en cas de confusion !
# ````

# %% cell_style="split"
# à la création
g = Gauge(1000); g

# %% cell_style="split"
# ou à la modification
g.value = -10
g

# %%
# ou à la lecture
g.value


# %% [markdown]
# ````{admonition} on la voit dans le help()
# :class: admonition-small
#
# regardez ce que donne le `help(g)`, vous verrez apparaitre `value` dans les descriptors, avec son *docstring*
# ````

# %% [markdown] tags=[]
# ## l'autre syntaxe
#
# en fait il y a deux syntaxes pour définir une property, choisir entre les deux est une question de goût  
# (perso je préfère celle-ci, je la trouve plus facile à retenir)
#
# quoi qu'il en soit, voici la deuxième syntaxe, utilisée dans la classe `Gauge`

# %% tags=[]
# version avec une property - deuxième syntaxe

class Gauge:

    # le début est inchangé
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"[Gauge {self.value}]"
    
    # le getter - généralement on le cache avec ce _ au début du nom
    def _get_value(self):
        """
        the docstring
        """
        return self._value

    # pareil
    def _set_value(self, newvalue):
        self._value = max(0, min(newvalue, 100))
        
    # et voici enfin la syntaxe pour définir la property
    value = property(_get_value, _set_value)


# %% tags=[] cell_style="split"
# à la création
g = Gauge(1000); g

# %% tags=[] cell_style="split"
# ou à la modification
g.value = -10
g

# %% [markdown]
# ````{admonition} les détails
# :class: admonition-x-small
#
# `property` attend au maximum 4 paramètres:
# - le getter - doit retourner la valeur lue
# - le setter - accès en écriture interdit si non fourni
# - le deleter - `del` interdit si non fourni
# - le docstring - peut être fourni ici , sinon pris dans le getter
# ````

# %%
help(g)

# %% [markdown]
# ## use cases
#
# quelques exemples de classes où on pourrait vouloir mettre des properties
#
# - la classe `Gauge`, ou toute autre variante où les données doivent respecter des contraintes
# - la classe `Temperature`, ou toute variante où on veut pouvoir accéder à une valeur selon plusieurs unités (`t.kelvin = 0; t.celsius == -273`)
# - la classe `RomanNumber`, pour pouvoir lire ou écrire en chiffres ou en lettres
# - ...

# %% [markdown]
# ## conclusion

# %% [markdown]
# en Python, on aime bien **accéder aux attributs** d'un objet **directement**, et ne pas **s'encombrer de *getters* et *setters*** qui obscurcissent le code pour rien
#
# comme on a parfois besoin que l'accès à un attribut passe par une **couche de logique**
#
# * soit pour implémenter une indirection
# * soit pour contrôler la validité des arguments
#
# dans ces cas-là on **définit une property**, qui permet de conserver le code existant (pas de changement de l'API)
#
# ````{admonition} les accès aux attributs
# :class: warning
#
# le lecteur curieux doit se dire à ce stade que les **accès aux attributs**, tels qu'on les a présentés dans ce qui précède,
# n'expliquent pas du tout comment peuvent bien fonctionner les *properties*
#
# et effectivement, jusqu'ici on n'a présenté qu'une version **très édulcorée** de la mécanique générale, qui est passablement complexe, et sur laquelle on reviendra plus longuement dans le dernier chapitre  
# cela dit, pour une utilisation de base des classes et des objets, tout ceci est amplement suffisant pour écrire du code correct et efficace :)
# ````

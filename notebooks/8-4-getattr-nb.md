---
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
  title: properties
---

+++ {"slideshow": {"slide_type": ""}}

(label-getattr)=
# attr.. (1/3) - `__getattr__`

ce notebook est le premier d'une série consacrée à l'**accès aux attributs**

on [a déjà vu dans le chapitre sur les classes](label-access-attributes-usual) comment fonctionne l'accès aux attributs d'un objet **dans le cas usuel**; rappelez-vous, on avait dit qu'on se basait sur le contenu des espaces de nom, et que:

- l'écriture d'un attribut se fait directement dans l'objet
- la lecture se fait en cherchant dans l'objet, puis en remontant la chaine d'héritage

en fait, cette présentation est **une simplification**, certes très utile en première approche  

mais déjà [dans le même chapitre](label-properties) on a vu - sans s'appesantir - le cas des properties, où les choses ne se passent pas exactement selon cette vision simpliste

car en réalité le mécanisme général d'accès aux attributs est **beaucoup plus complexe**, et nous allons essayer de nous y retrouver :)

+++

## `__getattr__`

et pour commencer nous allons voir un mécanisme assez simple, qui permet de **facilement** gérer de manière programmable ce  qu'on pourrait appeler la **génération automatique d'attributs**  

il s'agit d'un mécanisme relativement simple, et très ancien dans le langage  
avec `__getattr__` et ses compagnons `__setattr__` et `__delattr__`, œon veut qu'un objet puisse **"faire semblant" de possèder un attribut**, alors qu'en fait cet attribut n'est **pas présent dans son namespace**  

pour quoi faire me direz-vous ? les usages sont nombreux:

+++

### *use case* 1: le wrapper

souvenez-vous de la classe `Station`:
```python
stations = pd.read_csv("stations.csv")

class Station:
  def __init__(self, station_id):
      self.row = stations.iloc[station_id]
```
et on avait vu comment utiliser une *property* pour exposer l'attribut `latitude` *directement* sur la classe `Station`

mais en fait, avec les *properties* il faudrait refaire le même travail pour chaque colonne dans la table !
ce serait plus économique si on pouvait dire:
quand on cherche un attribut sur une `Station`, on va le chercher dans `self.row`

+++

### *use case* 2: une API

une légère variation: vous implémentez un service d'API
c'est-à-dire votre application est adossée à un service web, et vous avez besoin d'envoyer des requêtes à ce service web

pour cela vous créez une classe API
```python
class API:
  def __init__(self, url):
      self.session = ... # the details of the connection
```

mais bon vous, ce que vous voulez pouvoir faire, c'est ceci

```python
# l'occasion de dire qu'un context manager aussi serait utile ici
with API("http://webapi.com/") as api:
  # mais bon ne nous égarons pas...
  book = api.GET(book_id)
  # do some changes
  api.PUT(book)
  ...
```

ce qui naïvement impliquerait d'implémenter possiblement plein de méthodes comme `GET` dans la classe API
mais en fait ces méthodes, elles vont sans doute faire plus ou moins toutes la même chose! et donc c'est tentant de factoriser tout ça, mais comment faire ?

+++

## le code

la logique, c'est que si l'attribut n'est **pas trouvé** par la logique usuelle, on va utiliser **en dernier recours** ces méthodes, si elles existent

ce qui, dans le cas de la classe `Station`, nous donne quelque chose comme

```{code-cell} ipython3
import pandas as pd

stations = pd.read_csv("../data/stations.txt", index_col='station_id')

class Station:

    def __init__(self, station_id):
        self.row = stations.loc[station_id]

    def __getattr__(self, attribute):
        print("in __getattr__")
        if hasattr(self.row, attribute):
            # we could just as well simply call getattr()
            return getattr(self.row, attribute)
        else:
            # but it's better to make it explicit
            # that __getattr__ is expected to raise this exception when relevant
            # i.e. do not return None, it would mean the attribute exists and is None
            raise AttributeError(attribute)

s = Station(2122)
s.latitude, s.longitude
```

### affectation / destruction

avec les méthodes spéciales compagnon que sont `__setattr__` et `__delattr__` on peut également capturer les écritures et destructions d'attributs

juste une précision par rapport à ce qu'on a pu dire, et qui est toujours vrai:
> l'écriture d'un attribut se fait directement dans l'objet

dans ce contexte il faut l'interpréter comme: on appellera toujours `__setattr__` ou `__delattr__` sur l'objet, et jamais sur sa classe

+++

## conclusion

ce mécanisme - somme toute très simple - peut rendre de grands services, et il est à la portée des programmeurs intermédiaires, on peut l'utiliser sans connaitre le reste de la ménagerie (properties, descripteurs, `__getattribute__`)

dans les sections suivantes par contre, on va commencer à voir des détails qui sont réservés aux codeurs avancés voire très avancés:)

+++ {"slideshow": {"slide_type": "slide"}}

## exercices

* `attr-dynamic-properties`
* `attr-proxy`

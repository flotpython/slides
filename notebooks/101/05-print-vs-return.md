---
jupytext:
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
  title: print vs return
---

# `print()` *vs* `return`

+++

jusqu'ici on a fait pas mal de `print()`

**mais**

en fait dans la pratique on n'en fait **presque jamais** !!

mais alors me direz-vous, comment on construit un programme qui fait des choses utiles si on n'imprime jamais rien ?

+++

## exécution normale ou interactive ?

en premier, il y a une chose qui est troublante pour les gens qui commencent :

+++

### exécution normale 

dans un programme qu'on lance "normalement" c'est-à-dire depuis un terminal avec  
`$ python truc.py`  
eh bien dans ce cas les seules choses qui sont imprimées sont quand on appelle `print(..)`
  
toutes les autres étapes de calcul sont simplement passées sous silence;  
on les calcule bien sûr, mais on ne les affiche **que si** on appelle `print()`  
l'idée c'est que si on devait montrer toutes les valeurs intermédiaires on serait complètement noyé !

+++

### interactive
par contre, quand on utilise un mode *interactif*, c'est-à-dire soit
* le python 'standard' en mode interactif
  ```bash
  $ python
  >>>
  ```
* le IPython (que je recommande chaudement par rapport au précédent)  
  ```bash
  $ ipython

  In [1]:
  ```
* ou encore comme ici **dans un notebook**

+++

alors dans tous ces modes de fonctionnement, Python se comporte **comme un REPL**
  
c'est quoi un REPL ? ça signifie *Read Eval Print Loop*  
dit autrement, la logique de Python dans ce mode c'est
* on lit le code que vous avez tapé
* on l'évalue / exécute
* et si ça retourne quelque chose, alors **on l'imprime**
* et on recommence comme ça jusqu'à la fin des temps...

+++

### en pratique

+++

je vous montre la différence avec ce programme totalement bidon

```{literalinclude} run_or_repl.py
```

#### normal run

+++

d'abord si je l'exécute normalement, je vois .. combien de lignes affichées ?

```{code-cell} ipython3
!python run_or_repl.py
```

#### interactivement dans le notebook

```{code-cell} ipython3
# cellule 1

10 + 10
```

```{code-cell} ipython3
# cellule 2

def double(x):
    return x + x
```

```{code-cell} ipython3
# cellule 3
double(10)
```

```{code-cell} ipython3
# cellule 4

print("au beau milieu")

double("truc")
```

vous voyez que là on a beaucoup plus de texte affiché:
* à chaque cellule, le résultat de la **dernière expression** est affiché  
  enfin seulement s'il y en a un, par exemple on n'a rien d'intéressant à montrer dans la cellule 2
* par contre le `print()` lui se fait toujours
* enfin vous remarquez une subtile différence entre la façon d'afficher
  * `au beau milieu`
  * `'tructruc'`
  
en effet les choses qui sont affichées en tant que "résultat (du dernier code) de la cellule" sont affichées en mode "plus développeur"

et ici par exemple la cellule 4 a pour résultat la valeur retournée par `double("truc")`, qui est une chaine, du coup on la montre (en mode dével) avec les `'` autour

+++

plusieurs remarques

* les chaines peuvent être créées indifféremment avec des simple quote `'` ou des double quotes, pourvu que ce soit le même style de quote au début et à la fin
* on peut ajouter deux chaines, ca crée (une nouvelle chaine qui est) la *concaténation* des deux chaines  
  **question**: pourquoi on ne modifie pas plutôt la première des deux chaines ?

+++

## `print()` *vs* `return`

+++

Une fois qu'on a dissipé cette source de confusion, reprenons...

Et posons-nous la question de savoir si c'est une bonne idée d'écrire une fonction qui imprime toujours son résultat ?

Imaginons le cas d'une fonction qui calcule le cube

La réponse est simple: une fonction c'est fait pour **calculer** quelque chose; donc l'appelant doit pouvoir écrire quelque chose comme

```python
c = cube(10)
```

on a deux choix

```{code-cell} ipython3
# une version qui ne fait qu'imprimer le cube
def cube_qui_print(x):
    print(x*x*x)
```

```{code-cell} ipython3
# une version qui retourne proprement le résultat
def cube_qui_return(x):
    return x*x*x
```

### `print()`

```{code-cell} ipython3
# regardons ce que ça donne
c = cube_qui_print(10)
```

alors effectivement on a imprimé 1000, **mais attention**

```{code-cell} ipython3
# dans c on a None
print(c)
```

**question**: il se passerait quoi si dans la cellule du dessus j'avais mis juste `c` au lieu de `print(c)`

+++

### `return`

```{code-cell} ipython3
# alors que avec return
c = cube_qui_return(10)
```

on n'a rien affiché pendant le calcul, mais on a bien

```{code-cell} ipython3
print(c)
```

## que retenir ?

* en mode normal, les seules impressions sont celles qu'on fait avec un `print()`
* en mode interactif, pour nous simplifier la vie, Python nous affiche les résultats intermédiaires (typiquement le dernier calcul de chaque cellule)
* mais à partir de maintenant, on ne fera plus que des fonctions qui font `return` - et pas `print()`
* il sera toujours temps pour l'appelant d'afficher le résultat - si ça fait du sens pour lui

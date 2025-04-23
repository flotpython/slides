---
celltoolbar: Slideshow
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
  title: numpy - pandas
---

+++ {"slideshow": {"slide_type": ""}}

# numpy - pandas

ce sont deux librairies qui **ne font pas partie** de la librairie standard, mais qui ont une importance considérable dans l'écosystème Python  
il est **important** de les connaitre a minima - ne serait-ce que pour ne pas réinventer la roue !

+++

Licence CC BY-NC-ND, Thierry Parmentelat & Arnaud Legout

```{code-cell} ipython3
from IPython.display import HTML
HTML(filename="_static/style.html")
```

## numpy

les structures de données natives de Python - listes, tuples, dictionnaires, ensembles, etc... - sont très pratiques, mais pas super efficaces !  
si vous avez un besoin de faire des **calculs intensifs**, cela va vite être problématique - escomptez un rapport de performance de l'ordre de 70 à 100 fois plus lent ! que du code compilé...  
numpy apporte une solution très raisonnable 

* les moins:  
  * on manipule des données **homogènes** et **contigües**  
  * ce qui signifie donc aussi *taille fixe*, et *pas de mélange de types* genre `None` ou autres
* les plus:
  * très efficace (comparable à du code compilé) - tire profit de SIMD
  * choix des types concrets (comme avec du code compilé, pensez `uint8`), donc économe en mémoire
  * en dimension quelconque

+++

### programmation vectorielle

avec `numpy` on change de paradigme:  
jusqu'ici on vous a dit "en Python, on itère de préférence avec la boucle `for`"  
eh bien avec `numpy` on vous dit: "surtout n'écrivez pas de boucle `for`" !!

pourquoi ? eh bien pour tirer profit au maximum de l'architecture des ordinateurs modernes, en numpy on va utiliser massivement la *programmation vectorielle*, ce qui signifie qu'à chaque fois que possible on va s'exprimer à base d'opérations **sur tout le tableau**, ce qui implicitement signifie **sur tous les éléments d'un tableau**

c'est un sujet qui mérite une formation à part entière, mais juste pour donner un aperçu voici comment on dessinerait la courbe d'un sinus

```{code-cell} ipython3
import numpy as np

# un tableau de 200 nombres bien répartis entre 0 et 4π
X = np.linspace(0, 4*np.pi, 200)

# pour calculer les 200 sinus, on ne fait **surtout pas de for**
# mais tout simplement
Y = np.sin(X)
```

```{code-cell} ipython3
# ce qu'on peut dessiner comme ceci
import matplotlib.pyplot as plt

plt.plot(X, Y);
```

## pandas

c'est l'arme absolue pour charger des données de type tabulaire - comme dans une table de base de données  
c'est-à-dire des données **en 2 dimensions** où les colonnes sont homogènes  
à nouveau c'est un sujet à soi tout seul, mais ici encore il **faut absolument savoir que ça existe!!**

avec pandas, on peut faire en gros tout ce qui possible en SQL - la seule restriction étant que pandas travaille en mémoire    
mais fonctionnellement, on trouve dans pandas les équivalents de tous les traits de SQL: select, join, where, sort, ...  
avec en plus des facillités pour traiter les séries temporelles, mais là on s'égare

```{code-cell} ipython3
import pandas as pd

df = pd.read_csv("../data/Worldwide-Earthquake-database.csv")

df.head()
```

```{code-cell} ipython3
# les colonnes
df.columns
```

```{code-cell} ipython3
# select year, latitude, longitude, intensity from df where eq_primary >= 7
extract = df.loc[df.EQ_PRIMARY >= 7].loc[:, ['YEAR', 'LATITUDE', 'LONGITUDE', 'INTENSITY']]

extract.head()
```

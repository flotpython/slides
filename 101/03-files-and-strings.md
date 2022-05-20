---
jupytext:
  cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control,-trusted
  notebook_metadata_filter: all, -jupytext.text_representation.jupytext_version, -jupytext.text_representation.format_version,
    -language_info.version, -language_info.codemirror_mode.version, -language_info.codemirror_mode,
    -language_info.file_extension, -language_info.mimetype, -toc
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
  title: fichiers et chaines
rise:
  scroll: true
---

# fichiers et chaines

c'est important de savoir utiliser les fichiers depuis un programme

+++

## ouvrir un fichier en écriture (`'w'`)

+++

pour commencer voyons **comment créer un fichier** depuis un programme  
* pour cela on utilise **la fonction `open()`** en lui passant le mode `'w'` qui signifie ***write***
* on l'utilise **toujours** dans une instruction `with`  
  cela nous permet d'être totalement sûr que le fichier sera bien refermé à la fin du `with`

```{code-cell} ipython3
# c'est comme ça qu'on crée un fichier pour écrire dedans
#            le mode:  ↓↓↓
with open("tmp-names.txt", 'w') as writer:
    print("Achille", file=writer)
    print("Bob", file=writer)
    print("Charlie", file=writer)
```

si vous faites tourner ça sur votre ordi, vous devez constater la présence d'un nouveau fichier `tmp-names.txt` dans votre explorateur de fichier; et dedans nous avons écrit trois lignes avec les 3 noms

+++

depuis le notebook vous pouvez aussi faire

```{code-cell} ipython3
# ça c'est juste pour vérifier le contenu
# du fichier qu'on vient de créer

!cat tmp-names.txt
```

qui signifie:
* lancer dans le terminal (c'est le propos du `!` en début de ligne)
* la commande `cat tmp-names.txt` (sans le `!` donc)
* c'est-à-dire tout simplement, afficher le contenu du fichier `tmp-names.txt`

et on y trouve bien ce à quoi on s'attendait

+++

### que retenir ?

* on ouvre un fichier avec `open()`
* on le fait **toujours** dans une instruction `with`
* le mode permet de dire si on veut lire ou écrire le fichier
  * en lecture, il faut que le fichier soit déjà présent
  * en écriture par contre, il est créé dans tous les cas - qu'il existe déjà ou pas
* le with définit une variable (ici `writer`)  
  comme pour toutes les variables, on aurait pu choisir n'importe quoi
* en appelant `print()` avec `file=writer`, on a provoqué l'écriture dans le fichier et non plus dans le terminal

+++

et aussi - mais c'est un peu plus subtil:

* ici nous avons créé un **fichier texte**
* du coup toutes les opérations sur le fichier (lecture et écriture)  
  vont se faire à base de **chaines de caractères**
* c'est-à-dire que si je veux écrire l'entier 64 dans le fichier,
  je ne peux le faire qu'en écrivant dans le fichier les 2 caractères `6` et `4`

question: comment on pourrait aussi vouloir écrire l'entier `64` dans un fichier ?

+++

## ouvrir un fichier en lecture (`'r'`)

+++

Bien sûr ce fichier, on aurait pu l'écrire avec un éditeur de texte

Mais peu importe comment on l'a créé, maintenant voyons comment on peut le relire par programme

C'est la même idée exactement, mais on va cette fois passer à open un mode d'ouverture qui est `r` - pour, *wait for it...* **`read`** eh oui !

```{code-cell} ipython3
with open("tmp-names.txt", 'r') as reader:
    for line in reader:
        line = line.strip()
        print(f"hello {line}")
```

à essayer:

* supprimez la ligne avec `line.strip()`
  que remarquez-vous ?  
  
* ce qui se passe ici, c'est que
  * entre deux lignes, on trouve dans le fichier un caractère **NEWLINE** qui matérialise la fin de ligne
  * et ce caractère est laissé dans `line` lorsqu'on fait le parcours avec `for line in reader`
  * du coup dans la f-string de la dernière ligne il va déjà y avoir un NEWLINE
  * et ensuite c'est `print()` qui en rajoute encore un - parce que par défaut `print()` ajoute un NEWLINE une fois qu'il a fini son travail
  * du coup on a 2 NEWLINE au lieu d'un, et ça crée cette ligne vide en trop dans la sortie
  * le travail de `strip()` est justement de nettoyer une chaine de caractères
  
petit TP:

* trouvez la documentation de la méthode `strip()` sur les chaines
* indice: le site officiel de la doc Python est `docs.python.org`
* réponse: https://docs.python.org/3/library/stdtypes.html#str.strip
* pourquoi dit-on dans la doc que la méthode strip() renvoie une copie de la chaine ?

+++

### que retenir ?

* on ouvre un fichier en lecture avec le mode `'r'`
* une fois ouvert on peut parcourir toutes les lignes du fichier avec une simple instruction `for` sur le fichier
  on dit que l'objet fichier est **itérable** (et ça signifie juste qu'on peut, justement, faire une boucle dessus)
* il est utile de 'nettoyer' les chaines lues dans un fichier avant toute chose
* il y a plein de méthodes disponibles sur les chaines

+++

## `str.split()` et `str.join()`

+++

on ne va pas les passer toutes en revue bien sûr, mais bon certaines sont plus utiles que d'autres

notamment voici `split()` et `join()` en action

+++

### `split(c)`

```{code-cell} ipython3
# une chaine 

s = "nom;prénom;date de naissance"
```

```{code-cell} ipython3
# on découpe son contenu
# ici je vais préciser un caractère
s.split(';')
```

### `split()`

+++

remarquez qu'ici j'ai dû préciser le séparateur `;`  
si les mots sont séparés, de manière plus usuelle, par des espaces, on fera simplement

```{code-cell} ipython3
s2 = "nom prénom date-de-naissance"
s2.split()
```

et l'avantage - outre que c'est plus concis - c'est que ça va découper aussi les tabulations et les NEWLINE

```{code-cell} ipython3
s3 = "nom\tprénom\ndate-de-naissance"

# voyons déjà ce que signifie cette notation absconse
print(s3)
```

```{code-cell} ipython3
# sans rien préciser à split, il découpe les 3 sortes d'espaces
s3.split()
```

### `join()`

+++

dans l'autre sens, on peut facilement reconstruire une chaine en mettant bout à bout les morceaux d'une liste, avec cette méthode qui est un peu le complèment de `split()`

```{code-cell} ipython3
L = s.split(';')
L
```

```{code-cell} ipython3
# je peux recoller avec n'importe quel autre séparateur
'|'.join(L)
```

```{code-cell} ipython3
# vraiment n'importe quoi
'-=-'.join(L)
```

### que retenir ?

* le type `str` vient avec un très grand nombre de méthodes, par ex.  
  * chercher ou remplacer une sous-chaine
  * mettre en majuscule, minuscule
  * ...
* on a fréquemment besoin notamment de 
  * `.strip()` pour nettoyer les lignes d'un fichier
  * `.split()` pour découper une chaine en morceaux
  * `.join()` pour recoller les morceaux

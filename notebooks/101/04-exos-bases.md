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
  title: exos - fichiers et chaines
---

# exos

+++

## exo

+++

Voici un nouveau fichier de données

```{code-cell} ipython3
%cat data-students.txt
```

On vous demande d'écrire un programme qui produit ce texte

```
Hello Alice
Hello Bob
Hello Charlie
```

+++

## exo

+++

modifiez votre code (ou écrivez-en un autre) pour produire maintenant ceci

```
Alice::Rivest::12
Bob::Shamir::25
Charlie::Adleman::36
```

+++

## digression

on a vu les méthodes sur les chaines

je vous signale aussi deux méthodes super-utiles sur les listes
* `L.append(item)` pour ajouter à la fin d'une liste (on l'a déjà rencontrée)
* `L.pop()` qui enlève (et retourne) le dernier élément dans une liste

```{code-cell} ipython3
L = [1, 2, 3]
L.append(100)
L
```

```{code-cell} ipython3
L.pop()
```

```{code-cell} ipython3
L
```

## exo

+++

modifiez votre code (ou écrivez-en un autre) pour produire maintenant ceci

```
alice::rivest
bob::shamir
charlie::adleman
```

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
  display_name: jupytext-dev
  language: python
  name: jupytext-dev
language_info:
  name: python
  pygments_lexer: ipython3
---

dans le temps les calculs sur les noms et métadonnées des fichiers étaient faits à base de 

* `import os, os.util, glob`

maintenant on peut tout faire à base de simplement

```{code-cell} ipython3
from pathlib import Path 
```

## exercice v1

* écrire une fonction qui prend en paramètre un dossier (une str)
* qui liste tous les fichiers avec une certaine extension dans le dossier
* afficher pour chacun d'eux
  * le nom complet, sa taille et la date/heure de dernière modification
  * la première ligne
  
* en option, on peut avoir envie de trier les fichiers par nom

```{code-cell} ipython3
# exemple d'appel
"""
scanv1("/Users/Jean Dupont/cours-python/", "py")
""";
```

## exercice v2

idem mais

* on peut passer le dossier sous la forme d'une str ou d'un Path
* l'extension peut être vide (tous les fichiers) ou une chaine simple, ou un itérable d'extensions
* on peut passer un paramètre optionnel `recursive=False` qui indique si la recherche se fait dans tout le contenu du dossier, ou si au contraire seuls les fichiers placés directement sous le dossier sont concernés

```{code-cell} ipython3
# exemple d'appel
"""
scanv2(Path.home() / "cours-python/", ("py", "md", "ipynb", recursive=True)
""";
```

---

```{code-cell} ipython3
def scanv1(folder, extension):
    path = Path(folder)
    for child in path.glob(f"*.{extension}"):
        print(f"File {child.resolve()}")
        print(f"  {child.stat().st_size} B last modified on {child.stat().st_mtime}")
        with child.open() as feed:
            print("  first line:", next(feed), end="")
```

```{code-cell} ipython3
scanv1("../slides", "md")
```

```{code-cell} ipython3
# si on veut trier, il suffit de rajouter un sorted()
# remarquez que ça signifie que path.glob() 
# sait se faire trier
def scanv1_sorted(folder, extension):
    path = Path(folder)
    #            ↓↓↓↓↓↓↓
    for child in sorted(path.glob(f"*.{extension}")):
        print(f"File {child.resolve()}")
        print(f"  {child.stat().st_size} B last modified on {child.stat().st_mtime}")
        with child.open() as feed:
            print("  first line:", next(feed), end="")
```

```{code-cell} ipython3
scanv1_sorted("../slides", "md")
```

```{code-cell} ipython3
# en fait la v1 accepte déjà les objets de type Path

def scanv2(folder, extensions=None, recursive=False):
    # optionnel mais si on veut éviter la création
    # d'objets inutiles
    path = folder if isinstance(folder, Path) else Path(folder)
    pattern = "**/*" if recursive else "*"
    for child in path.glob(pattern):
        ext = child.suffix[1:]
        if extensions is not None:
            if isinstance(extensions, str):
                if ext != extensions:
                    continue
            else:
                if ext not in extensions:
                    continue
        print(f"File {child.resolve()}")
        print(f"  {child.stat().st_size} B last modified on {child.stat().st_mtime}")
        with child.open() as feed:
            print("  first line:", next(feed), end="")
```

quelques défauts résiduels:

* les fichiers de taille nulle posent problème (pour le `next(feed)`)
* les fichiers binaires posent problème (pareil)

pour arranger ça il faut être un peu plus soigneux....

```{code-cell} ipython3
scanv2("..", ('md', 'txt'), recursive=True)
```

```{code-cell} ipython3

```

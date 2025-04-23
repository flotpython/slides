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
  title: instructions
---

+++ {"slideshow": {"slide_type": "slide"}}

## le debugger Python : `pdb`

+++ {"slideshow": {"slide_type": ""}}

### `breakpoint()`

+++

pour mettre un point d'arrêt dans un programme on peut utiliser `breakpoint()`

```{code-cell} ipython3
:tags: [gridwidth-1-2]

def fact(n):
    if n<=1:
        breakpoint()
        return 1
    else:
        return n * fact(n-1)
```

+++ {"tags": ["gridwidth-1-2"]}

**raccourcis**

| clavier | quoi |
|------|---------|
| l (lowercase L)  | list source |
| w  | show stack | 
| n | next statement (stay in same function)|
| s | step into (dive into function call) |
| c | continue |
| p | print |

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
# si on exécute, le programme s'arrête 
# et on peut ensuite exécuter pas à pas, 
# inspecter la pile et les variables, ...
# fact(3)
```

+++ {"slideshow": {"slide_type": "slide"}}

### `pdb.run()`

+++

* le module pdb permet de debugger facilement un programme Python
```python
import pdb 
import mymodule 
pdb.run('mymodule.test()') 
```

* lance le debugger depuis la console sur la fonction `test()`

+++ {"slideshow": {"slide_type": "slide"}}

### `pdb.pm()` - post-mortem

+++

```python
import pdb 
import mymodule 
mymodule.test() 
Traceback (most recent call last): 
	File "<stdin>", line 1, in ? 
	File "./mymodule.py", line 4, in test 
		test2() 
	…
pdb.pm()
```

* lance le debugger en post-mortem

+++ {"slideshow": {"slide_type": "slide"}}

### sous IPython

dans `ipython` (ou dans un notebook), vous pouvez utiliser la *magic* `%%debug`  

````{admonition} magic de cellule
:class: tip

rappelez-vous que avec **un seul `%`** on a affaire à une *magic* de **ligne**  
et avec **deux pourcents `%%`** c'est une magique **de cellule** 

donc nous ici on utilise presque toujours le double pourcent
````

```{code-cell} ipython3
def fact(n):
    print(f"in fact with {n=}")
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)
```

pour essayer, enlever les commentaires dans cette cellule

```{code-cell} ipython3
# %%debug
# fact(3)
```

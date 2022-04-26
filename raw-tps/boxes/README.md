---
jupytext:
  cell_metadata_filter: all, -hidden, -heading_collapsed, -run_control, -trusted
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
  title: Notebooks Jupyter
  version: '3.0'
---

# Unicode characters for grid-like objects on a terminal

+++

Unicode comes with a few characters that can be used to draw squares or rectangles on the terminal

+++

See e.g. this page for a list 

https://en.wikipedia.org/wiki/Box-drawing_character

+++

**NOTE** these examples may look a little awkward on the notebook, but will look fine when run on a terminal, provided that it uses a fixed-width font, something that any decent terminal does

+++

## a first example

```{code-cell} ipython3
print ("wide box")
print ("\u250f\u2501\u2513")   # 3 odd characters
print ("\u2503 \u2503")        # 2 oddities + 1 space in the middle
print ("\u2517\u2501\u251b")   # 3 odd characters
```

for creating this example, all I had to do was to find the codepoint for each of the characters that I need, and insert them in a Python string using the '\unnnn' notation, where `nnnn` is the 4-digit hexadecimal codepoint.

```{code-cell} ipython3
# an example with one single character 
"\u250f"
```

## adding color

+++

optionnally, like we've seen for the evaluation, we can draw color on the terminal with the `colorama` library; note that it is useful mostly for Windows terminals (as other devices has standard ways to do color).

```{code-cell} ipython3
from colorama import Fore, Style
```

```{code-cell} ipython3
def red_text(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"
```

```{code-cell} ipython3
"hello " + red_text("to the") + " world"
```

well here again, the output is awkward on the notebook, never mind...

+++

## putting it together

```{code-cell} ipython3
print ("thin box")
print ("\u250c\u2500\u2510")
print ("\u2502 \u2502")
print ("\u2514\u2500\u2518")
```

```{code-cell} ipython3
print ("wide connectable box")
print ("\u254b\u2501\u2513")
print ("\u2503 \u2523")
print ("\u2517\u2501\u251b")
```

```{code-cell} ipython3
# of course we could also do this
thin_box = """\u250f\u2501\u2513
\u2503 \u2503
\u2517\u2501\u251b"""
print(thin_box)
```

```{code-cell} ipython3
print(red_text(thin_box))
```

```{code-cell} ipython3
# or that
double_box = """\u2554\u2566\u2557
\u2560\u256c\u2563
\u255a\u2569\u255d"""
print(double_box)
```

```{code-cell} ipython3
print(red_text(double_box))
```

well, you get the picture..

+++

## assignment

+++

We want to be able to write sentences like this

```{code-cell} ipython3
from boxes import Box1
```

```{code-cell} ipython3
b11 = Box1(4, 3, style='thin')
print(b11.box())
```

```{code-cell} ipython3
b12 = Box1(10, 4, color=Fore.BLUE, style='thin')
print(b12.box())
```

ou encore mieux

```{code-cell} ipython3
from boxes import Box2
```

```{code-cell} ipython3
b21 = Box2(4, 3, style='thin')
print(b21)
```

```{code-cell} ipython3
b22 = Box2(10, 4, color=Fore.BLUE, style='thin')
print(b22)
```

## assignment - if you're done

+++

a few suggestions about how to improve
* accept for the width and height a **list of integers** 
  as well as a plain integer, to build boxes with inside lines
  ```python
  b = Box3(10, [2, 2])
  ```
* make it reconnectable ?
* ...

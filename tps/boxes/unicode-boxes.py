# %% [markdown]
# # Unicode characters for grid-like objects on a terminal

# %% [markdown]
# Unicode comes with a few characters that can be used to draw squares or rectangles on the terminal

# %% [markdown]
# See e.g. this page for a list 
#
# https://en.wikipedia.org/wiki/Box-drawing_character

# %% [markdown]
# **NOTE** these examples may look a little awkward on the notebook, but will look fine when run on a terminal, provided that it uses a fixed-width font, something that any decent terminal does

# %% [markdown]
# ## a first example

# %%
print ("wide box")
print ("\u250f\u2501\u2513")
print ("\u2503 \u2503")
print ("\u2517\u2501\u251b")

# %% [markdown]
# for creating this example, all I had to do was to find the codepoint for each of the characters that I need, and insert them in a Python string using the '\unnnn' notation, where `nnnn` is the 4-digit hexadecimal codepoint.

# %%
# an example with one single character 
"\u250f"

# %% [markdown]
# ## adding color

# %% [markdown]
# optionnally, like we've seen for the evaluation, we can draw color on the terminal with the `colorama` library; note that it is useful mostly for Windows terminals (as other devices has standard ways to do color).

# %%
from colorama import Fore, Style

# %%
def red_text(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"

# %%
"hello " + red_text("to the") + " world"

# %% [markdown]
# well here again, the output is awkward on the notebook, never mind...

# %% [markdown]
# ## putting it together

# %%
print ("thin box")
print ("\u250c\u2500\u2510")
print ("\u2502 \u2502")
print ("\u2514\u2500\u2518")


# %%
print ("wide connectable box")
print ("\u254b\u2501\u2513")
print ("\u2503 \u2523")
print ("\u2517\u2501\u251b")

# %%
# of course we could also do this
thin_box = """\u250f\u2501\u2513
\u2503 \u2503
\u2517\u2501\u251b"""
print(thin_box)

# %%
print(red_text(thin_box))

# %%
# or that
print("red double")
double_box = """\u2554\u2566\u2557
\u2560\u256c\u2563
\u255a\u2569\u255d"""

# %%
print(red_text(double_box))

# %% [markdown]
# well, you get the picture..

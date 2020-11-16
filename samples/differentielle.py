# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all,-hidden,-heading_collapsed,-run_control
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# quelques notes prises en relisant le pdf de Séb

# %%
import math
import numpy as np


# %% [markdown]
# dans le pdf on dit qu'on fait intervenir
# une classe Node pour une sombre histoire de `__radd__`;
# j'ai trouvé l'argument fallacieux, si on introduit
# Node c'est pour une raison très différente !

# %%
class Float(float):

    def __add__(self, other):
        print('adding')
        result = super().__add__(other)
        if isinstance(result, Float):
            return result
        else:
            return Float(result)

    __radd__ = __add__
        


# %% [markdown]
# # Conserver la structure du calcul

# %% [markdown]
# la classe Node serait plus jolie si on décidait qu'elle accepte 
# un nombre variable d'arguments, plutôt que la liste qui est assez moche
#
# aussi j'ai trouvé que de remettre le `repr()` dans l'ordre $f(x,y) = z$ était plus lisible
#
# ne serait-il pas bienvenu d'appeler ça un arbre syntaxique ?

# %%
class Node:
    def __init__(self, value, function=None, *args):
        self.value = value
        self.function = function
        self.args = args
        
    def __repr__(self):
        if self.function is None:
            return f"Node({self.value})"
        else:
            function_name = self.function.__qualname__
            pretty_args = ', '.join(repr(arg) for arg in self.args)
            return f"{function_name}({pretty_args})={self.value}"


# %%
def wrap(function):
    
    def wrapper(*args):
        if any(isinstance(arg, Node) for arg in args):
            node_args = []
            values = []
            for arg in args:
                if isinstance(arg, Node):
                    node_args.append(arg)
                    values.append(arg.value)
                else:
                    node_args.append(Node(arg))
                    values.append(arg)
            return Node(function(*values), wrapper, *node_args)
        else:
            return function(*args)
        
    wrapper.__qualname__ = function.__qualname__
    return wrapper


# %%
import operator

add = wrap(operator.add)
Node.__add__ = Node.__radd__ = add
mul = wrap(operator.mul)
Node.__mul__ = Node.__rmul__ = mul

# %%
sin = wrap(math.sin)
cos = wrap(math.cos)


# %%
# mais pourquoi ça s'appelle trace si on n'écrit rien à l'écran ?

def trace(function, *args):
    return function(*(Node(arg) for arg in args))


# %%
def f(x):
    return 1.0 + cos(x)


# %%
from math import pi
zero = trace(f, pi)
zero

# %%
zero


# %%
def f1(x, y):
    return x * (x + y)
trace(f1, 1.0, 2.0)

# %% [markdown]
# # Calcul automatique des dérivées

# %% [markdown]
# ## Différentielles des fonctions élémentaires

# %%
registry = {}

registry[add] = lambda x, y: lambda dx, dy: dx +dy
# en version équivalente :
#def d_add(x, y):
#    return add
#registry[add] = d_add

registry[mul] = lambda x, y: lambda dx, dy: x*dy + y*dx
#def d_mul(x, y):
#    return lambda dx, dy: x*dy + y*dx
#registry[mul] = d_mul

# %%
def differential_from_derivative(derivative):
    return lambda x: lambda dx: derivative(x) * dx

def minus_sin(x):
    return - sin(x)


# %%
registry[cos] = differential_from_derivative(minus_sin)
registry[sin] = differential_from_derivative(cos)


# %% [markdown]
# **version Sébastien**

# %% [markdown] slideshow={"slide_type": "slide"}
# ```python
# # la version de Sébastien
# # pas très pythonique à mon humble avis
# def find_and_sort_nodes(end_node):
#     todo = [end_node]
#     nodes = []
#     while todo:
#         node = todo.pop()
#         nodes.append(node)
#         for parent in node.args:
#             if parent not in nodes + todo:
#                 todo.append(parent)
#     done = []
#     while nodes:
#         for node in nodes[:]:
#             if all(parent in done for parent in node.args):
#                 done.append(node)
#                 nodes.remove(node)
# return done
# ```

# %% [markdown]
# **première ébauche**

# %% [markdown]
# ```python
# # une proposition pour un simple parcours en
# # profondeur d'abord 
# # 
# # cette version a l'avantage d'être simple 
# # mais elle duplique les noeuds qui apparaissent
# # plusieurs fois dans l'expression
# # 
# def deep_first_scan(node):
#     if node.function:
#         for arg in node.args:
#             yield from deep_first_scan(arg)
#     yield node
# ```

# %%
# pour éviter la duplication il faut 
# en effet complexifier ce qui rend 
# la démarche moins avantageuse 
# puisque justement on cherchait à simplifier

def deep_first_scan(entry_point):
    scanned = set()
    def recursive(node):
        if node in scanned:
            return
        if node.function:
            for arg in node.args:
                yield from recursive(arg)
        yield node
        scanned.add(node)
    yield from recursive(entry_point)


# %%
# pour tester le parcours

node = trace(f1, 3.0, 10.0)
print(f"subject node:\n\t{node}\n")

for i, nav in enumerate(deep_first_scan(node), 1):
    print(i, nav, id(nav))


# %%
def d(f):
    def df(*args): # args=(x1, x2, ...)
        start_nodes = [Node(arg) for arg in args]
        end_node = f(*start_nodes)
        if not isinstance(end_node, Node): # constant value
                end_node = Node(end_node)

        def df_x(*d_args): # d_args = (d_x1, d_x2, ...)
            for node in deep_first_scan(end_node):
                if node in start_nodes:
                    i = start_nodes.index(node)
                    node.d_value = d_args[i]
                elif node.function is None: # constant node
                    node.d_value = 0.0
                else:
                    _d_f = registry[node.function]
                    _args = node.args
                    _args_values = (_node.value for _node in _args)
                    _d_args = (_node.d_value for _node in _args)
                    node.d_value = _d_f(*_args_values)(*_d_args)
            return end_node.d_value
        return df_x
    return df


# %%
def deriv(f):
    df = d(f)
    def deriv_f(x):
        return df(x)(1.0)
    return deriv_f


# %% [markdown]
# $f: x \rightarrow \pi$

# %%
def constant(x):
    return math.pi

deriv(constant)(0) == 0 and deriv(constant)(pi) == 0


# %% [markdown]
# $f: x\rightarrow 2x+3$

# %%
def affine(x):
    return 2*x + 3

deriv(affine)(4) == 2


# %% [markdown]
# $f: x\rightarrow x^2 + 2x +1$

# %%
def poly2(x):
    return x*x + 2*x + 1

(   deriv(poly2)(0) == 2.0
and deriv(poly2)(1) == 4.0
and deriv(poly2)(2) == 6.0)


# %% [markdown]
# $f: x\rightarrow cos^2x + sin^2x$ (fonction constante = 1)

# %%
def circle_radius(x):
    return cos(x)*cos(x) + sin(x)*sin(x)

deriv(circle_radius)(1) == 0

# %%
deriv(circle_radius)(pi/2) == 0


# %% [markdown]
# $f: x\rightarrow sin(x) . cos(x)$

# %%
def sincos(x):
    return cos(x) * sin(x)


# manual derivation
def sincos_prime(x):
    return cos(x)*cos(x) - sin(x)*sin(x)


# %%
# for x in 0, pi/4, pi/2:
#    expected = sincos_prime(x)
#    computed = deriv(sincos)(x)
#    print(f"{x:.4g} → {expected:.4g} {'ok' if computed == expected else computed}")

# %%
(   deriv(sincos)(0) == 1
and np.isclose(deriv(sincos)(pi/4), 0.)
and deriv(sincos)(pi/2) == -1)

# %%
(   derivbis(poly2)(0) == 2.0
and derivbis(poly2)(1) == 4.0
and derivbis(poly2)(2) == 6.0)

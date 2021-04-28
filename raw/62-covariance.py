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
#   notebookname: covariance et ACP
#   version: '1.0'
# ---

# %% [markdown]
# <span style="float:left;">Licence CC BY-NC-ND</span><span style="float:right;">Thierry Parmentelat&nbsp;<img src="media/inria-25.png" style="display:inline"></span><br/>

# %%
from math import pi, cos, sin, atan, fabs, sqrt
import numpy as np

# %%
from collections import OrderedDict

# %%
from ipywidgets import interact, fixed
from ipywidgets import SelectionSlider, IntSlider


# %% [markdown]
# # Helpers

# %% [markdown]
# ### Translate a set of points

# %%
def translate(points, vector):
    X, Y = points
    x0, y0 = vector
    return X + x0, Y + y0


# %% [markdown]
# ### Rotate a set of points

# %%
def rotate(points, alpha):
    x, y = points
    return x*cos(alpha) - y*sin(alpha), x*sin(alpha) + y*cos(alpha)


# %% [markdown]
# ### Get the average (center of gravity)

# %%
# for a 1-dimension array
def average1(dim1):
    return sum(dim1)/len(dim1)

def average(points):
    x, y = points
    return average1(x), average1(y)


# %% [markdown]
# # Generating input : an ellipse

# %% [markdown]
# ### Centered and not rotated

# %%
# the 2 radiuses, plus n as the number of points 
def ellipse(rx, ry, n):
    return (rx * np.cos(2 * pi / n * np.arange(n)),
            ry * np.sin(2 * pi / n * np.arange(n)))


# %%
el3 = ellipse(3, 1, 100)

# %% [markdown]
# ### How to display a set of points

# %% [markdown]
# The optional `directions` argument gives you a way to specify additional lines to be displayed. Each element in the `directions` parameter should be tuple of the form `alpha, length`.
#
# E.g.
#
#     show_points( points, [ (pi/3, 10) ])
#     
# would cause a line of angle $\pi/3$ and length 10 to be drawn from the center of gravity of the points

# %%
# %matplotlib notebook
import matplotlib.pyplot as plt

from math import pi, cos, sin

def show_points(points, directions=[]):
    x , y = points
    fig = plt.figure()
    plt.scatter(x, y, marker='.', color='g')
    if directions:
        cx, cy = average(points)
        for alpha, length in directions:
            plt.plot( (cx, cx + length * cos(alpha)),
                      (cy, cy + length * sin(alpha)),
                    )
                 
    fig.show()


# %% [markdown]
# ### A rotated and translated ellipse

# %%
# just rotated
elr = rotate(el3, pi/6)
show_points(elr, [ (pi/6, 4), [pi/2, 2]])

# %%
# rotate and then translate
#el3t = translate(el3, (1,2))

# %%
el = translate(rotate(el3, pi/6), (4, 2))
show_points(el)


# %% [markdown]
# # Generating input : random gaussian

# %%
def random_points(sdx, sdy, n):
    """ 
    returs n points in an alliptic gaussian distrib 
    with corresponding standard deviations in x and y
    """
    return (np.random.normal(0, sdx, n),
            np.random.normal(0, sdy, n))


# %% [markdown]
# ### a sample random cloud

# %%
# random around an ellipse rx=3 ry=10
ra100 = random_points(10, 3, 100)

# %%
# rotate and translate
ra = translate(rotate(ra100, pi/6), (10, 20))

# 10 is the standard deviation, so let's be sure the line is long enough
show_points(ra, [ (pi/6, 30)])

# %% [markdown]
# # Computing covariance matrix

# %%
average(el)


# %% [markdown]
# ### The covariance matrix

# %%
def covariance(points):
    # translate to the center of gravity
    mx, my = average(points)
    centered = translate(points, (-mx, -my))
    # convert into a np.array if needed
    m = np.array(centered)
    # compute tranposed
    t = np.transpose(m)
    # just multiply both
    return np.dot(m, t)


# %%
# try it out on our sample ellipse
co = covariance(el)
print(co)

# %% [markdown]
# ### Eigen values

# %% [markdown]
# Just use the numpy library to compute its eigen values

# %%
lambdas, A = np.linalg.eig(co)
print("Eigen values", lambdas)
print("Matrix", A)


# %% [markdown]
# # Various attempts

# %%
# we use this to check if 2 floats are almost equal
# np.isclose?

# %% [markdown]
# A helper function to see if 2 value are almost equal...

# %%
def almost(x1, x2):
    return np.isclose(x1, x2, rtol=0.001, atol=0.001)


# %% [markdown]
# This helper function would display the set of points, and then compute the ACP output. If an expected angle is known in advance (like when the set of points has a known pattern), it is displayed as well.

# %%
def loopback(points, expected_alpha=None, directions=None):
    x, y = points
    n = len(x)
    co = covariance(points)
    lambdas, A = np.linalg.eig(co)
    # A is expected to be an isometric rotation
    (a11, a12), (a21, a22) = A
    radius = a11*a22 - a12*a21
    if not almost(a11, a22): 
        print("ISOMETRY - WARNING 1")
    if not almost(fabs(a21), fabs(a12)):
        print("ISOMETRY - WARNING 2")
    if not almost(1., radius):
        print("ISOMETRY - WARNING 3")
    l1, l2 = lambdas
    print("valeurs propres {:.2f} - {:.2f}".format(l1, l2))
    #print("ACP ->", A)
    computed_alpha = pi/2 if a11 == 0 else atan(a12/a11)
    print("a11={:.3f}, a21={:.3f}".format(a11, a21))
    print("computed alpha = {:.3f}".format(computed_alpha))
    if expected_alpha:
        print("expected_alpha = {:.3f}".format(expected_alpha))
    # show lines as specified by the caller 
    directions = directions or []
    # add the computed one
    directions.append((-computed_alpha, sqrt(l1/n)))
    show_points(points, directions)

#        if not almost(computed_alpha, -expected_alpha):
#            print("MISMATCH")
#        α = expected_alpha
#        print("cos(α) = {}, sin(α) = {}".format(cos(α), sin(α)))


# %% [markdown]
# ###  Synthesized ellipses

# %%
def loopback_el(rx, ry, cx, cy, alpha, n):
    e = ellipse(rx, ry, n)
    ert = translate(rotate(e, alpha), (cx, cy))
    # show only one direction
    loopback(ert, alpha, [ (alpha, max(rx, ry)) ])


# %%
loopback_el_datasets = OrderedDict()
loopback_el_datasets['pi_6'] = (3, 1, 5, 10, pi/6, 100)
loopback_el_datasets['pi_4'] = (5, 1, 20, 30, pi/4, 50)
loopback_el_datasets['pi_3'] = (10, 1, 100, 200, pi/3, 25)
loopback_el_datasets['pi_2'] = (1.2, 1, 100, 200, pi/2, 100)

def loopback_el_wrap(k):
    args = loopback_el_datasets[k]
    print("args = ", args)
    loopback_el(*args)

interact(loopback_el_wrap, 
         k = SelectionSlider(options = list(loopback_el_datasets.keys()),
                             continuous_update = False));


# %% [markdown]
# ### Gaussian distribs

# %%
def loopback_ra(cx, cy, sdx, sdy, alpha, n):
    raw = random_points(sdx, sdy,n)
    points = translate(rotate(raw, alpha), (cx, cy))
    loopback(points, alpha, [ (alpha, 3*max(sdx, sdy)) ])


# %% [markdown]
# #### More and more points

# %%
interact(loopback_ra,
         cx = fixed(10), 
         cy = fixed(20),
         sdx = fixed(10),
         sdy = fixed(4),
         alpha = fixed(pi/6),
         n = IntSlider(min=10, max=1000, step=20, continuous_update = False)
        );

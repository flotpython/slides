# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-jupytext.text_representation.jupytext_version,-jupytext.text_representation.format_version
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   notebookname: Fourier
# ---

# %% [markdown]
# # Visualizating the effect of the Fourier Transform

# %% [markdown]
# ## The periodic case

# %% [markdown]
# ### an input function

# %% [markdown]
# Let's consider a periodic function such as this one

# %%
import numpy as np

def f(t): 
    'sin(x) + sin(2x) + sin(3x) + 2'
    return np.sin(t) + np.sin(2*t) + np.sin(3*t) - 2


# %% [markdown]
# We can visualize it, just to get a glimpse, like this

# %%
import matplotlib as mpl

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# %matplotlib notebook

# %%
def plot(fun, domain):
    image = fun(domain)
    plt.plot(domain, image)
    plt.title(f"{fun.__doc__}")
    plt.show()

# period is 2 pi, let us plot between 0 and 15 with a .001 step
plot(f, np.linspace(0, 15, 100))

# %% [markdown]
# ### Its Fourier transform

# %% [markdown]
# The Fourier Transform of $f$ is a function that will attach to each frequency $\phi$ the value
#
# $Four(f): \phi \rightarrow \int_{-\infty}^{\infty}f(t)e^{-2i\pi\phi t}dt$

# %% [markdown]
# So the whole deal is to compute, for each frequency $\phi$, the integral over $\mathbb{R}$ of the complex function
#
# $ F_{\phi}(t) = f(t)e^{-2i\pi\phi t}$
#
# And to get a grip on what this integral can be, we will represent this function in 3d, with axis X representing time, and axis Y and Z representing the real and imaginary part of $F_{\phi}(t)$
#
# Now let's assume our initial $f$ function has real values itself, like in the case of a sound signal for example. In this case, $F$'s curve is essentially $f$'s curve but rotating around the X axis with frequency $\phi$.

# %%
import math

mpl.rcParams['legend.fontsize'] = 12

# we plot : F(t) = e**(-2iPI.f.x) * f(x) 
# x = t
# y = real_part (F(t))
# z = img_part (F(t))

def rotating_plot (f, phi, rounds): 
    """
    Plotting function F for input <f> 
    at frequency <freq> over <rounds> rounds

    since we want to span <rounds> rounds around the X axis,
    we will have <t> range from 0 to 2*pi*rounds
    """
    fig = plt.figure()
    # initially show as if looking from infinite time
    ax = fig.gca(projection='3d', azim = 0., elev=0.)
    t = np.linspace(0, rounds * 2 * math.pi, 100 * rounds)
    x = t
    y = f(t)*np.cos(phi * t)
    z = f(t)*np.sin(phi * t)
    ax.plot(x, y, z,
            label=f'Fourier for {f.__doc__} ||  phi={phi} on {rounds} rounds')
    ax.legend()
    plt.show()


# %% [markdown]
# The one thing that you do need to understand is that, given the specific form of $F$ as it rotates around the time axis on a **uniform angular speed** $\phi$, you can compute (mentally) the integral in your head by finding out the **barycenter of the figure** that you get when looking at $F$ along the time (X) axis.

# %% [markdown]
# ## The frequencies that resonate with f

# %% [markdown]
# When computing $F$ with integer frequencies - that are thus multiple of the primary harmonic of f - you will see that each round repeats itself exactly, and so the overall integrap of $F$ has a non-nul value.

# %%
from ipywidgets import interact, interactive, fixed
from ipywidgets import SelectionSlider, IntSlider

# %%
# regular integers are resonating frequencies
resonating_frequencies = SelectionSlider(
    options = (1, 2, 3, 4)
)


# %%
# on a fixed number of rounds 
interact(rotating_plot, f=fixed(f), rounds=fixed(20), phi=resonating_frequencies);

# %% [markdown]
# ## The frequencies that do not resonate with f

# %% [markdown]
# Still looking at F along the time axis, the following values for the frequencies do not resonate. After a sufficient number of rounds, you can see that the picture is centered on (0, 0) and this is why the overall integral is nul.
#

# %%
# these frequencies do not resonate
disonating_freqs = SelectionSlider(options = [ 1.01, 1.1, 1.5, 1.52 ])
# pushing the number of rounds for frequencies like 1.01 that is almost right
rounds = IntSlider(min=10, max=120, step=5, continuous_update=False)

# %%
interact(rotating_plot, f=fixed(f), phi=disonating_freqs, rounds=rounds);

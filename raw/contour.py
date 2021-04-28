#!/usr/bin/env python

# Python 3.6 Standard Library
import sys

# Scientific Stack
import autograd
import autograd.numpy as np
import matplotlib

#matplotlib.use("TkAgg")  # Qt broken somehow on my PC :(
import matplotlib.pyplot as pp

### TODO: 
#
#  - investigate Qt shit ?
#
#  - still *some* suspect redundancy in some cells, investigate
#    Update: still some duplicated paths.
#
#  - contour: consider list of fragment outputs instead of the current
#    xs, ys output
#
#  - optional: assemble the contour fragments.
#
#  - optional: bilinear interpolation of the output (try with very sparse
# #  points settings).

# Automatic Differentiation Helper
# ------------------------------------------------------------------------------
def grad(f):
    g = autograd.grad
    return lambda x, y: np.r_[g(f, 0)(x, y), g(f, 1)(x, y)]

def J(f):
    j = autograd.jacobian
    return lambda x, y: np.c_[j(f, 0)(x, y), j(f, 1)(x, y)]

# Constants
# ------------------------------------------------------------------------------
eps = np.sqrt(np.finfo(np.float64).eps)
delta = 0.1

# Dichotomy Root Finder
# ------------------------------------------------------------------------------
def root(f, xmin=0.0, xmax=1.0, eps=eps):
    fxmin, fxmax = f(xmin), f(xmax)
    if fxmin * fxmax > 0:
        return None
    elif fxmin == 0:
        return xmin
    elif fxmax == 0:
        return xmax
    else:
        while xmax - xmin > eps:
            x = (xmin + xmax) / 2
            fx = f(x)
            if fx == 0:
                return x
            elif fxmin * fx < 0:
                xmax = x
                fxmax = fx
            else:
                assert fx * fxmax < 0
                xmin = x
                fxmin = fx
        return (xmin + xmax) / 2

# Level Curve Seed Finder
# ------------------------------------------------------------------------------
def find_seed(f, c=0):  # always search on the left edge
    f00, f01 = f(0, 0), f(0, 1)
    if min(f00, f01) <= c <= max(f00, f01):
        def g(t):
            return f(0.0, t) - c
        return (0.0, root(g))
    else:
        return None


# Newton Root Finders
# ------------------------------------------------------------------------------
def Newton_step(f, x, y):
    try:
        return np.array([x, y]) - np.linalg.solve(J(f)(x, y), f(x, y))
    except np.linalg.LinAlgError:
        return np.r_[np.nan, np.nan]

def Newton(f, x, y, n=1000, eps=np.sqrt(eps)):
    while True:
        fxy = f(x, y)
        if np.isinf(fxy).any() or np.isnan(fxy).any() or n == 0:
            return np.nan, np.nan
        else:
            xn, yn = Newton_step(f, x, y)
            # print("x, y / xn, yn:", x, y, "/", xn, yn)
            if (x - xn) * (x - xn) + (y - yn) * (y - yn) <= eps * eps:
                return xn, yn
            x, y = xn, yn
            n = n - 1

def forward_x(f, xs, ys, delta):
    return xs[-1] + delta, ys[-1]

def freeze_x(f, xs, ys, delta):
    x0 = xs[-1]
    def constraint(x, y):
        return x - x0 - delta
    return constraint

def forward(f, xs, ys, delta):
    x0, y0 = xs[-1], ys[-1]
    u, v = 1.0, 0.0  # default direction
    if len(xs) >= 2:
        u, v = x0 - xs[-2], y0 - ys[-2]
        norm = np.sqrt(u * u + v * v)
        u, v = u / norm, v / norm
    return x0 + delta * u, y0 + delta * v

def forward_constrainer(f, xs, ys, delta):
    x0, y0 = xs[-1], ys[-1]
    x1, y1 = forward(f, xs, ys, delta)
    def constraint(x, y):
        return (x - x0) * (x1 - x0) + (y - y0) * (y1 - y0) - delta * delta
    return constraint

def distance(f, xs, ys, delta):
    x0, y0 = xs[-1], ys[-1]
    def constraint(x, y):
        return (x - x0) * (x - x0) + (y - y0) * (y - y0) - delta * delta
    return constraint

# Simple Contouring
# ------------------------------------------------------------------------------
def solve_constrained_f(f, c, constraint, x0, y0):
    """
    Solve f(x, y) = c and constraint(x, y) = 0.
    """
    def g(x, y):
        return np.r_[f(x, y) - c, constraint(x, y)]
    x, y = Newton(g, x0, y0)
    if np.isnan(x) or np.isnan(y):
        raise ValueError("divergence: unable to find a root for f.")
    return x, y

def simple_contour(
    f, 
    c, 
    starter=forward, 
    constrainer=distance, 
    delta=delta, 
):
    output = np.array([]), np.array([])
    seed = find_seed(f, c)
    if seed is not None:
        x0, y0 = seed ; assert x0 == 0
        xs, ys = [x0], [y0]
        while True:
            x0, y0 = starter(f, xs, ys, delta)
            constraint = constrainer(f, xs, ys, delta)
            try:
                x, y = solve_constrained_f(f, c, constraint, x0, y0)
                xs.append(x); ys.append(y)
            except ValueError:
                break
            
            xn, yn = xs[-1], ys[-1]
            # Manage out-of-bounds (last iteration)
            if xn <= 0 or 1 <= xn or yn <= 0 or 1 <= yn:
                # Find the edge crossed, adjust constraint accordingly
                # so that the last point belongs to this edge.
                if xn <= min(1.0 - yn, 0.0, yn): # quadrant selection
                    x0, y0 = 0.0, ys[-1]
                    constraint = lambda x, y: x
                elif max(yn, 1.0, 1.0 - yn) <= xn:
                    x0, y0 = 1.0, ys[-1]
                    constraint = lambda x, y: x - 1
                elif yn <= 0:
                    x0, y0 = xs[-1], 0.0
                    constraint = lambda x, y: y
                else:
                    assert 1 <= yn
                    x0, y0 = xs[-1], 1.0
                    constraint = lambda x, y: y - 1
                # (Try to) replay the last step
                xs.pop(); ys.pop()
                try:
                    x, y = solve_constrained_f(f, c, constraint, x0, y0)
                    xs.append(x); ys.append(y)
                except ValueError:
                    pass
                break
        output = np.array(xs), np.array(ys)
    return output

# Rotators
# ------------------------------------------------------------------------------
LEFT, UP, RIGHT, DOWN = 0, 1, 2, 3 # clockwise

def rotate_direction(direction, n=1):
    return (direction + n) % 4

def rotate(x, y, n=1):
    if n == 0:
        return x, y
    elif n >= 1:
        return rotate(1 - y, x, n - 1)
    else:
        assert n < 0
        return rotate(x, y, n=-3 * n)

def rotate_function(f, n=1):
    def rotated_function(x, y):
        xr, yr = rotate(x, y, -n)
        return f(xr, yr)
    return rotated_function

# Complex Contouring
# ------------------------------------------------------------------------------
def contour(
    f,
    c,
    xs=[0.0, 1.0],
    ys=[0.0, 1.0],
    starter=forward,
    constrainer=distance,
    delta=delta,
):
    curves = []
    nx, ny = len(xs), len(ys)
    for i in range(nx - 1):
        for j in range(ny - 1):
            xmin, xmax = xs[i], xs[i + 1]
            ymin, ymax = ys[j], ys[j + 1]
            # print("cell i, j:", i, j)
            # print("xmin, xmax, ymin, ymax:", xmin, xmax, ymin, ymax)
            def f_cell(x, y):
                return f(xmin + (xmax - xmin) * x, ymin + (ymax - ymin) * y)
            
            done = set()
            #print(10*"-")
            for n in [0, 1, 2, 3]:
                if n not in done:
                    rotated_f_cell = rotate_function(f_cell, n)
                    x_curve_r, y_curve_r = simple_contour(
                        rotated_f_cell, c, starter, constrainer, delta
                    )
                    exit = None
                    if len(x_curve_r) >= 1:
                        xf, yf = x_curve_r[-1], y_curve_r[-1]
                        if xf == 0.0:
                            exit = LEFT
                        elif xf == 1.0:
                            exit = RIGHT
                        elif yf == 0.0:
                            exit = DOWN
                        elif yf == 1.0:
                            exit = RIGHT
                    if exit is not None: # a fully successful contour fragment
                        #print("n, exit before:", n, exit)
                        exit = rotate_direction(exit, n)
                        done.add(exit)
                        #print("n, exit, done:", n, exit, done)

                    x_curve, y_curve = [], []
                    for x_r, y_r in zip(x_curve_r, y_curve_r):
                        x, y = rotate(x_r, y_r, n=-n)
                        x_curve.append(x)
                        y_curve.append(y)
                    x_curve = np.array(x_curve)
                    y_curve = np.array(y_curve)
                    curves.append(
                        (
                            xmin + (xmax - xmin) * x_curve,
                            ymin + (ymax - ymin) * y_curve,
                        )
                    )
    return curves

# Reference Functions
# ------------------------------------------------------------------------------
def bilinear(f00, f01, f10, f11):
    def f(x, y):
        fx0 = f00 * (1 - x) + f10 * x
        fx1 = f01 * (1 - x) + f11 * x
        return fx0 * (1 - y) + fx1 * y
    return f

def quadratic(x, y):
    return (x - 0.2) * (x - 0.25) + (y - 0.25) * (y - 0.25)

def two_gaussians(x, y):
    return 2 * (
        np.exp(-x * x - y * y) - np.exp(-(x - 1) * (x - 1) - (y - 1) * (y - 1))
    )


# ------------------------------------------------------------------------------
def main_1():
    xn, yn = simple_contour(
        quadratic, c=0.5 ** 2, starter=forward_x, constrainer=freeze_x
    )
    xk, yk = simple_contour(
        quadratic, c=0.5 ** 2, starter=forward, constrainer=forward_constrainer
    )
    xl, yl = simple_contour(
        quadratic, c=0.5 ** 2, starter=forward, constrainer=distance
    )
    pp.plot(xn, yn, "r+")
    pp.plot(xk, yk, "g+")
    pp.plot(xl, yl, "c+")
    pp.xlim(0.0, 1.0)
    pp.ylim(0.0, 1.0)
    pp.gca().set_aspect(1.0)
    pp.grid(True)
    pp.show()


def main_2():
    f = (
        lambda x, y: (x - 0.25) * (x - 0.25) + (y - 0.5) * (y - 0.5) - 0.5 ** 2
    )  # x + y - 0.75
    f = lambda x, y: 2 * (
        np.exp(-x * x - y * y) - np.exp(-(x - 1) * (x - 1) - (y - 1) * (y - 1))
    )
    xs = np.linspace(-2, 3, 5 * 2 + 1)  # np.linspace(-2, 3, 5*3 + 1)
    ys = np.linspace(-1, 2, 3 * 2 + 1)  # np.linspace(-1, 2, 3*3 + 1)
    # print(contour_)
    # pp.grid(True)
    for x in xs:
        # print("x:", x)
        pp.plot([x, x], [ys[0], ys[-1]], "k:", alpha=0.5)
    for y in ys:
        # print("y:", y)
        pp.plot([xs[0], xs[-1]], [y, y], "k:", alpha=0.5)
    
   
    cs = np.r_[-1.5:2.0:0.5]
    for c in cs:
        contour_ = contour(f, c, xs, ys)
        for x, y in contour_:
            pp.plot(x, y, "+")
    # pp.plot(*alt_level_curve(f, c=0))
    pp.xlim(xs[0], xs[-1])
    pp.ylim(ys[0], ys[-1])
    pp.gca().set_aspect(1.0)
    pp.show()

if __name__ == "__main__":
    main_2()
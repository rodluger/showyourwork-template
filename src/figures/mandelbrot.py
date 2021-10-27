"""Plot a pretty fractal.

This script plots the Mandelbrot set (mandelbrot.pdf).
The code below was adapted from

https://scipy-lectures.org/intro/numpy/auto_examples/plot_mandelbrot.html
"""
from utils import compute_mandelbrot
import numpy as np
import matplotlib.pyplot as plt
import copy


fig = plt.figure(figsize=(8, 8))
mandelbrot_set = np.round(1 - compute_mandelbrot(500, 50.0, 601, 401))
tab10 = copy.copy(plt.get_cmap("tab10"))
tab10.set_over("w")
plt.imshow(
    mandelbrot_set.T,
    extent=[-2, 1, -1.5, 1.5],
    interpolation="nearest",
    cmap=tab10,
    vmin=0,
    vmax=0.9,
)
plt.gca().axis("off")
fig.savefig("mandelbrot.pdf", bbox_inches="tight")
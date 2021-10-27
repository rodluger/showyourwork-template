import numpy as np
from numpy import newaxis


def compute_mandelbrot(N_max, some_threshold, nx, ny):
    x = np.linspace(-2, 1, nx)
    y = np.linspace(-1.5, 1.5, ny)
    c = x[:, newaxis] + 1j * y[newaxis, :]
    z = c
    with np.warnings.catch_warnings():
        np.warnings.simplefilter("ignore")
        for j in range(N_max):
            z = z ** 2 + c
        mandelbrot_set = abs(z) < some_threshold
    return mandelbrot_set
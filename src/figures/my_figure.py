"""
Generate a figure from the simulation results.

"""
import numpy as np
import matplotlib.pyplot as plt


# Load the "simulation" results
X = [np.loadtxt(f"../data/results_{value}.dat") for value in range(0, 10)]

# Plot them
fig, ax = plt.subplots(1)
plt.plot(X)
fig.savefig("my_figure.pdf", bbox_inches="tight")
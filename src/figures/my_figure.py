"""
Generate a figure from the random numbers.

"""
import numpy as np
import matplotlib.pyplot as plt


# Load the simulation results
X = np.loadtxt("../data/random.dat", delimiter=",")

# Plot the figure
fig, ax = plt.subplots(1)
ax.plot(X)
fig.savefig("my_figure.pdf", bbox_inches="tight")
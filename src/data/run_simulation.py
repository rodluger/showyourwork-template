"""
Run a (fake) simulation and generate a simulation results file.

"""
import numpy as np
import sys

# Get the command line argument
value = int(sys.argv[1])

# Generate an array of random numbers with a given seed.
# This is a placeholder for an "expensive" operation.
np.random.seed(value)
X = np.random.randn(10)

# Save the "simulation" results to disk
np.savetxt(f"src/data/results_{value}.dat", X=X)
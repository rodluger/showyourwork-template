"""Plot a figure that uses LaTeX to render math-mode text.

"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib


# Force LaTeX backend
matplotlib.rc("text", usetex=True)


fig = plt.figure(figsize=(8, 8))
plt.annotate(
    r"$\alpha \beta \sqrt{\gamma}$",
    xy=(0.5, 0.5),
    ha="center",
    va="center",
    fontsize=128,
)
plt.gca().axis("off")
fig.savefig("figure_with_latex.pdf", bbox_inches="tight")

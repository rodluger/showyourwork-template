import numpy as np
from scipy.special import factorial

# Number of days in 10! seconds
answer = factorial(10) / 86400

with open("answer.tex", "w") as f:
    print(int(answer), file=f)
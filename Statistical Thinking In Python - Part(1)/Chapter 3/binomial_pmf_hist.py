import matplotlib.pyplot as plt
import numpy as np

# Take 10,000 samples out of the binomial distribution: n_defaults
n_defaults = np.random.binomial(100,0.05,size=10000)
# Compute bin edges: bins
bins = np.arange(0,max(n_defaults) + 1.5) - 0.5

# Generate histogram
plt.hist(n_defaults, density=True, bins=bins)

# Label axes
plt.xlabel('No. of defaults')
plt.ylabel('Binomial PMF')
plt.show()
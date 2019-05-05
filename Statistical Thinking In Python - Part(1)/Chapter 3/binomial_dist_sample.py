import matplotlib.pyplot as plt
import numpy as np
from customlib import ecdf
# Take 10,000 samples out of the binomial distribution: n_defaults
n_defaults = np.random.binomial(100,0.05,size=10000)

# Compute CDF: x, y
x, y = ecdf.ecdf.ecdf_compute(n_defaults)

# Plot the CDF with axis labels
plt.plot(x,y, marker ='.',linestyle='none')
plt.xlabel('No. of defaults')
plt.ylabel('CDF')

plt.show()
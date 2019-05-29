"""How does the current effect depend on lane position?

To quantify the effect of lane number on performance, perform a linear regression on the f_13 versus lanes data.
Do a pairs bootstrap calculation to get a 95% confidence interval. Finally, make a plot of the regression."""
import numpy as np
import dc_stat_think as dcst
import matplotlib.pyplot as plt

# Compute the slope and intercept of the frac diff/lane curve
slope, intercept = np.polyfit(lanes, f_13, 1)

# Compute bootstrap replicates
bs_reps_slope, bs_reps_int = dcst.draw_bs_pairs_linreg(lanes, f_13, size=10000)

# Compute 95% confidence interval of slope
conf_int = np.percentile(bs_reps_slope, [2.5, 97.5])

# Print slope and confidence interval
print("""
slope: {0:.5f} per lane
95% conf int: [{1:.5f}, {2:.5f}] per lane""".format(slope, *conf_int))

# x-values for plotting regression lines
x = np.array([1, 8])

# Plot 100 bootstrap replicate lines
for i in range(100):
    _ = plt.plot(x, bs_reps_slope[i] * x + bs_reps_int[i],
                 color='red', alpha=0.2, linewidth=0.5)

# Update the plot
plt.draw()
plt.show()

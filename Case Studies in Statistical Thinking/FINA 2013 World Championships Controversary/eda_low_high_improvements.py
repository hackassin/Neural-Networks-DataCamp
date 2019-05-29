"""ECDF of improvement from low to high lanes

Now that you have a metric for improvement going from low- to high-numbered lanes, plot an ECDF of this metric.
I have put together the swim times of all swimmers who swam a 50 m semifinal in a high numbered lane and the final
in a low numbered lane, and vice versa. The swim times are stored in the Numpy arrays swimtime_high_lanes and
swimtime_low_lanes. Entry i in the respective arrays are for the same swimmer in the same event."""
import matplotlib.pyplot as plt
import numpy as np
import dc_stat_think as dcst

# Compute the fractional improvement of being in high lane: f
f = (swimtime_low_lanes - swimtime_high_lanes) / swimtime_low_lanes

# Make x and y values for ECDF: x, y
x, y = dcst.ecdf(f)

# Plot the ECDFs as dots
_ = plt.plot(x, y, marker='.', linestyle='none')

# Label the axes and show the plot
plt.xlabel('f')
plt.ylabel('ECDF')

plt.show()

"""Estimation of mean improvement

You will now estimate how big this current effect is. Compute the mean fractional improvement for being in a 
high-numbered lane versus a low-numbered lane, along with a 95% confidence interval of the mean."""

# Compute the mean difference: f_mean
f_mean = np.mean(f)

# Draw 10,000 bootstrap replicates: bs_reps
bs_reps = dcst.draw_bs_reps(f, np.mean, size=10000)

# Compute 95% confidence interval: conf_int
conf_int = np.percentile(bs_reps, [2.5, 97.5])
# Print the result
print("""
mean frac. diff.: {0:.5f}
95% conf int of mean frac. diff.: [{1:.5f}, {2:.5f}]""".format(f_mean, *conf_int))

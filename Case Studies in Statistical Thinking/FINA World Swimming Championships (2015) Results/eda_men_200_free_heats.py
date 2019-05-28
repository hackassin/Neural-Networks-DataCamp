"""Graphical EDA of men's 200 free heats

In the heats, all contestants swim, the very fast and the very slow. To explore how the swim times are
distributed, plot an ECDF of the men's 200 freestyle."""
import dc_stat_think as dcst
import matplotlib.pyplot as plt
# Generate x and y values for ECDF: x, y
x, y = dcst.ecdf(mens_200_free_heats)

# Plot the ECDF as dots
_ = plt.plot(x,y,marker='.',linestyle='none')
# Label axes and show plot
plt.xlabel('time (s)')
plt.ylabel('ECDF')
plt.show()

"""200 m free time with confidence interval

Now, you will practice parameter estimation and computation of confidence intervals by computing the mean and 
median swim time for the men's 200 freestyle heats. The median is useful because it is immune to heavy tails 
in the distribution of swim times, such as the slow swimmers in the heats. mens_200_free_heats is still 
in your namespace."""

# Compute mean and median swim times
mean_time = np.mean(mens_200_free_heats)
median_time = np.median(mens_200_free_heats)

# Draw 10,000 bootstrap replicates of the mean and median
bs_reps_mean = dcst.draw_bs_reps(mens_200_free_heats,np.mean,size=10000)
bs_reps_median = dcst.draw_bs_reps(mens_200_free_heats, np.median,size=10000)

# Compute the 95% confidence intervals
conf_int_mean = np.percentile(bs_reps_mean,[2.5,97.5])
conf_int_median = np.percentile(bs_reps_median, [2.5,97.5])

# Print the result to the screen
print("""
mean time: {0:.2f} sec.
95% conf int of mean: [{1:.2f}, {2:.2f}] sec.

median time: {3:.2f} sec.
95% conf int of median: [{4:.2f}, {5:.2f}] sec.
""".format(mean_time, *conf_int_mean, median_time, *conf_int_median))
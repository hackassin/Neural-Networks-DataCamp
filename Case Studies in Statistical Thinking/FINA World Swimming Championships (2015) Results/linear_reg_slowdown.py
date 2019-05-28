"""Linear regression of average split time

We will assume that the swimmers slow down in a linear fashion over the course of the 800 m event.
The slowdown per split is then the slope of the mean split time versus split number plot.
Perform a linear regression to estimate the slowdown per split and compute a pairs bootstrap 95% confidence interval
on the slowdown. Also show a plot of the best fit line.
Note: We can compute error bars for the mean split times and use those in the regression analysis,
but we will not take those into account here, as that is beyond the scope of this course."""
import numpy as np
import matplotlib.pyplot as plt
import dc_stat_think as dcst
# Perform regression
slowdown, split_3 = np.polyfit(split_number,mean_splits,1)

# Compute pairs bootstrap
bs_reps, _ = dcst.draw_bs_pairs_linreg(split_number,mean_splits,size=10000)

# Compute confidence interval
conf_int = np.percentile(bs_reps,[2.5,97.5])

# Plot the data with regressions line
_ = plt.plot(split_number, mean_splits, marker='.', linestyle='none')
_ = plt.plot(split_number, slowdown * split_number  + split_3, '-')

# Label axes and show plot
_ = plt.xlabel('split number')
_ = plt.ylabel('split time (s)')
plt.show()

# Print the slowdown per split
print("""
mean slowdown: {0:.3f} sec./split
95% conf int of mean slowdown: [{1:.3f}, {2:.3f}] sec./split""".format(
    slowdown, *conf_int))
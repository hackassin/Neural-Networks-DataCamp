"""EDA: finals versus semifinals

First, you will get an understanding of how athletes' performance changes from the semifinals to the finals by
computing the fractional improvement from the semifinals to finals and plotting an ECDF of all of these values.
The arrays final_times and semi_times contain the swim times of the respective rounds. The arrays are aligned
such that final_times[i] and semi_times[i] are for the same swimmer/event. If you are interested in the
strokes/events, you can check out the data frame df in your namespace, which has more detailed information,
but is not used in the analysis."""
import dc_stat_think as dcst
import matplotlib.pyplot as plt
# Compute fractional difference in time between finals and semis
f = (semi_times - final_times) / semi_times

# Generate x and y values for the ECDF: x, y
x,y = dcst.ecdf(f)

# Make a plot of the ECDF
plt.plot(x,y,marker=".",linestyle='none')

# Label axes and show plot
_ = plt.xlabel('f')
_ = plt.ylabel('ECDF')
plt.show()

"""Parameter estimates of difference between finals and semifinals

Compute the mean fractional improvement from the semifinals to finals, along with a 95% confidence interval of the 
mean. The Numpy array f that you computed in the last exercise is in your namespace."""

# Mean fractional time difference: f_mean
f_mean = np.mean(f)

# Get bootstrap reps of mean: bs_reps
bs_reps = dcst.draw_bs_reps(f,np.mean,size=10000)

# Compute confidence intervals: conf_int
conf_int = np.percentile(bs_reps,[2.5,97.5])

# Report
print("""
mean frac. diff.: {0:.5f}
95% conf int of mean frac. diff.: [{1:.5f}, {2:.5f}]""".format(f_mean, *conf_int))
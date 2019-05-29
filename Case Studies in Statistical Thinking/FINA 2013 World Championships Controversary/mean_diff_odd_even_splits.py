"""EDA: mean differences between odd and even splits

To investigate the differences between odd and even splits, you first need to define a difference metric.
In previous exercises, you investigated the improvement of moving from a low-numbered lane to a high-numbered lane,
defining f = (ta - tb) / ta. There, the ta in the denominator served as our reference time for improvement.
Here, you are considering both improvement and decline in performance depending on the direction of swimming,
so you want the reference to be an average. So, we will define the fractional difference as f = 2(ta - tb) / (ta + tb).
Your task here is to plot the mean fractional difference between odd and even splits versus lane number."""
import numpy as np
import dc_stat_think as dcst

f = (swimtime_low_lanes_15 - swimtime_high_lanes_15) / swimtime_low_lanes_15
f_mean = np.mean(f)

# Draw 10,000 bootstrap replicates
bs_reps = dcst.draw_bs_reps(f, np.mean, size=10000)

# Compute 95% confidence interval
conf_int = np.percentile(bs_reps, [2.5, 97.5])

# Shift f
f_shift = f - np.mean(f)

# Draw 100,000 bootstrap replicates of the mean
bs_reps = dcst.draw_bs_reps(f_shift, np.mean, size=100000)

# Compute the p-value
p_val = np.sum(bs_reps >= np.mean(f)) / 100000

# Print the results
print("""
mean frac. diff.: {0:.5f}
95% conf int of mean frac. diff.: [{1:.5f}, {2:.5f}]
p-value: {3:.5f}""".format(f_mean, *conf_int, p_val))

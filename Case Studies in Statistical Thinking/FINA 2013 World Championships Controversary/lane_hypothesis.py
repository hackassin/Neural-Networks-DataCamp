"""Hypothesis test: Does lane assignment affect performance?

Perform a bootstrap hypothesis test of the null hypothesis that the mean fractional improvement going from low-numbered
lanes to high-numbered lanes is zero. Take the fractional improvement as your test statistic, and "at least as extreme as" to mean that the
test statistic under the null hypothesis is greater than or equal to what was observed."""
import numpy as np
import dc_stat_think as dcst

# Shift f: f_shift
f_shift = f - np.mean(f)

# Draw 100,000 bootstrap replicates of the mean: bs_reps
bs_reps = dcst.draw_bs_reps(f_shift, np.mean, size=100000)

# Compute and report the p-value
p_val = np.sum(bs_reps >= np.mean(f)) / 100000
print('p =', p_val)

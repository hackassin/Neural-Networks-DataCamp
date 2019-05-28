"""Hypothesis test: Do women swim the same way in semis and finals?

Test the hypothesis that performance in the finals and semifinals are identical using the mean of the fractional
improvement as your test statistic. The test statistic under the null hypothesis is considered to be at least as extreme
as what was observed if it is greater than or equal to f_mean, which is already in your namespace.
The semifinal and final times are contained in the numpy arrays semi_times and final_times."""
import numpy as np
# Set up array of permutation replicates
perm_reps = np.empty(1000)

for i in range(1000):
    # Generate a permutation sample
    semi_perm, final_perm = swap_random(semi_times, final_times)

    # Compute f from the permutation sample
    f = (semi_perm - final_perm) / semi_perm

    # Compute and store permutation replicate
    perm_reps[i] = np.mean(f)

# Compute and print p-value
print('p =', np.sum(perm_reps >= f_mean) / 1000)
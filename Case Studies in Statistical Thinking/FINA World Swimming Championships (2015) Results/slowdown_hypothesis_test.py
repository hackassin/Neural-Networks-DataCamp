"""Hypothesis test: are they slowing down?

Now we will test the null hypothesis that the swimmer's split time is not at all correlated with the distance
they are at in the swim. We will use the Pearson correlation coefficient (computed using dcst.pearson_r())
as the test statistic."""
import numpy as np
import dc_stat_think as dcst
# Observed correlation
rho = dcst.pearson_r(split_number, mean_splits)

# Initialize permutation reps
perm_reps_rho = np.empty(10000)

# Make permutation reps
for i in range(10000):
    # Scramble the split number array
    scrambled_split_number = np.random.permutation(split_number)

    # Compute the Pearson correlation coefficient
    perm_reps_rho[i] = dcst.pearson_r(scrambled_split_number, mean_splits)

# Compute and print p-value
p_val = np.sum(perm_reps_rho >= rho) / len(perm_reps_rho)
print('p =', p_val)

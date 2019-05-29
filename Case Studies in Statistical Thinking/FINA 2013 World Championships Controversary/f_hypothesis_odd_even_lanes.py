"""
Hypothesis test: can this be by chance?

The EDA and linear regression analysis is pretty conclusive. Nonetheless, you will top off the analysis of the
zigzag effect by testing the hypothesis that lane assignment has nothing to do with the mean fractional difference
between even and odd lanes using a permutation test. You will use the Pearson correlation coefficient,
which you can compute with dcst.pearson_r() as the test statistic. The variables lanes and f_13 are already in
your namespace.
"""
import numpy as np
import dc_stat_think as dcst

# Compute observed correlation: rho
rho = dcst.pearson_r(lanes, f_13)

# Initialize permutation reps: perm_reps_rho
perm_reps_rho = np.empty(10000)

# Make permutation reps
for i in range(10000):
    # Scramble the lanes array: scrambled_lanes
    scrambled_lanes = np.random.permutation(lanes)

    # Compute the Pearson correlation coefficient
    perm_reps_rho[i] = dcst.pearson_r(scrambled_lanes, f_13)

# Compute and print p-value
p_val = np.sum(perm_reps_rho[i] >= rho) / 10000
print('p =', p_val)

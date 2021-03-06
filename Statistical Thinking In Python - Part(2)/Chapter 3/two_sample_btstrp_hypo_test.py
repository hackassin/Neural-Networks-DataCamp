import numpy as np
from customlib import bootstrap_repl as bt
# Compute mean of all forces: mean_force
mean_force = np.mean(forces_concat)
# Generate shifted arrays
force_a_shifted = force_a - np.mean(force_a) + mean_force
force_b_shifted = force_b - np.mean(force_b) + mean_force

# Compute 10,000 bootstrap replicates from shifted arrays
bs_replicates_a = bt.draw_bs_reps(force_a_shifted, np.mean, 10000)
bs_replicates_b = bt.draw_bs_reps(force_b_shifted, np.mean, 10000)
# Get replicates of difference of means: bs_replicates
bs_replicates = bs_replicates_a - bs_replicates_b

empirical_diff_means = np.mean(force_a)- np.mean(force_b)
# Compute and print p-value: p
p =  np.sum(bs_replicates >= empirical_diff_means)/ len(bs_replicates)
#print('p', p)
print('p-value =', p)
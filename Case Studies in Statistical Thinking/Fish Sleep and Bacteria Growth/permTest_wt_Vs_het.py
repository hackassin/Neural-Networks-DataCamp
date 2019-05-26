"""Permutation test: wild type versus heterozygote

Test the hypothesis that the heterozygote and wild type bout lengths are identically distributed
using a permutation test."""
import numpy as np
from customlib import fish_sleep_df as fish
import dc_stat_think as dcst
# Extracting fish data
bout_lengths_wt = fish.fish_data_extract('wt')
bout_lengths_het = fish.fish_data_extract('het')
# Compute the difference of means: diff_means_exp

diff_means_exp = np.mean(bout_lengths_het) - np.mean(bout_lengths_wt)
# Draw permutation replicates: perm_reps
perm_reps = dcst.draw_perm_reps(bout_lengths_het, bout_lengths_wt,
                               dcst.diff_of_means, size=10000)

# Compute the p-value: p-val
p_val = np.sum(perm_reps >= diff_means_exp) / len(perm_reps)
print(diff_means_exp)
# Print the result
print('p =', p_val)
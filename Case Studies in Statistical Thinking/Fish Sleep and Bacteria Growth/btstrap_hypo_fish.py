"""Bootstrap hypothesis test

The permutation test has a pretty restrictive hypothesis, that the heterozygotic and wild type bout lengths are
identically distributed. Now, use a bootstrap hypothesis test to test the hypothesis that the means are equal,
making no assumptions about the distributions."""

import numpy as np
import dc_stat_think as dcst
from customlib import fish_sleep_df as fish
# Extracting fish data
bout_lengths_wt = fish.fish_data_extract('wt')
bout_lengths_het = fish.fish_data_extract('het')
# Concatenate arrays: bout_lengths_concat
bout_lengths_concat = np.concatenate((bout_lengths_wt, bout_lengths_het))

# Compute mean of all bout_lengths: mean_bout_length
mean_bout_length = np.mean(bout_lengths_concat)

# Generate shifted arrays
wt_shifted = bout_lengths_wt - np.mean(bout_lengths_wt) + mean_bout_length
het_shifted = bout_lengths_het - np.mean(bout_lengths_het) + mean_bout_length

# Compute 10,000 bootstrap replicates from shifted arrays
bs_reps_wt = dcst.draw_bs_reps(wt_shifted,np.mean,size=10000)
bs_reps_het = dcst.draw_bs_reps(het_shifted,np.mean,size=10000)

# Get replicates of difference of means: bs_replicates
bs_reps = bs_reps_het - bs_reps_wt
diff_means_exp = 2.669817067793108
# Compute and print p-value: p
p = np.sum(bs_reps >= diff_means_exp) / len(bs_reps)
print('p-value =', p)
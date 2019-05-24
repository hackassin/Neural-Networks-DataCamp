"""Hypothesis test: Are beaks deeper in 2012?

Your plot of the ECDF and determination of the confidence interval make it pretty clear that the beaks of G. scandens
on Daphne Major have gotten deeper. But is it possible that this effect is just due to random chance?
In other words, what is the probability that we would get the observed difference in mean beak depth if the
means were the same?
Be careful! The hypothesis we are testing is not that the beak depths come from the same distribution.
For that we could use a permutation test. The hypothesis is that the means are equal.
To perform this hypothesis test, we need to shift the two data sets so that they have the same mean and
then use bootstrap sampling to compute the difference of means."""

import pandas as pd
import numpy as np
from customlib import bootstrap_repl as bt

df1 = pd.read_csv("C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib/datasets/finch_beaks_1975.csv")
df2 = pd.read_csv("C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib\datasets/finch_beaks_2012.csv")
df = pd.concat([df1,df2], sort=False)
bd_1975 = df1['Beak depth, mm'].values
bd_2012 = df2['Beak depth, mm'].values

# Compute mean of combined data set: combined_mean
combined_mean = np.mean(np.concatenate((bd_1975, bd_2012)))

# Shift the samples
bd_1975_shifted = bd_1975 - np.mean(bd_1975) + combined_mean
bd_2012_shifted = bd_2012 - np.mean(bd_2012) + combined_mean

# Get bootstrap replicates of shifted data sets
bs_replicates_1975 = bt.draw_bs_reps(bd_1975_shifted,np.mean,10000)
bs_replicates_2012 = bt.draw_bs_reps(bd_2012_shifted,np.mean,10000)

# Compute replicates of difference of means: bs_diff_replicates
bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975

mean_diff = 0.22622047244094645
# Compute the p-value
p = np.sum(bs_diff_replicates >= mean_diff) / len(bs_diff_replicates)

# Print p-value
print('p =', p)
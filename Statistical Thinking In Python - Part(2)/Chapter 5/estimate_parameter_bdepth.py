"""Parameter estimates of beak depths

Estimate the difference of the mean beak depth of the G. scandens samples from 1975 and 2012 and
report a 95% confidence interval."""

import pandas as pd
import numpy as np
from customlib import bootstrap_repl as bt

df1 = pd.read_csv("C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib/datasets/finch_beaks_1975.csv")
df2 = pd.read_csv("C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib\datasets/finch_beaks_2012.csv")
df = pd.concat([df1,df2], sort=False)
bd_1975 = df1['Beak depth, mm'].values
bd_2012 = df2['Beak depth, mm'].values

# Compute the difference of the sample means: mean_diff
mean_diff = np.mean(bd_2012) - np.mean(bd_1975)

# Get bootstrap replicates of means
bs_replicates_1975 = bt.draw_bs_reps(bd_1975,np.mean,10000)
bs_replicates_2012 = bt.draw_bs_reps(bd_2012,np.mean,10000)

# Compute samples of difference of means: bs_diff_replicates
bs_diff_replicates = bs_replicates_2012 - bs_replicates_1975

# Compute 95% confidence interval: conf_int
conf_int = np.percentile(bs_diff_replicates,[2.5, 97.5])

# Print the results
print('difference of means =', mean_diff, 'mm')
print('95% confidence interval =', conf_int, 'mm')
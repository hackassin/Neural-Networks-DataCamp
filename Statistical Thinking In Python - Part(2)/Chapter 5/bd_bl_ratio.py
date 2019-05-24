"""Beak length to depth ratio

The linear regressions showed interesting information about the beak geometry. The slope was the same in 1975 and 2012,
suggesting that for every millimeter gained in beak length, the birds gained about half a millimeter in depth in both
years. However, if we are interested in the shape of the beak,
we want to compare the ratio of beak length to beak depth. Let's make that comparison. """
import pandas as pd
import numpy as np
from customlib import bootstrap_repl as bt

df1 = pd.read_csv("C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib/datasets/finch_beaks_1975.csv")
df2 = pd.read_csv("C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib\datasets/finch_beaks_2012.csv")
df = pd.concat([df1,df2], sort=False)
bd_1975 = df1['Beak depth, mm'].values
bd_2012 = df2['Beak depth, mm'].values
bl_1975 = df1['Beak length, mm'].values
bl_2012 = df2['Beak length, mm'].values

# Compute length-to-depth ratios
ratio_1975 = bl_1975/bd_1975
ratio_2012 = bl_2012/bd_2012

# Compute means of original data
mean_ratio_1975 = np.mean(ratio_1975)
mean_ratio_2012 = np.mean(ratio_2012)

# Generate bootstrap replicates of the means
bs_replicates_1975 = bt.draw_bs_reps(ratio_1975,np.mean,10000)
bs_replicates_2012 = bt.draw_bs_reps(ratio_2012,np.mean,10000)

# Compute the 99% confidence intervals
conf_int_1975 = np.percentile(bs_replicates_1975, [0.5, 99.5])
conf_int_2012 = np.percentile(bs_replicates_2012, [0.5, 99.5])

# Print the results
print('1975: mean ratio =', mean_ratio_1975,
      'conf int =', conf_int_1975)
print('2012: mean ratio =', mean_ratio_2012,
      'conf int =', conf_int_2012)
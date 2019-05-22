"""Bootstrap hypothesis test on bee sperm counts

Now, you will test the following hypothesis: On average, male bees treated with neonicotinoid insecticide have
the same number of active sperm per milliliter of semen than do untreated male bees. You will use the difference
of means as your test statistic. For your reference, the call signature for the draw_bs_reps() function
you wrote in chapter 2 is draw_bs_reps(data, func, size=1)"""

import numpy as np
import pandas as pd
from customlib import bootstrap_repl as bt

df = pd.read_csv('C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib/datasets/bee_sperm.csv', skiprows=3)
control, treated = df[df['Treatment']=='Control']['AliveSperm'], df[df['Treatment']=='Pesticide']['AliveSperm']
# Compute the difference in mean sperm count: diff_means
diff_means = np.mean(control) - np.mean(treated)

# Compute mean of pooled data: mean_count
sperm_concat = np.concatenate((control,treated))
mean_count = np.mean(sperm_concat)

# Generate shifted data sets
control_shifted = control - np.mean(control) + mean_count
treated_shifted = treated - np.mean(treated) + mean_count

# Generate bootstrap replicates
bs_reps_control = bt.draw_bs_reps(control_shifted,
                       np.mean, size=10000)
bs_reps_treated = bt.draw_bs_reps(treated_shifted,
                       np.mean, size=10000)

# Get replicates of difference of means: bs_replicates
bs_replicates = bs_reps_control - bs_reps_treated

# Compute and print p-value: p
p = np.sum(bs_replicates >= np.mean(control) - np.mean(treated)) \
            / len(bs_replicates)
print('p-value =', p)
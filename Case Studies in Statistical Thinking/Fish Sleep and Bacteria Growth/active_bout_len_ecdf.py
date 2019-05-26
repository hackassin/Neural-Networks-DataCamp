"""EDA: Plot ECDFs of active bout length

An active bout is a stretch of time where a fish is constantly moving. Plot an ECDF of active bout length for the
mutant and wild type fish for the seventh night of their lives. The data sets are in the numpy arrays
bout_lengths_wt and bout_lengths_mut. The bout lengths are in units of minutes."""

# Import the dc_stat_think module as dcst
import dc_stat_think as dcst
import matplotlib.pyplot as plt
from customlib import fish_sleep_df as fish
# Extracting fish data
bout_lengths_wt = fish.fish_data_extract('wt')
bout_lengths_mut = fish.fish_data_extract('mut')
# Generate x and y values for plotting ECDFs
x_wt, y_wt = dcst.ecdf(bout_lengths_wt)
x_mut,y_mut = dcst.ecdf(bout_lengths_mut)

# Plot the ECDFs
_ = plt.plot(x_wt, y_wt, marker='.', linestyle='none')
_ = plt.plot(x_mut,y_mut,marker='.', linestyle='none')

# Make a legend, label axes, and show plot
_ = plt.legend(('wt', 'mut'))
_ = plt.xlabel('active bout length (min)')
_ = plt.ylabel('ECDF')
plt.show()
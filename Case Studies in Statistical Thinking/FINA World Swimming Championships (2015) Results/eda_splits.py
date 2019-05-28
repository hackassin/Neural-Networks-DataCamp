"""EDA: Plot all your data

To get a graphical overview of a data set, it is often useful to plot all of your data. In this exercise,
plot all of the splits for all female swimmers in the 800 meter heats. The data are available in a Numpy a
rrays split_number and splits. The arrays are organized such that splits[i,j] is the split time for swimmer
i for split_number[j]."""
import matplotlib.pyplot as plt
import numpy as np
# Plot the splits for each swimmer
for splitset in splits:
    _ = plt.plot(split_number, splitset, linewidth=1, color='lightgray')

# Compute the mean split times
mean_splits = np.mean(splits,axis=0)

# Plot the mean split times
plt.plot(split_number,mean_splits,marker='.',linewidth=3,markersize=12)

# Label axes and show plot
_ = plt.xlabel('split number')
_ = plt.ylabel('split time (s)')
plt.show()
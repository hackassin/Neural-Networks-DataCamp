"""ECDFs of beak depths
While bee swarm plots are useful, we found that ECDFs are often even better when doing EDA. Plot the ECDFs for the 1975
and 2012 beak depth measurements on the same plot. For your convenience, the beak depths for the respective
years has been stored in the NumPy arrays bd_1975 and bd_2012."""
import pandas as pd
import matplotlib.pyplot as plt
from customlib import ecdf

from customlib import finch_beaks_df as finch

bd_1975, bd_2012, bl_1975, bl_2012 = finch.draw_finch_data()
# Compute ECDFs
x_1975, y_1975 = ecdf.ecdf.ecdf_compute(bd_1975)
x_2012, y_2012 = ecdf.ecdf.ecdf_compute(bd_2012)

# Plot the ECDFs
_ = plt.plot(x_1975, y_1975, marker='.', linestyle='none')
_ = plt.plot(x_2012, y_2012, marker='.', linestyle='none')

# Set margins
plt.margins(0.02)

# Add axis labels and legend
_ = plt.xlabel('beak depth (mm)')
_ = plt.ylabel('ECDF')
_ = plt.legend(('1975', '2012'), loc='lower right')

# Show the plot
plt.show()
"""Assessing the growth rate

To compute the growth rate, you can do a linear regression of the logarithm of the total bacterial area versus time.
Compute the growth rate and get a 95% confidence interval using pairs bootstrap. The time points, in units of hours,
are stored in the numpy array t and the bacterial area, in units of square micrometers, is stored in bac_area."""
import dc_stat_think as dcst
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
# Extracting bacterial data
df = pd.read_csv(r"C:\Users\amlan\Documents\Git Repos\Machine Learning\Neural-Networks-DataCamp\customlib\datasets\park_bacterial_growth.csv")
bac_area = df['bacterial area (sq. microns)']
t = df['time (hr)']
# Compute logarithm of the bacterial area: log_bac_area
log_bac_area = np.log(bac_area)

# Compute the slope and intercept: growth_rate, log_a0
growth_rate, log_a0 = np.polyfit(t,log_bac_area,1)

# Draw 10,000 pairs bootstrap replicates: growth_rate_bs_reps, log_a0_bs_reps
growth_rate_bs_reps, log_a0_bs_reps = \
            dcst.draw_bs_pairs_linreg(t, log_bac_area, size=10000)
# Compute confidence intervals: growth_rate_conf_int
growth_rate_conf_int = np.percentile(growth_rate_bs_reps, [2.5, 97.5])

# Print the result to the screen
print("""
Growth rate: {0:.4f} sq. µm/hour
95% conf int: [{1:.4f}, {2:.4f}] sq. µm/hour
""".format(growth_rate, *growth_rate_conf_int))

"""Plotting the growth curve

You saw in the previous exercise that the confidence interval on the growth curve is very tight. 
You will explore this graphically here by plotting several bootstrap lines along with the growth curve. 
You will use the plt.semilogy() function to make the plot with the y-axis on a log scale. 
This means that you will need to transform your theoretical linear regression curve for plotting 
by exponentiating it."""

# Plot data points in a semilog-y plot with axis labeles
_ = plt.semilogy(t, bac_area, marker='.', linestyle='none')

# Generate x-values for the bootstrap lines: t_bs
t_bs = np.array([0, 14])

# Plot the first 100 bootstrap lines
for i in range(100):
    y = np.exp(growth_rate_bs_reps[i] * t_bs + log_a0_bs_reps[i])
    _ = plt.semilogy(t_bs, y, linewidth=0.5, alpha=0.05, color='red')

# Label axes and show plot
_ = plt.xlabel('time (hr)')
_ = plt.ylabel('area (sq. µm)')
plt.show()
"""Do neonicotinoid insecticides have unintended consequences?

As a final exercise in hypothesis testing before we put everything together in our case study in the next chapter,
you will investigate the effects of neonicotinoid insecticides on bee reproduction. These insecticides are very widely
used in the United States to combat aphids and other pests that damage plants.
In a recent study, Straub, et al. (Proc. Roy. Soc. B, 2016) investigated the effects of neonicotinoids on the sperm of
pollinating bees. In this and the next exercise, you will study how the pesticide treatment affected the count of live
sperm per half milliliter of semen. First, we will do EDA, as usual. Plot ECDFs of the alive sperm count for
untreated bees (stored in the Numpy array control) and bees treated with pesticide
(stored in the Numpy array treated)."""
import matplotlib.pyplot as plt
from customlib import ecdf

import pandas as pd
df = pd.read_csv('C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib/datasets/bee_sperm.csv', skiprows=3)
control, treated = df[df['Treatment']=='Control']['AliveSperm'], df[df['Treatment']=='Pesticide']['AliveSperm']
# Compute x,y values for ECDFs
x_control, y_control = ecdf.ecdf.ecdf_compute(control)
x_treated, y_treated = ecdf.ecdf.ecdf_compute(treated)

# Plot the ECDFs
plt.plot(x_control, y_control, marker='.', linestyle='none')
plt.plot(x_treated, y_treated, marker='.', linestyle='none')

# Set the margins
plt.margins(0.02)

# Add a legend
plt.legend(('control', 'treated'), loc='lower right')

# Label axes and show plot
plt.xlabel('millions of alive sperm per mL')
plt.ylabel('ECDF')
plt.show()
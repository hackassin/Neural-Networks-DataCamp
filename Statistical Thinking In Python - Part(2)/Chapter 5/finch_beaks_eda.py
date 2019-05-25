"""EDA of beak depths of Darwin's finches

For your first foray into the Darwin finch data, you will study how the beak depth (the distance, top to bottom, of a
closed beak) of the finch species Geospiza scandens has changed over time. The Grants have noticed some changes of
beak geometry depending on the types of seeds available on the island, and they also noticed that there was some
interbreeding with another major species on Daphne Major, Geospiza fortis. These effects can lead to changes in the
species over time. In the next few problems, you will look at the beak depth of G. scandens on Daphne Major in 1975
and in 2012.
To start with, let's plot all of the beak depth measurements in 1975 and 2012 in a bee swarm plot.
The data are stored in a pandas DataFrame called df with columns 'year' and 'beak_depth'. The units of beak depth
are millimeters (mm)."""
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from customlib import finch_beaks_df as finch

finch_1975_df, finch_2012_df, finch_concat_df = finch.drw_finch_df()
# Create bee swarm plot
_ = sns.swarmplot(x = "year", y = "Beak depth, mm", data= finch_concat_df)

# Label the axes
_ = plt.xlabel('year')
_ = plt.ylabel('beak depth (mm)')

# Show the plot
plt.show()
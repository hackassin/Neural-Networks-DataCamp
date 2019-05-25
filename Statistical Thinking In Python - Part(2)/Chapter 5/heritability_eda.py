""""EDA of heritability

The array bd_parent_scandens contains the average beak depth (in mm) of two parents of the species G. scandens.
The array bd_offspring_scandens contains the average beak depth of the offspring of the respective parents.
The arrays bd_parent_fortis and bd_offspring_fortis contain the same information about measurements from G. fortis birds.
Make a scatter plot of the average offspring beak depth (y-axis) versus average parental beak depth (x-axis) for both species.
Use the alpha=0.5 keyword argument to help you see overlapping points."""
import matplotlib.pyplot as plt
from customlib import finch_beaks_df as finch

bd_parent_fortis, bd_offspring_fortis, bd_parent_scandens,bd_offspring_scandens = finch.finch_parent_offspring()
# Make scatter plots
_ = plt.plot(bd_parent_fortis, bd_offspring_fortis,
             marker='.', linestyle='none', color='blue', alpha=0.5)
_ = plt.plot(bd_parent_scandens, bd_offspring_scandens,
             marker='.', linestyle='none', color='red', alpha=0.5)

# Label axes
_ = plt.xlabel('parental beak depth (mm)')
_ = plt.ylabel('offspring beak depth (mm)')

# Add legend
_ = plt.legend(('G. fortis', 'G. scandens'), loc='lower right')

# Show plot
plt.show()
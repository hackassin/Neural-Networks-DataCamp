"""Pearson correlation of offspring and parental data

The Pearson correlation coefficient seems like a useful measure of how strongly the beak depth of parents are inherited
by their offspring. Compute the Pearson correlation coefficient between parental and offspring beak depths for
G. scandens. Do the same for G. fortis. Then, use the function you wrote in the last exercise to compute a
95% confidence interval using pairs bootstrap. """
import numpy as np
from customlib import bootstrap_repl as bt
from customlib import pearson_coeff as pr
from customlib import finch_beaks_df as finch

bd_parent_fortis, bd_offspring_fortis, bd_parent_scandens,bd_offspring_scandens = finch.finch_parent_offspring()
# Compute the Pearson correlation coefficients
r_scandens = pr.pearson_r(bd_parent_scandens,bd_offspring_scandens)
r_fortis = pr.pearson_r(bd_parent_fortis, bd_offspring_fortis)

# Acquire 1000 bootstrap replicates of Pearson r
bs_replicates_scandens = bt.draw_bs_pairs(bd_parent_scandens,bd_offspring_scandens, pr.pearson_r, 1000)

bs_replicates_fortis = bt.draw_bs_pairs(bd_parent_fortis, bd_offspring_fortis, pr.pearson_r, 1000)


# Compute 95% confidence intervals
conf_int_scandens = np.percentile(bs_replicates_scandens, [2.5, 97.5])
conf_int_fortis = np.percentile(bs_replicates_fortis, [2.5, 97.5])

# Print results
print('G. scandens:', r_scandens, conf_int_scandens)
print('G. fortis:', r_fortis, conf_int_fortis)
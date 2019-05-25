"""Measuring heritability

Remember that the Pearson correlation coefficient is the ratio of the covariance to the geometric mean of the variances
of the two data sets. This is a measure of the correlation between parents and offspring, but might not be the best
estimate of heritability. If we stop and think, it makes more sense to define heritability as the ratio of the
covariance between parent and offspring to the variance of the parents alone. In this exercise, you will estimate
the heritability and perform a pairs bootstrap calculation to get the 95% confidence interval.

This exercise highlights a very important point. Statistical inference (and data analysis in general) is not a
plug-n-chug enterprise. You need to think carefully about the questions you are seeking to answer with your data
and analyze them appropriately. If you are interested in how heritable traits are, the quantity we
defined as the heritability is more apt than the off-the-shelf statistic, the Pearson correlation coefficient."""

import numpy as np
from customlib import finch_beaks_df as finch
from customlib import bootstrap_repl as bt
bd_parent_fortis, bd_offspring_fortis, bd_parent_scandens,bd_offspring_scandens = finch.finch_parent_offspring()

def heritability(parents, offspring):
    """Compute the heritability from parent and offspring samples."""
    covariance_matrix = np.cov(parents, offspring)
    return covariance_matrix[0, 1] / covariance_matrix[0, 0]


# Compute the heritability
heritability_scandens = heritability(bd_parent_scandens, bd_offspring_scandens)
heritability_fortis = heritability(bd_parent_fortis, bd_offspring_fortis)

# Acquire 1000 bootstrap replicates of heritability
replicates_scandens = bt.draw_bs_pairs(
    bd_parent_scandens, bd_offspring_scandens, heritability, size=1000)

replicates_fortis = bt.draw_bs_pairs(
    bd_parent_fortis, bd_offspring_fortis, heritability, size=1000)

# Compute 95% confidence intervals
conf_int_scandens = np.percentile(replicates_scandens, [2.5, 97.5])
conf_int_fortis = np.percentile(replicates_fortis, [2.5, 97.5])

# Print results
print('G. scandens:', heritability_scandens, conf_int_scandens)
print('G. fortis:', heritability_fortis, conf_int_fortis)

"""The heritability of beak depth in G. scandens seems low. It could be that this observed heritability 
was just achieved by chance and beak depth is actually not really heritable in the species.
 You will test that hypothesis here. To do this, you will do a pairs permutation test."""
# Initialize array of replicates: perm_replicates
perm_replicates = np.empty(10000)

# Draw replicates
for i in range(10000):
    # Permute parent beak depths
    bd_parent_permuted = np.random.permutation(bd_parent_scandens)
    perm_replicates[i] = heritability(bd_parent_permuted, bd_offspring_scandens)


# Compute p-value: p
p = np.sum(perm_replicates >= heritability_scandens) / len(perm_replicates)

# Print the p-value
print('p-val =', p)

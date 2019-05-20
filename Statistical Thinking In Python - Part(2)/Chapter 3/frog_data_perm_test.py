"""The average strike force of Frog A was 0.71 Newtons (N), and that of Frog B was 0.42 N
for a difference of 0.29 N. It is possible the frogs strike with the same force and this observed difference
was by chance. You will compute the probability of getting at least a 0.29 N difference in mean strike force
under the hypothesis that the distributions of strike forces for the two frogs are identical.
We use a permutation test with a test statistic of the difference of means to test this hypothesis.

For your convenience, the data has been stored in the arrays force_a and force_b."""
import numpy as np
from customlib import permutation_repl as prm


def diff_of_means(data_1, data_2):
    """Difference in means of two arrays."""

    # The difference of means of data_1, data_2: diff
    diff = np.mean(data_1) - np.mean(data_2)

    return diff

# Compute difference of mean impact force from experiment: empirical_diff_means
empirical_diff_means = diff_of_means(force_a,force_b)

# Draw 10,000 permutation replicates: perm_replicates
perm_replicates = prm.draw_perm_reps(force_a, force_b,
                                 diff_of_means, size=10000)

# Compute p-value: p
p = np.sum(perm_replicates >= empirical_diff_means) / len(perm_replicates)

# Print the result
print('p-value =', p)
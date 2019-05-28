"""Generating permutation samples

As you worked out in the last exercise, we need to generate a permutation sample by randomly swapping
corresponding entries in the semi_times and final_times array. Write a function with signature swap_random(a, b)
that returns arrays where random indices have the entries in a and b swapped."""
import numpy as np

def swap_random(a, b):
    """Randomly swap entries in two arrays."""
    # Indices to swap
    swap_inds = np.random.random(size=len(a)) < 0.5

    # Make copies of arrays a and b for output
    a_out = a
    b_out = b

    # Swap values
    a_out[swap_inds] = a[swap_inds]
    b_out[swap_inds] = b[swap_inds]

    return a_out, b_out
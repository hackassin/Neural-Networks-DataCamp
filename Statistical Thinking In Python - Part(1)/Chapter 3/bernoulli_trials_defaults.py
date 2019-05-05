import matplotlib.pyplot as plt
import numpy as np
from customlib import ecdf
def perform_bernoulli_trials(n, p):
    """Perform n Bernoulli trials with success probability p
    and return number of successes."""
    # Initialize number of successes: n_success
    n_success = 0

    # Perform trials
    for i in range(n):
        # Choose random number between zero and one: random_number
        random_number = np.random.random()

        # If less than p, it's a success so add one to n_success
        if random_number < p:
            n_success += 1

    return n_success

# Seed random number generator
np.random.seed(42)

# Initialize the number of defaults: n_defaults
# n_defaults: No. of loan defaulters
n_defaults = np.empty(1000)

# Compute the number of defaults
for i in range(1000):
    n_defaults[i] = perform_bernoulli_trials(100,0.05)


# Plot the histogram with default number of bins; label your axes
_ = plt.hist(n_defaults,density=True)
_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('probability')

# Show the plot
plt.show()
# To compute if bank fails
# Compute ECDF: x, y
x, y = ecdf.ecdf.ecdf_compute(n_defaults)
# Plot the ECDF with labeled axes
plt.plot(x, y, marker = '.',linestyle = 'none')
plt.xlabel('No. of defaults')
plt.ylabel('ECDF')

# Show the plot
plt.show()
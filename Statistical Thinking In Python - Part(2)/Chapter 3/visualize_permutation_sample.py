"""Visualizing permutation sampling

To help see how permutation sampling works, in this exercise you will generate permutation samples
and look at them graphically.We will use the Sheffield Weather Station data again,
this time considering the monthly rainfall in July (a dry month) and November (a wet month).
We expect these might be differently distributed, so we will take permutation samples
to see how their ECDFs would look if they were identically distributed. The data are stored in the
Numpy arrays rain_june and rain_november. As a reminder, permutation_sample() has a
function signature of permutation_sample(data_1, data_2) with a return value of
permuted_data[:len(data_1)], permuted_data[len(data_1):],
where permuted_data = np.random.permutation(np.concatenate((data_1, data_2)))"""
import matplotlib.pyplot as plt
from customlib import ecdf
from customlib import permutation_repl as prm
import pandas


df = pandas.read_fwf("C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib/datasets/sheffield_weather_station.csv",skiprows=8)
rain_june, rain_november = df[df['mm']==6]['rain'], df[df['mm']==11]['rain']
for _ in range(50):
    # Generate permutation samples
    perm_sample_1, perm_sample_2 = prm.permutation_sample(rain_june,rain_november)


    # Compute ECDFs
    x_1, y_1 = ecdf.ecdf.ecdf_compute(perm_sample_1)
    x_2, y_2 = ecdf.ecdf.ecdf_compute(perm_sample_2)

    # Plot ECDFs of permutation sample
    _ = plt.plot(x_1, y_1, marker='.', linestyle='none',
                 color='red', alpha=0.02)
    _ = plt.plot(x_2, y_2, marker='.', linestyle='none',
                 color='blue', alpha=0.02)

# Create and plot ECDFs from original data
x_1, y_1 = ecdf.ecdf.ecdf_compute(rain_june)
x_2, y_2 = ecdf.ecdf.ecdf_compute(rain_november)
_ = plt.plot(x_1, y_1, marker='.', linestyle='none', color='red')
_ = plt.plot(x_2, y_2, marker='.', linestyle='none', color='blue')

# Label axes, set margin, and show plot
plt.margins(0.02)
_ = plt.xlabel('monthly rainfall (mm)')
_ = plt.ylabel('ECDF')
plt.show()

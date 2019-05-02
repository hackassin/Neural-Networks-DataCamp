from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import pandas
import numpy as np
iris = load_iris()
df = pandas.DataFrame(iris.data, columns=iris.feature_names)
df['label'] = iris.target
label_versicolor = df['label'] == 1
versicolor_data = df[label_versicolor]
versicolor_petal_length = np.array(versicolor_data['petal length (cm)'])
# Specify array of percentiles: percentiles
percentiles = np.array([2.5,25,50,75,97.5])

# Compute percentiles: ptiles_vers
ptiles_vers = np.percentile(versicolor_petal_length,percentiles)

# Print the result
print(ptiles_vers)

def ecdf(data):
    """Compute ECDF (Empirical Cumulative Distribution Functions) for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1,len(x)+1) / len(x)
    return x, y

# Compute ECDF
x_vers,y_vers = ecdf(versicolor_petal_length)
# Plot the ECDF
_ = plt.plot(x_vers, y_vers, '.')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Overlay percentiles as red diamonds.
_ = plt.plot(ptiles_vers, percentiles/100, marker='D', color='red',
         linestyle='none')

# Show the plot
plt.show()
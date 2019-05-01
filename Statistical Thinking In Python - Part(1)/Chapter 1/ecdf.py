from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import pandas
import numpy as np
def ecdf(data):
    """Compute ECDF (Empirical Cumulative Distribution Functions) for a one-dimensional array of measurements."""
    # Number of data points: n
    n = len(data)

    # x-data for the ECDF: x
    x = np.sort(data)

    # y-data for the ECDF: y
    y = np.arange(1,len(x)+1) / len(x)
    return x, y
#importing the dataframe
iris = load_iris()
df = pandas.DataFrame(iris.data, columns=iris.feature_names)
df['label'] = iris.target
label_versicolor = df['label'] == 2
versicolor_data = df[label_versicolor]
versicolor_petal_length = np.array(versicolor_data['petal length (cm)'])
# Compute ECDF for versicolor data: x_vers, y_vers
x_vers,y_vers = ecdf(versicolor_petal_length)
# Generate plot
_ = plt.plot(x_vers,y_vers,marker = '.', linestyle = 'none')
# Label the axes
_ = plt.xlabel('Petal Lengths (cm)')
_ = plt.ylabel('ECDF')
# Display the plot
plt.show()
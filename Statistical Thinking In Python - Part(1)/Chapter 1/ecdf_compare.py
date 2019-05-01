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
#labelling the dataframe
df['label'] = iris.target
label_setosa = df['label'] == 0
label_versicolor = df['label'] == 1
label_virginica = df['label'] == 2

setosa_data = df[label_setosa]
versicolor_data = df[label_versicolor]
virginica_data = df[label_virginica]

setosa_petal_length = np.array(setosa_data['petal length (cm)'])
versicolor_petal_length = np.array(versicolor_data['petal length (cm)'])
virginica_petal_length = np.array(virginica_data['petal length (cm)'])
# Compute ECDF for versicolor data: x_vers, y_vers
x_set, y_set = ecdf(setosa_petal_length)
x_vers, y_vers = ecdf(versicolor_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)
# Plot all ECDFs on the same plot
plt.plot(x_set,y_set,marker='.',linestyle='none')
plt.plot(x_vers,y_vers,marker='.',linestyle='none')
plt.plot(x_virg,y_virg,marker='.',linestyle='none')
# Annotate the plot
plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('ECDF')

# Display the plot
plt.show()
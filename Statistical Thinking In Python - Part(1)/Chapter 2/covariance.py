from sklearn.datasets import load_iris
import pandas
import numpy as np

#loading the datframe
iris = load_iris()
df = pandas.DataFrame(iris.data, columns=iris.feature_names)

#extracting the versicolor_petal_length & width
df['label'] = iris.target
label_versicolor = df['label'] == 1
versicolor_data = df[label_versicolor]
versicolor_petal_length = np.array(versicolor_data['petal length (cm)'])
versicolor_petal_width = np.array(versicolor_data['petal width (cm)'])


# Compute the covariance matrix: covariance_matrix
covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)

# Print covariance matrix
print(covariance_matrix)

# Extract covariance of length and width of petals: petal_cov
petal_cov = covariance_matrix[0][1]

# Print the length/width covariance
print('Covariance:\n',petal_cov)
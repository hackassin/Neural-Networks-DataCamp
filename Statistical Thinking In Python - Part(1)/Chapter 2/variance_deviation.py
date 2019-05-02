from sklearn.datasets import load_iris
import pandas
import numpy as np

#loading the datframe
iris = load_iris()
df = pandas.DataFrame(iris.data, columns=iris.feature_names)

#extracting the versicolor_petal_length
df['label'] = iris.target
label_versicolor = df['label'] == 1
versicolor_data = df[label_versicolor]
versicolor_petal_length = np.array(versicolor_data['petal length (cm)'])
# Array of differences to mean: differences
differences = versicolor_petal_length - np.mean(versicolor_petal_length)

# Square the differences: diff_sq
diff_sq = differences**2

# Compute the mean square difference: variance_explicit
variance_explicit = np.mean(diff_sq)

# Compute the variance using NumPy: variance_np
variance = np.var(versicolor_petal_length)
print(variance)

# Print the square root of the variance
print(variance**0.5)

# Print the standard deviation
print(np.std(versicolor_petal_length))
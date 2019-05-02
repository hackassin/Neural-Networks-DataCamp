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

def pearson_r(x,y):
    """Compute Pearson correlation coefficient between two arrays."""
    # Compute correlation matrix: corr_mat
    corr_mat = np.corrcoef(x,y)
    #print("corr_mat:\n",corr_mat)
    # Return entry [0,1]
    return corr_mat[0,1]

# Compute Pearson correlation coefficient for I. versicolor: r
r = pearson_r(versicolor_petal_length, versicolor_petal_width)
# Print the result
print(r)
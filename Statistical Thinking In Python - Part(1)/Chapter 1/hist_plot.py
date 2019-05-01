from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import pandas
import numpy as np
iris = load_iris()
df = pandas.DataFrame(iris.data, columns=iris.feature_names)
#df = pandas.DataFrame(np.column_stack((iris.data, iris.target)), columns = iris.feature_names+[])
df['label'] = iris.target
#df2 = df.assign(iris.target)
#print(df.head())
#print(iris)
label_versicolor = df['label'] == 2
versicolor_data = df[label_versicolor]
versicolor_petal_length = np.array(versicolor_data['petal length (cm)'])
print('versicolor_petal_length:\n', versicolor_data['petal length (cm)'])
print('all_petal_length:\n', df['petal length (cm)'])
#print(df[label_versicolor])
#print(versicolor_petal_length)

# Set default Seaborn style
sns.set()
# Plot histogram of versicolor petal lengths
_ = plt.hist(versicolor_petal_length)
# Label axes
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')
# Show histogram
plt.show()
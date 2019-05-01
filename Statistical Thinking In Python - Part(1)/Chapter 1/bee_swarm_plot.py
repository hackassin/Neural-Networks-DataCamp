from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import pandas
import numpy as np
iris = load_iris()
df = pandas.DataFrame(iris.data, columns=iris.feature_names)
#df = pandas.DataFrame(np.column_stack((iris.data, iris.target)), columns = iris.feature_names+[])
df['label'] = iris.target
df['species'] = df.label.replace(dict(enumerate(iris.target_names)))
# Set default Seaborn style
sns.set()
# Create bee swarm plot with Seaborn's default settings
_ = sns.swarmplot(x = 'species',y = 'petal length (cm)', data = df)
# Label the axes
_ = plt.xlabel('species')
_ = plt.ylabel('petal length (cm)')
# Show the plot
plt.show()
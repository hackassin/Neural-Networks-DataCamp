"""Look before you leap: EDA before hypothesis testing Kleinteich and Gorb (Sci. Rep., 4, 5225, 2014) performed
an interesting experiment with South American horned frogs. They held a plate connected to a force transducer,
along with a bait fly, in front of them. They then measured the impact force and adhesive force of the
frog's tongue when it struck the target. Frog A is an adult and Frog B is a juvenile. The researchers measured the
impact force of 20 strikes for each frog. In the next exercise, we will test the hypothesis that the two frogs have the
same distribution of impact forces. But, remember, it is important to do EDA first! Let's make a bee swarm plot for the data.
They are stored in a Pandas data frame, df, where column ID is the identity of the frog and column impact_force is
the impact force in Newtons (N)."""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas
df = pandas.read_csv('C:/Users/amlan/Documents/Git Repos/Machine Learning/Neural-Networks-DataCamp/customlib/datasets/frog_tongue.csv', skiprows=14)
# Make bee swarm plot
_ = sns.swarmplot(x = 'ID',y = 'impact force (mN)', data=df)

# Label axes
_ = plt.xlabel('frog')
_ = plt.ylabel('impact force (N)')

# Show the plot
plt.show()
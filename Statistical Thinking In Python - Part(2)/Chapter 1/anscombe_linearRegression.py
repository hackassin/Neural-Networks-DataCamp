import numpy as np
import pandas
import matplotlib.pyplot as plt

#extracting anscombe dataset
ab = pandas.read_csv('./anscombe.xslx')
x, y = ab.iloc[1:, 0].astype(float), ab.iloc[1:, 1].astype(float)
# Perform linear regression: a (slope), b (intercept)
a, b = np.polyfit(x,y,1)

# Print the slope and intercept
print(a,b)

# Generate theoretical x and y data: x_theor, y_theor
x_theor = np.array([3,15])
y_theor = a * x_theor + b

# Plot the Anscombe data and theoretical line
_ = plt.plot(x,y,marker='.',linestyle='none')
_ = plt.plot(x_theor,y_theor)

# Label the axes
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()
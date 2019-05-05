import numpy as np
import pandas

ab = pandas.read_csv('anscombe.xslx')
x, y = ab.iloc[1:, 0].astype(float), ab.iloc[1:, 1].astype(float)

anscombe_x = [ab.iloc[1:, 0].astype(float), ab.iloc[1:, 2].astype(float),
              ab.iloc[1:, 4].astype(float), ab.iloc[1:, 6].astype(float)]

anscombe_y = [ab.iloc[1:, 1].astype(float), ab.iloc[1:, 3].astype(float),
              ab.iloc[1:, 5].astype(float), ab.iloc[1:, 7].astype(float)]


# Iterate through x,y pairs
# zip takes iterables anscombe_x,anscombe_y
for x, y in zip(anscombe_x , anscombe_y ):
    # Compute the slope and intercept: a, b
    a, b = np.polyfit(x,y,1)

    # Print the result
    print('slope:', a, 'intercept:', b)
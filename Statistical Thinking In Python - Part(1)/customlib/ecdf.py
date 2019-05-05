import numpy as np
class ecdf:
    def ecdf_compute(data):
        """Compute ECDF (Empirical Cumulative Distribution Functions) for a one-dimensional array of measurements."""
        # Number of data points: n
        n = len(data)
        # x-data for the ECDF: x
        #print('Inside ecdf module')
        x = np.sort(data)
        # y-data for the ECDF: y
        y = np.arange(1,len(x)+1) / len(x)
        return x, y
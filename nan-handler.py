import numpy as np
from numpy import nan

# Source:
# https://stackoverflow.com/questions/6518811/interpolate-nan-values-in-a-numpy-array

def nan_helper(y):
    """Helper to handle indices and logical indices of NaNs.

    Input:
        - y, 1d numpy array with possible NaNs
    Output:
        - nans, logical indices of NaNs
        - index, a function, with signature indices= index(logical_indices),
          to convert logical indices (list of True/False) of NaNs to 'equivalent' indices
    """
    return np.isnan(y), lambda z: z.nonzero()[0]

# Example vector
y = np.array([1, 1, 1, nan, nan, 2, 2, nan, 0])

nans, x = nan_helper(y)

# Lista of True & False, (logical indices)
print("nans:\t\t", nans)

# nans:		 [False False False  True  True False False  True False]


# indices of non zero values (True = 1)
print("nans.nonzero():\t", nans.nonzero())

# nans.nonzero():	 (array([3, 4, 7], dtype=int64),)


print("initial vector:\t",list(map('{:5.2f}'.format,y)))

# initial vector:	 [' 1.00', ' 1.00', ' 1.00', '  nan', '  nan', ' 2.00', ' 2.00', '  nan', ' 0.00']


# replace the nans (y[nans indices]) with the interpolation
# the vectors used to interpolate don't contain nans
y[nans] = np.interp(x(nans), x(~nans), y[~nans])

print("final vector:\t",list(map('{:5.2f}'.format,y)))

# final vector:	 [' 1.00', ' 1.00', ' 1.00', ' 1.33', ' 1.67', ' 2.00', ' 2.00', ' 1.00', ' 0.00']

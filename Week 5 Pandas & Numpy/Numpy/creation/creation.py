# 1.creating arrays from python list
# np.array([ele1,ele2,....])

import numpy as np 
arr = np.array([1,2,3])
print(arr)

# 2.with default values
# np.zeros(shape) (3) for 1d, (3,3) for 2d

zeroes_arr = np.zeros((2,3))
print(zeroes_arr)

# 3.ones(shape)

ones_arr = np.ones(3)
print(ones_arr)

# 4.full(shape,value)

filled_arr = np.full((2,2),5)
print(filled_arr)

# 5.creating sequence of numbers in numpy
# arange(start,stop,step)

arr = np.arange(2,12,2)
print(arr)

# 6.creating identity matrices
# eye(size)

identity_matrix = np.eye(4)
print(identity_matrix)
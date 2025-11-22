'''
reshape(rows, column) specify new shape
if dimension match
'''

import numpy as np
arr = np.array([1,2,3,4,5,6])
print(arr.reshape(3,2))
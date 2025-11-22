# np.isinf(array) 10*1000
# 1/0

import numpy as np

arr = np.array([10, 20, np.inf, 40, -np.inf])
print(arr)
print(np.isinf(arr))
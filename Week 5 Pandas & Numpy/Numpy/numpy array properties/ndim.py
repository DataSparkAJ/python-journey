import numpy as np

arr_1d = np.arange(3)
arr_2d = np.array([[1,2,3],
                   [4,5,6]])
arr_3d = np.array([[[1,23],[34,32],[2,3],[7,8]]])
print(arr_3d.ndim)
print(arr_2d.ndim)
print(arr_1d.ndim)
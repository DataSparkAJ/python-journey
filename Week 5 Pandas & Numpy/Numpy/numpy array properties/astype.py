import numpy as np 

arr = np.array([23.9,4.4,3.3])
print(arr.dtype)

int_arr = arr.astype(int)
print(int_arr,int_arr.dtype)
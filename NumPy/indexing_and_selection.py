import numpy as np

arr = np.arange(0,11)
print(arr[9])
print(arr[1::])
arr[0:5] = 100
print(arr)
arr = np.arange(0, 11)
slice_of_arr = arr[:5]
print(slice_of_arr)
slice_of_arr[0:] = 10
print(slice_of_arr)
print(arr)
arr = np.arange(0, 11)
arr_copy = arr[:5].copy()
print(arr_copy)
arr_copy[0:5] = 12
print(arr_copy)
print(arr)


arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)
print(arr_2d[0])
print(arr_2d[:, 1:])

arr = np.arange(0, 11)
print(arr > 4)
bool_arr = arr > 4
print(arr[ bool_arr])

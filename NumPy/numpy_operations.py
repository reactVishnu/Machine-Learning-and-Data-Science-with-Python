import numpy as np

arr = np.arange(11)
print(arr + arr)
print(arr - arr)
print(arr * arr)
# print(arr/arr)

print(arr + 1)
# print(1/arr)

print(arr.sum())
print(np.sqrt(arr))
print(np.square(arr))
print(np.sin(arr))
print(np.mean(arr))
print(np.var(arr))
print(np.std(arr))

arr_2d = np.arange(0, 25).reshape(5, 5)
print(arr_2d)
print(arr_2d.sum())
print(arr_2d.sum(axis=0))  # Sum of columns
print(arr_2d.sum(axis=1))  # Sum of rows
print(arr_2d[:,0:1].sum())

mylist = [1, 2, 3]


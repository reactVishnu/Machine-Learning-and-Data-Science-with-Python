import random

import numpy as np

mylist = [1, 2, 3]
print(mylist)
my_arr = np.array(mylist)
print(my_arr[1])

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(np.array(my_matrix))

print(np.zeros((5, 1)))

print(np.ones((1, 1)))

print(np.linspace(0, 3, 5))

print(np.eye(4))

print(np.random.rand(1 ))
print(np.random.randn(8))

print(np.random.randint(1, 4, (3, 4)))
print(random.randint(10, 50))

# np.random.seed(42)
print(np.random.randint(3, 42))

arr = np.arange(11,25)
print(arr.reshape(7, 2))
print(arr.dtype)

arr = arr.reshape(7, 2)
print(arr.shape)
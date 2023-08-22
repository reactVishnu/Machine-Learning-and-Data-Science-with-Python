import numpy as np

print(np.zeros(10))
print(np.ones(10))
print(np.random.randint(5,6,10))
print(np.arange(10,51,2))

print(np.arange(0, 9).reshape(3, 3))
print(np.eye(3))

print(np.random.randn(25))
print(np.linspace(0,1,20))

print(np.arange(12,20).reshape(2, 4))

mat = np.arange(1,26).reshape(5,5)
print(mat)
print(mat[3,4])
print(mat[3:])
print(mat.sum(axis=0))
import numpy as np


# usinf Aggreate function

arr1 = np.reshape(np.arange(3*3) , (3,3))

arr2 = np.reshape(np.arange(3*4) , (3,4))

print(arr1)

print(arr1.sum())

print(arr1.sum(axis = 0))
print(arr1.sum(axis = 1))

print(arr1.min())

print(arr1.min(axis = 0))

print(arr1.max())

print(arr1.prod())

print(arr1.prod(axis = 0))

print(arr1.mean()) # mean

print(arr1.std()) # standard deviation

print(arr1.var()) # variance

print(arr1.argmin()) # index of minimum value
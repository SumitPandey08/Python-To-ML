import numpy as np

# Transpose

arr1 = np.reshape(np.arange(3*3) , (3,3))
print(arr1.transpose())

arr2 = np.reshape(np.arange(2*3) , (2,3))
print(arr2.transpose())

arr3 = np.reshape(np.arange(2*3*4) , (2,3,4))
print(arr3.transpose())
print(arr3)

# moveAxis

print(np.moveaxis(arr3 , 0 , -1))
# print(np.moveaxis(arr2 , 0 , 1))


# swapaxes

print(np.swapaxes(arr3 , 0 , -1))
# print(np.swapaxes(arr2 , 0 , -1))
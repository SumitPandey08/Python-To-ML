import numpy as np

# reverse

arr1 = np.arange(11)
print(arr1[::-1])

print(np.flip(arr1))

arr2 = np.reshape(np.arange(3*4) , (3,4))
print(arr2[::-1]) # reverse the rows of the matrix

print(np.flip(arr2)) # reverse then matrix

print(arr2[:,::-1]) # reverse the coloumns of the matrix

print(np.flip(arr2 , axis = 0)) # reverse the rows of the matrix

print(np.flip(arr2 , axis = 1)) # reverse the coloumns of the matrix

arr3 = np.reshape(np.arange(2*3*4) , (2,3,4))

print(arr3[::-1]) # reverse the rows of the matrix

print(np.flip(arr3)) # reverse then matrix
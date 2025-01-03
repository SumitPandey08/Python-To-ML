import numpy as np

# indexing

oneDimArray = np.arange(1 , 12)
print(oneDimArray)

print(oneDimArray[0])

oneDimArray[0] = 100
print(oneDimArray)

twoDimArray = np.reshape(np.arange(4 * 5) , (4 , 5))
print(twoDimArray)

print(twoDimArray[0 , 0])
print(twoDimArray[1 , -1]) 

twoDimArray[0 , 0] = 100
print(twoDimArray)


threeDimArray = np.reshape(np.arange(4 * 5 * 3) , (4 , 5 , 3))
print(threeDimArray)

print(threeDimArray[0 , 0 , 0])
print(threeDimArray[1 , -1 , -1])

threeDimArray[0 , 0 , 0] = 100
print(threeDimArray)


# slicing

slice1d = oneDimArray[1 : 5]
print(slice1d)

slice2d = twoDimArray[1 :  , 1 : ] # all rows from 1 and all columns from 1
print(slice2d)

slice3d = threeDimArray[1 :  , 1 :  , 1 : ] # all rows from 1 and all columns from 1 and all depth from 1
print(slice3d)
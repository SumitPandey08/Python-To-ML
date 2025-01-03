import numpy as np

# reshapes

firstArray = np.arange(1 , 13)
print(firstArray)

secondArray = firstArray.reshape(3 , 4)
print(secondArray)

thirdArray = firstArray.reshape(2 , 6)
print(thirdArray)

# fourthArray = firstArray.reshape(4 , 4) # this will give error as we have 12 elements
# print(fourthArray)

# fifthArray = firstArray.reshape(3 , 3) # this will give error as we have 12 elements
# print(fifthArray)

sixthArray = np.array([[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9]])
print(sixthArray)

seventhArray = sixthArray.reshape(-1) # this will flatten the array
print(seventhArray)

eighthArray = sixthArray.reshape(3 ,3) # this will convert 1d array to 2d array
print(eighthArray)

# now using flatten method and ravel method

ninthArray = sixthArray.flatten()
print(ninthArray) # this will give 1d array but it will copy the data

tenthArray = sixthArray.ravel()
print(tenthArray) # this will give 1d array but it will not copy the data
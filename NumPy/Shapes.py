import numpy as np

# create a shapes array
firstArray = np.arange(10)
print(firstArray)

secondArray = np.linspace((1, 2) , (10 , 20) , 10) # 10 numbers between (1, 2) and (10 , 20)
print(secondArray)

thirdArray = np.full((2 , 2 , 2) , 10) # 2 by 2 by 2 array filled with 10
print(thirdArray)

firstShapesArray = np.shape(firstArray)
print(firstShapesArray)

secondShapesArray = np.shape(secondArray)
print(secondShapesArray)

thirdShapesArray = np.shape(thirdArray)
print(thirdShapesArray)

# now size

firstSizeArray = np.size(firstArray)
print(firstSizeArray)

secondSizeArray = np.size(secondArray)
print(secondSizeArray)

thirdSizeArray = np.size(thirdArray)
print(thirdSizeArray)
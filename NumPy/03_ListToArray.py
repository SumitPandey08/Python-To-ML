import numpy as np

# List To Array

firstList = [1 , 2 , 3 , 4 , 5]
firstArray = np.array(firstList)

print(firstArray)

secondList = [1 , -1 , 4 , 3 , 0.5 ,  0.67 , 10 , 8]
secondArray = np.array(secondList)   # everything will be converted to float 

print(secondArray)


thirdList = ['Aizen' , 'bankai' , 'Ichigo' , 1 , 3 , 5 , 6 ]
thirdArray = np.array(thirdList)
print(thirdArray) # everything will be converted to string


#tuple to array
firstTuple = (1 , 2 , 3 , 4 , 5)
tupleToArray = np.array(firstTuple)
print(tupleToArray)
print(type(tupleToArray))

# multi dimention List to array
multiDimentionList = [[1 , 2 , 3] , [4 , 5 , 6] , [7 , 8 , 9]]
multiDimentionArray = np.array(multiDimentionList)
print(multiDimentionArray)
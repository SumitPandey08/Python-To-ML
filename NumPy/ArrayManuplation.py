import numpy as np

# Array Manuplation


firstArray = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10])

# add in array

newFirstArray = np.insert(firstArray , 10 , 12) # insert 12 at index 10
print(newFirstArray)


secondArray = np.array([1 , 2 , 3, 4 , 5])

newSecondArray = np.append(secondArray, 6) # append 6 at the end
print(newSecondArray)

# delete from array

thirdArray = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10])

newThirdArray = np.delete(thirdArray , 5) # delete element at index 5
print(newThirdArray)


# sort array
fourthArray = np.random.randint(1 , 100 , 10)
print(fourthArray)

newFourthArray = np.sort(fourthArray)
print(newFourthArray)

# for two dimentional array

array2d = np.array([[9 , 4  , 10] , [43 , 15 , 36] , [17 , 48 , 99]])
newSortedArray = np.sort(array2d) # sort each row
print(newSortedArray)

# Now test it for string

colors = np.array(['red' , 'blue' , 'green' , 'yellow' , 'black'])
sortColor = np.sort(colors)
print(sortColor)
import numpy as np

# broadcasting


arr1 = np.reshape(np.arange(3*3) , (3,3))

arr2 = np.reshape(np.arange(3) , (3,1))

operation1 = arr1 + arr2
print(operation1) # it will add the arr2 to each row of arr1 and it shows compatibilty as it have 3 coloumns and arr2 have 3 rows and 3 coloumn

arr3 = np.array([1 , 2])

# operation2 = arr1 + arr3
# print(operation2) # it will show error because the shape of arr3 is not same as arr1 alos it is not compatible for operation with it

arr4 = np.reshape(np.arange(2*3*4) , (2,3,4))
arr5 = np.reshape(np.arange(3*4) , (3,4))

operation3 = arr4 + arr5
print(operation3) # it will add the arr5 to each row of arr4 and it shows compatibilty as it have 4 coloumns and arr5 have 3 rows and 4 coloumn
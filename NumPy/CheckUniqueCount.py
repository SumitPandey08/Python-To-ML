import numpy as np

# Check unique  and count

arr1 = np.array([1, 2, 3, 2 , 4  , 4 , 1 ,4 , 7 , 9 , 6 , 7 ])
print(np.unique(arr1))

arr2 = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [4, 5, 6]])
print(np.unique(arr2))

print(np.unique(arr2 , axis = 0))

print(np.unique(arr1 , return_index=True )) # return the index of unique values

print(np.unique(arr1 , return_counts=True )) # return the count of unique values



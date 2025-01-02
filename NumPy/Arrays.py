import numpy as np

array = np.array([1 , 2  , 3 , 4 , 5])
print(array)

# Output: [1 2 3 4 5]

print(type(array))
# Output: <class 'numpy.ndarray'>

print(array[0])
# Output: 1
array[0] = 10

print(array)

array[0] = 21.6
print(array)
# Output: [21  2  3  4  5] beacuse the array is of type int

print(array.dtype)
# Output: int64

# we can change even bytes of the array

smallArray = np.array(array , dtype = 'int8')

print(array.nbytes)
# Output: 40
print(smallArray.nbytes)
# Output: 5

# overflow = np.array([127 , 129 , 126] , dtype = 'int8')
# print(overflow)
# # Output: error because 129 is out of range of int8


floatArr = np.array([1.2 , 2.3 , 3.4 , 4.5 , 5.6])
print(floatArr)

floatArr[0] = 23
print(floatArr) # 23 convert into 23.0

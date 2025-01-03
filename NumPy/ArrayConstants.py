import numpy as np

# creating arrays full of zeros

zeroArray = np.zeros(10)
print(zeroArray)

zeroArray = np.zeros((3 , 4)) # we pass a tuple to create multi dimention array
print(zeroArray) # 3 rows and 4 columns

zeroArray = np.zeros((3 , 4 , 5)) # 3 rows , 4 columns and 5 depth
print(zeroArray) 
print(zeroArray.ndim) # 3

# Now creating arrays full of ones

oneArray = np.ones(10)
print(oneArray)

oneArray = np.ones((3 , 4)) # we pass a tuple to create multi dimention array
print(oneArray) # 3 rows and 4 columns

oneArray = np.ones((3 , 4 ) , dtype=int) # dtype for int one
print(oneArray) # 3 rows and 4 columns 

# now using empty

emptyArray = np.empty(10 , dtype = int)
filled_Array = emptyArray.fill(12) # first creates an empty then fills it with 12
print(emptyArray)

# full array
fullArray = np.full(10 , 12) # create an array of 10 elements and fill it with 12
print(fullArray)

fullDimArray = np.full((3 , 4) , 8) # create a 3 by 4 array and fill it with 12
print(fullDimArray)
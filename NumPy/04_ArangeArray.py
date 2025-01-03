import numpy as np

# Arange Array

firstArray = np.arange(10)
print(firstArray)

secondArray = np.arange(100 , 130)
print(secondArray)

thirdArray = np.arange(120 , 151 , 2)
print(thirdArray)


# creating using linspace

FloatArray = np.linspace(10 , 20)  # by  default num = 50
print(FloatArray)

FloatArray = np.linspace(10 , 20 , 5)
print(FloatArray) # 5 numbers between 10 and 20

FloatArray = np.linspace(10 , 20 , 5 , endpoint = False)
print(FloatArray) # 5 numbers between 10 and 20 but 20 is not included

FloatArray = np.linspace(10 , 20 , 5 , retstep = True)
print(FloatArray) # 5 numbers between 10 and 20 and the step is 2.5

FloatArray = np.linspace(10 , 20 , 5 , dtype = int)
print(FloatArray) # 5 numbers between 10 and 20 and the data type is int


# creating using random

randomArray = np.random.rand(10)
print(randomArray)

randomArray = np.random.rand(10 , 3)
print(randomArray) # 10 rows and 3 columns
print(randomArray.ndim) # 2

# now using randint
randomArray = np.random.randint(10 , 30 , 10)
print(randomArray) # create 10 random numbers between 10 and 30
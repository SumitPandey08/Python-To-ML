import numpy as np

# first checking Assingment

mainArray = np.array([1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10])

assignArray = mainArray
print(assignArray)

print(f'id of mainArray: {id(mainArray)}')
print(f'id of assignArray: {id(assignArray)}')
# we can see both have same id

assignArray[0] = 10

print(f'mainArray: {mainArray}')
print(f'assignArray: {assignArray}')

# we can see assign changes are also reflected in main array

# now we will use copy method

copyArray = mainArray.copy()
print(copyArray)

print(f'id of mainArray: {id(mainArray)}')
print(f'id of copyArray: {id(copyArray)}')
# we can see both have different id


copyArray[0] = 100

print(f'mainArray: {mainArray}')
print(f'copyArray: {copyArray}')

# we can see changes in copy array are not reflected in main array

# now we will use view method

viewArray = mainArray.view()
print(viewArray)

print(f'id of mainArray: {id(mainArray)}')
print(f'id of viewArray: {id(viewArray)}')
# we can see both have different id

viewArray[0] = 1000

print(f'mainArray: {mainArray}')
print(f'viewArray: {viewArray}')

print(" base of copyArray" , copyArray.base)
print(" base of viewArray" , viewArray.base)
# we can see copyArray is not base of mainArray

import numpy as np

# joining arrays

arr1 = np.array([1, 2, 3, 4 , 5])
arr2 = np.array([6, 7, 8, 9, 10])

arr = np.concatenate((arr1, arr2))
print(arr)

# Join two 2-D arrays along rows (axis=1):

arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr3 , arr4) , axis = 1)
print(arr)

# Joining arrays using stack functions

arr = np.stack((arr3, arr4))
print(arr) # 3D array

arr0 = np.stack((arr3, arr4) , axis = 1)
print(f"arr0 :  {arr0}") # 3D array

arrhst = np.hstack((arr3, arr4))
print(f"arrhst :  {arrhst}") # 2D array

arr2vst = np.vstack((arr3, arr4))
print(f"arr2vst :  {arr2vst}") # 2D 



arrayst = np.stack((arr1 , arr2) )
print(f"arrays12 : {arrayst}")

arrayhst = np.hstack((arr1 , arr2))
print(f"arrayhst : {arrayhst}")

arrayvst = np.vstack((arr1 , arr2))
print(f"arrayvst : {arrayvst}")


# Splitting arrays

firstArr = np.arange(1 , 16)
print(firstArr)

sp_firstArr = np.array_split(firstArr , 3)
print(sp_firstArr)

sp_firstArr2 = np.array_split(firstArr , 4)
print(sp_firstArr2)

# Splitting 2-D arrays

arr5 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
sp_arr5 = np.array_split(arr5 , 3)
print(sp_arr5)

hsp_arr5 = np.hsplit(arr5 , 2)
print(hsp_arr5)

vsp_arr5 = np.vsplit(arr5 , 3)
print(vsp_arr5)
import numpy as np

# zero Dimensional
a = np.array(42)

# one Dimensional
b = np.array([1 , 2 , 3 , 4 , 5])
b[0] =  10


# two Dimensional
c = np.array([[1 , 2 , 3] , [4 , 5 , 6]])
print(c[1 , 1])
print(c)

# three Dimensional
d = np.array([[[1 , 2 , 3] , [4 , 5 , 6]] , [[7 , 8 , 9] , [10 , 11 , 12]]])
print(d[1 , 0 , 2])


print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
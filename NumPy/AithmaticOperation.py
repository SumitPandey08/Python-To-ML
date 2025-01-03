import numpy as np

a = np.arange(1 , 11)
b = np.arange(11 , 21)

# Addition
print(np.add(a , b))
print(a + b)

# Subtraction
print(np.subtract(a , b))
print(a - b)

# Multiplication
print(np.multiply(a , b))
print(a * b)

# Division
print(np.divide(a , b))
print(a / b)

# Modulus
print(np.mod(b , a))
print(b % a)

# Power
print(np.power(a , 2))
print(a ** 2)

print(np.sqrt(b))

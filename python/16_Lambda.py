# lamda is like a function it can assign to a variable
# it can be passed as an argument to a function

x = lambda a : a * a
print(x(5))  # output: 25

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

# also use in function for chain reaction

def multiply(n) :
    return lambda a : a * n 

doubler = multiply(2)

print(doubler(12))

# return 22

#similarly

tripler = multiply(3)
print(tripler(12))  # output: 36
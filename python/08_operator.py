
# Operator 

# Assignment Operator
x = 5
print(x)  # Output: 5

y = x + 5
print(y)  # Output: 10

y = x - 4
print(y)  # Output: 1

y = x*3
print(y)  # Output: 15

y = x/3
print(y)  # Output: 1.6666666666666667

y = x%2
print(y)  # Output: 1

y = x//2
print(y)  # Output: 2

y = x**2
print(y)  # Output: 25


x = 5

x += 3 # equivalent to x = x + 3

print(x)   # Output: 8

x = 5

x -= 3

print(x) # Output: 2

x *= 3
print(x) # Output: 6
x /= 3
print(x) # Output: 2.0

# Logical Operator
# AND Operator
x = 5
y = 10
print(x>y and y>x)
# Output: False

# OR Operator
x = 5
y = 10
print(x>y or y>x)
# Output: True

# not Operator
x = 5
print(not x>10)
# Output: True

# identity Operator
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

print(x is not z)

# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y, even if they have the same content

print(x != y)

# to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to y


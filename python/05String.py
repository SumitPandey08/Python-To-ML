x = "string"
y= 'string'

z = '''this is 
a multi line string'''

strX = "Hello World"
print(len(strX))

a = strX[3]
print(a) # prints "l"

# iterating
for i in strX:
    print(i) # prints each character of the string

#test of Membership Operator

print('H' in strX) # prints True
print("H" not in strX) # prints False

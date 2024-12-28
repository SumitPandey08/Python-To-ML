# comparison Operator returns Boolean Value

a = 9
b = 10
print(a == b)  # Output: False
print(a < b) # Output : True
print(a > b) # Output : False

# variable is assign by anything other that none or empty then its true
a = 5
b = None
print(bool(a))
# Output: True
print(bool(b)) # Output: False

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
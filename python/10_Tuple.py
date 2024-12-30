thisTuple = ("one peice" , "naruto" , "bleach")
print(thisTuple)
print(len(thisTuple))

# tuple are unchangable or unmutable

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tupleMix = ("abc", 34, True, 40, "male")

tuple1 = tuple(("Demon" , "SLayer" , "Alchamist"))
print(tuple1)

print(thisTuple[1])
print(thisTuple[-2])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")


# How to  make Tuple Mutable

x = ("apple", "banana", "cherry") # tuple
y = list(x) # change into List
y[1] = "kiwi" # as List are mutable
x = tuple(y) # change back to Tuple

print(x)

# we can add Items too
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# remove tooo
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


# Unpack of tuple

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits     # * means else elment goes in to red

print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits 

print(green)
print(tropic)
print(red)

# iteratability in tuple

thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


# Join o tuple

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.count(5)

print(x)

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)

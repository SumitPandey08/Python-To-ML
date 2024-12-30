
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

print(thisdict["brand"])
# now Dictionaries are ordered

print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "model": "Mustang",
  "colors": ["red", "white", "blue"]  # we can add other datatypes as well
}

isdict = dict(name = "John", age = 36, country = "Norway")
print(isdict)

x = thisdict["model"]

x = thisdict.get("model")

x = thisdict.keys() # Give ALl the Keys in  list
print(x)

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["MaxSpeed"] = "200Km/hr"

print(x) #after the change

x = thisdict.values() # return all values
print(x)
print(thisdict.items()) # give the key value pair in an array

# Update Method

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2099})

# add and Update both using update()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") # remove model with value
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem() # delte last key and value pair
print(thisdict)


thisdict.clear()
print(thisdict) #clear the dictionary


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(x) #  give all the keys

for x in thisdict:
  print(thisdict[x]) # give all the values

for x, y in thisdict.items():
  print(x, y) # give the key and value both


# Nested Dictionary
nested = {
  "child1" = {
  "name" : "Emil",
  "year" : 2004
} ,
"child2" = {
  "name" : "Tobias",
  "year" : 2007
} ,
"child3" = {
  "name" : "Linus",
  "year" : 2011
} ,

"myfamily" = {
  "child1" : "child1",
  "child2" : "child2",
  "child3" : "child3"
}  
}


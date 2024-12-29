myList = ["apple" , "grapes" , "orange"]
myList.append("banana")
print(myList)  # Output: ['apple', 'grapes', 'orange', 'banana']
print(len(myList))
print(myList[1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

## very  Good Method
myList.insert(2, "watermelon")
print(myList)

thislist.append("orange")  # add at last
print(thislist)

thislist.pop() # remove from last
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  # as like as concat in js
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple) # tuple too

thislist = ["apple", "banana", "cherry", "watermelon", "kiwi"] 
thislist.remove("banana") # remove the element by name
print(thislist)

thislist.pop(1)  # remove element by index
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[1] # also delete the elemnt
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.clear() # delete whole thing
print(thislist)

#iteratability

thislist = ["apple", "banana", "cherry"]
for i in thislist:
  print(i)

for i in range(len(thislist)):
  print(thislist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1  

# List COmprehensibility
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x) # append the element to the new list who have a in them

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# sorting

thislist = ["orange", "mango", "apple" , "kiwi", "pineapple", "banana"]

thislist.sort() # sort by alphabatic order

print(thislist)

thislist = [100, 50, 65, 82, 23]

thislist.sort() # sort in ascending order

print(thislist)

thislist.sort(reverse = True) # sort in descending order
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() # copy() the mylist
print(mylist)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2   # join the list
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

'''
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list

'''
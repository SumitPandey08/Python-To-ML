thisset = {"apple", "banana", "cherry"}  # unordered and unchangable
print(thisset)
thisset = {"apple", "banana", "cherry", True, 1, 2} # in set 1 and True are same value

print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0} # 0 and false are same too

print(thisset)

print(len(thisset))

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("banana" in thisset)

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")  # just add randomly

print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)  # update work to join them

print(thisset)

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
# thisset.update(mylist) 

thisset.update(mylist)

print(thisset)

sets = {"fmab" , "demonSlayer" , "H X H"}
tuples = ("naruto" , "Bleach" , "One Peice")
sets.update(tuples)
print(sets)  

thisset = {"apple", "banana", "cherry"}

thisset.remove("banana") #  If the item to remove does not exist, remove() will raise an error.

print(thisset)

thisset = {"apple", "banana", "cherry"}

thisset.discard("banana") # If the item to remove does not exist, discard() will NOT raise an error.

print(thisset)


thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x) #removed item

print(thisset) #the set after removal

thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


# join in Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)

print(set3)

# You can use the | operator instead of the union() method, and you will get the same result.

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

myset = set1 | set2 | set3 |set4
print(myset)

set1 = {"a", "b", "c"}  # just add the set2 in set1 without creating new variable
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)  # give the common value in both
print(set3)


# & also used for intersection

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)


set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2) # check set 1 on the basis of set 2 and return non similar value 
print(set3)

#You can use the - operator instead of the difference() method, and you will get the same result.

set3 =  set1 - set2
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2  # intersection remove and then join
print(set3)


'''
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
'''

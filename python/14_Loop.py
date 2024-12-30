# while loop

i = 0
while i < 10:
    print(i)
    i += 1

# using break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# using Continue

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Note that number 3 is missing in the result


# For Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

  
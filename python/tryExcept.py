def func():
    try:
        return 1/0
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    except Exception :
        return "Some thing is worg"

print(func())

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# Usage of Else

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

# Finally wil always occured no matter what
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# raise a error
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
  
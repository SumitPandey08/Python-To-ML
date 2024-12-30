def my_function():
  print("Hello from a function")

my_function()


def greeting(name) :
    print("Hello, " + name)
    
greeting("John")  # Outputs: Hello, John


# predefined argument
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def table(num) :
   i = 1 
   while i <= 10:
      print(f"{num} x {i} = {num * i}")
      i += 1

table(9)


    

x = "Hello World"

# Slice
print(x[0:5])  # Output: Hello

#for first para 0 is Default
print(x[:5]) # Output: Hello

# for 2nd length - 1 is default
print(x[0:]) # Output: Hello World

#  negative represent length from last
print(x[-5:-2]) # Output : Wor


# UppurCase and LowerCase
print(x.upper()) # Output: HELLO WORLD
print(x.lower()) # Output: hello world


# strip() remove white space from start and end
s = "  One Peice "
print(s.strip()) # Output: One Peice

# replace() use to replace value
print(s.replace("One", "Two")) # Output: Two Peice

#split() split or separate the string rom a point and make array
s = "One,Two,Three,Four,Five"
print(s.split(",")) # Output: ['One', 'Two', 'Three', 'Four', 'Five']

# conatation of string
print(x + " hello")

#format String
print("My name is {} and i am {} years old".format("John", 25))

#f is imp here
print(f"this is multipliaction insidea string 53 * 21 = {53*21}")
# Output: this is multipliaction insidea string 53 * 21 = 1113

price = 59
txt = f"The price is {price:.2f} dollars" #  is float and 2 represetn length after the decimal
print(txt)
# Output: The price is 59.00 dollars

# txt = "We are the so-called "Vikings" from the north." shows Error
txt = "We are the so-called \"Vikings\" \n from the north." # shows no
print(txt)
''' Output: We are the so-called "Vikings" 
from the north. '''
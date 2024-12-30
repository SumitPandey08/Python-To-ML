# creating a class

class Dog:
    def __init__(self , name): # initializing for a Class
        self.name = name 
        self.foots = 4 

    def speak(self):  #here we use a function
        print(self.name + "  !   Bark" )

myDog = Dog("Bruno")
anotherDog = Dog("Fluffy")
myDog.speak()
anotherDog.speak()


class SayIntro:
    def __init__(self, name , age , gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return (f"Hello, my name is {self.name} , I am a {self.gender} and I am {self.age}")


forBoy = SayIntro("Satyam" , "18" , "male")
forGirl = SayIntro('Saraswati' , '18' , 'female')

print(forBoy)
print(forGirl)
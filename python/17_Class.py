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



# work on super() and child class and Parent class

class Parent:
    def __init__(self, name, age , blood):
        self.name = name
        self.age = age
        self.blood = "O+" or blood

    def intro(self):
            return (f"Hello, my name is {self.name} , I am {self.age} and My blood group is {self.blood}")

class Child(Parent):
    def __init__(self, name, age, blood , sc):
        super().__init__(name, age, blood)


child = Child("Beta" , 18 , "" , "as" )
print(child.intro())




class Wordset :
    def __init__(self):
        self.words = set()

    def addText(self , text) :
        text = self.cleanText(text)
        for word in text.split():
            self.words.add(word)
    
    def cleanText(self , text) :
        text = text.replace("/", '').replace('!' , "").replace('.', ' ').replace(',', ' ').replace('?', ' ').replace(';', ' ').replace(':', ' ').replace('(', ' ').replace(')', ' ')
        return text.lower()


wordSet = Wordset()
wordSet.addText("Hello, my name is Satyam. I am a student.")
print(wordSet.words)
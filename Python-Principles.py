#Variables 
x = 2 #x is the variable and 2 is the string 
x == x + 5
print(x) 
 
#Strings
a = "abe"
b = "xyx"
z = a + b 
print(z)

#Functions 
def f(g):
    y = g+2
    return y 
print(f(5)) 
 
def f(x):
    43
    return x + 5
print(f(5))

def hello(first_name, last_name, age):
    print(f"Hello, have a good day {first_name} {last_name}!")
    print(f"You are {age} year old!")
hello("Nick", "Guerilla", 15)

#Keyword arguments (Functions)
def hello(first_word,middle_word,last_word):
    print(f"Hello {first_word} {middle_word} {last_word}.")
hello(first_word= "world", middle_word= "its a", last_word= "beautiful day")

#Lists
fruits = ["Apples", "Grapes", "Oranges", "Bananas"] 
print(fruits)  

#Lists
fruits = ["Apples", "Grapes", "Oranges", "Bananas"]
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
 
#Dictionaries
d = {'name': 'John', 'age': 30, 'city': 'New York'}
print(d)

#Tuples
t = ('John', 30, 'New York')
print(t)

#Sets
s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(s)

#Loops 
for i in range(1,10000):
   if i%2 == 0:
      print(i)  

#args
def add(*args):
    sum = 0 
    for i in args:
        sum += i
    return sum
print(add(1,2,3,4,5,6,7,8,9,10))

#kwargs
def play_with_toys(**kwargs):
    for toy_name, toy in kwargs.items():
        print("Playing with", toy_name, "toy!")
        # Do something fun with the toy

# Let's play with some toys!
play_with_toys(car="red", ball="blue", doll="pink")

#Object Oriented Programming (Declaring/Defining Classes)
class Vehicle:
    def __init__(self, color, model):
        self.color = color
        self.model = model
    
    def start(self):
        print(f"The {self.color} {self.model} has started.")
    
    def stop(self):
        print(f"The {self.color} {self.model} has stopped.")

car = Vehicle("red", "sedan")
car.start() # "The red sedan has started."
car.stop() # "The red sedan has stopped." 

#Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Meow!")

# Create instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the make_sound() method
animal.make_sound()  # Output: Animal sound
dog.make_sound()     # Output: Woof!
cat.make_sound()     # Output: Meow!

#-----------Multi-level Inheritance---------
class Prey:
    def hunted(self):
        print("This animal is being hunted!")

class Predator:
    def hunting(self):
        print("This animal is hunting another animal!")

class Rabbit(Prey):
    print("The Rabbit is the prey!")

class Hawk(Predator):
    print("The Hawk is the predator!")

class Fish(Prey, Predator):
    print("The Fish can be both the prey and predator!")

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
rabbit.hunted()
hawk.hunting()
fish.hunted()
fish.hunting()

#----------Method Overriding------------
class Animal:
    def make_sound(self):
        print("Animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

# Create instances of the classes
animal = Animal()
dog = Dog()

# Call the make_sound() method
animal.make_sound()  # Output: Animal sound
dog.make_sound()     # Output: Woof!

#-------Method Chaining-------
class Cake:
    def mix(self):
        print("Mixing ingredients...")
        return self

    def pour_into_pan(self):
        print("Pouring batter into a pan...")
        return self

    def bake(self):
        print("Baking the cake...")
        return self

    def add_frosting(self):
        print("Adding frosting...")
        return self

# Create an instance of the Cake class
my_cake = Cake()

# Use method chaining to perform the baking process
my_cake.mix().pour_into_pan().bake().add_frosting()
#------------------------------------------------#

#Abstract Method
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("You drive the car!")

    def stop(self):
        print("This car has stopped!")


class Motorcycle(Vehicle):
    def go(self):
        print("This motorcycle is driving!")

    def stop(self):
        print("This motorcycle has stopped!")

car = Car()
motor = Motorcycle()

car.go()
motor.go()
car.stop()
motor.stop()

#Objects as arguments 
class ToyCar:
    def drive(self):
        print("The toy car is driving!")
    
    def stop(self):
        print("The toy car has stopped!")

class ToyBall:
    def bounce(self):
        print("The toy ball is bouncing!")

    def roll(self):
        print("The toy ball is rolling!")

def play(car, ball):
    car.drive()
    car.stop()
    ball.bounce()
    ball.roll()

toy_car = ToyCar()
toy_ball = ToyBall()

play(toy_car, toy_ball)

#Duck Typing
class Duck:
    def walking(self):
        print("The duck is waddling around!")

    def talking(self):
        print("The duck is talking!")

class Chicken:
    def walking(self):
        print("The chicken is walking!")

    def talking(self):
        print("The chicken is clucking!")

class Person():
    def catching(self, duck):
        duck.walking()
        duck.talking()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catching(chicken)

#Walrus Operator
foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

#Threading
import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("I've eaten breakfast!")
#eat_breakfast()

def drink_coffee():
    time.sleep(4)
    print("I've drunken my coffee!")
#drink_coffee()

def study():
    time.sleep(5)
    print("I've studied!")
#study()

x = threading.Thread(target=eat_breakfast)
x.start()

y = threading.Thread(target=drink_coffee)
y.start()

z = threading.Thread(target=study)
z.start()

print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())

#Daemon threads
import threading
import time

def magical_train():
    for i in range(5):
        print("Choo-choo! The train is now moving!")
        time.sleep(1)
    print("This train has reached its destination. It's time to stop!")

train_thread = threading.Thread(target=magical_train)
train_thread.daemon = True
train_thread.start()

time.sleep(3)
print("The train station is now closing. This magical train is leaving very soon!!!")

#---------File Operations--------------
#File Detection
#For Files
import os 

path = "C:\\Users\\sharo\\Downloads\\test.txt"

if os.path.exists(path):
    print("File exists")
    if os.path.isfile(path):
        print("Its a file")
elif os.path.isdir(path):
    print("That's a directory!")
else:
    print("This location doesn't exist!")

#For Folders
path = "C:\\Users\\sharo\\Downloads\\"
if os.path.exists(path):
    print("File exists")
    if os.path.isdir(path):
        print("This folder exists!")
    else:
        print("This folder doesn't exist!")

#Read a file
with open("C:\\Users\\sharo\\Downloads\\text.txt") as file:
    print(file.read())

#Write a file
text = "Yooo\n This is Python text\n"
with open('text.txt','w') as file:
    file.write(text)

#Copy file
import os
os.system("copy C:\\Users\\sharo\\Downloads\\text.txt C:\\Users\\sharo\\Downloads\\text2.txt")

#Delete files
import os
path = "tesst.txt"
try:
    os.remove(path)
except FileNotFoundError:
    print("File not found!")

#Deletes folder with files
import shutil
shutil.rmtree("folder_path")

#Deletes folder
import os
os.rmdir("folder_path")
#------------------------------------

#Import modules
import messages as msg
def hello():
    print("Hi!")
def bye():
    print("Bye!")
msg.hello()
msg.bye()

print("hello world") 
first_word = "Good" 
middle_word = "Morning" 
last_word = "World"  
full_word = first_word + " " + middle_word + " " + last_word
print("The full word is: " +str(full_word)) 
Jesus = "alive"
print(Jesus)  
 
name = "Chris"
if name == "Bob" or "Tom" or "Mike":
  print("Access Denied")
if name == "Chris":
  print("Access Granted") 

#Variables 
x = 2 
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
 
#Lists
fruits = ["Apples", "Grapes", "Oranges", "Bananas"] 
print(fruits)  
 
#Loops 
for i in range(1,10000):
   if i%2 == 0:
      print(i)  

#Object Oriented 
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

#String manipulation
print("hello world!"[::-1]) # - reverses a string!
print("hello world!"[:-1:]) # - removes string letters/numbers
print("hello world"[-1::]) # - only displays a specfic letter/number in a string 


"""
#while True:
import random

password_length = 8

characters = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=[]{}|;':\",./<>?"

password = ""

for i in range(password_length):
    password += random.choice(characters)
print(password)

import calendar
year = 2023
month = 5
print(calendar.month(year, month))

Random module example
while True:
    import random 
    x = random.randint(1,6)
    y = random.random()
    print(y)
    myList = ["Rock", "Paper", "Scissors"]
    z = random.choice(myList)

    cards = [1,2,3,4,5,6,7,8,9,10,'a','b','c','d','e','f','g','h','i','j']

    random.shuffle(cards)
    print(cards)

"""

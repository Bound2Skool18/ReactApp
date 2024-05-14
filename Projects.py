#Rock, Paper, Scissors Game 
while True: 
    import random
    choices = ["Rock", "Paper", "Scissors"]
    player1 = input("Choose your hand Player 1:")
    player2 = random.choice(choices)

    while player1 not in choices:
        player1 = input("Incorrect choice!, try again Player 1!:")

    print("Player 1 chose: ", player1)
    print("Player 2 chose: ", player2) 

    if player1 == player2:
        print("Its a tie!!!")
    elif (player1 == "Scissors" and player2 == "Paper") or (player1 == "Rock" and player2 == "Paper") or (player1 == "Rock" or player2 == "Scissors"):
        print("You win player 1!!!")
    else: 
        print("You win Player 2!!!")

    play_again = input("Play again? Yes/No").lower()

    if play_again != "yes":
        break

    print("Thanks for playing!!!") 


#Timer
while True:
    import time
    minutes = int(input("Set your timer:"))
    seconds = minutes*60
    if minutes <= 1:
        print(f"Your timer has been set to {minutes} minute.")
    else:
        print(f"Your timer has been set to {minutes} minutes.")
    time.sleep(seconds)
    print("Don't forget!") 

#or
while True:
    import time
    print(f"Reminder set to: {minutes} minute.")
    minutes = int(input("Set your time till reminded:"))
    seconds = minutes*60
    time.sleep(seconds)
    print("Dont forget to remember!!!")


# Quiz program
score = 0
# Question 1
answer = input("What is the capital of France? \n(a) Paris\n(b) London\n(c) New York\n")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 2
answer = input("What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Mars\n")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 3
answer = input("What is the smallest country in the world?\n(a) Russia\n(b) Vatican City\n(c) China\n")
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

#Question 4
answer = input("What is 1+1?\n(a) 2\n(b) 5\n(c) 10\n")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

print("You got", score, "questions correct.")

#Calculator
while True:
    def add(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return num1 - num2

    def multiply(num1, num2):
        return num1 * num2

    def divide(num1, num2):
        return num1 / num2
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

    num1 = int(input("Enter your 1st number: "))
    num2 = int(input("Enter your 2nd number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = add(num1,num2)
    elif operation == "-":
        result = subtract(num1,num2)
    elif operation == "*":
        result = multiply(num1,num2)
    elif operation == "/":
        result = divide(num1,num2)
    print(result)


#Clock with GUI display
from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000,update)

window = Tk()

time_label = Label(window,font=("Calibri",50), fg="#00FF00",bg="black")
time_label.pack()

date_label = (Label(window,font=("Calibri",25)))
date_label.pack()

day_label = Label(window,font=("Calibri",25))
day_label.pack()

update()

window.mainloop()


#Bank
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

def deposit():
    while True:
        amount = input("Enter your deposit:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0!")
        else:
            print("Please enter a number!:")
    
    return amount

def get_number_of_lines():
    while True:
        lines = int(input(f"Enter the number of lines to bet on (1-{MAX_LINES}): "))
        if lines <= 0:
            print("Amount needs to be greater than 0!")
        elif lines > 3:
            print("Amount needs to be 3 or less!")
        else:
            return lines

def get_bet():
    while True:
        bet = int(input("Enter your bet?:"))
        if MIN_BET <= bet <= MAX_BET:
            break
        else:
            print(f"Bets must be between {MIN_BET} and {MAX_BET}!")
    return bet
get_bet()

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    print(f"Your balance is ${balance}.")
    print(f"Your have: {lines} lines.")
    print(f"You bet: ${bet} on {lines}")
main()

#Weather API
import requests

API_KEY = "65a63485b2b8250eafcafb56c8a4b896"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Choose your city:")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature_celsius = round(data["main"]["temp"] - 273.15, 2)
    temperature_fahrenheit = round((temperature_celsius * 9/5) + 32, 2)
    print("Weather: ", weather)
    print(f"Temperature: {temperature_fahrenheit}°F")
else:
    print("An error occurred!")

#Text Assistant
import datetime
import webbrowser

def greet():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "Good Morning! How can I assist you today?"
    elif 12 <= hour < 18:
        return "Good Afternoon! How can I assist you today?"
    else:
        return "Good Evening! How can I assist you today?"

def assistant(query):
    if 'hello' in query:
        return greet()

    elif 'time' in query:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print("Current time in 12-hour format:", current_time)

    elif 'date' in query:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."

    elif 'day' in query:
        current_day = datetime.datetime.now().strftime("%A")
        return f"Today is {current_day}."


    elif 'open' in query:
        url = query.split('open ')[-1]
        webbrowser.open_new_tab(f"https://www.google.com/search?q={url}")
        return f"Opening {url} in your web browser."
    
    elif 'anime' in query:
        url = query.split('open ')[-1]
        webbrowser.open_new_tab(f"https://hianime.to/home?source=pwa{url}")
        return f"Opening {url} in your web browser."
    
    elif 'google' in query:
        url = query.split('open ')[-1]
        webbrowser.open_new_tab(f"https://www.google.com/{url}")
        return f"Opening {url} in your web browser."

    else:
        return "I'm sorry, I don't understand that. Try again or ask another question:"

def main():
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Exiting the assistant...")
            break
        else:
            response = assistant(user_input)
            print("Assistant:", response)

if __name__ == "__main__":
    main()

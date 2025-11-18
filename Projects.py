# Rock, Paper, Scissors Game
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
    elif (
        (player1 == "Scissors" and player2 == "Paper")
        or (player1 == "Rock" and player2 == "Paper")
        or (player1 == "Rock" or player2 == "Scissors")
    ):
        print("You win player 1!!!")
    else:
        print("You win Player 2!!!")

    play_again = input("Play again? Yes/No").lower()

    if play_again != "yes":
        break

    print("Thanks for playing!!!")


# Timer
while True:
    import time

    minutes = int(input("Set your timer:"))
    seconds = minutes * 60
    if minutes <= 1:
        print(f"Your timer has been set to {minutes} minute.")
    else:
        print(f"Your timer has been set to {minutes} minutes.")
    time.sleep(seconds)
    print("Don't forget!")

# or
while True:
    import time

    print(f"Reminder set to: {minutes} minute.")
    minutes = int(input("Set your time till reminded:"))
    seconds = minutes * 60
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
answer = input(
    "What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Mars\n"
)
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 3
answer = input(
    "What is the smallest country in the world?\n(a) Russia\n(b) Vatican City\n(c) China\n"
)
if answer.lower() == "b":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

# Question 4
answer = input("What is 1+1?\n(a) 2\n(b) 5\n(c) 10\n")
if answer.lower() == "a":
    print("Correct!")
    score += 1
else:
    print("Incorrect.")

print("You got", score, "questions correct.")

# Calculator
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
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    print(result)


# Clock with GUI display
from tkinter import *
from time import *


def update():
    time_string = strftime("%I:%M:%S")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()

time_label = Label(window, font=("Calibri", 50), fg="#00FF00", bg="black")
time_label.pack()

date_label = Label(window, font=("Calibri", 25))
date_label.pack()

day_label = Label(window, font=("Calibri", 25))
day_label.pack()

update()

window.mainloop()


# Bank
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

# Weather API
import requests
import os
from dotenv import load_dotenv

# Load environment variables from a local .env file if present
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY", "")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Choose your city:")
if not API_KEY:
    print(
        "Missing OPENWEATHER_API_KEY. Create a .env file and set OPENWEATHER_API_KEY, or set it in your environment."
    )
else:
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        print(weather)
        temperature_celsius = round(data["main"]["temp"] - 273.15, 2)
        temperature_fahrenheit = round((temperature_celsius * 9 / 5) + 32, 2)
        print("Weather: ", weather)
        print(f"Temperature: {temperature_fahrenheit}°F")
    else:
        print("An error occurred!")

# Weather API with Tkinter
import tkinter as tk
from tkinter import messagebox
import requests

# Your API key and base URL (loaded from env; see section above)
API_KEY = os.getenv("OPENWEATHER_API_KEY", API_KEY if "API_KEY" in globals() else "")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


# Function to get weather data
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showerror("Input Error", "Please enter a city name.")
        return
    if not API_KEY:
        messagebox.showerror(
            "Configuration Error",
            "Missing OPENWEATHER_API_KEY. Create a .env file and set OPENWEATHER_API_KEY, or set it in your environment.",
        )
        return

    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temperature_celsius = round(data["main"]["temp"] - 273.15, 2)
        temperature_fahrenheit = round((temperature_celsius * 9 / 5) + 32, 2)

        weather_label.config(text=f"Weather: {weather}")
        temp_label.config(text=f"Temperature: {temperature_fahrenheit}°F")
    else:
        messagebox.showerror("Error", "An error occurred while fetching the data!")


# Create the main window
root = tk.Tk()
root.title("Weather App")

# Create and place the city input widgets
city_label = tk.Label(root, text="Choose your city:")
city_label.pack(pady=10)

city_entry = tk.Entry(root)
city_entry.pack(pady=5)

# Create and place the buttons and labels for displaying weather info
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

weather_label = tk.Label(root, text="")
weather_label.pack(pady=5)

temp_label = tk.Label(root, text="")
temp_label.pack(pady=5)

# Run the main event loop
root.mainloop()


# Text Assistant
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
    if "hello" in query:
        return greet()

    elif "time" in query:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        print("Current time in 12-hour format:", current_time)

    elif "date" in query:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."

    elif "day" in query:
        current_day = datetime.datetime.now().strftime("%A")
        return f"Today is {current_day}."

    elif "open" in query:
        url = query.split("open ")[-1]
        webbrowser.open_new_tab(f"https://www.google.com/search?q={url}")
        return f"Opening {url} in your web browser."

    elif "anime" in query:
        url = query.split("open ")[-1]
        webbrowser.open_new_tab(f"https://hianime.to/home?source=pwa{url}")
        return f"Opening {url} in your web browser."

    elif "google" in query:
        url = query.split("open ")[-1]
        webbrowser.open_new_tab(f"https://www.google.com/{url}")
        return f"Opening {url} in your web browser."

    else:
        return "I'm sorry, I don't understand that. Try again or ask another question:"


def main():
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Exiting the assistant...")
            break
        else:
            response = assistant(user_input)
            print("Assistant:", response)


if __name__ == "__main__":
    main()

# Mini Web Scraper
import pandas as pd

# Read all tables from the Wikipedia page
tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")

# Check the number of tables read
print(f"Number of tables found: {len(tables)}")

# Access and print the first two tables if they exist
if len(tables) > 0:
    print("First table:")
    print(tables[0])
else:
    print("No tables found.")

if len(tables) > 1:
    print("Second table:")
    print(tables[1])
else:
    print("Less than two tables found.")

# Video Splitter (Visual Studio Code Ver. (AI))
import os

# Set the IMAGEIO_FFMPEG_EXE environment variable to the path of the ffmpeg executable
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"  # macOS example
# os.environ["IMAGEIO_FFMPEG_EXE"] = r"C:\ffmpeg\bin\ffmpeg.exe"  # Windows example

from moviepy.video.io.VideoFileClip import VideoFileClip


def split_video(video_path, clip_duration):
    # Load the video
    video = VideoFileClip(video_path)

    # Get the video duration in seconds
    video_duration = int(video.duration)

    # Extract the directory, file name, and extension from the video path
    directory, file_name = os.path.split(video_path)
    file_base, file_extension = os.path.splitext(file_name)

    # Loop through the video and create clips
    for start_time in range(0, video_duration, clip_duration):
        end_time = min(start_time + clip_duration, video_duration)
        clip = video.subclip(start_time, end_time)
        clip_name = f"{file_base}_clip_{start_time}_{end_time}{file_extension}"
        clip_path = os.path.join(directory, clip_name)

        # Write the clip to a file
        clip.write_videofile(clip_path, codec="libx264", audio_codec="aac")

    print("Video splitting complete.")


if __name__ == "__main__":
    # Example usage
    video_path = "lifefacts.mp4"  # Replace with your video file path
    clip_duration = 20  # Set the desired clip duration in seconds (20 or 30)

    split_video(video_path, clip_duration)

# Video Splitter (Replit Ver. AI)
import os
from moviepy.video.io.VideoFileClip import VideoFileClip

# Set the IMAGEIO_FFMPEG_EXE environment variable to the path of the ffmpeg executable
# Adjust the path according to your system
os.environ["IMAGEIO_FFMPEG_EXE"] = "/opt/homebrew/bin/ffmpeg"  # macOS example
# os.environ["IMAGEIO_FFMPEG_EXE"] = r"C:\ffmpeg\bin\ffmpeg.exe"  # Windows example


def split_video(video_path, clip_duration):
    # Load the video
    video = VideoFileClip(video_path)

    # Get the video duration in seconds
    video_duration = int(video.duration)

    # Extract the directory, file name, and extension from the video path
    directory, file_name = os.path.split(video_path)
    file_base, file_extension = os.path.splitext(file_name)

    # Loop through the video and create clips
    for start_time in range(0, video_duration, clip_duration):
        end_time = min(start_time + clip_duration, video_duration)
        clip = video.subclip(start_time, end_time)
        clip_name = f"{file_base}_clip_{start_time}_{end_time}{file_extension}"
        clip_path = os.path.join(directory, clip_name)

        # Write the clip to a file
        clip.write_videofile(clip_path, codec="libx264", audio_codec="aac")

    print("Video splitting complete.")


if __name__ == "__main__":
    # Example usage
    video_path = "lifefacts.mp4"  # Replace with your video file path
    clip_duration = 20  # Set the desired clip duration in seconds (20 or 30)

    split_video(video_path, clip_duration)

# Quiz App for PHP Programming I
import tkinter as tk
from tkinter import messagebox

# List of questions with explanations for both correct and incorrect answers
questions = [
    {
        "question": "What does the Model in the MVC pattern consist of?",
        "options": [
            "PHP files representing the data",
            "HTML files for user interface",
            "Files for handling requests",
        ],
        "answer": "PHP files representing the data",
        "explanation": {
            "PHP files representing the data": "The model in MVC handles the data of the application.",
            "HTML files for user interface": "The view represents the user interface, not the model.",
            "Files for handling requests": "The controller handles the requests, not the model.",
        },
    },
    {
        "question": "What is used to redirect a request to another URL in PHP?",
        "options": ["include()", "header()", "forward()"],
        "answer": "header()",
        "explanation": {
            "include()": "The include() function is used to include PHP files, not to redirect URLs.",
            "header()": "The header() function is used for URL redirection.",
            "forward()": "There's no such function as forward() in PHP for URL redirection.",
        },
    },
    {
        "question": "What pattern helps prevent resubmission of POST data?",
        "options": ["MVC", "PRG", "DRY"],
        "answer": "PRG",
        "explanation": {
            "MVC": "MVC is an architectural pattern, not used for preventing POST resubmission.",
            "PRG": "The PRG (Post-Redirect-Get) pattern is used to prevent resubmission of POST data.",
            "DRY": "DRY refers to the principle of 'Don’t Repeat Yourself', not for POST data handling.",
        },
    },
    {
        "question": "What should you do to avoid duplicating code in multiple parts of an application?",
        "options": ["Use the DRY principle", "Refactor the code", "Use MVC pattern"],
        "answer": "Use the DRY principle",
        "explanation": {
            "Use the DRY principle": "DRY stands for 'Don’t Repeat Yourself', which helps avoid code duplication.",
            "Refactor the code": "Refactoring can help clean up code, but it doesn't specifically avoid duplication.",
            "Use MVC pattern": "MVC is a design pattern, not directly related to avoiding code duplication.",
        },
    },
    {
        "question": "What should you do to make a variable available inside a function?",
        "options": [
            "Use a return statement",
            "Use the global keyword",
            "Use an argument list",
        ],
        "answer": "Use the global keyword",
        "explanation": {
            "Use a return statement": "A return statement sends data back, but it doesn't make the variable available inside the function.",
            "Use the global keyword": "The global keyword makes an outside variable available inside a function.",
            "Use an argument list": "The argument list passes values into a function, not to make a variable accessible globally.",
        },
    },
    {
        "question": "What is refactoring in programming?",
        "options": [
            "Redesigning the user interface",
            "Modifying the structure of the application",
            "Changing the programming language",
        ],
        "answer": "Modifying the structure of the application",
        "explanation": {
            "Redesigning the user interface": "Refactoring isn't related to the user interface; it focuses on internal code structure.",
            "Modifying the structure of the application": "Refactoring means improving or modifying the structure of the code without changing its functionality.",
            "Changing the programming language": "Refactoring isn't about changing languages; it's about improving the organization of the code.",
        },
    },
    {
        "question": "What is required when calling a function?",
        "options": [
            "Compatible arguments in the same order as parameters",
            "A global variable",
            "A return statement",
        ],
        "answer": "Compatible arguments in the same order as parameters",
        "explanation": {
            "Compatible arguments in the same order as parameters": "When calling a function, the arguments must match the parameters in order and type.",
            "A global variable": "Global variables are separate from function calls and not required to call a function.",
            "A return statement": "A return statement is used within a function, not when calling a function.",
        },
    },
    {
        "question": "What does the controller in MVC handle?",
        "options": [
            "Requests and returning views",
            "Data storage",
            "User interface layout",
        ],
        "answer": "Requests and returning views",
        "explanation": {
            "Requests and returning views": "The controller handles requests, interacts with the model, and returns views.",
            "Data storage": "Data storage is the responsibility of the model, not the controller.",
            "User interface layout": "The user interface layout is part of the view, not the controller.",
        },
    },
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiple Choice Flashcard Quiz")
        self.root.geometry("500x400")
        self.question_index = 0
        self.correct_score = 0
        self.wrong_score = 0

        # Display question and options
        self.question_label = tk.Label(
            root, text="", font=("Arial", 25), wraplength=450
        )
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.radio_buttons = []
        for i in range(3):
            radio_button = tk.Radiobutton(
                root, text="", variable=self.var, value="", font=("Arial", 25)
            )
            radio_button.pack(anchor="w")
            self.radio_buttons.append(radio_button)

        # Buttons for next question and score
        self.submit_button = tk.Button(
            root,
            text="Submit",
            command=self.submit_answer,
            font=("Arial", 25),
            bg="lightblue",
        )
        self.submit_button.pack(pady=20)

        # Feedback from Right/Wrong Answer
        self.feedback_label = tk.Label(root, text="", font=("Arial", 20))
        self.feedback_label.pack()

        # Button for next question
        self.next_button = tk.Button(
            root,
            text="Next",
            command=self.next_question,
            state=tk.DISABLED,
            font=("Arial", 25),
            bg="lightgreen",
        )
        self.next_button.pack(pady=10)

        # Button for trying again after finishing
        self.try_again_button = tk.Button(
            root,
            text="Try Again",
            command=self.reset_quiz,
            state=tk.DISABLED,
            font=("Arial", 25),
            bg="lightyellow",
        )
        self.try_again_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        # Get current question and options
        current_question = questions[self.question_index]
        self.question_label.config(text=current_question["question"])
        self.var.set(None)

        # Display options as radio buttons
        for i, option in enumerate(current_question["options"]):
            self.radio_buttons[i].config(text=option, value=option)

        self.feedback_label.config(text="")
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def submit_answer(self):
        selected_answer = self.var.get()
        if selected_answer == "":
            messagebox.showwarning("No Answer", "Please select an answer!")
            return

        current_question = questions[self.question_index]
        explanation = current_question["explanation"][selected_answer]

        # Check if the answer is correct
        if selected_answer == current_question["answer"]:
            self.correct_score += 1
            self.feedback_label.config(text=f"Correct! {explanation}", fg="green")
            self.submit_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.NORMAL)
        else:
            self.wrong_score += 1
            self.feedback_label.config(text=f"Wrong! {explanation}", fg="red")
            # Keep the submit button active so the user can try again

    def next_question(self):
        self.question_index += 1
        if self.question_index < len(questions):
            self.show_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        self.question_label.config(
            text=f"Quiz Over! You got {self.correct_score} correct and {self.wrong_score} wrong."
        )
        self.feedback_label.config(text="")
        for radio_button in self.radio_buttons:
            radio_button.pack_forget()
        self.submit_button.pack_forget()
        self.next_button.pack_forget()
        self.try_again_button.config(state=tk.NORMAL)

    def reset_quiz(self):
        # Reset all the quiz data and UI
        self.question_index = 0
        self.correct_score = 0
        self.wrong_score = 0
        for radio_button in self.radio_buttons:
            radio_button.pack(anchor="w")
        self.submit_button.pack(pady=20)
        self.try_again_button.config(state=tk.DISABLED)
        self.show_question()


# Initialize tkinter
root = tk.Tk()
quiz_app = QuizApp(root)
root.mainloop()

import tkinter as tk
from tkinter import messagebox

# List of questions with explanations for both correct and incorrect answers
questions = [
    {
        "question": "Which of the following reside at the physical layer of the OSI model? (Select 3 answers)",
        "options": [
            "IP address",
            "Network switch",
            "Hub",
            "Router",
            "Network cabling",
            "Ethernet frame",
            "Repeater",
        ],
        "answer": ["Hub", "Network cabling", "Repeater"],
        "explanation": "IP address, Network switch, and Router are not physical layer devices.",
    },
    {
        "question": "What are the characteristic components of the OSI data link layer? (Select 3 answers)",
        "options": [
            "MAC address",
            "IP packet",
            "Network switch",
            "Router",
            "Network cabling",
            "Ethernet frame",
        ],
        "answer": ["MAC address", "Network switch", "Ethernet frame"],
        "explanation": "IP packet, Router, and Network cabling are not specific to the data link layer.",
    },
    {
        "question": "Which of the following devices forward frames between network segments?",
        "options": ["Hub", "Switch", "Firewall", "Router"],
        "answer": ["Switch"],
        "explanation": "Hub broadcasts all data, while a Switch forwards frames intelligently based on MAC addresses.",
    },
    {
        "question": "Which of the following refer to OSI network layer components? (Select 3 answers)",
        "options": [
            "Router",
            "Ethernet frame",
            "IP address",
            "TCP/UDP protocols",
            "Packet",
            "Network switch",
        ],
        "answer": ["Router", "IP address", "Packet"],
        "explanation": "Ethernet frames are data link layer, TCP/UDP are transport layer, and Network switch operates at data link.",
    },
    {
        "question": "What is the name of a network layer protocol that specifies the format of packets?",
        "options": ["UDP", "IP", "TCP", "NetBIOS"],
        "answer": ["IP"],
        "explanation": "IP is the protocol that defines packet structure and addressing in the network layer.",
    },
    {
        "question": "Layer 4 of the OSI model is also known as:",
        "options": [
            "Network layer",
            "Data link layer",
            "Session layer",
            "Transport layer",
        ],
        "answer": ["Transport layer"],
        "explanation": "Transport layer (Layer 4) is responsible for reliable data transfer and flow control.",
    },
    {
        "question": "Which OSI layer maintains connections between applications?",
        "options": [
            "Network layer",
            "Data link layer",
            "Application layer",
            "Session layer",
        ],
        "answer": ["Session layer"],
        "explanation": "Session layer is responsible for establishing, maintaining, and terminating sessions.",
    },
    {
        "question": "Authentication and authorization take place at the:",
        "options": [
            "Application layer",
            "Network layer",
            "Session layer",
            "Presentation layer",
        ],
        "answer": ["Application layer"],
        "explanation": "The Application layer handles user authentication and authorization processes.",
    },
    {
        "question": "Layer 5 of the OSI model is also referred to as:",
        "options": [
            "Session layer",
            "Application layer",
            "Transport layer",
            "Presentation layer",
        ],
        "answer": ["Session layer"],
        "explanation": "Layer 5 is specifically known as the Session layer.",
    },
    {
        "question": "Data format translation and encryption take place at the:",
        "options": [
            "Application layer",
            "Presentation layer",
            "Session layer",
            "Transport layer",
        ],
        "answer": ["Presentation layer"],
        "explanation": "The Presentation layer formats and encrypts data for the application layer.",
    },
    {
        "question": "Which of the following protocols reside at the application layer? (Select all that apply)",
        "options": ["ATM", "HTTP", "FTP", "IP", "SMTP", "TCP/UDP"],
        "answer": ["HTTP", "FTP", "SMTP"],
        "explanation": "ATM is a data link layer protocol, while IP and TCP/UDP are lower layer protocols.",
    },
    {
        "question": "In the OSI model, the physical layer PDU is known as:",
        "options": ["Bit", "Frame", "Packet", "Segment", "Datagram"],
        "answer": ["Bit"],
        "explanation": "The Physical layer's Protocol Data Unit (PDU) is referred to as bits.",
    },
    {
        "question": "In the OSI model, the layer 2 PDU is called:",
        "options": ["Bit", "Frame", "Packet", "Segment", "Datagram"],
        "answer": ["Frame"],
        "explanation": "The Data Link layer's PDU is known as a frame.",
    },
    {
        "question": "Which of the following refers to OSI layer 2 header data? (Select 2 answers)",
        "options": [
            "Destination port number",
            "Source MAC address",
            "Destination MAC address",
            "Source port number",
        ],
        "answer": ["Source MAC address", "Destination MAC address"],
        "explanation": "Port numbers are not part of the Data Link layer header.",
    },
    {
        "question": "In the OSI model, the layer 3 PDU is known as:",
        "options": ["Bit", "Frame", "Packet", "Segment", "Datagram"],
        "answer": ["Packet"],
        "explanation": "The Network layer's PDU is referred to as a packet.",
    },
    {
        "question": "Which of the following refer to examples of network layer header data? (Select 2 answers)",
        "options": [
            "Source IP address",
            "Destination IP address",
            "Source port number",
            "Destination port number",
        ],
        "answer": ["Source IP address", "Destination IP address"],
        "explanation": "Port numbers are part of the Transport layer, not the Network layer.",
    },
    {
        "question": "User Datagram Protocol (UDP) is a connection-oriented protocol.",
        "options": ["True", "False"],
        "answer": ["False"],
        "explanation": "UDP is a connectionless protocol that does not establish a connection before sending data.",
    },
    {
        "question": "Transmission Control Protocol (TCP) is an example of a connectionless protocol.",
        "options": ["True", "False"],
        "answer": ["False"],
        "explanation": "TCP is a connection-oriented protocol that uses a three-way handshake to establish a connection.",
    },
    {
        "question": "Which of the following protocols reside at the OSI transport layer? (Select 2 answers)",
        "options": ["UDP", "IP", "SSL/TLS", "ICMP", "TCP", "ATM"],
        "answer": ["UDP", "TCP"],
        "explanation": "UDP and TCP are both transport layer protocols; others are in different layers.",
    },
    {
        "question": "Which OSI layer is known as Layer 3?",
        "options": [
            "Network layer",
            "Data link layer",
            "Session layer",
            "Transport layer",
        ],
        "answer": ["Network layer"],
        "explanation": "Layer 3 is specifically the Network layer.",
    },
    {
        "question": "In the OSI model, the layer 4 PDU is known as:",
        "options": ["Bit", "Frame", "Packet", "Segment", "Datagram"],
        "answer": ["Segment"],
        "explanation": "The Transport layer's PDU is called a segment.",
    },
    {
        "question": "Which of the following protocols reside at the OSI transport layer? (Select 2 answers)",
        "options": ["UDP", "TCP", "ICMP", "SMTP", "HTTP"],
        "answer": ["UDP", "TCP"],
        "explanation": "UDP and TCP are transport layer protocols; ICMP, SMTP, and HTTP are not.",
    },
    {
        "question": "Which OSI layer is responsible for reliable communication?",
        "options": [
            "Physical layer",
            "Data link layer",
            "Transport layer",
            "Application layer",
        ],
        "answer": ["Transport layer"],
        "explanation": "The Transport layer ensures reliable data transfer and error recovery.",
    },
    {
        "question": "Which layer is responsible for establishing, maintaining, and terminating sessions?",
        "options": [
            "Transport layer",
            "Session layer",
            "Network layer",
            "Application layer",
        ],
        "answer": ["Session layer"],
        "explanation": "The Session layer manages sessions between applications.",
    },
    {
        "question": "The encapsulation process at the OSI model involves adding headers and trailers as data moves down the layers.",
        "options": ["True", "False"],
        "answer": ["True"],
        "explanation": "Data encapsulation is crucial in the OSI model for adding headers at each layer.",
    },
    {
        "question": "Which of the following terms refers to the OSI presentation layer?",
        "options": ["Layer 6", "Layer 5", "Layer 4", "Layer 3"],
        "answer": ["Layer 6"],
        "explanation": "The Presentation layer is referred to as Layer 6 in the OSI model.",
    },
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Multiple Choice Flashcard Quiz")
        self.root.geometry("500x400")
        self.question_index = 0
        self.correct_score = 0
        self.wrong_score = 0

        # Display question and options
        self.question_label = tk.Label(
            root, text="", font=("Arial", 25), wraplength=450
        )
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.radio_buttons = []
        for i in range(7):  # Adjust for maximum options
            radio_button = tk.Radiobutton(
                root, text="", variable=self.var, value="", font=("Arial", 25)
            )
            radio_button.pack(anchor="w")
            self.radio_buttons.append(radio_button)

        # Buttons for next question and score
        self.submit_button = tk.Button(
            root,
            text="Submit",
            command=self.submit_answer,
            font=("Arial", 25),
            bg="lightblue",
        )
        self.submit_button.pack(pady=20)

        # Feedback from Right/Wrong Answer
        self.feedback_label = tk.Label(root, text="", font=("Arial", 20))
        self.feedback_label.pack()

        # Button for next question
        self.next_button = tk.Button(
            root,
            text="Next",
            command=self.next_question,
            state=tk.DISABLED,
            font=("Arial", 25),
            bg="lightgreen",
        )
        self.next_button.pack(pady=10)

        # Button for trying again after finishing
        self.try_again_button = tk.Button(
            root,
            text="Try Again",
            command=self.reset_quiz,
            state=tk.DISABLED,
            font=("Arial", 25),
            bg="lightyellow",
        )
        self.try_again_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        # Get current question and options
        current_question = questions[self.question_index]
        self.question_label.config(text=current_question["question"])
        self.var.set(None)

        # Display options as radio buttons
        for i, option in enumerate(current_question["options"]):
            self.radio_buttons[i].config(text=option, value=option)
            self.radio_buttons[i].pack(anchor="w")  # Ensure radio buttons are visible

        # Hide any unused radio buttons
        for j in range(len(current_question["options"]), len(self.radio_buttons)):
            self.radio_buttons[j].pack_forget()

        self.feedback_label.config(text="")
        self.submit_button.config(state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def submit_answer(self):
        selected_answer = self.var.get()
        if selected_answer == "":
            messagebox.showwarning("No Answer", "Please select an answer!")
            return

        current_question = questions[self.question_index]
        explanation = current_question["explanation"]

        # Check if the answer is correct
        if selected_answer in current_question["answer"]:
            self.correct_score += 1
            self.feedback_label.config(text=f"Correct! {explanation}", fg="green")
            self.submit_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.NORMAL)
        else:
            self.wrong_score += 1
            self.feedback_label.config(text=f"Wrong! {explanation}", fg="red")
            self.submit_button.config(state=tk.DISABLED)
            self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.question_index += 1
        if self.question_index < len(questions):
            self.show_question()
        else:
            self.show_final_score()

    def show_final_score(self):
        self.question_label.config(
            text=f"Quiz Over! You got {self.correct_score} correct and {self.wrong_score} wrong."
        )
        self.feedback_label.config(text="")
        for radio_button in self.radio_buttons:
            radio_button.pack_forget()
        self.submit_button.pack_forget()
        self.next_button.pack_forget()
        self.try_again_button.config(state=tk.NORMAL)

    def reset_quiz(self):
        # Reset all the quiz data and UI
        self.question_index = 0
        self.correct_score = 0
        self.wrong_score = 0
        self.show_question()
        for button in self.radio_buttons:
            button.pack(anchor="w")
        self.submit_button.pack(pady=20)
        self.try_again_button.config(state=tk.DISABLED)


# Initialize tkinter
root = tk.Tk()
quiz_app = QuizApp(root)
root.mainloop()

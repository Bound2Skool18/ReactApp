import datetime
import random
import webbrowser
import wikipedia

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

    elif 'wikipedia' in query:
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        return f"According to Wikipedia: {result}"

    elif 'open' in query:
        url = query.split('open ')[-1]
        webbrowser.open_new_tab(f"https://www.google.com/search?q={url}")
        return f"Opening {url} in your web browser."

    else:
        return "I'm sorry, I don't understand that. Can you please ask something else?"

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

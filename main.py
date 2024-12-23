"""
Program Instructions:

This program is a voice-activated personal assistant that performs the following tasks:
1. Speak "Time" to know the current time:
   - The assistant will speak out the current time in HH:MM AM/PM format.

2. Speak "News" to know the top 5 latest news:
   - The assistant fetches the top 5 news headlines using a News API. 
   - To activate this feature, go to "https://newsapi.org/" and get your API key.
   - Paste the API key in the `News_Api_Key` variable at Line 12.

3. Speak "Reminder" to set a reminder:
   - The assistant will prompt you for the reminder name and time.
   - Enter the time in the command line in HH:MM format (24-hour format).
   - At the specified time, the reminder will be spoken aloud.

4. Speak "Exit" to end the program:
   - The program will terminate upon hearing this command.

Setup Instructions:
1. API Keys:
   - Weather API Key: Get your API key from "https://openweathermap.org/" and paste it in the `Weather_Api_Key` variable at Line 11.
   - News API Key: Get your API key from "https://newsapi.org/" and paste it in the `News_Api_Key` variable at Line 12.

2. Install Required Modules:
   Run the following command in your terminal to install the required Python modules:
   Command: pip install SpeechRecognition pyttsx3 requests

Note: This program uses free APIs for fetching weather and news. Make sure your API keys are valid and active.
"""

import speech_recognition as sr
import pyttsx3
import requests
from datetime import datetime
from threading import Thread, Lock
import time

# Api Keys
Weather_Api_Key = "Enter_Your_KEY"
News_Api_Key = "Enter_Your_KEY"

# Initialize text-to-speech engine and lock
engine = pyttsx3.init()
engine_lock = Lock()
engine.setProperty('rate', 150)

# Global reminder list
reminders = []

# Speak function
def speak(text):
    with engine_lock:
        engine.say(text)
        engine.runAndWait()

# Recognize speech function
def recognize_speech(prompt="", mode = ""):
    if prompt:
        speak(prompt)
    if mode == "SR":
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            try:
                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                return command
            except:
                speak("Sorry, I couldn't understand. Please try again.")
                return None
    else:
        return input("Enter Command: ").lower()

# Fetch weather data
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={Weather_Api_Key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            return "City not found. Please try again."
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        return f"The weather in {city} is {desc} with a temperature of {temp}°C."
    except:
        return "Unable to fetch weather data at the moment."

# Fetch news headlines using web scraping
def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={News_Api_Key}"
    try:
        response = requests.get(url)
        articles = response.json().get("articles", [])[:5]
        if not articles:
            return "No news available."
        news_list = [f"{i+1}. {article['title']}" for i, article in enumerate(articles)]
        return "\n".join(news_list)
    except:
        return "Unable to fetch news at the moment."

# Add reminder
def add_reminder(task, remind_time):
    reminders.append({"task": task, "time": remind_time})
    speak(f"Reminder set for {task} at {remind_time}.")

# Check reminders continuously
def check_reminders():
    while True:
        now = datetime.now().strftime("%H:%M")
        for reminder in reminders[:]:
            if reminder["time"] == now:
                speak(f"Reminder: {reminder['task']}")
                reminders.remove(reminder)
        time.sleep(30)

# Main assistant logic
def personal_assistant():
    speak("Hello! How can I assist you today?")
    while True:
        command = recognize_speech()
        if not command:
            continue
        if "weather" in command:
            city = recognize_speech("Which city's weather would you like to know?")
            if city:
                weather_info = get_weather(city)
                speak(weather_info)
        elif "news" in command:
            speak("Fetching the latest news.")
            news = get_news()
            print(news)
            speak(news)
        elif "reminder" in command:
            task = recognize_speech("What should I remind you about?")
            speak("Please Enter the time? it should be in HH:MM format.")
            time_input = input("Enter Time in HH:MM format (eg. 20:08): ")
            try:
                datetime.strptime(time_input, "%H:%M")  # Validate time format
                add_reminder(task, time_input)
            except ValueError:
                speak("Invalid time format. Please try again.")
        elif "time" in command:
            current_time = datetime.now().strftime("%H:%M")
            speak(f"The current time is {current_time}.")
        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a nice day!")
            break
        else:
            speak("Sorry, I didn't understand that command.")

# Run the assistant
if __name__ == "__main__":
    # Start the reminder checker in the background
    reminder_thread = Thread(target=check_reminders, daemon=True)
    reminder_thread.start()

    # Start the personal assistant
    personal_assistant()

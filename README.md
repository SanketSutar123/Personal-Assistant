# Voice-Activated Personal Assistant

This project is a **Voice-Activated Personal Assistant** created during my internship at **CodexIntern**. The assistant can perform various tasks based on voice commands, such as providing the current time, fetching the latest news, setting reminders, and ending the program.

---

## Features
1. **Time**: Speak "Time" to know the current time in HH:MM AM/PM format.
2. **News**: Speak "News" to fetch the top 5 latest news headlines using the News API.
3. **Reminder**: Speak "Reminder" to set a reminder. The assistant will ask for the reminder name and time (in HH:MM format) and remind you at the specified time.
4. **Exit**: Speak "Exit" to end the program.

---

## Setup Instructions
### 1. API Keys
Before running the program, you need to set up API keys for weather and news services:

- **Weather API Key**: Go to [OpenWeatherMap](https://openweathermap.org/) and get your API key. Paste it in the `Weather_Api_Key` variable at Line 11 of the code.
- **News API Key**: Go to [NewsAPI](https://newsapi.org/) and get your API key. Paste it in the `News_Api_Key` variable at Line 12 of the code.

### 2. Install Required Modules
Run the following command in your terminal to install the required Python modules:
Command: pip install SpeechRecognition pyttsx3 requests

### Run the main Python file:
Command: python main.py

### Speak one of the following commands:

- **"Time"** to know the current time.
- **"News"** to get the latest news headlines.
- **"Reminder"** to set a reminder.
- **"Exit"** to end the program.

### Example Commands
1. **"Time"**: Output: The assistant will speak the current time, e.g., "The current time is 20:30"
2. **"News"**: Output: The assistant will speak out the top 5 latest news headlines.
3. **"Reminder"**: Output: The assistant will ask you to set a reminder and speak the reminder aloud at the specified time.
4. **"Exit"**: Output: The program will terminate.


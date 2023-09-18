import requests
import json
import pyttsx3

# Function to speak the provided text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=161c3eb2a02443c09bf172949231809&q={city}"

r = requests.get(url)#This line uses the requests.get() method to send an HTTP GET request to the URL constructed above.
# The response is stored in the variable r.

if r.status_code == 200:#response code 200 means OK
    data = r.json()
    temperature = data['current']['temp_c']
    print(f"The temperature in {city} is {temperature}°C.")
    speak(f"The temperature in {city} is {temperature} degrees Celsius.")
else:
    print("Failed to retrieve weather data. HTTP status code:", r.status_code)
    speak("Failed to retrieve weather data.")

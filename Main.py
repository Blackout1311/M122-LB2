import requests

API_KEY = "PASTE YOUR API CODE HERE"
city = input("Hallo! Bitte gib eine Stadt ein.")

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=1156afb1ccaf38803781a34203a1daca&units=metric'
data = requests.get(url).json()
temp = data['main']['temp']
humidity = data['main']['humidity']

print(f'In {city} beträgt die Temperatur {temp}. Die Luftfeuchtigkeit beträgt {humidity}.')
import requests
import json
from urllib.request import urlopen

API_KEY = "1156afb1ccaf38803781a34203a1daca"


def getcity():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    city = json.load(response)['region']
    return city


url = f'https://api.openweathermap.org/data/2.5/weather?q={getcity()}&appid={API_KEY}&units=metric'
data = requests.get(url).json()
temp = data['main']['temp']
humidity = data['main']['humidity']

print(f'In {getcity()} beträgt die Temperatur {temp}°. Die Luftfeuchtigkeit beträgt {humidity}.')

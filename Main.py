import requests
import json
from urllib.request import urlopen
import yagmail
import webbrowser
import time

API_KEY = "1156afb1ccaf38803781a34203a1daca"


def getcity():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    city = json.load(response)['region']
    return city



user = 'mikka.widmer.06@gmail.com'
app_password = 'cwxfiatasaasahxl' # a token for gmail
to = 'mikka.widmer.06@gmail.com'

url = f'https://api.openweathermap.org/data/2.5/weather?q={getcity()}&appid={API_KEY}&units=metric'
data = requests.get(url).json()
temp = data['main']['temp']
humidity = data['main']['humidity']



print(f'In {getcity()} beträgt die Temperatur {temp}°. Die Luftfeuchtigkeit beträgt {humidity}%.')

subject = 'Weather'
content = [f'In {getcity()} beträgt die Temperatur {temp}°. Die Luftfeuchtigkeit beträgt {humidity}%.']

html_content = f"<html> <head> </head> <h1>{content}</h1> <body> </body> </html>"

with open("index.html", "w")as html_file:
    html_file.write(html_content)
    print("html file was created successfully")

with yagmail.SMTP(user, app_password) as yag:
    yag.send(to, subject, content)
    print('Sent email successfully')


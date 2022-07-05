import requests
import json
from urllib.request import urlopen
import yagmail
from fpdf import FPDF
from datetime import date
from ftplib import FTP

API_KEY = "1156afb1ccaf38803781a34203a1daca"


def getcity():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    city = json.load(response)['region']
    return city


user = 'mikka.widmer.06@gmail.com'
app_password = 'cwxfiatasaasahxl'  # a token for gmail
to = 'mikka.widmer.06@gmail.com'

url = f'https://api.openweathermap.org/data/2.5/weather?q={getcity()}&appid={API_KEY}&units=metric'
data = requests.get(url).json()
temp = data['main']['temp']
humidity = data['main']['humidity']

ftp = FTP('mikkawidmer.bplaced.net')
ftp.login(user='mikkawidmer', passwd='M!kka2006')
ftp.cwd('\www')

print(f'In {getcity()} beträgt die Temperatur {temp}°. Die Luftfeuchtigkeit beträgt {humidity}%.')

subject = 'Weather'
content = f'In {getcity()} beträgt die Temperatur {temp}°. Die Luftfeuchtigkeit beträgt {humidity}%.'

today = date.today()
print("Today's date:", today)

if (temp > 20):
    image = 'sunny.png'
elif (temp > 0):
    image = 'cloud.png'
elif (temp < 0):
    image = 'snow.png'




def createPdf(content, today, image):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(f'{image}', x=75, y=50, w=60)
    pdf.set_font("Arial", size=11)
    pdf.set_text_color(0, 0, 0)
    pdf.text(50, 50, txt=f'{content}')
    pdf.output(f'wheater{today}.pdf')
    return f'wheater{today}.pdf'


def grabFile():
    filename = 'index.html'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()

def placeFile():
    filename = 'index.html'
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

with yagmail.SMTP(user, app_password) as yag:
    #yag.send(to, subject, createPdf(content, today, image))
    print('Sent email successfully')

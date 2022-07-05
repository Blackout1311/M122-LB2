import ftplib
import json
from datetime import date
from urllib.request import urlopen
import requests
import yagmail
from fpdf import FPDF

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

zuhause = 'einsiedeln'
url = f'https://api.openweathermap.org/data/2.5/weather?q={zuhause}&appid={API_KEY}&units=metric'
data = requests.get(url).json()
temphome = data['main']['temp']
humidityhome = data['main']['humidity']

subject = 'Weather'
content = f'In {getcity()} beträgt die Temperatur {temp}°. Die Luftfeuchtigkeit beträgt {humidity}%.'
homecontent = f'Zuhause beträgt die Temperatur {temphome}°. Die Luftfeuchtigkeit beträgt {humidityhome}%.'
print(content)

today = date.today()
print("Today's date:", today)

if (temp > 20):
    image = 'sunny.png'
elif (temp > 0):
    image = 'cloud.png'
elif (temp < 0):
    image = 'snow.png'

if (temphome > 20):
    imagehome = 'sunny.png'
elif (temphome > 0):
    imagehome = 'cloud.png'
elif (temphome < 0):
    imagehome = 'snow.png'


def createPdf(content, today, image, homecontent, imagehome):
    pdf = FPDF()
    pdf.add_page()
    pdf.image(f'{image}', x=75, y=60, w=60)
    pdf.set_font("Arial", size=11)
    pdf.set_text_color(0, 0, 0)
    pdf.text(50, 50, txt=f'{content}')
    pdf.image(f'{imagehome}', x=75, y=140, w=60)
    pdf.set_font("Arial", size=11)
    pdf.set_text_color(0, 0, 0)
    pdf.text(50, 130, txt=f'{homecontent}')
    pdf.output(f'wheater{today}.pdf')
    return f'wheater{today}.pdf'

createPdf(content, today, image, homecontent, imagehome)

server_address = 'mikkawidmer.bplaced.net'
username = 'mikkawidmer'
password = 'M!kka2006'
filename = 'wheater2022-07-05.pdf'


def upload_pdf_ftp(server_address, username, password, filename):
    # ftp upload of the pdf
    session = ftplib.FTP(server_address, username, password)
    file = open(filename, 'rb')  # file to send
    session.cwd("/www")
    session.storbinary('STOR ' + filename, file)  # send the file
    file.close()  # close file and FTP
    session.quit()


upload_pdf_ftp(server_address, username, password, filename)

with yagmail.SMTP(user, app_password) as yag:
    # yag.send(to, subject, createPdf(content, today, image))
    print('Sent email successfully')

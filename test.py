import json
from urllib.request import urlopen

url='http://ipinfo.io/json'
response=urlopen(url)
city=json.load(response)['region']

print(city)


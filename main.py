#! python3
# Get the weasther from open weather api, and send by email

import logging, os
from apiWeather import getApiWeather, extractWeather
from apiLocation import getlocation

# Files and initial vars
currentDir = os.path.dirname(__file__)
credentailsPath = os.path.join(currentDir, 'credentials.json')
commandsPath = os.path.join(currentDir, 'commands.json')
logPath = os.path.join(currentDir, 'logs.txt')

logging.basicConfig(filename=logPath, level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# Get current location
location = getlocation()

lat = location['lat']
lon = location['lon']
apikey = "148200b8d1c12c3d891801dc216b8f87"

weatherList = getApiWeather (lat, lon, apikey)
text = extractWeather (weatherList)
for item in text: 
    print (item)
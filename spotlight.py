import json
import requests
import configparser
from datetime import datetime

class SpotLightTimer:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        self.api_url = '{0}weather?zip=48462,us{1}'.format(config['API']['API_BASE_URL'],
        config['API']['API_TOKEN'])

    def requestTime(self):
        res = requests.get(self.api_url)
        if res.status_code == 200:
            sunrise = json.loads(res.content.decode('utf8'))['sys']['sunrise']
            sunset = json.loads(res.content.decode('utf-8'))['sys']['sunset']
            print('sunrise: {0}'.format(datetime.utcfromtimestamp(sunrise)))
            print('sunset {0}'.format(datetime.utcfromtimestamp(sunset)))
            #print(json.loads(res.content.decode('utf-8')))
        else:
            print(res.status_code)

if __name__ == '__main__':
    light = SpotLightTimer()
    light.requestTime()
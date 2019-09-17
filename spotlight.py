import json
import requests
import configparser
import logging
from datetime import datetime
from models import models

class SpotLightTimer:

    def logTimes(self, checkTime, sunrise, sunset):
        t = models.Timer(checkTime, sunrise, sunset)
        models.session.add(t)
        models.session.commit()

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
            checkTime = datetime.now()
            self.logTimes(checkTime, sunrise, sunset)
            logging.debug('sunrise: {0}'.format(datetime.utcfromtimestamp(sunrise)))
            logging.debug('sunset {0}'.format(datetime.utcfromtimestamp(sunset)))
        else:
            print(res.status_code)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(asctime)s %(message)s")
    light = SpotLightTimer()
    light.requestTime()
import json
import requests
import configparser
import log
from datetime import datetime
from models import models

class SpotLightTimer:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.api_url = '{0}weather?zip=48462,us{1}'.format(config['API']['API_BASE_URL'],
        config['API']['API_TOKEN'])

    def logTimes(self, checkTime, sunrise, sunset):
        t = models.Timer(checkTime, sunrise, sunset)
        models.session.add(t)
        models.session.commit()

    def requestTime(self):
        res = requests.get(self.api_url)
        if res.status_code == 200:
            sunriseUnix = json.loads(res.content.decode('utf8'))['sys']['sunrise']
            sunsetUnix = json.loads(res.content.decode('utf-8'))['sys']['sunset']
            sunrise = datetime.utcfromtimestamp(sunriseUnix)
            sunset = datetime.utcfromtimestamp(sunsetUnix)
            log.debug('sunrise: {0}'.format(sunrise))
            log.debug('sunset {0}'.format(sunset))
            return (sunriseUnix, sunsetUnix)
        else:
            print(res.status_code)

if __name__ == '__main__':
    SpotLightTimer()
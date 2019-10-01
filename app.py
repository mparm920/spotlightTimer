import spotlight 
import datetime

sl = spotlight.SpotLightTimer()
sunrise, sunset = sl.requestTime()
sl.logTimes(datetime.datetime.now(), sunrise, sunset)



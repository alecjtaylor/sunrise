import os, json, ast
from datetime import datetime, timedelta

# encoded as unicode for some reason - not sure if this will be an issue later on
f = open("sunrise.json", 'r')
sunriseDict = json.load(f)
f.close

# Set time and date to now so can be used later (everything in GMT)!
timeNow = datetime.utcnow()#.strftime("%H:%M:%S")
dateNow = datetime.utcnow()#.strftime("%Y-%m-%d")

# grab times as strings from dict using todays date as a key - the value is a list containing sunrise and sunset
sunrise = str(sunriseDict[dateNow][0])
sunriseRaw = datetime.strptime(sunrise, "%H:%M:%S")

sunset = str(sunriseDict[dateNow][1])
sunsetRaw = datetime.strptime(sunset, "%H:%M:%S")

#Check to see if the time objects can be used in calcs (comparisons didn't work as there was no date element to the sunrise and sunset times)
if timeNow >= sunriseRaw and timeNow < sunsetRaw:
    print 
    print "yes, take a photo,  the time is now " + timeNow.strftime("%H:%M:%S") + " and sunrise was " + sunrise + " and the sunset is at " + sunset
    print
elif timeNow <= sunriseRaw or timeNow >= sunsetRaw:
    print
    print "no, take a long exposure, the time is now " + timeNow.strftime("%H:%M:%S") + " and the sunset was at " + sunset
    print
else:
    print "Something has gone wrong!"

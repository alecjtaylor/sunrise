import os, json, ast
from datetime import datetime, timedelta

# encoded as unicode for some reason - not sure if this will be an issue later on
f = open("sunrise.json", 'r')
sunriseDict = json.load(f)
f.close


# Set time and date to now so can be used later!
timeNow = datetime.utcnow().strftime("%H:%M:%S")
dateNow = datetime.utcnow().strftime("%Y-%m-%d")

# grab times as strings from dict using todays date as a key - the value is a list containing sunrise and sunset
sunrise = sunriseDict[dateNow][0]
sunset = sunriseDict[dateNow][1]

#Check to see if the time objects can be used in calcs (comparisons didn't work as there was no date element to the sunrise and sunset times)
if timeNow >= sunrise:
    print 
    print "yes, take a photo,  the time is now " + timeNow + " and sunrise was " + sunrise + " and the sunset is at " + sunset
    print
elif timenow >= sunset:
    print
    print "no, take a long exposure, the time is now " + timeNow + "and the sunset was at " + sunset
    print
else:
    print "Something has gone wrong!"

import os, json, ast, time
from datetime import datetime, timedelta

# encoded as unicode for some reason - not sure if this will be an issue later on
f = open("sunrise.json", 'r')
sunriseDict = json.load(f)
f.close

    #### Start Loop Here ####
try:   
    while True:
            
        # Set time and date to now so can be used later (everything in GMT)!
        timeNow = datetime.utcnow()
        dateNow = datetime.utcnow().strftime("%Y-%m-%d")

        # grab times as strings from dict using todays date as a key - the value is a list containing sunrise and sunset strings which need to be converted to datetime objects
        sunrise = str(sunriseDict[dateNow][0])
        sunset = str(sunriseDict[dateNow][1])

        # Convert to datetime object
        sunriseRaw = datetime.strptime(sunrise, "%Y-%m-%d %H:%M:%S")
        sunsetRaw = datetime.strptime(sunset, "%Y-%m-%d %H:%M:%S")

        if timeNow >= sunriseRaw and timeNow < sunsetRaw:

            print "Greater than sunrise time and less than sunset time"
            print "Take normal timelapse and wait 10 seconds until next image"

            time.sleep(10)
        
        elif timeNow < sunriseRaw or timeNow >= sunsetRaw:

            print "Less than sunrise or greater than sunset"
            print "Take long exposure images"

            time.sleep(60)
except KeyboardInterrupt:
    print('interrupted!')
import os, json, ast
from datetime import datetime, timedelta

# encoded as unicode for some reason - not sure if this will be an issue later on
f = open("sunrise.json", 'r')
sunriseDict = json.load(f)
f.close


# Set time and date to now so can be used later!
timeNow = datetime.utcnow().strftime("%H:%M:%S")
dateNow = datetime.utcnow().strftime("%Y-%m-%d")

# grab times as strings from dict
sunrise = sunriseDict[dateNow][0]
sunset = sunriseDict[dateNow][1]

#Check to see if the time objects can be used in calcs (comparisons didn't work as there was no date element to the sunrise and sunset times)
if timeNow >= sunrise:
    print "yes, take a photo,  the time is now " + timeNow + " and sunrise was " + sunrise
elif timenow >= sunset:
    print "no, take a long exposure, the time is now " + timeNow + "and the sunset will be " + sunset
else:
    print "Something has gone wrong!"






# create datetime.datetime objects for use in loop




# check to see what the sunrise and sunset times are today

    # if inside take normal photo 

    # if outside take long exposure photo - control exposure settings - maybe add to name 


# check to see if a today directory exists, if not create it
# put photo into todays directory

# wait for 1 min inside of sunset-rise time and 10 mins outside


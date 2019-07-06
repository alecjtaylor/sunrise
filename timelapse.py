import os, json
from datetime import datetime
from picamera import PiCamera
from time import sleep

# Read in sunrise and sunset times from json file
f = open("sunrise.json", 'r')
sunriseDict = json.load(f)
f.close

try:   
    while True:
            
        # Set time and date to now so can be used later (everything in GMT)!
        timeNow = datetime.utcnow()
        dateNow = datetime.utcnow().strftime("%Y-%m-%d")
        yearNow = datetime.utcnow().strftime("%Y")
        monthNow = datetime.utcnow().strftime("%m")
        dayNow = datetime.utcnow().strftime("%d")

        # Convert to datetime object
        sunriseRaw = datetime.strptime(sunriseDict[dateNow][0], "%Y-%m-%d %H:%M:%S")
        sunsetRaw = datetime.strptime(sunriseDict[dateNow][1], "%Y-%m-%d %H:%M:%S")


        filePath = "~/images/" + yearNow + "/" + monthNow + "/" + dayNow
        # Check if todays year, month and day folder exists
        if not os.path.exists(filePath):
            os.makedirs(filePath)

        if timeNow >= sunriseRaw and timeNow < sunsetRaw:

            print "Greater than sunrise time and less than sunset time"
            
            # camera.exposure = 'auto'
            # camera.capture(filePath + "/" + timeNow + ".jpg")
            # this needs to be put into a days worth of images in a folder

            print "Take normal timelapse and wait 10 seconds until next image"

            time.sleep(10)
        
        elif timeNow < sunriseRaw or timeNow >= sunsetRaw:

            print "Less than sunrise or greater than sunset"
            print "Take long exposure images"
            # camera.exposure = 'night'
            # camera.capture(filePath + "/" + timeNow + ".jpg")
            # this needs to be put into a days worth of images in a folder

            time.sleep(60)
except KeyboardInterrupt:
    print('interrupted!')
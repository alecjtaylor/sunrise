import os, json
from datetime import datetime
from picamera import PiCamera
from time import sleep

# Read in sunrise and sunset times from json file
f = open("sunrise.json", 'r')
sunriseDict = json.load(f)
f.close

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.rotation = 180

try:   
    while True:
            
        # Set time and date to now so can be used later (everything in GMT)!
        timeNow = datetime.utcnow()
        timeNowFilePath = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        dateNow = datetime.utcnow().strftime("%Y-%m-%d")
        yearNow = datetime.utcnow().strftime("%Y")
        monthNow = datetime.utcnow().strftime("%m")
        dayNow = datetime.utcnow().strftime("%d")

        # Convert to datetime object
        sunriseRaw = datetime.strptime(sunriseDict[dateNow][0], "%Y-%m-%d %H:%M:%S")
        sunsetRaw = datetime.strptime(sunriseDict[dateNow][1], "%Y-%m-%d %H:%M:%S")


        filePath = "/home/pi/images/" + str(yearNow) + "/" + str(monthNow) + "/" + str(dayNow)
        # Check if todays year, month and day folder exists

        if not os.path.exists(filePath):
            os.makedirs(filePath)

        if timeNow >= sunriseRaw and timeNow < sunsetRaw:
            print "Take normal timelapse and wait 10 seconds until next image"
            camera.exposure_mode = 'auto'
            camera.capture(filePath + "/" + str(timeNowFilePath) + ".jpg")
            sleep(10)
        
        elif timeNow < sunriseRaw or timeNow >= sunsetRaw:
            print "Take long exposure images"
            camera.exposure_mode = 'night'
            camera.capture(filePath + "/" + str(timeNowFilePath) + ".jpg")
            sleep(60)
except KeyboardInterrupt:
    print('interrupted!')
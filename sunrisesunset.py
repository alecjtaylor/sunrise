import requests , json
from datetime import datetime, timedelta

#Todo
def createDateList(numDays):
    # Set time to now so that the script won't break if run just before midnight!
    dateValue = datetime.utcnow()
    dateList =[]
    i = 0

    while i < numDays:
        dateList.append((dateValue + timedelta(days=i)).strftime('%Y-%m-%d'))
        i += 1
    return dateList

def createApiRequest(dateList):
    '''
    Todo 
    Allow other lat long values as arguments
    '''

    apiList =[]
    for i in dateList:
        apiList.append("https://api.sunrise-sunset.org/json?lat=53.739020&lng=-1.394565&date=%s" % str(i))
    return apiList

def sunriseTimes(days):

    apiCallList = createApiRequest(createDateList(days))
    mydict={}

    for i in apiCallList:
        print i
        r = requests.get(i)
        data = json.loads(r.content)["results"]
        sunDate = i[-10:]
        sunriseT = datetime.strptime(str(data["sunrise"]), "%I:%M:%S %p").strftime("%H:%M:%S")
        sunsetT = datetime.strptime(str(data["sunset"]), "%I:%M:%S %p").strftime("%H:%M:%S")
        sunrise = sunDate + " " + sunriseT 
        sunset =  sunDate + " " + sunsetT
        mydict[sunDate] = [sunrise, sunset]
    return mydict

outputJson = json.dumps(sunriseTimes(1000), sort_keys=True)

# ugly code!
f = open("sunrise.json", "w") 
f.write(outputJson)
f.close() 
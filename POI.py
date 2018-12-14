import requests, json, sys, time

# enter your api key here

# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# The file to create
f = open("pois.xml", "a")


# get method of requests module
# return response object
key = str(input("enter places api key: "))


def poi():
    while True:
        query = input("enter the query: ")
        if query.lower() == 'stop'.lower():
            f.close()
            sys.exit()
        r = requests.get(url + 'query=' + query +
                         '&key=' + key)

        # json method of response object convert
        #  json format data into python format data
        x = r.json()
        if str(x["status"]) == "OVER_QUERY_LIMIT":
            print("exceeded per minute limit, stopping for some time")
            time.sleep(55)
            poi()
        y = x["results"]

        for i in range(len(y)):
            print(str(i) + ": " + y[i]['name'])
        index = input('The index of place you want to add: ')
        name = y[int(index)]['name']
        lat = y[int(index)]['geometry']['location']['lat']
        lng = y[int(index)]['geometry']['location']['lng']
        heading = input("Enter required heading: ")
        tilt = input("Enter required tilt: ")
        f.write("\nEarth@"+name+"@flytoview=<LookAt><longitude>"+str(lng)+"</longitude><latitude>"+str(lat)+"</latitude><altitude>0</altitude><heading>"+heading+"</heading><tilt>"+tilt+"</tilt><gx:altitudeMode>relativeToSeaFloor</gx:altitudeMode></LookAt>")
poi()

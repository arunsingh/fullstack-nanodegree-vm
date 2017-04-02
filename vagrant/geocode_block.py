import httplib2
import json


def geoCodeLocation(inputString):
    google_api_key = "AIzaSyBL1eeqspMmSZVOKXkxirXexc8G3Pfz3Ms"
    locationString = inputString.replace(" ", "+")
    url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'
           % (locationString, google_api_key))

    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)

    # Print respnse

    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    # print "response header: %s \n \n" % response
    return (latitude, longitude)

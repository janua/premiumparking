import requests
import json

MOST_READ_URL = "http://api.ophan.co.uk/api/mostread"

DEFAULT_PARAMS = {
    "api-key" : "francis_hackday",
    "age" : 7 * 24 * 60 * 60,
    "count" : 20,
    }

def getTop20Articles():
    return getOphanUrl(MOST_READ_URL)

def getOphanUrl(url, params=DEFAULT_PARAMS):
    response = requests.get(url, params=params)
    results = list()

    try:
        results = json.loads(response.content)
    except Exception as e:
        print "Error: " + str(e)

    return results

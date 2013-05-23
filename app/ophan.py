import requests
import json

def getCurrentArticles():
    base_url = "http://api.ophan.co.uk/api/mostread"

    params = {
    "api-key" : "francis_hackday",
    "age" : 7 * 24 * 60 * 60,
    "count" : 20,
    }

    result = requests.get(base_url, params=params)
    articles = list()

    try:
        articles = json.loads(result.content)
    except Exception as e:
        print "Error: " + str(e)

    return {'articles': articles }

import requests
import json
import contentapi

OPHAN_CACHE = dict()

MOST_READ_URL = "http://api.ophan.co.uk/api/mostread"

DEFAULT_PARAMS = {
    "api-key" : "francis_hackday",
    "age" : 7 * 24 * 60 * 60,
    "count" : 20,
    }

def getTop20ArticlesThroughContentAPI():
    results = list()
    for article in getTop20Articles():
        #26 is http://www.guardian.co.uk/
        contentApiItem = contentapi.getArticle(article['url'][26:])     
        results.append(contentApiItem['response']['content'])

    return results


def getTop20Articles():
    return getOphanUrl(MOST_READ_URL)

def getOphanUrl(url, params=DEFAULT_PARAMS):
    try:
        #Doesn't include the params as cache key
        return OPHAN_CACHE[url]
    except:
        print 'Ophan cache miss'

    response = requests.get(url, params=params)
    results = list()

    try:
        results = json.loads(response.content)
        OPHAN_CACHE[url] = results
    except Exception as e:
        print "Error: " + str(e)

    return results

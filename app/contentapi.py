import requests
import json

API_KEY = ""

CONTENT_API_URL = ""

CONTENT_API_CACHE = dict()

DEFAULT_PARAMS = {
    'api-key': API_KEY,
    'format': 'json'
}

def getArticle(articleId, params=DEFAULT_PARAMS):
    try:
        return CONTENT_API_CACHE[articleId]
    except:
        print "ContentApi cache miss" 

    result = dict()

    url = "{0}{1}".format(CONTENT_API_URL, articleId)

    response = requests.get(url, params=params)
    print response.url

    try:
        result = json.loads(response.content)
        CONTENT_API_CACHE[articleId] = result
    except Exception as e:
        print "Error: " + str(e)

    return result


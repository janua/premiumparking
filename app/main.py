import ophan
from flask import Flask
import contentapi
from flask import render_template, jsonify
app = Flask(__name__)

STATE = dict()

@app.route("/")
def index():
    return render_template('index.html', articles=ophan.getTop20ArticlesThroughContentAPI())

@app.route("/article/<path:article_id>")
def article(article_id):
    return render_template('article.html', article=contentapi.getArticle(article_id)) 

@app.route("/sandbox")
def sandbox():
    return jsonify({'data:':ophan.getTop20ArticlesThroughContentAPI()})
    #return str(ophan.getOphanUrl("http://api.ophan.co.uk/viral"))
	#return jsonify({'data': ophan.getTop20Articles()})

if __name__ == "__main__":
    app.debug = True
    app.run()
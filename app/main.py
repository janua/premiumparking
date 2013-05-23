import ophan
from flask import Flask
from flask import render_template, jsonify
app = Flask(__name__)

STATE = dict()

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/state")
def state():
	return jsonify(ophan.getCurrentArticles())

if __name__ == "__main__":
    app.debug = True
    app.run()
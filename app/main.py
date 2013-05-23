import ophan
from flask import Flask
from flask import render_template, jsonify
app = Flask(__name__)

STATE = dict()

@app.route("/")
def index():
    return render_template('index.html', articles=ophan.getTop20Articles())

@app.route("/sandbox")
def sandbox():
	return jsonify({'data': ophan.getTop20Articles()})

if __name__ == "__main__":
    app.debug = True
    app.run()
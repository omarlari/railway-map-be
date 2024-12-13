import os, logging
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
CORS(app)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/test')
def appRoot():
    person = {'name': 'PR request 1', 'birth-year': 1979}
    return jsonify(person)

if __name__ == '__main__':
    app.run()
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

@app.route('/map')
def map():
    r = jsonify({'type':'FeatureCollection',
    'features': [
        {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -122.4194,
             37.7449
             ]},
    'properties':{
        'title': "San Francisco",
        'cluster': False,
        'venue': 'SF Center',
        'event_count': 20
    }
    },
    {'type': 'Feature', 
        'geometry': {
        'type': 'Point', 
        'coordinates': [
            -122.3960,
             37.7897
             ]},
    'properties':{
        'title': "SF Tower",
        'cluster': False,
        'venue': 'SF Tower',
        'event_count': 33
    }
    },
    ]})
    return r

if __name__ == '__main__':
    app.run()
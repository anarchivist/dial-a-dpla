import re

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import urllib
from twilio import twiml
from requests import get as rget
from requests.compat import urlencode
import os
import random

api_key = os.environ.get('DPLA_API_KEY', None)

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('local_settings.py')

@app.route('/')
def hello():
    r = twiml.Response()
    r.say("Welcome to Dial a D P L A!")
    r.say("Today we are providing access to Kentucky Digital Library's Claude Sullivan audio recordings.")
    with r.gather(numDigits=4, action="lookup", method="POST") as g:
        g.say("Please enter a four digit year of recording followed by the pound key.")
    return str(r)
        

@app.route('/lookup', methods=['POST'])
def obj():
    year = request.values.get('Digits', None)
    r = twiml.Response()
    params = {
        "sourceResource.type": "sound",
        "provider.name": "Kentucky Digital Library",
        "sourceResource.date.begin": str(year),
        "api_key": api_key,
        "page_size": 100
    }
    url = "http://api.dp.la/v2/items/?%s" % urllib.urlencode(params)
    results = rget(url).json()
    if len(results['docs']) < 1:
        r.say("Sorry, nothing matched your query.")
    else:
        if results['count'] > params['page_size']:
            upper_bound = params['page_size'] - 1
        else:
            upper_bound = results['count'] - 1
        index = random.randint(0, upper_bound)
        item = results['docs'][index]
        stream = item['object']
        stream = stream.replace("_tb.mp3", ".mp3")
        phrase = "You are about to listen to: " + item['sourceResource']['title'] + ". "
        phrase += "This item is from " + item['dataProvider'] + "."
        r.say(phrase)
        r.play(stream)
    return str(r)

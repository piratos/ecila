from flask import Flask, jsonify
from functools import wraps
from nlu_model import run_nlu

import json
import requests
import os


app = Flask(__name__)
WEATHER_PORT = int(os.environ.get('WEATHER_PORT', '5000'))
MAIN_PORT = int(os.environ.get('MAIN_PORT', 5000))


def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = 'showmsg'
        if callback:
            content = str(callback) + '(' + f(kwargs['query']).data.decode('utf-8') + ')'
            return app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)
    return decorated_function


@app.route('/a/<query>')
@support_jsonp
def respond(query):
	print(query)
	nlu_res = run_nlu(query, config='mitie')
	intent = nlu_res.get('intent').get('name')
	intent_confidence = nlu_res.get('intent').get('confidence')
	msg = None
	if intent == 'inform_weather':
		weather_date = None
		weather_location = None
		for entity in nlu_res.get('entities', []):
			if entity.get('entity') == 'date':
				weather_date = entity.get('value')
			elif entity.get('entity') == 'location':
				weather_location = entity.get('value')
		# get the response
		if weather_location:
			res = requests.get('http://weather:%d/loc/%s' % (WEATHER_PORT, weather_location)).text
			full_answer = 'it will be %s in %s %s' %(res, weather_location, weather_date)
			msg = full_answer
	elif intent == 'greet':
		msg = 'Hi how are you?'
	elif intent == 'goodbye':
		msg = 'see ya'
	else:
		msg = 'I am so dump jesus !'
	return jsonify(msg=msg)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=MAIN_PORT)

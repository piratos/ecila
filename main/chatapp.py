from flask import Flask
import json
import requests

from nlu_model import run_nlu

app = Flask(__name__)

@app.route('/a/<query>')
def respond(query):
	print(query)
	nlu_res = run_nlu(query)
	intent = nlu_res.get('intent').get('name')
	intent_confidence = nlu_res.get('intent').get('confidence')
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
			res = requests.get('http://127.0.0.1:5001/loc/%s' % weather_location).text
			full_answer = 'it will be %s in %s %s' %(res, weather_location, weather_date)
			return full_answer
	elif intent == 'greet':
		return 'Hi how are you?'
	elif intent == 'goodbye':
		return 'see ya'
	return 'I am so dump jesus !'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
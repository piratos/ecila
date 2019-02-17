import os

from flask import Flask

import openweathermapy as owm

app = Flask(__name__)

APPID=""
with open("key.env", "r") as fd:
    APPID = fd.read().strip()

SETTINGS = {"units": "metric", "lang": "EN", "APPID": APPID}
WEATHER_PORT = int(os.environ.get('WEATHER_PORT', '80'))
WEATHER_EP = os.environ.get('WEATHER_EP', '0.0.0.0')


@app.route('/loc/<location>')
def get_weather_by_location(location):
    result = "error"
    try:
        data = owm.get_current(location, **SETTINGS)
        condition = data['weather'][0]['description']
        tempmin = data['main']['temp_min']
        tempmax = data['main']['temp_max']
        result = "{0} with temperature between {1} and {2}".format(
            condition, tempmin, tempmax)
    except Exception as ex:
        # raise, for debug
        print('error getting weather: ', ex)
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=WEATHER_PORT)


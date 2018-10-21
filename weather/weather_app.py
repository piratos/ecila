from weather import Weather, Unit
from flask import Flask
import os

app = Flask(__name__)

weather = Weather(unit=Unit.CELSIUS)
WEATHER_PORT = int(os.environ.get('WEATHER_PORT', '80'))
WEATHER_EP = os.environ.get('WEATHER_EP', '0.0.0.0')


@app.route('/loc/<location>')
def get_weather_by_location(location):
    lookup = weather.lookup_by_location(location)
    if not lookup:
        return 'FAIL'
    result = dict()
    condition = lookup.condition
    return condition.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=WEATHER_PORT)


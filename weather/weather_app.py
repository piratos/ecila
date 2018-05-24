from weather import Weather, Unit
from flask import Flask

app = Flask(__name__)

weather = Weather(unit=Unit.CELSIUS)


@app.route('/loc/<location>')
def get_weather_by_location(location):
    lookup = weather.lookup_by_location(location)
    result = dict()
    condition = lookup.condition
    return condition.text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)


import json, requests


urlwheather = 'https://api.openweathermap.org/data/2.5/weather'

paramswheather = dict(
    q='Bangalore,IN',
    appid='YOUR_API_KEY',
    units='metric'
)

data = None


def __init__():
    global data
    resp = requests.get(url=urlwheather, params=paramswheather)
    data = resp.json()
    json.dumps(data)
    getData()
    # printData()


def getData():
    temperature = data['main']['temp']
    weather = data['weather'][0]['description']
    rainfall = data.get('rain', {}).get('1h', 0)
    return (temperature, weather, rainfall)


def printData():
    print(data['main']['temp'])
    print(data['weather'][0]['description'])
    print(data.get('rain', {}).get('1h', 0))


# run
__init__()
printData()



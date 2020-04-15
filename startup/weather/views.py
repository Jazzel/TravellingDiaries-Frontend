import requests
from django.shortcuts import render

# Create your views here.


def index(request):

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=ab1511265be0e3512b8a68c06a71358f'
    city = 'Karachi'
    # request the API data and convert the JSON to Python data types
    city_weather = requests.get(url.format(city)).json()
    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }

    context = {'weather': weather}
    # returns the index.html template
    return render(request, 'weather/weather.html', context)

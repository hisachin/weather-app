from django.shortcuts import render
from .models import City
from django.http import JsonResponse

import requests

# show search city view
def index(request):
    return render(request, 'weather_info_app/city_weather.html', {})

# validate city
def get_city_weather(request):
	city_name = request.GET.get('city_name')
	is_city_exists = City.objects.filter(city_name = city_name).exists()
	if(is_city_exists):
		location_url = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey=ZIjdntYAGTo9V2aiIJ5DYG3tzyLgFmto&q="+city_name
		location_key = requests.get(location_url).json()[0]['Key']
		if(location_key):
			weather_url = "http://dataservice.accuweather.com/forecasts/v1/daily/1day/"+location_key+"?apikey=ZIjdntYAGTo9V2aiIJ5DYG3tzyLgFmto"
			weather_data = requests.get(weather_url).json()
			if(weather_data):
				weather_details = { 
						'city': city_name,
						'max_temp':weather_data['DailyForecasts'][0]['Temperature']['Maximum'],
						'min_temp':weather_data['DailyForecasts'][0]['Temperature']['Minimum'],
						'day_weather':weather_data['DailyForecasts'][0]['Day']['IconPhrase'],
						'night_weather':weather_data['DailyForecasts'][0]['Night']['IconPhrase'],
						'date':weather_data['DailyForecasts'][0]['Date'],
						'headline':weather_data['Headline']['Text']
					}
				response = {'status':True,'message': weather_details}
			else:
				response = {'status':False,'message':'City Weather Not Found'}
		else:
			response = {'status':False,'message':'City Not Valid'}	
	else:
		response = {'status':False,'message':'City Not Valid'}

	return JsonResponse(response,safe=False)


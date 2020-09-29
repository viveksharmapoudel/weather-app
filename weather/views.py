from django.shortcuts import render
from .models import City
from .forms import *
import requests
# Create your views here.

def index(request): 
	url='http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=53f9b7cd6151420eee02b3b5f3ca5be4'


	#########for saving the data 
	if request.method=='POST':
		cities = City.objects.all()
		form =CityForm(request.POST)

		temp=True
		for city in cities: 
			if str(form['name'].value()).lower() == city.name.lower(): 
				temp=False
				print(" yes this time similar ")
				break
		if temp:
			form.save()
	

	cities = City.objects.all()
	form=CityForm()
	weathers=[]
	for city in cities:
		city_weather= requests.get(url.format(city)).json()

		if city_weather['cod'] ==200:
			weathers.append({
				'city':city,
				'temperature':city_weather['main']['temp'],
				'description': city_weather['weather'][0]['description'],
				'icon':city_weather['weather'][0]['icon']
			})

	return render(request, 'weather/index.html',{'weathers': weathers, 'form':form})


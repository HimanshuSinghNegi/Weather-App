from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests

# Create your views here.
def home(request):
	return render(request,'home.html',{})

def about(request):
	return render(request,'about.html',{})

def weather(request):
	return render (request,'weather.html',{})

def analyze(request):
	pin_code= request.POST.get("zipcode1","default")
	link= "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+pin_code+"&distance=5&API_KEY=C43BF23F-E295-463A-8231-AA4894D8493A"


	try:
		api_request = requests.get(link).json()
		city = api_request[0]["ReportingArea"]
		quality = api_request[0]["AQI"]
		category = api_request[0]['Category']["Name"]
		date = api_request[0]["DateObserved"]

		if category == "Good":
			weather_color = "#0C0"
		elif category == "Moderate":
			weather_color = "#FFFF00"
		elif category == "Unhealthy For Sensitive Groups":
			weather_color = "#ff9900"
		elif category == "Unhealthy":
			weather_color = "#FF0000"
		elif category == "Very Unhealthy":
			weather_color = "#9900066"
		elif category == "Hazardous":
			weather_color = "#660000"
		return render(request, "we.html",
					  {'city': city, 'quality': quality, 'category': category,"date" :date, 'color': weather_color})

	except:
		return HttpResponse("<strong><h1>Sorry This pin code Weather will be Available Soon !!!</h1></strong>")
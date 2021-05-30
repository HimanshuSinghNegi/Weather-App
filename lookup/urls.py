
from django.urls import path
from . import views
urlpatterns = [
	path('home.html',views.home,name="home"),
	path('about.html',views.about,name="about"),
	path('',views.weather,name="weather"),
	path('analyze',views.analyze,name="analyze"),

]
    


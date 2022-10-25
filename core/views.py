from django.shortcuts import render
from blogs.models import *
from core.models import *
from datetime import date, datetime, timedelta
from .forms import ContactForm
import requests


def home(request):
    startdate = date.today()
    enddate = startdate - timedelta(days=6)
    category=Category.objects.all()
    blogs=BlogList.objects.all()[0:2]
    recents=BlogList.objects.filter(abstractmodel_created_at=datetime.today())[0:4]
    blog=BlogList.objects.all()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0005219349da9b71072cceef33e1e6e0'
    city = 'Baku'
    city_weather = requests.get(url.format(city)).json()
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    ab={}
    for i in blog:
        comments=Comments.objects.filter(blogs=i.id)
        ab[f'{i.id}']=comments
   
    context={
        "category":category,
        "blogs":blogs,
        'recents':recents,
        'comments':ab,
        'weather':weather
    }    
    
    return render(request, 'index.html',context)


def about(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0005219349da9b71072cceef33e1e6e0'
    city = 'Baku'
    city_weather = requests.get(url.format(city)).json()
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    about=About.objects.all().first()
    context={
        "about":about,
        "weather":weather
    }
    
    return render(request, 'about-us.html',context)

    
def contact(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0005219349da9b71072cceef33e1e6e0'
    city = 'Baku'
    city_weather = requests.get(url.format(city)).json()
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    form=ContactForm()
    if request.method =="POST":
        form=ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            form=ContactForm()
            
    context={
        "form":form,
        "weather":weather
    }
    return render(request, 'contact.html',context)



from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *
from .forms import CommentForm,AddBlogForm
from datetime import date,timedelta
import requests


def blog_detail(request,id):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0005219349da9b71072cceef33e1e6e0'
    city = 'Baku'
    city_weather = requests.get(url.format(city)).json()
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
    startdate = date.today()
    enddate = startdate - timedelta(days=6)
    blog=BlogList.objects.get(id=id)
    comments=Comments.objects.filter(blogs=blog.id)
    categories=Category.objects.all()
    recents=BlogList.objects.filter(created_at__range=[enddate,startdate])[0:4]
    form=CommentForm()
  
    if request.method == 'POST':
        form= CommentForm(request.POST)
        print(form)
        if form.is_valid():
            user=Comments(name=form.cleaned_data["name"],email=form.cleaned_data["email"],message=form.cleaned_data["message"],blogs=blog,user=request.user)
            user.save()
    context={
        "blog":blog,
        "form":form,
        "comments":comments,
        "categories":categories,
        "recents":recents,
        "weather":weather
    }
    
    
    return render(request, 'blog-detail.html',context)

def add_blog(request):
    form=AddBlogForm()
    if request.method == 'POST':
        form=AddBlogForm(request.POST)
        blog=BlogList(title=request.POST.get("title"),image=request.POST.get("image"),
        short_description=request.POST.get("short_description"),long_description=request.POST.get("long_description"),
        author=request.user)
        blog.save()
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0005219349da9b71072cceef33e1e6e0'
    city = 'Baku'
    city_weather = requests.get(url.format(city)).json()
    weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }        
    context={
        "form":form,
        "weather":weather
    }
    return render(request, 'addBlog.html',context)

class BlogListView(ListView):
    
    model=BlogList
    template_name="blog-list.html"
    context_object_name='blogs'
    paginate_by= 2
    def get_context_data(self, **kwargs):
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=0005219349da9b71072cceef33e1e6e0'
        city = 'Baku'
        city_weather = requests.get(url.format(city)).json()
        weather = {
        'city' : city,
        'temperature' : city_weather['main']['temp'],
        'description' : city_weather['weather'][0]['description'],
        'icon' : city_weather['weather'][0]['icon']
    }
        startdate = date.today()
        enddate = startdate - timedelta(days=6)
        blog=BlogList.objects.all()
        recents=BlogList.objects.filter(created_at__range=[enddate,startdate])
        print(recents)
        ab={}
        for i in blog:
           comments=Comments.objects.filter(blogs=i.id)
           ab[f'{i.id}']=comments
        #    print(ab)
        context=super(BlogListView, self).get_context_data(**kwargs)
        context['categories']=Category.objects.all()
        context["comment"]=ab
        context["recents"]=recents
        context["weather"]=weather
        
        return context



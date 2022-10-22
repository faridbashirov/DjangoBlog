from django.shortcuts import render
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import  authenticate,login as django_login,logout as django_logout
from .forms import RegisterForm,LoginForm
from django.contrib import messages


def login(request):
    form=LoginForm()
    next_page=request.GET.get("next","/")
    
   
    if request.method == "POST":
        form=LoginForm(data=request.POST)
       
        if form.is_valid():
            
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data["password"])
            if user:
                django_login(request,user)
                messages.add_message(request, messages.INFO, 'welcome')
                return redirect(next_page)
            else:
                messages.add_message(request, messages.ERROR ,'invalid username')
    context={
        "form":form
    }
    return render(request, 'login.html',context)
def logout_page(request):
    django_logout(request)
    messages.add_message(request,messages.ERROR,"LOGOUT OLDUNUZ")
    return redirect(reverse_lazy('login'))


def register(request):
    form=RegisterForm()
    form = RegisterForm(data=request.GET)
    if request.method=="POST":
        form = RegisterForm(data=request.POST)
       
        if form.is_valid():
            
           
                
                user= form.save()
                user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect(reverse_lazy('login'))
           
    context={
        "form":form
    }
    return render(request,"register.html",context)
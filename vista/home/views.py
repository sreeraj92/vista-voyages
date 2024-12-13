from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
import os

# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    if request.method=="POST":
        try:
            email=request.POST.get("Email")
            password=request.POST.get("password")
            logindata=User_registration.objects.get(Email=email,Password=password)
            request.session['email']=logindata.Email
            request.session['id']=logindata.id
            return redirect('index')
        except User_registration.DoesNotExist as e:
            messages.info(request,'incorrect password or email')
    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        username=request.POST.get("Username")
        email=request.POST.get("Email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        if password==confirm_password:
            if User_registration.objects.filter(Email=email).exists():
                messages.info(request,'Email already exists')
            else:
                data=User_registration(Username=username,Password=password,Email=email)  
                data.save()
                return redirect("login")
        else:
            messages.info(request,'Passwords do not match')
    return render(request,'register.html')
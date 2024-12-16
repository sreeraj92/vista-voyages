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
            return redirect('uhome')
        except User_registration.DoesNotExist as e:
            messages.info(request,'incorrect password or email')
    return render(request,'login.html')
def register(request):
    if request.method=="POST":
        username=request.POST.get("Username")
        email=request.POST.get("Email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        image=request.FILES.get("image")
        if password==confirm_password:
            if User_registration.objects.filter(Email=email).exists():
                messages.info(request,'Email already exists')
            else:
                data=User_registration(Username=username,Password=password,Email=email,image=image)  
                data.save()
                return redirect("login")
        else:
            messages.info(request,'Passwords do not match')
    return render(request,'register.html')
def uhome(request):
    return render (request,'uhome.html')
def profile(request):
    re = User_registration.objects.get(id=request.session['id'])
    if request.method=="POST":
        re.Username=request.POST.get("Username")
        re.Email=request.POST.get("Email")
        re.Password=request.POST.get("password")
        re.save()
    return render(request,'profile.html',{'re':re})
def adlog(request):
    if request.method=="POST":
        try:
            email=request.POST.get("Email")
            password=request.POST.get("password")
            logindata=admin_login.objects.get(Email=email,Password=password)
            request.session['email']=logindata.Email
            request.session['id']=logindata.id
            return redirect('adhome')
        except admin_login.DoesNotExist as e:
            messages.info(request,'incorrect password or email')

    return render(request,'adlog.html')
def adhome(request):
    return render (request,'adhome.html')
def adprofile(request):    
    e= User_registration.get(id=request.session['id'])
    if request.method=="POST":
         if len(request.FILES)!=0:
            e.Images = request.POST.get("Images")
            e.Email = request.POST.get("Email")
            e.Password = request.POST.get("password")
            e.save()
            return render(request,"adprofile.html")
def drlog(request):
    if request.method=="POST":
        try:
            email=request.POST.get("Email")
            password=request.POST.get("password")
            logindata=driver_registration.objects.get(Email=email,Password=password)
            if logindata.Roles=="CAB":
                request.session['email']=logindata.Email
                request.session['id']=logindata.id
                return redirect('cabhome')
            else:
                request.session['email']=logindata.Email
                request.session['id']=logindata.id
                return redirect('drhome')
        except driver_registration.DoesNotExist as e:
            messages.info(request,'incorrect password or email')
    return render(request,'drlog.html')
def drreg(request):
    if request.method=="POST":
        username=request.POST.get("Username")
        email=request.POST.get("Email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        image=request.FILES.get("image")
        Age=request.POST.get("Age")
        Phone=request.POST.get("Phone")
        Address=request.POST.get("Address")
        State=request.POST.get("State")
        Aadhar=request.POST.get("Aadhar")
        Experience=request.POST.get("Experience")
        Roles=request.POST.get("Roles")
        LicenseImage=request.FILES.get("LicenseImage")
        if password==confirm_password:
            if driver_registration.objects.filter(Email=email).exists():
                messages.info(request,'Email already exists')
            else:
                data=driver_registration(Username=username,Roles=Roles,Password=password,Email=email,image=image,Age=Age,Phone=Phone,Address=Address,State=State,Aadhar=Aadhar,Experience=Experience,LicenseImage=LicenseImage)  
                data.save()
                return redirect('drlog')
        else:
            messages.info(request,'Passwords do not match')
    return render(request,'drreg.html')
def drhome(request):
    return render (request,'drhome.html')
def drbooking(request):
    return render (request,"drbooking.html")
def drprofile(request):
    return render(request,"drprofile.html")
def cabhome(request):
    return render(request,'cabhome.html')
def About(request):
     if request.method=="POST":
        Cab_Type=request.POST.get("cabType")
        Make_Model=request.POST.get("makeModel")
        Registration_Number=request.POST.get("registrationNumber")
        Color=request.POST.get("color")
        vehicle_image=request.POST.get("photo")
        Driver_Name=request.POST.get("driverName")
        Driver_Contact=request.POST.get("driverContact")
        Seating_Capacity=request.POST.get("seatingCapacity")
        Base_Fare=request.POST.get("baseFare")
        Fare_per_Kilometer=request.POST.get("farePerKm")
        Safety_Features=request.POST.get("safetyFeatures")           
        Availability=request.POST.get("availability")
     return render(request,"About.html")

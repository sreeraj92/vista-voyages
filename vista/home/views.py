from django.shortcuts import render,redirect
from.models import *
from django.contrib import messages
import os

# Create your views here.
def index(request):
    return render(request,'index.html')

def hotel(request):
    return render(request,'hotel.html')

def single(request):
    return render(request,'single.html')

def hotelsingle(request):
    return render(request,'hotelsingle.html')    

def user(request):
    return render(request,'user.html') 

def drive(request):
    return render(request, 'drive.html')
    
def hotelreg(request):
    return render(request, 'hotelreg.html')

def reshotel(request):
    return render(request, 'reshotel.html')

def cab(request):
    return render(request, 'cab.html')

def driver(request):
    return render(request, 'driver.html') 
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
    re = User_registration.objects.get(id=request.session['id'])

    return render (request,'uhome.html',{'re':re})

def profile(request):
    re = User_registration.objects.get(id=request.session['id'])
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(re.img)>0:
                os.remove(re.img.path)
                re.img=request.FILES['img']
        re.Username=request.POST.get("username")
        re.Email=request.POST.get("email")
        re.Password=request.POST.get("password")
        re.save()
    return render(request,'profile.html',{'re':re})


def drive(request):
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
    return render(request,'drive.html')
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
    d= driver_registration.objects.get(id=request.session['id'])
    if request.method=="POST":
        d.Username=request.POST.get("Username")
        d.Email=request.POST.get("Email")
        d.Password=request.POST.get("password")
        d.save()
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
        data=about_cab(Cab_Type=Cab_Type,Make_Model=Make_Model,Registration_Number=Registration_Number,Color=Color,vehicle_image=vehicle_image,Driver_Name=Driver_Name,Driver_Contact=Driver_Contact,Seating_Capacity=Seating_Capacity,Base_Fare=Base_Fare,Fare_per_Kilometer=Fare_per_Kilometer,Safety_Features=Safety_Features,Availability=Availability)  
        data.save()
    return render(request,"About.html")
def cabprofile(request):
    c= driver_registration.objects.get(id=request.session['id'])
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(c.image)>0:
                os.remove(c.image.path)
                c.image=request.FILES['image']
        c.Username=request.POST.get("Username")
        c.Email=request.POST.get("Email")
        c.Password=request.POST.get("password")
        c.save()
    return render(request,'cabprofile.html',{'c':c})
def drprofile(request):
    d= driver_registration.objects.get(id=request.session['id'])
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(d.image)>0:
                os.remove(d.image.path)
                d.image=request.FILES['image']
        d.Username=request.POST.get("Username")
        d.Email=request.POST.get("Email")
        d.Password=request.POST.get("password")
        d.save()
    return render(request,'drprofile.html',{'d':d})
def rentlog(request):
    return render (request,'rentlog.html')

# ************************************************************ADMIN**************************************
def signin(request):
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
    return render(request,'padmin/signin.html')

def adhome(request):
    return render (request,'padmin/adhome.html')
def transport(request):
    return render (request,'admin/transport.html')
def chart(request):
    return render (request,'admin/chart.html')
def restaurants(request):    
            return render(request,"admin/restaurants.html")    
def hotels(request):    
            return render(request,"admin/hotels.html")    
def adprofile(request):    
            return render(request,"adprofile.html")
            logindata=rental_registration.objects.get(Email=email,Password=password)
            request.session['email']=logindata.Email
            request.session['id']=logindata.id
            return redirect('renthome')
        except rental_registration.DoesNotExist:
            messages.info(request,'incorrect password or email')
    return render(request,'rentlog.html')
def rentreg(request):
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
        LicenseImage=request.FILES.get("LicenseImage")
        if password==confirm_password:
            if rental_registration.objects.filter(Email=email).exists():
                messages.info(request,'Email already exists')
            else:
                data=rental_registration(Username=username,Password=password,Email=email,image=image,Age=Age,Phone=Phone,Address=Address,State=State,Aadhar=Aadhar,Experience=Experience,LicenseImage=LicenseImage)  
                data.save()
                return redirect('rentlog')
        else:
            messages.info(request,'Passwords do not match')
    return render(request,'rentreg.html')
def renthome(request):
    return render (request,'renthome.html')
def rentprofile(request):
    rp= rental_registration.objects.get(id=request.session['id'])
    if request.method=="POST":
        if len(request.FILES)!=0:
            if len(rp.image)>0:
                os.remove(rp.image.path)
                rp.image=request.FILES['image']
        rp.Username=request.POST.get("Username")
        rp.Email=request.POST.get("Email")
        rp.Password=request.POST.get("password")
        rp.save()
    return render(request,'rentprofile.html',{'rp':rp})

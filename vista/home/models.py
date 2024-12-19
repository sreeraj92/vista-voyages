from django.db import models

# Create your models here.
class User_registration(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=40)
    Confirm_Password=models.CharField(max_length=40)
    image=models.ImageField(upload_to='img',null=True)
class driver_registration(models.Model):
    Username=models.CharField(max_length=50,null=True)
    Email=models.CharField(max_length=50,null=True)
    Password=models.CharField(max_length=40,null=True)
    image=models.ImageField(upload_to='dpimg',null=True)
    Age=models.CharField(max_length=10,null=True)
    Phone=models.CharField(max_length=15,null=True)
    Address=models.CharField(max_length=100,null=True)
    State=models.CharField(max_length=100,null=True)
    Aadhar=models.CharField(max_length=25,null=True)
    Experience=models.CharField(max_length=200,null=True)
    Roles=models.CharField(max_length=200,null=True)
    LicenseImage=models.ImageField(upload_to='License',null=True)
class admin_login(models.Model):
    Username=models.CharField(max_length=50,null=True)
    Email=models.CharField(max_length=50,null=True)   
    Password=models.CharField(max_length=40,null=True)
class about_cab(models.Model):
    Cab_Type=models.CharField(max_length=100,null=True)
    Make_Model=models.CharField(max_length=100,null=True)
    Registration_Number=models.CharField(max_length=177,null=True)
    Color=models.CharField(max_length=98,null=True)
    vehicle_image=models.ImageField(upload_to='cabimg',null=True)
    Driver_Name=models.CharField(max_length=234,null=True)
    Driver_Contact=models.CharField(max_length=345,null=True)
    Seating_Capacity=models.CharField(max_length=90,null=True)
    Base_Fare=models.CharField(max_length=342,null=True)
    Fare_per_Kilometer=models.CharField(max_length=456,null=True)
    Safety_Features=models.CharField(max_length=700,null=True) 
    Availability=models.CharField(max_length=780,null=True)


# Vehicle Model
class Vehicle(models.Model):
    vehicle_reg_number = models.CharField(max_length=20, unique=True,null=True)
    vehicle_type = models.CharField(max_length=20,null=True)
    make_model = models.CharField(max_length=100,null=True)
    year_of_manufacture = models.PositiveIntegerField(null=True)
    fuel_type = models.CharField(max_length=10,null=True)
    transmission_type = models.CharField(max_length=10,null=True)
    mileage = models.PositiveIntegerField(help_text="Mileage in kilometers",null=True)
    engine_capacity = models.CharField(max_length=10, help_text="Engine capacity in liters",null=True)
    rental_price_per_day = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    availability = models.BooleanField(default=True,null=True)
    vehicle_image = models.ImageField(upload_to='vehicleimg',null=True)
class rental_registration(models.Model):
    Username=models.CharField(max_length=50,null=True)
    Email=models.CharField(max_length=50,null=True)
    Password=models.CharField(max_length=40,null=True)
    image=models.ImageField(upload_to='dpimg',null=True)
    Age=models.CharField(max_length=10,null=True)
    Phone=models.CharField(max_length=15,null=True)
    Address=models.CharField(max_length=100,null=True)
    State=models.CharField(max_length=100,null=True)
    Aadhar=models.CharField(max_length=25,null=True)
    Experience=models.CharField(max_length=200,null=True)
    Roles=models.CharField(max_length=200,null=True)
    LicenseImage=models.ImageField(upload_to='License',null=True)
    
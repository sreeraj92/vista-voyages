from django.db import models

# Create your models here.
class User_registration(models.Model):
    Username=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    Password=models.CharField(max_length=40)
    Confirm_Password=models.CharField(max_length=40)
  
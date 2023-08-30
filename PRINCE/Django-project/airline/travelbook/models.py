from django.db import models

# Create your models here.
class Booking(models.Model):
    From=models.CharField(max_length=50)
    To=models.CharField(max_length=50)
    Depart_date=models.DateField()
    Return_date=models.DateField()
    Class=models.CharField(max_length=50,default="")
    No_of_person=models.IntegerField(default=0)

class Flights(models.Model):
    #image=models.ImageField(upload_to="airline\images",default="")
    flight_company=models.CharField(max_length=50)
    depart_time=models.TimeField()
    arrival_time=models.TimeField()
    price=models.IntegerField(default=0)

class Contact(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    message=models.CharField(max_length=120)
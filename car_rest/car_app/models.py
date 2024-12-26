from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User

# Validators
def alphanumeric(value):
    if not value.isalnum():
        raise ValidationError("Car number should be alphanumeric.")
    return value

class ShowRoom(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=100)
    
    def __str__(self):
        return self.name
class CarList(models.Model):
    car_name = models.CharField(max_length=100)
    car_decstr = models.CharField(max_length=500)
    active = models.BooleanField(default=False)
    car_number = models.CharField(max_length=100,blank=True,null=True,validators=[alphanumeric])
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    ShowRoomlist = models.ForeignKey(ShowRoom,on_delete=models.CASCADE,related_name='showrooms',null=True)
    
    def __str__(self):
        return self.car_name
    

class Reivew(models.Model):
    apiUser = models.ForeignKey(User,on_delete=models.CASCADE)
    raiting = models.IntegerField(validators=[MinValueValidator,MaxValueValidator])
    comments = models.CharField(max_length=200,null=True)
    car = models.ForeignKey(CarList, null=True,on_delete=models.CASCADE,related_name='reiviews')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "The rating of the " + self.car.car_name + " is " + str(self.raiting)
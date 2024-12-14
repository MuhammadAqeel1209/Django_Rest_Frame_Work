from django.db import models

class CarList(models.Model):
    car_name = models.CharField(max_length=100)
    car_decstr = models.CharField(max_length=500)
    active = models.BooleanField(default=False)
    car_number = models.CharField(max_length=100,blank=True,null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)

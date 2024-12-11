from django.db import models


class CarList(models.Model):
    car_name = models.CharField(max_length=100)
    car_decstr = models.CharField(max_length=500)
    active = models.BooleanField(default=False)
from django.db import models
from django.contrib import admin
class Car(models.Model):
    car_name= models.CharField(max_length=300)
    car_model = models.CharField(max_length=100)
    release_date = models.DateField()
    milage = models.IntegerField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    colour = models.CharField()

class CarAdmin(admin.ModelAdmin):
    list_display = ('car_name', 'car_model', 'release_date', 'milage', 'rating','colour')

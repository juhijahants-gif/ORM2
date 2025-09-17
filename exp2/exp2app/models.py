from django.db import models
from django.contrib import admin
class Car2(models.Model):
    car_name = models.CharField()
    car_model = models.CharField()
    release_date = models.DateField()
    millage = models.IntegerField()
    colour = models.CharField()

class Car2Admin(admin.ModelAdmin):
    list_display = ('car_name', 'car_model', 'release_date', 'millage', 'colour')

from django.db import models

# Create your models here.

class Car_Varity(models.Model):
    Car_Varity_Type = [
        ('HD','Hondai'),
        ("WG" , "Wganor"),
        ('BMW' , 'Bmw'),
        ('BU' , 'Bhugati'),
    ]

    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars/')
    type = models.CharField(max_length=3, choices=Car_Varity_Type)


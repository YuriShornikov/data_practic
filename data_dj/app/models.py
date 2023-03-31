from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    cost = models.CharField(max_length=20)

class People(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=30)
    date_age = models.CharField(max_length=10)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
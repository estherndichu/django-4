from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    occupants = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

class User(models.Model):
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    hood = models.ForeignKey(Neighborhood,models.CASCADE)

    def __str__(self):
        return self.name.first_name


class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE)
    email =models.EmailField()

    def __str__(self):
        return self.name
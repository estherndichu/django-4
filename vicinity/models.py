from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Neighborhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    occupants = models.ForeignKey(User,on_delete=models.CASCADE)
    admin = models.ForeignKey('Profile', on_delete=models.CASCADE)
    health_hotline = models.IntegerField(blank=True, null=True)
    police_hotline = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return f'{self.name}'

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def search_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=50,blank=True)
    email = models.EmailField()
    location =models.CharField(max_length=80)
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE, null=True,related_name='members', blank=True)

    def __str__(self):
        return self.name

def create_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

post_save.connect(create_profile, sender = User)        


class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='owner')
    hood = models.ForeignKey(Neighborhood,on_delete=models.CASCADE, related_name='business')
    email =models.EmailField()

    def __str__(self):
        return self.name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()
    
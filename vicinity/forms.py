from django import forms
from .models import Neighborhood, Profile, Business, Post
from django.contrib.auth.models import User

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude=('admin',)      

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user', 'hood')

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'hood')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "details"] 
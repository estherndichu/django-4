from django import forms
from .models import Neighborhood, Profile, Business
from django.contrib.auth.models import User

class NeighborhoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude=('admin',)      
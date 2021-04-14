from django.shortcuts import render,redirect, get_object_or_404
from .models import Neighborhood, Profile, Business
from .forms import NeighborhoodForm,ProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    vicinity = Neighborhood.objects.all()
    return render(request,'hood/index.html',{'vicinity':vicinity})
    
def new_vicinity(request):
    if request.method == 'POST':
        form = NeighborhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('index')
    else:
        form = NeighborhoodForm()

    return render(request, 'hood/new_vicinity.html', {'form': form})

def profile(request):
    current_user_id = request.user.id
    user_profile = Profile.objects.get(user_id=current_user_id)
    
    try:
        profile = Profile.objects.get(user_id=current_user_id)
    except Profile.DoesNotExist:
        return redirect(update_profile)    

    return render(request, 'hood/profile.html', {"user_profile": user_profile},)


def update_profile(request):
    current_user_id = request.user.id
    user_profile = Profile.objects.get(user_id=current_user_id)
    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid(): 

            user_profile.name = form.cleaned_data.get('name')
            user_profile.email = form.cleaned_data.get('email')
            user_profile.location = form.cleaned_data.get('location')

            user_profile.save()
        return redirect(profile)

    else:
        form = ProfileForm()
    return render(request, 'hood/update_profile.html', {"form": form})    


def join(request, id):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighbourhood = neighborhood
    request.user.profile.save()
    return redirect('index')

def leave(request, id):
    hood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('index')    

def single_hood(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    return render(request,'hood/single.html',{'hood':hood})    
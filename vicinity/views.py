from django.shortcuts import render
from .models import Neighborhood, Profile, Business
from .forms import NeighborhoodForm

# Create your views here.
def index(request):
    vicinity = Neighborhood.objects.all()
    return render(request,'hood/index.html',{'vicinity':vicinity})
    
def new_vicinity(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()
            return redirect('index')
    else:
        form = NeighbourHoodForm()

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
    user = User.objects.get(username=username)
    if request.method == 'POST':

        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid(): 
            form.save()
        return redirect(profile)

    else:
        form = ProfileForm()
    return render(request, 'hood/update_profile.html', {"form": form})    


def join(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('index')

def leave(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('index')    
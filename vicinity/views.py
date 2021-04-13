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

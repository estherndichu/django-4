from django.shortcuts import render
from .models import Neighborhood, User, Business
from .forms import NeighborhoodForm

# Create your views here.
def index(request):
    return render(request,'vicinity/index.html')
    
def new_vicinity(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('index')
    else:
        form = NeighbourHoodForm()
    return render(request, 'vicinity/vicinity.html', {'form': form})


from django.shortcuts import render
from .models import Neighborhood, Profile, Business
from .forms import NeighborhoodForm

# Create your views here.
def index(request):
    vicinity = Neighborhood.objects.all()
    return render(request,'vicinity/index.html',{'vicinity':vicinity})
    
def new_vicinity(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.save()
            return redirect('index')
    else:
        form = NeighbourHoodForm()

    return render(request, 'vicinity/vicinity.html', {'form': form})

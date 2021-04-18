from django.shortcuts import render,redirect, get_object_or_404
from .models import Neighborhood, Profile, Business, Post
from .forms import NeighborhoodForm,ProfileForm, BusinessForm,PostForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    vicinity = Neighborhood.objects.all()
    return render(request,'hood/index.html',{'vicinity':vicinity})

@login_required(login_url='/accounts/login/')   
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

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user_id = request.user.id
    user_profile = Profile.objects.get(user_id=current_user_id)
    
    try:
        profile = Profile.objects.get(user_id=current_user_id)
    except Profile.DoesNotExist:
        return redirect('update_profile')    

    return render(request, 'hood/profile.html', {"user_profile": user_profile},)

@login_required(login_url='/accounts/login/')
def join(request, id):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('index')

@login_required(login_url='/accounts/login/')
def leave(request, id):
    hood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('index')    

@login_required(login_url='/accounts/login/')
def single_hood(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    business = Business.objects.filter(hood = hood)
    posts = Post.objects.filter(hood=hood)
    return render(request,'hood/single.html',{'hood':hood, 'business':business, 'posts':posts})   

@login_required(login_url='/accounts/login/')
def business(request,hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.user = current_user
            biz.hood = hood
            biz.save()
        return redirect('single_hood', hood.id)
    else:
        form = BusinessForm(auto_id=False)
    return render(request, 'hood/business.html', {"form": form})     

@login_required(login_url='/accounts/login/')
def post(request):
    user = Profile.objects.get(user=request.user.id)
    posts = Post.objects.all().filter(hood=user.neighborhood)
    current_user = request.user
    if request.method == 'POST':
        hood = Neighborhood.objects.get(name=user.neighborhood)
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.save(commit=False)
            title.author = current_user
            title.hood = hood
            title.save()
            return redirect('single_hood', hood.id)
    else:
        form = PostForm
    return render(request, 'hood/post.html', {'posts':posts, "form": form})      
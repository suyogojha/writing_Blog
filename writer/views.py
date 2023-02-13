from django.shortcuts import render, redirect
from .models import Profile
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
# Create your views here.

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'writer/profile.html', context)

def account(request):
    useraccount = request.user.profile
    context = {'account': useraccount}
    return render(request, 'writer/account.html', context)

def registration(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your account has been created successfully')
            return redirect('signin')
    context = {'form': form}
    return render(request, 'writer/registration.html', context)

def signin(request):
    
    if request.user.is_authenticated:
        return redirect("account")
    
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.warning(request, 'Invalid Credentials')
    return render(request, 'writer/login.html')

def signout(request):
    logout(request)
    return redirect('signin')

@login_required(login_url=login)
def updateProfile(request):
    profile = request.user.profile
    form = EditProfileForm(instance=profile)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance = profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile looks good')
            return redirect('account')
    context = {'form': form}
    return render(request, 'writer/profile-update.html', context)

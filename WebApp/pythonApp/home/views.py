from django.shortcuts import render,redirect
#from .forms import RegistrationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from home.models import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

def home(request):
    return render(request, 'page/home.html', {}) 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Tên người dùng hoặc mật khẩu không đúng')
    return render(request, 'page/login.html', {})

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect the user after saving
    return render(request, 'page/register.html', {'form': form})

def base(request):
    return render(request, 'page/base.html', {})   








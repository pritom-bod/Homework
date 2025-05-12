from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import userForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def userCreate(request):
    if request.method == 'POST':
        form = userForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = userForm()
    return render(request, 'auth/register.html', {'form':form})

def userLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form':form})
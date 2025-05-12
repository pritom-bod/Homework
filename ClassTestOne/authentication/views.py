from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import userForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
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

def logout_form(request):
    logout(request)
    return HttpResponseRedirect('login')


#change password with old password

def change_with_old(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return render(request, 'auth/success.html')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'auth/withold.html', {'form':form})
    else:
        return HttpResponseRedirect('login')
    
#change password without old password

def without_old(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data= request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return render(request, 'auth/success.html')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'auth/withoutold.html', {'form':form})
    else:
        return HttpResponseRedirect('login')
    



#success massage
def success(request):
    return render(request, 'auth/success.html')
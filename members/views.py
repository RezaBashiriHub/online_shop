from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm
from django.contrib.auth.models import User
from django import forms

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
    
        if user is not None:
            messages.success(request,("با موفقیت وارد شدید"))
            login(request, user)
            return redirect('homepage')
        
        else:
            messages.success(request,("اشتباهی رخ داده دوباره تلاش کنید."))
            return redirect('login')

    else:
        return render(request, 'registration/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,("با موفقیت از حساب خارج شدید!"))
    return redirect('homepage')

def signup_user(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password=password)
            login(request,user)
            messages.success(request, ("با موفقیت ثبت نام شدید!"))
            return redirect('homepage')
        else:
            messages.success(request, ('اشتباهی در ثبت نام پیش امده لطفا دوباره امتحان کنید!'))
            return redirect('signup')
    else:
        form = RegisterUserForm()

    return render(request, 'registration/signup.html', {
        'form': form,
    })
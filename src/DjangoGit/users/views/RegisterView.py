from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms.RegisterForm import UserRegisterForm
from django.contrib.auth import login
from django.contrib.auth.models import User

def register(request):
    if request.user.is_authenticated:
        return render(request, 'GitHub/home.html')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            new_user = User.objects.get(username=username)
            login(request, new_user)
            return redirect('home')
        else:
            messages.error(request, 'Unable to register! Make sure username is unique.')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'register_form': form})

def set_redirect(request):
    return redirect('/users/register')

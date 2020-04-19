from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages

def log_out(request):
    logout(request)
    return redirect("/users")
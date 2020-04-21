from django.shortcuts import render, redirect
from DjangoGit.users.views import RegisterView
import requests
from django.http import HttpResponse
from ..services import Gitoauth, GetGitRepos
from ... import application_properties

# Create your views here.
def git_authorize(request):
    redirect_url = 'http://localhost:8000/'
    return redirect('https://github.com/login/oauth/authorize?client_id='+application_properties.client_id+'&scope=public_repo&'+redirect_url)

def store_oauth(request):
    got_access_token = Gitoauth.GetAccessToken.execute(request, {'current_user':request.user})
    if got_access_token:
        return redirect('git_public_repos')
    else:    
        return redirect('home')

def public_repos(request):
    result, status_code = GetGitRepos.GetPublicRepos.execute(request, {'current_user':request.user})

    if status_code == 401:
        return redirect('home')
    context = {
            'error_status_code': status_code,
            'data':result
        }
    
    return render(request, 'GitHub/git_repositories.html', context)

def select_repo(request):
    print("entered")
    selected_repo=request.POST.get("selected_repo"," ")
    context = {
        "data":selected_repo
    }
    return render(request, 'Github/selected_repositories.html', context)
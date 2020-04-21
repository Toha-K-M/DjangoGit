from django.shortcuts import render, redirect
from DjangoGit.users.views import RegisterView
import requests, json
from django.http import HttpResponse
from ..services import Gitoauth, GetGitRepos, SaveSelectedRepo
from ... import application_properties
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def get_hook_payload(request):
    print('ngork working')
    jsondata = request.body
    print(request)
    data = json.loads(jsondata)
    print(data)
    return redirect('http://localhost:8000/git_repositories/')
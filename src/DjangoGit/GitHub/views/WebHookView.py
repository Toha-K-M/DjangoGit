from django.shortcuts import render, redirect
from DjangoGit.users.views import RegisterView
import requests, json
from django.http import HttpResponse
from django.contrib.auth.models import User

from ..services.SaveEvents import SaveEvents
from ... import application_properties
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from ..models import GitEvents

@csrf_exempt
@require_POST
def get_hook_payload(request):
    print('ngork working')
    jsondata = request.body
    print(request)
    data = json.loads(jsondata)
    gitEvents = SaveEvents.execute(request, {"current_user":request.user, "data":data})
    return redirect('http://localhost:8000/git_repositories/')

def hook_list(request):
    try:
        events = GitEvents.objects.filter(payload__repository__owner__id=request.user.gitprofile.git_id)
        context = {
            "events": events
        }
        return render(request, 'GitHub/event_list.html',context)
    except Exception as e:
        return redirect("git_repositories")
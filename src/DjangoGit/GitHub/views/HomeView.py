from django.shortcuts import render, redirect
from DjangoGit.users.views import RegisterView
# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        return render(request, 'GitHub/home.html')
    else:
        return redirect(RegisterView.register)


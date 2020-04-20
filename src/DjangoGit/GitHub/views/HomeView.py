from django.shortcuts import render, redirect
from DjangoGit.users.views import RegisterView
from ..services import Gitoauth
# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        is_linked = Gitoauth.access_token_is_valid.execute(request, {"current_user":request.user})
        if is_linked:
            return redirect('git_public_repos')
        else:
            return render(request, 'GitHub/home.html')
    else:
        return redirect(RegisterView.register)


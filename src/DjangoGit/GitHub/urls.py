from django.urls import path
from django.conf.urls import include,url
from .views import HomeView, GithubView

urlpatterns = [
    path('', HomeView.Home, name='home'),
    path('git/', GithubView.git_authorize, name='git'),
    path('git/redirect/', GithubView.store_oauth, name='git_redirect'),
    path('git_repositories/', GithubView.public_repos, name='git_public_repos'),
    path('selected_repo/', GithubView.select_repo, name='select_repo')
]
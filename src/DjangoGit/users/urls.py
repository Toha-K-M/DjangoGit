from django.urls import path
from django.conf.urls import include,url
from django.contrib.auth import views as auth_views
from .views import RegisterView, LogoutView
urlpatterns = [
    path('register/', RegisterView.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.log_out, name='logout'),
    path('', RegisterView.set_redirect)
]
from django.urls import path
from django.conf.urls import include,url
from .views.HomeView import HomeView
urlpatterns = [
    path('', HomeView, name='home'),
]
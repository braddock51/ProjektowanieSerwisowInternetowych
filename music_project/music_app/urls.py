from django.urls import path
from music_app import views

urlpatterns = [
    path('', views.index, name='index')
]
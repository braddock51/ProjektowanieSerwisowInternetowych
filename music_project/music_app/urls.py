from django.urls import path
from music_app import views


urlpatterns = [
    path('account/register', views.UserCreate.as_view(), name=views.UserCreate.name ),
]
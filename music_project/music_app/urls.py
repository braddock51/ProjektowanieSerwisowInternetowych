from django.urls import path
from music_app import views


urlpatterns = [
    path('account/register', views.UserCreate.as_view(), name=views.UserCreate.name ),
    path('users/<int:pk>', views.UsersList.as_view(), name=views.UsersList.name ),
    path('songs', views.SongList.as_view(), name=views.SongList.name),
    path('songs/<int:pk>', views.SongDetail.as_view(), name=views.SongDetail.name),
    path('playlists', views.PlaylistList.as_view(), name=views.PlaylistList.name),
    path('playlists/<int:pk>', views.PlaylistDetail.as_view(), name=views.PlaylistDetail.name),
    path('playlists-songs', views.SongInThePlaylist.as_view(), name=views.SongInThePlaylist.name),
]

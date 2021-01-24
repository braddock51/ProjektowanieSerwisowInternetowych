from django.urls import path
from music_app import views

urlpatterns = [
    path('artists', views.ArtistList.as_view()),
    path('artists/<int:pk>', views.ArtistDetail.as_view()),
    path('albums', views.AlbumList.as_view()),
    path('albums/<int:pk>', views.AlbumDetail.as_view()),
    path('songs', views.SongList.as_view()),
    path('songs/<int:pk>', views.SongDetail.as_view()),
    path('playlists', views.PlaylistList.as_view()),
    path('playlists/<int:pk>', views.PlaylistDetail.as_view()),
    path('playlists-songs', views.PlaylistSongList.as_view()),
    path('playlists-songs/<int:pk>', views.PlaylistSongDetail.as_view()),
]
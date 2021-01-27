from rest_framework import generics
from .models import Song, Playlist, User, SongPlaylist
from .serializers import SongSerializer, PlaylistSerializer, UserSerializer, SongPlaylistSerializer
from rest_framework import permissions

class UsersList(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'users-list'

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-create'
    permission_classes = (permissions.AllowAny, )


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    name = 'song-detail'

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    name = 'song-list'

class PlaylistDetail(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    name = 'playlist-detail'

class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    name = 'playlist-list'
    
class SongInThePlaylist(generics.ListCreateAPIView):
    queryset = SongPlaylist.objects.all()
    serializer_class = SongPlaylistSerializer
    name = 'songs-in-the-playlists'  






    
from rest_framework import generics
from .models import Song, Playlist, User, SongPlaylist
from .serializers import SongSerializer, PlaylistSerializer, UserSerializer, SongPlaylistSerializer
from rest_framework import permissions
from rest_framework.reverse import reverse
from rest_framework.response import Response

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = [permissions.IsAuthenticated]
    
class UsersList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'users-list'
    search_fields = ['name']
    ordering_fields = ['name']
    permission_classes = [permissions.IsAdminUser]



class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-create'
    permission_classes = [permissions.AllowAny]


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    name = 'song-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    name = 'song-list'
    filterset_fields = ['artist', 'album']
    search_fields = ['track']
    ordering_fields = ['track', 'artist', 'album']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PlaylistDetail(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    name = 'playlist-detail'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    name = 'playlist-list'
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
class SongInThePlaylist(generics.ListCreateAPIView):
    queryset = SongPlaylist.objects.all()
    serializer_class = SongPlaylistSerializer
    name = 'songs-in-the-playlists' 
    filterset_fields = ['id_playlist'] 
    ordering_fields = ['id_playlist']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'users-list': reverse(UsersList.name, request=request),
            'user-create': reverse(UserCreate.name, request=request),
            'song-list': reverse(SongList.name, request=request),
            'playlist-list': reverse(PlaylistList.name, request=request),
            'songs-in-the-playlists': reverse(SongInThePlaylist.name, request=request)
        })






    
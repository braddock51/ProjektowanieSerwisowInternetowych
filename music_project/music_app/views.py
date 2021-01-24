from rest_framework import generics
from .models import Song, Playlist, User, SongPlaylist
from .serializers import SongSerializer, PlaylistSerializer, UserSerializer
from rest_framework import permissions

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-create'
    permission_classes = (permissions.AllowAny, )






    
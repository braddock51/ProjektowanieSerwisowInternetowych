from rest_framework import generics
from .models import Artist, Album, Song, Playlist, Playlist_Song
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, PlaylistSerializer, PlaylistSongSerializer


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    
class PlaylistList(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer

class PlaylistSongList(generics.ListCreateAPIView):
    queryset = Playlist_Song.objects.all()
    serializer_class = PlaylistSongSerializer


class PlaylistSongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist_Song.objects.all()
    serializer_class = PlaylistSongSerializer



    
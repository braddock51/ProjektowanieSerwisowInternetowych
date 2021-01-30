from rest_framework import serializers
from .models import Song, Playlist, User, SongPlaylist
from django.contrib.auth.models import User


class SongSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Song
        fields = ['pk', 'url', 'track', 'artist', 'album', 'length']
        

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    
    id_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    class Meta:
        model = Playlist
        fields = ['pk', 'url', 'name', 'number_of_songs', 'id_user']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'password','first_name', 'last_name', 'email', 'last_login', 'date_joined']
    

class SongPlaylistSerializer(serializers.ModelSerializer):
    id_song = serializers.SlugRelatedField(queryset=Song.objects.all(), slug_field='track')
    id_playlist = serializers.SlugRelatedField(queryset=Playlist.objects.all(), slug_field='name')
    class Meta:
        model = SongPlaylist
        fields = ['pk', 'id_song', 'id_playlist']







    


    





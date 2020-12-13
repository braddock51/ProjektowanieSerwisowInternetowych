from rest_framework import serializers
from .models import Artist, Album, Song, Playlist, Playlist_Song

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id', 'name', 'country']

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'name', 'number_of_songs', 'type_of_music', 'artist_id']

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'track', 'length', 'album_id']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'number_of_songs']

class PlaylistSongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist_Song
        fields = ['song_id', 'playlist_id']

    


    





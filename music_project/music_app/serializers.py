from rest_framework import serializers
from .models import Song, Playlist, User, SongPlaylist



class SongSerializer(serializers.ModelSerializer):
    song_name = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='songs-in-the-playlists' )
    class Meta:
        model = Song
        fields = ['pk','track', 'artist', 'album', 'length']
        

class PlaylistSerializer(serializers.HyperlinkedModelSerializer):
    playlist_name = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='songs-in-the-playlists' )
    id_user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    class Meta:
        model = Playlist
        fields = ['pk', 'name', 'number_of_songs', 'id_user']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='playlist-list')
    class Meta:
        model = User
        fields = ['pk', 'name', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class SongPlaylistSerializer(serializers.ModelSerializer):
    id_song = serializers.SlugRelatedField(queryset=Song.objects.all(), slug_field='track')
    id_playlist = serializers.SlugRelatedField(queryset=Playlist.objects.all(), slug_field='name')
    class Meta:
        model = SongPlaylist
        fields = ['pk', 'id_song', 'id_playlist']




    


    





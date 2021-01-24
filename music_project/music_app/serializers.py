from rest_framework import serializers
from .models import Song, Playlist, User, SongPlaylist



class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id','track', 'artist', 'album', 'length']

class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['id', 'name', 'number_of_songs', 'id_user']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user






    


    





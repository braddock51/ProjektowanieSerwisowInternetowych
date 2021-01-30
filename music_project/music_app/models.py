from django.db import models
import os, hashlib, binascii
from django.contrib.auth.models import User




class Song(models.Model):
    track = models.CharField(max_length=50, unique=True)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=70)
    length = models.TimeField(default='00:00:00')

    class Meta:
        ordering = ('track',)

    

    def __str__(self):
        return str(self.track)
 
  
class Playlist(models.Model):
    name = models.CharField(max_length=70)
    number_of_songs=models.IntegerField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    class Meta:
        ordering = ('name',)


    def __str__(self):
        return str(self.name)

class SongPlaylist(models.Model):
    id_song = models.ForeignKey(Song, on_delete=models.CASCADE, related_name='song_name')
    id_playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE, related_name='playlist_name')

    class Meta:
        ordering = ('id_playlist',)


    def __str__(self):
        return str(self.id_playlist)



    
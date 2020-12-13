from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=45, unique=True)
    country = models.CharField(max_length=45)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=45, unique=True)
    number_of_songs = models.IntegerField()
    type_of_music = models.CharField(max_length=45)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Song(models.Model):
    track = models.CharField(max_length=45, unique=True)
    length = models.TimeField()
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.track

class Playlist(models.Model):
    name = models.CharField(max_length=45, unique=True)
    number_of_songs = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Playlist_Song(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    playlist_id = models.ForeignKey(Playlist, on_delete=models.CASCADE)

    
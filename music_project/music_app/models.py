from django.db import models


class Song(models.Model):
    track = models.CharField(max_length=50, unique=True)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=70)
    length = models.TimeField()
    

    def __str__(self):
        return str(self.track)

class User(models.Model):
    name = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

class Playlist(models.Model):
    name = models.CharField(max_length=70)
    number_of_songs=models.IntegerField()
    idUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class SongPlaylist(models.Model):
    idSong = models.ForeignKey(Song, on_delete=models.CASCADE)
    idPlaylist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    
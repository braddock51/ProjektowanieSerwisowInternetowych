from django.db import models
import os, hashlib, binascii



def hash_password(password):
    
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

class Song(models.Model):
    track = models.CharField(max_length=50, unique=True)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=70)
    length = models.TimeField()
    

    def __str__(self):
        return str(self.track)

class User(models.Model):
    name = models.CharField(max_length=15, unique=True)
    password = models.CharField(max_length=10000)
    email = models.CharField(max_length=50)

    def set_password(self, password):
        self.password = hash_password(password)

    def __str__(self):
        return str(self.name)
    
    
        


class Playlist(models.Model):
    name = models.CharField(max_length=70)
    number_of_songs=models.IntegerField()
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class SongPlaylist(models.Model):
    id_song = models.ForeignKey(Song, on_delete=models.CASCADE)
    id_playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)



    
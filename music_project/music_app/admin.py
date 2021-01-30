from django.contrib import admin
from .models import Song, Playlist, SongPlaylist

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(SongPlaylist)



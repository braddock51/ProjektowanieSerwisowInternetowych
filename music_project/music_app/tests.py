from rest_framework.test import APITestCase
from . import views
from .models import Song
from rest_framework import status
from rest_framework.reverse import reverse
from django.utils.http import urlencode
from django import urls

class SongTests(APITestCase):
    def post_song(self, track, artist, album, length):
        url = reverse(views.SongList.name)
        data = {
            'track': track,
            'artist': artist,
            'album': album,
            'length': length
        }
        response = self.client.post(url, data, format='json')
        return response
    
    def test_post_and_get_song(self):
        track = 'Some track'
        artist = 'some artist'
        album = 'some album'
        length = '12:01:00'
        response = self.post_song(track, artist, album, length)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Song.objects.count(), 1)
        self.assertEqual(Song.objects.get().track, track)
    
    def test_post_existing_song(self):
        track = 'Some track'
        artist = 'some artist'
        album = 'some album'
        length = '12:01:00'
        response_one = self.post_song(track, artist, album, length)
        self.assertEqual(response_one.status_code, status.HTTP_201_CREATED)
        response_two = self.post_song(track, artist, album, length)
        self.assertEqual(response_two.status_code, status.HTTP_400_BAD_REQUEST)

    def test_filter_song_by_artist(self):
        song_artist_one = 'track01'
        song_artist_two = 'track02'
        self.post_song('some', song_artist_one, 'some', '00:00:00')
        self.post_song('some', song_artist_two, 'some', '00:00:00')
        filter_by_track = {'artist': song_artist_one}
        url= '{0}?{1}'.format(reverse(views.SongList.name), urlencode(filter_by_track))
        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['artist'], song_artist_one)
    
    def test_update_song(self):
        track = 'Some track'
        artist = 'some artist'
        album = 'some album'
        length = '12:01:00'
        
        
        response = self.post_song(track, artist, album, length)

        url = urls.reverse(views.SongDetail.name, None, {response.data['pk']})
        updated_track = 'new track'
        data = {
            'track': updated_track,
            'artist': artist,
            'album': album,
            'length': length
        }
        patch_response = self.client.patch(url, data, format='json')

        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        self.assertEquals(patch_response.data['track'], updated_track)

    




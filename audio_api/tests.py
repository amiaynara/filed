import json

from django.test import TestCase
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Song, Podcast, AudioBook
from .serializers import SongSerializer, PodcastSerializer, AudioBookSerializer

# Create your tests here.
class FileTestCase(APITestCase):

    def test_update_song(self):
        data =  {
                    "name": "bad luck",
                    "duration": 234,
                }
        response = self.client.post('/song/', data)
        data['name'] = 'new_name'
        id = response.data['id']
        endpoint = '/song/' + str(id) + '/'
        response = self.client.put(endpoint, data)        # by 
        self.assertEqual(response.status_code, 200) 

    def test_update_podcast(self):
        data =  {
                "name": "Dooji wari",
                "duration": 234,
                "host": "Lala",
                "prtcpnts": ["Amiay", "Shreya", "Nilanshi"]
                }
        response = self.client.post('/podcast/', data)         # first create an object which we will update later
        data['name'] = 'teesari waari'
        id = response.data['id']
        endpoint = '/podcast/' + str(id) + '/'
        response = self.client.put(endpoint , data)
        self.assertEqual(response.status_code, 200)

    def test_update_audiobook(self):
        data = {
                "title": "Edge",
                "author": "Sagar",
                "narrator": "Sameer",
                "duration": 234,
                }
        response = self.client.post('/audiobook/', data)
        data['title'] = 'Cutting Edge'
        id = response.data['id']
        endpoint = '/audiobook/' + str(id) + '/'
        response = self.client.put(endpoint, data)
        self.assertEqual(response.status_code, 200)

    def test_delete_song(self):
        data =  {
                    "name": "very good luck",
                    "duration": 234,
                }
        response = self.client.post('/song/', data)
        id = response.data['id']
        endpoint = '/song/' + str(id) + '/'
        response = self.client.delete(endpoint)        # by 
        self.assertEqual(response.status_code, 204)

    def test_delete_podcast(self):
        data =  {
                "name": "pahli wari",
                "duration": 234,
                "host": "Lala",
                "prtcpnts": ["Amiay", "Shreya", "Nilanshi"]
                }
        response = self.client.post('/podcast/', data)         # first create an object which we will update later
        id = response.data['id']
        endpoint = '/podcast/' + str(id) + '/'
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, 204)

    def test_delete_audiobook(self):
        # create create before deleting
        data = {
                "title": "hi Leading Edge",
                "author": "Sagar",
                "narrator": "Sameer",
                "duration": 234,
                }
        response = self.client.post('/audiobook/', data)        # create an audiobook object
        id = response.data['id']
        endpoint = '/audiobook/' + str(id) + '/'
        response = self.client.delete(endpoint)
        self.assertEqual(response.status_code, 204)

    def test_get_song(self):
        response = self.client.get('/song/')
        self.assertEqual(response.status_code, 200) 

    def test_get_podcast(self):
        response = self.client.get('/podcast/')
        self.assertEqual(response.status_code, 200) 

    def test_get_audiobook(self):
        response = self.client.get('/audiobook/')
        self.assertEqual(response.status_code, 200) 

    def test_get_documentation(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200) 

    def test_create_song(self):
        data =  {
                    "name": "luck",
                    "duration": 234,
                }
        response = self.client.post('/song/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_podcast(self):
        data =  {
                "name": "luck",
                "duration": 234,
                "host": "Manish",
                "prtcpnts": ["Amiay", "Aman", "Nilanshi"]
                }
        response = self.client.post('/podcast/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_audiobook(self):
        data = {
                "title": "Edge",
                "author": "Sagar",
                "narrator": "Sameer",
                "duration": 234,
                }
        response = self.client.post('/audiobook/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


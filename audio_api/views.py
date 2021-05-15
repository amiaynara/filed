from django.shortcuts import render
from django.http import JsonResponse                    # to send json response
from django.views.decorators.csrf import csrf_exempt    # not a good idea to exempt, but okay for learning
from rest_framework.parsers import JSONParser           # parses request object

# drf ways of handling
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import PodcastForm
from .models import Song, Podcast, AudioBook
from .serializers import SongSerializer
# Create your views here.
# here is some changes
def HomeView(request):
    form = PodcastForm()
    return render(request, 'audio_api/home.html', {'form': form})

@api_view(['GET', 'POST'])
def SongListView(request, format=None):
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def SongDetailView(request, pk, format=None):
        try:
            song = Song.objects.get(pk=pk)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = SongSerializer(song)
            data = serializer.data
            return Response(data, status=200)

        elif request.method == 'PUT':
            serializer = SongSerializer(song, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            song.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


# the class view implementation of the crud
from .serializers import SongSerializer, AudioBookSerializer, PodcastSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class FileListView(APIView):
    """
    List all the AudioBooks
    """
    def get(self, request, type, format=None):
        if type=="audiobook":
            books = AudioBook.objects.all()
            serializer = AudioBookSerializer(books, many=True)
        elif type == "song":
            songs = Song.objects.all()
            serializer = SongSerializer(songs, many=True)
        elif type == "podcast":
            podcasts = Podcast.objects.all()
            serializer = PodcastSerializer(podcasts, many=True) 
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({"Success":"See home page for instructions", "result": serializer.data})

    def post(self, request, type, format=None):
        if type=="audiobook":
            serializer = AudioBookSerializer(data=request.data)
        elif type == "song":
            serializer = SongSerializer(data=request.data)
        elif type == "podcast":
            serializer = PodcastSerializer(data=request.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileDetailView(APIView):
    def get(self, request, type, pk, format=None):
        try:
            if type == "song":
                song = Song.objects.get(pk=pk)
                serializer = SongSerializer(song, data=request.data)
            elif type == "podcast":
                podcast = Podcast.objects.get(pk=pk)
                serializer = PodcastSerializer(podcast, data=request.data)
            elif type == "audiobook":
                audiobook = AudioBook.objects.get(pk=pk)
                serializer = AudioBookSerializer(audiobook, data=request.data)
            else:
                return Response(status = status.HTTP_404_NOT_FOUND)
        except:
            return Response(status = status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

                
    def put(self, request, type, pk, format=None):
        try:
            if type == "song":
                song = Song.objects.get(pk=pk)
                serializer = SongSerializer(song, data=request.data)
            elif type == "podcast":
                podcast = Podcast.objects.get(pk=pk)
                serializer = PodcastSerializer(podcast, data=request.data)
            elif type == "audiobook":
                audiobook = AudioBook.objects.get(pk=pk)
                serializer = AudioBookSerializer(audiobook, data=request.data)
            else:
                return Response(status = status.HTTP_404_NOT_FOUND)
        except:
            return Response(status = status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, type, pk, format=None):
        try:
            if type == "song":
                file = Song.objects.get(pk=pk)
                serializer = SongSerializer(file, data=request.data)
            elif type == "podcast":
                file = Podcast.objects.get(pk=pk)
                serializer = PodcastSerializer(file, data=request.data)
            elif type == "audiobook":
                file = AudioBook.objects.get(pk=pk)
                serializer = AudioBookSerializer(file, data=request.data)
            else:
                return Response(status = status.HTTP_404_NOT_FOUND)
        except:
            return Response(status = status.HTTP_404_NOT_FOUND)
        file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


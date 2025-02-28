from rest_framework import viewsets
from .models import Album, Music
from .serializers import AlbumSerializer, MusicSerializer
from django.shortcuts import render
from django.http import HttpResponse

class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer

def home(request):
    return HttpResponse("Bem-vindo ao Music Streaming App!")

def react_app(request):
    return render(request, 'index.html')    

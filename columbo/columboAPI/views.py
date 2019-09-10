from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EpisodeSerializer, SeasonSerializer, CharacterSerializer, ActorSerializer, DirectorSerializer, WriterSerializer
from .models import Episode, Season, Character, Actor, Writer, Director

# Create your views here.

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all().order_by('season')
    serializer_class = EpisodeSerializer


class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all().order_by('number')
    serializer_class = SeasonSerializer



class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('last_name')
    serializer_class = CharacterSerializer



class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all().order_by('last_name')
    serializer_class = ActorSerializer



class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all().order_by('last_name')
    serializer_class = DirectorSerializer

class WriterViewSet(viewsets.ModelViewSet):
    queryset = Writer.objects.all().order_by('last_name')
    serializer_class = WriterSerializer

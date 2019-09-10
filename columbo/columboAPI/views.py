from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EpisodeSerializer
from .models import Episode

# Create your views here.

class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all().order_by('season')
    serializer_class = EpisodeSerializer

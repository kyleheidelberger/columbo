from rest_framework import serializers
from .models import Episode, Season, Character, Actor, Writer, Director


class EpisodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episode
        fields = ('title', 'season', 'air_date', 'director', 'writer', 'season_num', 'series_num', 'runtime', 'fun_facts', 'ep_image')


class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ('title', 'first_name', 'last_name', 'occupation', 'murderer', 'victim', 'played_by', 'appears_in', 'fun_facts')


class SeasonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Season
        fields = ('number', 'episodes', 'year_aired')


class ActorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Actor
        fields = ('first_name', 'last_name', 'fun_facts')


class WriterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Writer
        fields = ('first_name', 'last_name')


class DirectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Director
        fields = ('first_name', 'last_name')

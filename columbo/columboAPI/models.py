from django.db import models

# Create your models here.

class Episode(models.Model):
    title = models.CharField(max_length=100)
    season = models.PositiveIntegerField
    air_date = models.DateField
    director = models.ForeignKey('Director')
    writer = models.ForeignKey('Writer')
    season_num = models.PositiveIntegerField
    series_num
    runtime = models.DurationField
    fun_facts = models.TextField
    ep_image = models.URLField

    def __str__(self):
        return self.title

class Season(models.Model):
    number
    episodes
    year_aired

class Character(models.Model):
    title
    first_name
    last_name
    played_by
    appears_in
    fun_facts

class Actor(models.Model):
    first_name
    last_name
    appeared_as
    appeared_in
    fun_facts

class Director(models.Model):
    first_name
    last_name
    worked_on

class Writer(models.Model):
    first_name
    last_name
    worked_on
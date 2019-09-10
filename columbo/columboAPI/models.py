from django.db import models

# Create your models here.


class Episode(models.Model):
    title = models.CharField(max_length=100)
    season = models.PositiveIntegerField
    air_date = models.DateField
    director = models.ForeignKey('Director', on_delete=models.CASCADE)
    writer = models.ForeignKey('Writer', on_delete=models.CASCADE)
    season_num = models.PositiveIntegerField
    series_num = models.PositiveIntegerField
    runtime = models.DurationField
    fun_facts = models.TextField
    ep_image = models.URLField

    def __str__(self):
        return self.title


class Season(models.Model):
    number = models.PositiveIntegerField
    episodes = models.PositiveIntegerField
    year_aired = models.PositiveIntegerField

    def __str__(self):
        return self.number


class Character(models.Model):
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    murderer = models.BooleanField
    victim = models.BooleanField
    played_by = models.ForeignKey('Actor', on_delete=models.CASCADE)
    appears_in = models.ForeignKey(Episode, on_delete=models.CASCADE)
    fun_facts = models.TextField

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fun_facts = models.TextField

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Writer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

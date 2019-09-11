from django.db import models

# Create your models here.


class Episode(models.Model):
    title = models.CharField(max_length=100)
    season = models.PositiveIntegerField(default=00)
    air_date = models.DateField(null=True, blank=True)
    director = models.ManyToManyField('Director', default='')
    writer = models.ManyToManyField('Writer', default='')
    season_num = models.PositiveIntegerField(default=00)
    series_num = models.PositiveIntegerField(default=00)
    runtime = models.DurationField(null=True, blank=True)
    fun_facts = models.TextField(null=True, blank=True)
    ep_image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Season(models.Model):
    number = models.PositiveIntegerField(default=00)
    episodes = models.PositiveIntegerField(default=00)
    year_aired = models.PositiveIntegerField(default=00)

    def __str__(self):
        return f'{self.number}'


class Character(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    occupation = models.CharField(max_length=100, null=True, blank=True)
    murderer = models.BooleanField(null=True, blank=True)
    victim = models.BooleanField(null=True, blank=True)
    played_by = models.ForeignKey('Actor', on_delete=models.CASCADE, default='')
    appears_in = models.ForeignKey(Episode, on_delete=models.CASCADE, default='')
    fun_facts = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    fun_facts = models.TextField(null=True, blank=True)

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

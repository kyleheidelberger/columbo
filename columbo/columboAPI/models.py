from django.db import models

# Create your models here.

class Episode(models.Model):
    title = models.CharField(max_length=100)
    season = models.CharField(max_length=2)

    def __str__(self):
        return self.title
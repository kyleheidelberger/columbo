from django.contrib import admin
from .models import Episode, Season, Character, Actor, Writer, Director

# Register your models here.
admin.site.register(Episode)
admin.site.register(Season)
admin.site.register(Character)
admin.site.register(Actor)
admin.site.register(Writer)
admin.site.register(Director)
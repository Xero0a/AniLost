from django.contrib import admin
from .models import Genre, Anime, Jumbotron, AnimeGenre

admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(Jumbotron)
admin.site.register(AnimeGenre)

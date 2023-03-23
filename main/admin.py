from django.contrib import admin
from .models import Genre, Anime, AnimeGenre, AnimeAdmin, GenreAdmin

admin.site.register(Anime, AnimeAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(AnimeGenre)
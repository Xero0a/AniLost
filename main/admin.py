from django.contrib import admin
from .models import Genre, Anime, Jumbotron, AnimeGenre, AnimeAdmin, GenreAdmin

admin.site.register(Anime, AnimeAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Jumbotron)
admin.site.register(AnimeGenre)
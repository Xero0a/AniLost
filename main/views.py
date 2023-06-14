from django.shortcuts import render
from django.views import View
from .models import Genre, Anime


class IndexView(View):
    """Отображает главную страницу сайта"""

    def get(self, request):
        
        animes = Anime.objects.all()
        
        return render(request, "main/index.html", {"animes": animes})


class AnimeView(View):
    """Отображает страницу с информацией по отдельному аниме"""

    def get(self, request, anime_id):

        anime = Anime.objects.get(id=anime_id)

        return render(request, "main/anime.html", {"anime": anime})


class GenreView(View):
    """Отображает страницу жанров"""

    def get(self, request):

        genres = Genre.objects.all()

        return render(request, "main/genres.html", {"genres": genres})

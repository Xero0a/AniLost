from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Genre, Anime, AnimeGenre


class IndexView(ListView):
    """Отображает главную страницу сайта"""
    
    def get(self, request):
        
        animes = Anime.objects.all()
        paginator = Paginator(animes, 3)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, "main/index.html", {"page_obj": page_obj})


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


class AnimeGenreView(View):
    """Отображает аниме выбранного жанра"""

    def get(self, request, genre_id):

        genre = Genre.objects.get(id=genre_id)

        animes = Anime.objects.filter(genre=genre_id)

        return render(request, "main/animegenre.html", {"animes": animes, "genre": genre})


class SearchAnime(ListView):
    """Поиск на сайте по названию аниме или по жанру"""

    template_name = "main/index.html"
    context_object_name ="page_obj"

    def get_queryset(self):

        return Anime.objects.filter(name__iregex=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
    
        context = super().get_context_data(*args, **kwargs)
        context["q"] = self.request.GET.get("q")

        return context
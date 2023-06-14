from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Genre, Anime


class IndexView(ListView):
    """Отображает главную страницу сайта"""
    
    def get(self, request):
        
        animes = Anime.objects.all()
        paginator = Paginator(animes, 1)

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

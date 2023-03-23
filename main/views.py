from django.shortcuts import render
from .models import Genre, Anime


def index(request):
    
    animes = Anime.objects.all()
    
    return render(request, "main/index.html", {"animes": animes})


def view_anime(request, anime_id):

    anime = Anime.objects.get(id=anime_id)

    return render(request, "main/anime.html", {"anime": anime})


def jenres(request):

    name = Genre.objects.all()
    
    return render(request, "main/jenres.html", {"name": name})

from django.shortcuts import render
from .models import Genre, Anime, Jumbotron


def index(request):
    chainsawman = [
        Anime.objects.filter(name="Человек-бензопила"),
        Anime.objects.get(name="Человек-бензопила").image
    ]

    demonslayer = [
        Anime.objects.filter(name="Клинок рассекающий демонов"),
        Anime.objects.get(name="Клинок рассекающий демонов").image
    ]

    mobpsycho = [
        Anime.objects.filter(name="Моб-психо 100"),
        Anime.objects.get(name="Моб-психо 100").image
    ]

    return render(request, "main/index.html", {"chainsawman_name": chainsawman[0], "chainsawman_image": chainsawman[1],
                                               "demonslayer_name": demonslayer[0], "demonslayer_image": demonslayer[1],
                                               "mobpsycho_name": mobpsycho[0], "mobpsycho_image": mobpsycho[1]})


def demonslayer(request):
    name = Anime.objects.filter(name="Клинок рассекающий демонов")
    genre = Anime.objects.get(name="Клинок рассекающий демонов").genre.all()
    image = Anime.objects.get(name="Клинок рассекающий демонов").image
    jumbotron = Jumbotron.objects.get(anime="2").jumbotron_image
    return render(request, "main/anime.html", {"name": name, "genre": genre, "image": image, "jumbotron": jumbotron})


def mobpsycho(request):
    name = Anime.objects.filter(name="Моб-психо 100")
    genre = Anime.objects.get(name="Моб-психо 100").genre.all()
    image = Anime.objects.get(name="Моб-психо 100").image
    jumbotron = Jumbotron.objects.get(anime="3").jumbotron_image
    return render(request, "main/anime.html", {"name": name, "genre": genre, "image": image, "jumbotron": jumbotron})


def chainsawman(request):
    name = Anime.objects.filter(name="Человек-бензопила")
    genre = Anime.objects.get(name="Человек-бензопила").genre.all()
    image = Anime.objects.get(name="Человек-бензопила").image
    jumbotron = Jumbotron.objects.get(anime="1").jumbotron_image
    return render(request, "main/anime.html", {"name": name, "genre": genre, "image": image, "jumbotron": jumbotron})


def jenres(request):
    name = Genre.objects.all()
    return render(request, "main/jenres.html", {"name": name})

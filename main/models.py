from django.db import models


class Genre(models.Model):
    name_genre = models.CharField(max_length=120)


class Anime(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField()


class AnimeGenre(models.Model):
    anime = models.ManyToManyField("Anime")
    genre = models.ManyToManyField("Genre")


class Jumbotron(models.Model):
    anime = models.ForeignKey("Anime", on_delete=models.PROTECT)
    jumbotron_image = models.ImageField()


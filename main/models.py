from django.conf.global_settings import MEDIA_ROOT
from django.db import models


class Genre(models.Model):
    name_genre = models.CharField(max_length=120, verbose_name="Жанр")

    def __str__(self):
        return self.name_genre


class Anime(models.Model):
    name = models.CharField(max_length=300, verbose_name="Аниме")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Картинка", upload_to="img/")
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.name


class Jumbotron(models.Model):
    anime = models.ForeignKey("Anime", on_delete=models.PROTECT)
    jumbotron_image = models.ImageField(upload_to="img/")
from django.conf.global_settings import MEDIA_ROOT
from django.db import models
from django.contrib import admin

class Genre(models.Model):
    name_genre = models.CharField(max_length=120, verbose_name="Жанр")

    def __str__(self):
        return self.name_genre


class Anime(models.Model):
    name = models.CharField(max_length=300, verbose_name="Аниме")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Картинка", upload_to="img/")
    genre = models.ManyToManyField(Genre, through='AnimeGenre')

    def __str__(self):
        return self.name


class AnimeGenre(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.DO_NOTHING, related_name="anime")
    genre = models.ForeignKey(Genre, on_delete=models.DO_NOTHING, related_name="genre")


class AnimeGenreInline(admin.TabularInline):
    model = AnimeGenre
    extra = 1


class AnimeAdmin(admin.ModelAdmin):
    inlines = (AnimeGenreInline,)


class GenreAdmin(admin.ModelAdmin):
    inlines = (AnimeGenreInline,)

class Jumbotron(models.Model):
    anime = models.ForeignKey("Anime", on_delete=models.DO_NOTHING)
    jumbotron_image = models.ImageField(upload_to="img/")

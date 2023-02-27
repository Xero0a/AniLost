from django.db import models

# Create your models here.
class Genre(models.Model):
    name_genre = models.CharField(max_length=120)

class Anime(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    genre = models.ForeignKey("Genre", on_delete=models.CASCADE)


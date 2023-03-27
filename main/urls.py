from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view()),
    path("anime=<anime_id>", views.AnimeView.as_view()),
    path('genres', views.GenreView.as_view())
]
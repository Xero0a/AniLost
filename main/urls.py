from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("anime=<anime_id>", views.view_anime),
    path('genres', views.jenres)
]
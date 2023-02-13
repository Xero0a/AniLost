from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("demon-slayer", views.demonslayer),
    path("mob-psycho", views.mobpsycho),
    path("chainsaw-man", views.chainsawman),
]
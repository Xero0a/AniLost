from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "main/index.html")

def demonslayer(request):
    return render(request, "main/demonslayer.html")

def mobpsycho(request):
    return render(request, "main/mob.html")

def chainsawman(request):
    return render(request, "main/chainsawman.html")
from django.shortcuts import render
from .models import Song

# Create your views here.
def home(request):
    song = Song.objects.all()
    return render(request, 'musicbeats/index.html', {'song': song})

def songs(request):
    song = Song.objects.all()
    return render(request, 'musicbeats/songs.html', {'song': song})

def songpost(request, id):
    song = Song.objects.filter(song_id=id).first()
    return render(request, 'musicbeats/songpost.html', {'song': song})
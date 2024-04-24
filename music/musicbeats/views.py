from django.shortcuts import render
from .models import Song

# Create your views here.
def home(request):
    song = Song.objects.all()
    return render(request, 'musicbeats/index.html', {'song': song})
from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Song
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


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

def login(request, user):
    return render(request, 'musicbeats/login.html')

def signup(request):
    if request.method == "POST":
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = first_name
        myuser.last_name = last_name
        myuser.save()
        user = authenticate(username = username, password = pass1)
        login(request, user)

        return redirect('/')

    return render(request, 'musicbeats/signup.html')
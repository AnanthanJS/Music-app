from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Song, Watchlater
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Case, When


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

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        from django.contrib.auth import login
        login(request, user)
        
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


def logout(request):
    logout(request)
    return redirect('home')
    

def watchlater(request):
    if request.method == "POST":
        user = request.user
        video_id = request.POST['video_id']
        watch = Watchlater.objects.filter(user = user)
        
        for i in watch:
            if video_id == i.video_id:
                message = "Your video is already added."
                break
        else:
            watchlater = Watchlater(user = user, video_id = video_id)
            watchlater.save()
            message = "Your video is successfully added."
        song = Song.objects.filter(song_id = video_id).first()        
        return render(request, f"musicbeats/songpost.html", {"song": song, "message": message})
    
    wl = Watchlater.objects.filter(user = request.user)
    ids = []
    for i in wl:
        ids.append(i.video_id)
        
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(ids)])
    song = Song.objects.filter(song_id__in=ids).order_by(preserved)
        
    return render(request, 'musicbeats/watchlater.html', {'song': song})
from django.shortcuts import render, redirect, get_object_or_404
from .models import Song

def home(request):
    if request.method == 'POST':
        search = request.POST.get('search', '').lower()
        songs = Song.objects.all()
        songs = [s for s in songs if search in s.song_name.lower() or search in s.artist_name.lower()]
    else:
        songs = Song.objects.all()
    return render(request, 'home.html', {'songs': songs})

def welcome(request):
    return render(request, 'welcome.html')

def add_song(request):
    if request.method == 'POST':
        Song.objects.create(
            song_name=request.POST['song_name'],
            artist_name=request.POST['artist_name'],
            releasedate=request.POST['releasedate'],
            url=request.POST['url'],
            views=request.POST['views']
        )
        return redirect('home')
    return render(request, 'add.html')

def edit_song(request, id):
    song = get_object_or_404(Song, id=id)
    if request.method == 'POST':
        song.song_name = request.POST['song_name']
        song.artist_name = request.POST['artist_name']
        song.releasedate = request.POST['releasedate']
        song.url = request.POST['url']
        song.views = request.POST['views']
        song.save()
        return redirect('home')
    return render(request, 'edit.html', {'song': song})

def delete_song(request, id):
    song = get_object_or_404(Song, id=id)
    song.delete()
    return redirect('home')

def song_info(request, id):
    song = get_object_or_404(Song, id=id)
    return render(request, 'info.html', {'song': song})

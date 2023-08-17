import os.path
from django.conf import settings
from django.shortcuts import render
from .models import Project, Product, Songs, Artist, \
    Single, ArtistEP, Album, albumLite, singleSong, Event, \
    Developer, News
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404

# Create your views here.
def home(request):
    projects = Project.objects.all()
    products = Product.objects.all()
    songs = Songs.objects.all()
    artist = Artist.objects.all()
    singles = Single.objects.all()
    artist_ep = ArtistEP.objects.all()
    context = {'projects': projects, 'products': products,
               'songs': songs, 'artist': artist,
               'singles': singles, 'artist_ep': artist_ep}
    print(request.META.get('HTTP_REFERER'))
    return render(request, 'projects/index.html', context)

@login_required(login_url='login')
def ablum(request):
    album = Album.objects.all()
    lite = albumLite.objects.all()
    singles = singleSong.objects.all()
    content = {'album':album, 'lite': lite, 'singles': singles}

    return render(request, 'projects/albums-store.html', content)

@login_required(login_url='login')
def event(request):
    events = Event.objects.all()
    developers = Developer.objects.all()
    content = {'events':events, 'developers':developers}

    return render(request, 'projects/event.html', content)

@login_required(login_url='login')
def news(request):
    project = News.objects.all()
    content = {'project': project}

    return render(request, 'projects/blog.html', content)

@login_required(login_url='login')
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(),content_type="applicaton/file_audio")
            response['content-Disposition']='inline,filename='+os.path.basename(file_path)
            return response
    raise Http404
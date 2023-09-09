from django.shortcuts import render, redirect
from MyMusic.music_app.forms import ProfileCreateForm, AlbumCreateForm
from MyMusic.music_app.models import Profile, Album


def get_profile():
    try:
        return Profile.objects.get()

    except Profile.DoesNotExist:
        return None


def home_page(request):
    profile = get_profile()
    if profile is None:
        return redirect('add profile')

    context = {
        'albums': Album.objects.all(),
    }

    return render(request, "web/home-with-profile.html", context)


def add_album(request):
    if request.method == 'GET':
        form = AlbumCreateForm()
    else:
        form = AlbumCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }

    return render(request, "web/add-album.html", context)


def album_details(request, id):
    album = Album.objects.filter(id=id).get()
    context = {
        'album': album,
    }
    return render(request, "web/album-details.html", context)


def edit_album(request, id):
    return render(request, "web/edit-album.html")


def delete_album(request, id):
    return render(request, "web/delete-album.html")


def profile_details(request):
    return render(request, "web/profile-details.html")


def delete_profile(request):
    return render(request, "web/profile-delete.html")


def add_profile(request):
    if get_profile() is not None:
        return redirect('home page')

    if request.method == "GET":
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home page")

    context = {
        'form': form,
    }

    return render(request, "web/home-no-profile.html", context)


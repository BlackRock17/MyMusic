from django.shortcuts import render, redirect
from MyMusic.music_app.forms import ProfileCreateForm, AlbumCreateForm, AlbumEditForm, AlbumDeleteForm, \
    ProfileDeleteForm
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
    album = Album.objects.filter(id=id).get()

    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, "web/edit-album.html", context)


def delete_album(request, id):
    album = Album.objects.filter(id=id).get()

    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album)
    else:
        form = AlbumDeleteForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
        'album': album,
    }
    return render(request, "web/delete-album.html", context)


def profile_details(request):
    profile = get_profile()
    albums_count = Album.objects.count()
    context = {
        'profile': profile,
        'album_count': albums_count,
    }
    return render(request, "web/profile-details.html", context)


def delete_profile(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')

    context = {
        'form': form,
    }
    return render(request, "web/profile-delete.html", context)


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
        'hide_nav_links': True,
    }

    return render(request, "web/home-no-profile.html", context)


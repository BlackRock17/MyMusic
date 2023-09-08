from django.shortcuts import render, redirect

from MyMusic.music_app.forms import ProfileCreateForm
from MyMusic.music_app.models import Profile


def get_profile():
    try:
        return Profile.objects.get()

    except:
        return None


def home_page(request):
    profile = get_profile()
    if profile is None:
        return redirect('add profile')

    return render(request, "web/home-with-profile.html")


def add_album(request):
    return render(request, "web/add-album.html")


def album_details(request, id):
    return render(request, "web/album-details.html")


def edit_album(request, id):
    return render(request, "web/edit-album.html")


def delete_album(request, id):
    return render(request, "web/delete-album.html")


def profile_details(request):
    return render(request, "web/profile-details.html")


def delete_profile(request):
    return render(request, "web/profile-delete.html")


def add_profile(request):
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


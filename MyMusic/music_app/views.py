from django.shortcuts import render


def home_page(request):
    return None


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
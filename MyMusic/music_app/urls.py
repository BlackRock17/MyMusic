from django.urls import path, include
from MyMusic.music_app import views

urlpatterns = (
    path("", views.home_page, name='home page'),
    path("album/add/", views.add_album, name="add album"),
    path("album/details/<int:id>/", views.album_details, name="album details"),
    path("album/edit/<int:id>/", views.edit_album, name="edit album"),
    path("album/delete/<int:id>", views.delete_album, name="delete album"),
    path("profile/details/", views.profile_details, name="profile details"),
    path("profile/delete/", views.delete_profile, name="delete profile"),
    path("profile/add/", views.add_profile, name="add profile"),
)

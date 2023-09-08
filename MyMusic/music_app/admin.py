from django.contrib import admin
from MyMusic.music_app.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
    

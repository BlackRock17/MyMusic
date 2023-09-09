from django import forms
from MyMusic.music_app.models import Profile, Album


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'Album_Name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }
            ),
            'Artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist',
                }
            ),
            'Description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                }
            ),
            'Image_URL': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'Price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }
            ),
        }

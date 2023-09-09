from django import forms
from MyMusic.music_app.models import Profile, Album


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class AlbumBaseForm(forms.ModelForm):

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


class AlbumCreateForm(AlbumBaseForm):
    pass


class AlbumEditForm(AlbumBaseForm):
    pass


class AlbumDeleteForm(AlbumBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'




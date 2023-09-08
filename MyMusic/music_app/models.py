from django.core.validators import MinLengthValidator
from django.db import models

from MyMusic.music_app.validators import validate_string_alphanumeric, PositiveFloatValidator


class Profile(models.Model):
    Username = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(2),
            validate_string_alphanumeric,
        ]
    )

    Email = models.CharField(
            blank=False,
            null=False,
    )

    Age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.Username


class Album(models.Model):
    GENRE_CHOICES = [
        ("pop", "Pop Music"),
        ("jazz", "Jazz Music"),
        ("rnb", "R&B Music"),
        ("country", "Country Music"),
        ("dance", "Dance Music"),
        ("hiphop", "Hip Hop Music"),
        ("other", "Other")
    ]

    Album_Name = models.CharField(max_length=30, blank=False, null=False, unique=True)

    Artist = models.CharField(max_length=30, blank=False, null=False)

    Genre = models.CharField(max_length=30, blank=False, null=False, choices=GENRE_CHOICES)

    Description = models.TextField(blank=True, null=True)

    Image_URL = models.URLField(blank=False, null=False)

    Price = models.FloatField(blank=False, null=False, validators=[PositiveFloatValidator()])








# Generated by Django 4.2.5 on 2023-09-08 13:26

import MyMusic.music_app.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("music_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="Username",
            field=models.CharField(
                max_length=15,
                validators=[
                    django.core.validators.MinLengthValidator(2),
                    MyMusic.music_app.validators.validate_string_alphanumeric,
                ],
            ),
        ),
    ]
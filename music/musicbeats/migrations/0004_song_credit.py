# Generated by Django 5.0.4 on 2024-04-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicbeats', '0003_rename_movie_song_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='credit',
            field=models.CharField(default='', max_length=10000),
        ),
    ]

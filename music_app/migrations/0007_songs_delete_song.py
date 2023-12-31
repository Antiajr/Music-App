# Generated by Django 4.0.4 on 2023-05-30 09:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0006_song_file_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('ID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('file_image', models.ImageField(upload_to='pics/')),
                ('file_audio', models.FileField(upload_to='audio/')),
            ],
        ),
        migrations.DeleteModel(
            name='song',
        ),
    ]

# Generated by Django 4.0.4 on 2023-06-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0011_artistep'),
    ]

    operations = [
        migrations.AddField(
            model_name='artistep',
            name='ep_image',
            field=models.ImageField(default=0, upload_to='pics/'),
            preserve_default=False,
        ),
    ]

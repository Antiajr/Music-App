# Generated by Django 4.0.4 on 2023-06-09 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0016_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='arena',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 4.0.4 on 2023-06-09 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0018_alter_event_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]

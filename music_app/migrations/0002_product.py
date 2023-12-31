# Generated by Django 4.0.4 on 2023-05-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('profile_image', models.ImageField(upload_to='pics/')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]

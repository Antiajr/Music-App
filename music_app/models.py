from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='pics/')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(upload_to='pics/')
    price = models.FloatField(null=True, blank=True)
    offer = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Songs(models.Model):
    ID = models.UUIDField(default=uuid.uuid4, editable=False,
                          primary_key=True, unique=True)
    file_image = models.ImageField(upload_to='pics/')
    file_audio = models.FileField(upload_to='audio/')

    def __str__(self):
        return str(self.ID)

class Artist(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    artist_image = models.ImageField(upload_to='pics/')

    def __str__(self):
        return self.name

class Single(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    singles_image = models.ImageField(default='pics/')
    single_file = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.name

class ArtistEP(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    ep_image = models.ImageField(upload_to='pics/')

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    album_img = models.ImageField(upload_to='pics/')

    def __str__(self):
        return self.name

class albumLite(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='pics/')
    offer = models.BooleanField(default=False)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class singleSong(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='pics/')
    song = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='pics/')
    arena = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_created=True, null=True, blank=True)
    description = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Developer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='pics/')
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class News(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='pics/')
    description = models.TextField(max_length=200, blank=True, null=True)
    day = models.IntegerField(max_length=31, blank=True, null=True)
    month = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


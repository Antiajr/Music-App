from django.contrib import admin
from .models import Project, Product, Songs, Artist, Single,  \
    ArtistEP, Album, albumLite, singleSong, Event, Developer, News

# Register your models here.

admin.site.register(Project)
admin.site.register(Product)
admin.site.register(Songs)
admin.site.register(Artist)
admin.site.register(Single)
admin.site.register(ArtistEP)
admin.site.register(Album)
admin.site.register(albumLite)
admin.site.register(singleSong)
admin.site.register(Event)
admin.site.register(Developer)
admin.site.register(News)



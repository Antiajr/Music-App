from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('album/', views.ablum, name='album'),
    path('event/', views.event, name='event'),
    path('news/', views.news, name='news'),
]
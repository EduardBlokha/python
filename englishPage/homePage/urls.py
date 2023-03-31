from .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index, name='home-page'),
    path('text', views.text, name='text-page'),
    path('profil', views.profil, name='profil-page'),
    path('dictionary', views.dictionary, name='dictionary-page'),
]
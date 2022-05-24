from django.urls import path
from . import views

urlpatterns = [
    path('api/movie_autocomplete', views.movie_autocomplete, name = 'movie_autocomplete'),
    path('', views.movie_search, name = 'movie_search')
]

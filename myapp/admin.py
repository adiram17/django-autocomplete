from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display =  ['name', 'description']
    search_fields = ['name', 'description']

admin.site.register(Movie, MovieAdmin)
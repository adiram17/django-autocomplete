from django.http import  HttpResponse
from django.shortcuts import render
from .models import Movie
import json

def movie_autocomplete(request):
    data = None
    if request.is_ajax():
        query = request.GET.get("term", "")
        movies = Movie.objects.filter(name__icontains=query)
        results = []
        for movie in movies:
            place_json = movie.name
            results.append(place_json)
        data = json.dumps(results)
    mimetype = "application/json"
    return HttpResponse(data, mimetype)

def movie_search(request):
    return render(request, 'search.html', {})
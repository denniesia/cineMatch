from django.shortcuts import render
import requests
# Create your views here.
TMDB_API_KEY = 'a186f459fadf51ad863d0bb6e9e85805'

def index(request):
    return render(request, 'index.html')


def movies_view(request):
    TMDB_API_KEY = 'a186f459fadf51ad863d0bb6e9e85805'
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=en-US&page=1'
    data = requests.get(url).json()
    movies = data.get('results', [])
    return render(request, 'overview.html', {'movies': movies})
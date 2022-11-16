from django.conf import settings
from .models import Movie

import re
import requests




API_KEY = getattr(settings, 'TMDB_API_KEY')


# 인기 영화 목록 가져오기
def popular_movie():
    payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'region': 'KR'
        }
    url = 'https://api.themoviedb.org/3/movie/popular'
    r = requests.get(url, params=payload)
    rdata = r.json()['results']

    for data in rdata:
        movie = Movie()
        movie.adult = data['adult']
        movie.backdrop_path = data['backdrop_path']
        movie.genre_ids = data['genre_ids']
        movie.id = data['id']
        movie.original_title = data['original_title']
        movie.overview = data['overview']
        movie.popularity = data['popularity']
        movie.poster_path = data['poster_path']
        movie.release_date = data['release_date']
        movie.title = data['title']
        movie.video = data['video']
        movie.vote_average = data['vote_average']
        movie.vote_count = data['vote_count']
        movie.save()

    return rdata
# from django.shortcuts import render
# from rest_framework.response import Response
from django.http.response import JsonResponse
from django.conf import settings
from .models import Movie, Genre, Country, WatchProvider, People

import re
import json
import requests


API_KEY = getattr(settings, 'TMDB_API_KEY')


# 인기 영화 목록 가져오기
def popular_movie(request):
    payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'region': 'KR'
        }
    url = 'https://api.themoviedb.org/3/movie/popular'
    r = requests.get(url, params=payload)
    rdata = r.json()['results']
    return JsonResponse(rdata, safe=False) 




# 상위 영화 목록 가져오기
def top_rated_movie(request):
    payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'page': 1,
        'region': 'KR'
        }
    url = 'https://api.themoviedb.org/3/movie/top_rated'
    r = requests.get(url, params=payload)
    rdata = r.json()['results']
    return JsonResponse(rdata, safe=False)


# 상영 중인 영화 목록 가져오기
def now_playing_movie(request):
    p = 1
    now_playing_movie = []

    while True:
        # 상영 중인 영화 목록 가져오기
        payload = {
            'api_key': API_KEY,
            'language': 'ko-KR',
            'region': 'KR',
            'page': p,
            }
        url = 'https://api.themoviedb.org/3/movie/now_playing'
        r = requests.get(url, params=payload)
        rdata = r.json()['results']
        if rdata:
            now_playing_movie += rdata
            p += 1
        else:
            break

    # 상영 중인 영화 목록 출력
    return JsonResponse(now_playing_movie, safe=False)



# 상영 중인 영화 예고편 목록 가져오기
def now_playing_movie_video(request):

    p = 1
    now_playing_movie_video = []

    while True:
        # 상영 중인 영화 목록 가져오기
        payload = {
            'api_key': API_KEY,
            'language': 'ko-KR',
            'region': 'KR',
            'page': p,
            }
        url = 'https://api.themoviedb.org/3/movie/now_playing'
        r = requests.get(url, params=payload)
        rdata = r.json()['results']

        # 페이지가 존재할 경우 예고편 비디오 찾기
        if rdata:
            p += 1
            video_list = []

            for data in rdata:
                movie_id = str(data['id'])
                video_payload = {
                    'api_key': API_KEY,
                    'language': 'ko-KR',
                }
                video_url = 'https://api.themoviedb.org/3/movie/' + movie_id + '/videos'
                video_r = requests.get(video_url, params=video_payload)
                video_rdata = video_r.json()['results']
                if video_rdata:
                    if str(type(video_rdata)) == "<class 'list'>":
                        video_rdata = video_rdata[0]
                    video_rdata['title'] = data['title']
                    video_rdata['backdrop_path'] = data['backdrop_path']

                    video_list.append(video_rdata)

            now_playing_movie_video += video_list

        # 페이지가 존재하지 않을 경우 중지
        else:
            break

    return JsonResponse(now_playing_movie_video, safe=False)



# 키워드로 영화 검색
def search_movie(request):

    # 검색 키워드
    search_input = input()
    p = 1
    search_result = []

    # 영화 검색
    while True:
        payload = {
            'api_key': API_KEY,
            'language': 'ko-KR',
            'page': p,
            'include_adult': 'true',
            'query': search_input,
            # 'region': # 지역 설정 가능 ex. KR
            }
        url = 'https://api.themoviedb.org/3/search/movie'
        r = requests.get(url, params=payload)
        rdata = r.json()['results']

        if rdata:
            search_result += rdata
            p += 1
        else:
            break

    return JsonResponse(search_result, safe=False)


# 영화인 검색
def search_movie_people(request):

    # 검색 키워드
    search_input = input()
    p = 1
    search_result = []

    # 영화인 검색
    while True:
        payload = {
            'api_key': API_KEY,
            'language': 'ko-KR',
            'page': p,
            'include_adult': 'true',
            'query': search_input,
            # 'region': 'KR',
            }
        url = 'https://api.themoviedb.org/3/search/person'
        r = requests.get(url, params=payload)
        rdata = r.json()['results']

        if rdata:
            for data in rdata:
                ppl_id = str(data['id'])
                ppl_payload = {
                    'api_key': API_KEY,
                    'language': 'ko-KR',
                    'page': p,
                    'include_adult': 'true',
                    'query': search_input,
                    # 'region': 'KR',
                }
                ppl_url = 'https://api.themoviedb.org/3/person/' + ppl_id
                ppl_r = requests.get(ppl_url, params=ppl_payload)
                ppl_names = ppl_r.json()['also_known_as']

                # 다국어 이름 중 한글이 있는지 체크
                hangul_re = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
                for name in ppl_names:
                    if hangul_re.search(name) is not None:
                        data['name_eng'] = data['name']
                        data['name'] = name
                        break
                        
            search_result += rdata
            p += 1
        else:
            break

    return search_result

# ==================================================================================
#                                 DB 구성 영역           
#                              건드리면 폭발합니다
# ==================================================================================


# DB : 국가 목록 가져오기
def get_countries(request):
    payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        }
    url = 'https://api.themoviedb.org/3/watch/providers/regions'
    r = requests.get(url, params=payload)
    rdata = r.json()['results']

    for data in rdata:
        country = Country(iso_3166_1=data['iso_3166_1'])
        country.english_name = data['english_name']
        country.native_name = data['native_name']
        country.save()
    return JsonResponse(rdata, safe=False)


# DB : 장르 목록 가져오기
def get_genres(request):

    # 장르 목록
    payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        }
    url = 'https://api.themoviedb.org/3/genre/movie/list'
    r = requests.get(url, params=payload)
    rdata = r.json()['genres']
    for data in rdata:
        genre = Genre(id=data['id'])
        genre.name = data['name']
        genre.save()

    # 장르 목록 출력
    return JsonResponse(rdata, safe=False)


# DB : Provider 목록 가져오기
def get_providers(request):

    # Provider 목록
    payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'watch_region': 'KR',
        }
    url = 'https://api.themoviedb.org/3/watch/providers/movie'
    r = requests.get(url, params=payload)
    rdata = r.json()['results']
    for data in rdata:
        provider = WatchProvider(id=data["provider_id"])
        provider.name = data["provider_name"]
        provider.logo_path = data["logo_path"]
        provider.save()

    # Provider 목록 출력
    return JsonResponse(rdata, safe=False)


def get_movie(page):
    payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'region': 'KR',
        'page': page
        }
    url = 'https://api.themoviedb.org/3/movie/popular'
    r = requests.get(url, params=payload)
    rdata = r.json()['results']

    for data in rdata:

        if not data.get('overview').strip() or not data.get('poster_path') or not data.get('backdrop_path'):
            continue
        movie = Movie(id=data['id'])
        movie.adult = data.get('adult')
        movie.backdrop_path = data.get('backdrop_path')
        movie.original_title = data.get('original_title')
        movie.overview = data.get('overview')
        movie.popularity = data.get('popularity')
        movie.poster_path = data.get('poster_path')
        movie.release_date = data.get('release_date')
        movie.title = data.get('title')
        movie.video = data.get('video')
        movie.vote_average = data.get('vote_average')
        movie.vote_count = data.get('vote_count')


        # 디테일 정보 가져오기
        d_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        }
        d_url = 'https://api.themoviedb.org/3/movie/' + str(data['id'])
        d_r = requests.get(d_url, params=d_payload)
        d_data = d_r.json()
        movie.runtime = d_data['runtime']
        movie.status = d_data['status']


        # People 가져오기
        p_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        }
        p_url = 'https://api.themoviedb.org/3/movie/' + str(data['id']) + '/credits'
        p_r = requests.get(p_url, params=p_payload)
        p_data = p_r.json()


        # 감독 설정

        crews = p_data['crew']
        for crew in crews:
            if crew['job'] == "Director":
                if People.objects.filter(id=crew['id']):
                    movie.director = People.objects.get(id=crew['id'])
                else:
                    people = People(id=crew['id'])
                    people.name = crew['name']
                    people.department = crew['known_for_department']
                    people.profile_path = crew['profile_path']
                    people.save()
                    movie.director = people
        
        movie.save()

        # 출연진 설정
        casts = p_data['cast']

        for c in range(min(10, len(casts))):
            cast = casts[c]
            if People.objects.filter(id=cast['id']):
                movie.casts.add(People.objects.get(id=cast['id']))
            else:
                people = People(id=cast['id'])

                # 인물 디테일 조회
                ppl_id = str(cast['id'])
                ppl_payload = {
                    'api_key': API_KEY,
                    'language': 'ko-KR',
                }
                ppl_url = 'https://api.themoviedb.org/3/person/' + ppl_id
                ppl_r = requests.get(ppl_url, params=ppl_payload)
                ppl_names = ppl_r.json()['also_known_as']

                # 다국어 이름 중 한글이 있는지 체크
                hangul_re = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
                for name in ppl_names:
                    if hangul_re.search(name) is not None:
                        people.name_origin = cast['name']
                        people.name = name
                        break
                else:
                    people.name = cast['name']

                people.department = cast['known_for_department']
                people.profile_path = cast['profile_path']
                people.save()
                movie.casts.add(people)

        # 장르 설정
        for id in data['genre_ids']:
            movie.genres.add(Genre.objects.get(id=id))
        
        # 국가 설정
        for country in d_data['production_countries']:
            if Country.objects.filter(iso_3166_1=country['iso_3166_1']):
                movie.countries.add(Country.objects.get(iso_3166_1=country['iso_3166_1']))


        # Watch Provider 설정
        w_payload = {
        'api_key': API_KEY
        }
        w_url = 'https://api.themoviedb.org/3/movie/' + str(data['id']) + '/watch/providers'
        w_r = requests.get(w_url, params=w_payload)
        wdata = w_r.json()['results'].get('KR')
        if wdata:
            categories = ["flatrate", "rent", "buy"]

            for category in categories:
                if wdata.get(category):
                    for provider in wdata.get(category):
                        movie.watch_providers.add(WatchProvider.objects.get(id=provider['provider_id']))
        

    return 1


# DB : 영화 목록 가져오기
def get_movies(request):
    for p in range(21, 40):
        get_movie(p)
    return JsonResponse({"data" : "success!"}) 
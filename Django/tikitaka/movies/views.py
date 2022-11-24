from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from django.conf import settings
from django.core import serializers
from django.http.response import JsonResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Q

from .models import Movie, Genre, Country, WatchProvider, People, Backdrop
from .serializers import PosterListSerializer, PeopleSerializer, MovieDetailSerializer, MovieIdSerializer
from accounts.models import User
from accounts.serializers import BookmarkSerializer, PosterSerializer
from community.serializers import UserReviewSerializer

import re
import requests


API_KEY = getattr(settings, 'TMDB_API_KEY')


# 인기 영화 목록 가져오기
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def popular_movie(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-popularity')[:40]
        serializer = PosterListSerializer(movies, many=True)
        return Response(serializer.data)


# 상위 영화 목록 가져오기
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def top_rated_movie(request):
    if request.method == 'GET':
        movies = Movie.objects.order_by('-vote_count')[:40]
        serializer = PosterListSerializer(movies, many=True)
        return Response(serializer.data)



# 영화 검색
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def search_movie(request):
    search_input = request.GET.get('search','')
    genre_input = request.GET.getlist('genres[]')
    movies = Movie.objects.all()
    if search_input:
        movies = movies.filter(
            Q(title__contains=search_input) |
            Q(original_title__icontains=search_input)
        ).filter(
            genres__in=genre_input
        ).order_by('-popularity').distinct()[:30]
    serializer = PosterListSerializer(movies, many=True)
    return Response(serializer.data)



# 영화인 검색
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def search_movie_people(request):
    search_input = request.GET.get('search','') # value값이 없을 때 '' 반환
    people = People.objects.all()
    if search_input:
        search_result = people.filter(
            Q(name__icontains=search_input) |
            Q(name_origin__icontains=search_input)
        )
        serializer = PeopleSerializer(search_result, many=True)
    else:
        serializer = PeopleSerializer(people, many=True)
    return Response(serializer.data)

    


# 영화 디테일 조회
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def movie_detail(request):
    movie_id = request.GET.get('id','')
    movie = Movie.objects.get(id=int(movie_id))
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

# 영화 아이디 조회
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def movie_id(request):
    title = request.GET.get('title','')
    movie = Movie.objects.get(title=title)
    serializer = MovieIdSerializer(movie)
    return Response(serializer.data)



# 영화 기반 영화 추천
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def recommend_movie(request, movie_id):
    user_id = request.GET.get('user','')
    bookmarks = []
    reviews = []
    bookmark_lst = []
    review_lst = []
    if user_id:
        user = User.objects.get(pk=user_id)
        bookmarks = BookmarkSerializer(user).data['bookmarks']
        reviews = UserReviewSerializer(user).data['reviews']
    for bookmark in bookmarks:
        bookmark_lst.append(bookmark['id'])
    for review in reviews:
        review_lst.append(review['id'])
    print(bookmark_lst, '@@@@@@@@@@@@@@@@')

    recommend_lst = []
    target = Movie.objects.get(pk=movie_id)
    # 제목 기반
    title = target.title
    all_movie = Movie.objects.all()

    for movie in all_movie:
        cnt = 0
        for i in range(len(title)):
            if cnt == min(5, len(title)) or i >= len(movie.title) or len(recommend_lst)>2:
                break
            if title[i] == movie.title[i]:
                cnt += 1
            elif title[i] == movie.title[i] == ':':
                if movie not in recommend_lst and movie.id not in bookmark_lst and movie.id not in review_lst and movie.id != target.id:
                    recommend_lst.append(movie)
            else:
                break
        if cnt > 4 or cnt == len(title):
            if movie not in recommend_lst and movie.id not in bookmark_lst and movie.id not in review_lst and movie.id != target.id:
                recommend_lst.append(movie)
    # 제작진 기반
    director = People.objects.get(id=target.director.id)
    d_lst = director.movie_set.all().order_by('-vote_count')
    flag = 0
    for dr in d_lst:
        if flag > 2:
            break 
        if dr not in recommend_lst and dr.id not in bookmark_lst and dr.id not in review_lst and dr.id != target.id:
            recommend_lst.append(dr)
            flag += 1
    


    # 장르 기반
    genres = target.genres.all()
    for genre in genres:
        g = Genre.objects.get(id=genre.id)
        g_lst = g.movies.all().order_by('-vote_count')[:10]
        for gr in g_lst:
            if gr not in recommend_lst and gr.id not in bookmark_lst and movie.id not in review_lst and gr.id != target.id:
                recommend_lst.append(gr)
    serializer = PosterSerializer(recommend_lst, many=True).data
    # recommend_lst = list(set(list(serializer)))
    return Response(serializer)



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


# 영화 정보 가져오기 : 페이지
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
        movie.original_title = data.get('original_title')
        movie.overview = data.get('overview')
        movie.popularity = data.get('popularity')
        movie.poster_path = data.get('poster_path')
        movie.release_date = data.get('release_date')
        movie.title = data.get('title')
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


        # 예고편 가져오기
        video_payload = {
            'api_key': API_KEY,
            'language': 'ko-KR',
        }
        video_url = 'https://api.themoviedb.org/3/movie/' + str(data['id']) + '/videos'
        video_r = requests.get(video_url, params=video_payload)
        video_rdata = video_r.json()['results']
        if video_rdata:
            if str(type(video_rdata)) == "<class 'list'>":
                video_rdata = video_rdata[0]
            movie.video_key = video_rdata['key']





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




        # Backdrop 이미지 가져오기
        b_payload = {
        'api_key': API_KEY,
        }
        b_url = 'https://api.themoviedb.org/3/movie/' + str(data['id']) + '/images'
        b_r = requests.get(b_url, params=b_payload)
        b_rdata = b_r.json()['backdrops']
        for i in range(min(5, len(b_rdata))):
            img = Backdrop()
            img.path = b_rdata[i]['file_path']
            img.movie = movie
            img.save()
            
        # 출연진 설정
        casts = p_data['cast']

        for c in range(min(5, len(casts))):
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
                        if WatchProvider.objects.filter(id=provider['provider_id']):
                            movie.watch_providers.add(WatchProvider.objects.get(id=provider['provider_id']))
        

    return 1


# DB : 영화 목록 가져오기
def get_movies(request):
    for p in range(81, 101): # 100까지 시도
        get_movie(p)
    return JsonResponse({"data" : "success!"}) 
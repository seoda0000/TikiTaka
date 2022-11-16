# from django.shortcuts import render
# from rest_framework.response import Response
from django.http.response import JsonResponse
from django.conf import settings

import re
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
    return now_playing_movie



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
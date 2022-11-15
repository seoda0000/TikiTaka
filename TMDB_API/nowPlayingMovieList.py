import requests
from pprint import pprint

API_KEY = '90948a33935bf9b9275c46d36a90412c'


def now_playing_movie_list():

    # 상영 중인 영화 목록 가져오기
    p_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'region': 'KR',
        'page': 1,
        }
    url = 'https://api.themoviedb.org/3/movie/now_playing'
    r = requests.get(url, params=p_payload)
    rdata = r.json()
    # rdata.sort(key=lambda x: x['id'])

    # 상영 중인 영화 목록 출력
    return rdata




if __name__ == '__main__':
    """
    상영 중인 영화 목록 출력
    """
    pprint(now_playing_movie_list())


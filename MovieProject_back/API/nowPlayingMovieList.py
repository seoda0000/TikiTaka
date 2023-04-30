import requests
from pprint import pprint

API_KEY = '90948a33935bf9b9275c46d36a90412c'


def now_playing_movie_list():
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




if __name__ == '__main__':
    """
    상영 중인 영화 목록 출력
    """
    pprint(now_playing_movie_list())


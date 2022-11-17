import requests
from pprint import pprint

API_KEY = '90948a33935bf9b9275c46d36a90412c'


def get_movie_watch_provider():

    # 영화 공급자 출력
    movie_id = input()

    p_payload = {
        'api_key': API_KEY
        }
    url = 'https://api.themoviedb.org/3/movie/' + movie_id + '/watch/providers'
    r = requests.get(url, params=p_payload)
    rdata = r.json()['results'].get('KR')

    return rdata


if __name__ == '__main__':
    """
    영화 공급자 반환
    """
    pprint(get_movie_watch_provider())

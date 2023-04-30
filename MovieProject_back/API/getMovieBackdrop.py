import requests
from pprint import pprint

API_KEY = '90948a33935bf9b9275c46d36a90412c'


def get_movie_backdrop():
    # 영화 이미지
    movie_id = input()

    b_payload = {
        'api_key': API_KEY,
        }
    b_url = 'https://api.themoviedb.org/3/movie/' + movie_id + '/images'
    b_r = requests.get(b_url, params=b_payload)
    b_rdata = b_r.json()['backdrops']

    return rdata


if __name__ == '__main__':
    """
    영화 검색 결과 반환
    """
    pprint(get_movie_backdrop())

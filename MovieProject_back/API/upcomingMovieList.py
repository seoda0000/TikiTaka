import requests
from pprint import pprint


def upcoming_movie_list():

    # 상영 예정작 목록
    p_payload = {
        'api_key': '90948a33935bf9b9275c46d36a90412c',
        'language': 'ko-KR',
        'page': 1,
        'region': 'KR',
        }
    url = 'https://api.themoviedb.org/3/movie/upcoming'
    r = requests.get(url, params=p_payload)
    rdata = r.json()

    # 상영 예정작 목록
    return rdata


if __name__ == '__main__':
    """
    상영 예정작 목록 반환
    """
    pprint(upcoming_movie_list())

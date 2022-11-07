import requests
from pprint import pprint

API_KEY = '90948a33935bf9b9275c46d36a90412c'


def genre_list():

    # 장르 목록
    p_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        }
    url = 'https://api.themoviedb.org/3/genre/movie/list'
    r = requests.get(url, params=p_payload)
    rdata = r.json()['genres']
    rdata.sort(key=lambda x: x['id'])

    # 장르 목록 출력
    return rdata


if __name__ == '__main__':
    """
    # 장르 목록 반환
    """
    pprint(genre_list())

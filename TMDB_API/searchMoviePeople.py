import requests
from pprint import pprint


API_KEY = '90948a33935bf9b9275c46d36a90412c'


def search_movie_people():

    # 검색 키워드
    search_input = input()

    # 영화 검색
    p_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'page': 1,
        'include_adult': 'true',
        'query': search_input,
        # 'region':
        }
    url = 'https://api.themoviedb.org/3/search/person'
    r = requests.get(url, params=p_payload)
    rdata = r.json()

    return rdata


if __name__ == '__main__':
    """
    영화 검색 결과 반환
    """
    pprint(search_movie_people())

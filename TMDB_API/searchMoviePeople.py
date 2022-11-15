import requests
from pprint import pprint


API_KEY = '90948a33935bf9b9275c46d36a90412c'


def search_movie_people():

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
            search_result += rdata
            p += 1
        else:
            break

    return search_result




if __name__ == '__main__':
    """
    영화 검색 결과 반환
    """
    pprint(search_movie_people())

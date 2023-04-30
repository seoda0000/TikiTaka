import requests
from pprint import pprint

API_KEY = '90948a33935bf9b9275c46d36a90412c'


def get_movie_detail():

    # 영화 상세 정보
    # search_input = input()
    movie_id = input()

    p_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        }
    url = 'https://api.themoviedb.org/3/movie/' + movie_id
    r = requests.get(url, params=p_payload)
    rdata = r.json()

    return rdata


if __name__ == '__main__':
    """
    영화 검색 결과 반환
    """
    pprint(get_movie_detail())

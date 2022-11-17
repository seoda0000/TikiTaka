import requests
from pprint import pprint

API_KEY = '90948a33935bf9b9275c46d36a90412c'


def get_recommendations_for_movie():

    # 영화를 통한 추천 영화 목록
    movie_id = input()

    p_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'page': 1,
        }
    url = 'https://api.themoviedb.org/3/movie/' + movie_id + '/recommendations'
    r = requests.get(url, params=p_payload)
    rdata = r.json()

    return rdata


if __name__ == '__main__':
    """
    영화 공급자 반환
    """
    pprint(get_recommendations_for_movie())

import requests
from pprint import pprint

API_KEY = '90948a33935bf9b9275c46d36a90412c'


def get_similar_movie_list():

    # 해당 영화와 비슷한 영화 목록 (장르, 키워드 기준)
    movie_id = input()

    p_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'page': 1,
        }
    url = 'https://api.themoviedb.org/3/movie/' + movie_id + '/similar'
    r = requests.get(url, params=p_payload)
    rdata = r.json()

    return rdata


if __name__ == '__main__':

    pprint(get_similar_movie_list())

import requests
from pprint import pprint

API_KEY = '90948a33935bf9b9275c46d36a90412c'


def get_movie_video():
    # 영화 예고편
    movie_id = input()

    p_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        }
    url = 'https://api.themoviedb.org/3/movie/' + movie_id + '/videos'
    r = requests.get(url, params=p_payload)
    rdata = r.json()

    return rdata


if __name__ == '__main__':
    """
    영화 검색 결과 반환
    """
    pprint(get_movie_video())

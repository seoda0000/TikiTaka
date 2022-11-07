import requests
from pprint import pprint

API_KEY = '90948a33935bf9b9275c46d36a90412c'


def topRateMovieList():

    # 인기 영화 목록 가져오기
    p_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'page': 1,
        'region': 'KR'
        }
    url = 'https://api.themoviedb.org/3/movie/top_rated'
    r = requests.get(url, params=p_payload)
    rdata = r.json()['results']

    return rdata


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(topRateMovieList())

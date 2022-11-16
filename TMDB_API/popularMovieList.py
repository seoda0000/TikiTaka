import requests
from pprint import pprint

import json

file_path = "./movies.json"

API_KEY = '90948a33935bf9b9275c46d36a90412c'


def popular_movie_list():

    # 인기 영화 목록 가져오기
    p_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'region': 'KR'
        }
    url = 'https://api.themoviedb.org/3/movie/popular'
    r = requests.get(url, params=p_payload)
    rdata = r.json()['results']

    return rdata

with open(file_path, 'w', encoding="UTF-8") as outfile:
    json.dump(popular_movie_list(), outfile, indent=4, ensure_ascii=False)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':

    pprint(popular_movie_list())

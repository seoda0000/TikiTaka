import requests
from pprint import pprint

# JSON 파일 만들기
import json

file_path = "./genreList.json"




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



# with open(file_path, 'w') as outfile:
#     json.dump(genre_list(), outfile, indent=4, ensure_ascii=False)
pprint(genre_list())

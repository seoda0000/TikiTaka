import re
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
            for data in rdata:
                ppl_id = str(data['id'])
                ppl_payload = {
                    'api_key': API_KEY,
                    'language': 'ko-KR',
                    'page': p,
                    'include_adult': 'true',
                    'query': search_input,
                    # 'region': 'KR',
                }
                ppl_url = 'https://api.themoviedb.org/3/person/' + ppl_id
                ppl_r = requests.get(ppl_url, params=ppl_payload)
                ppl_names = ppl_r.json()['also_known_as']

                # 다국어 이름 중 한글이 있는지 체크
                hangul_re = re.compile('[\u3131-\u3163\uac00-\ud7a3]+')
                for name in ppl_names:
                    if hangul_re.search(name) is not None:
                        data['name_eng'] = data['name']
                        data['name'] = name
                        break

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

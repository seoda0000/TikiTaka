import requests
from pprint import pprint



def search_movie_people():

    search_input = input()


    # 영화 검색
    payload = {
        'key': 'c282be63aa7a1c93a2b0b3fe0cbf8cb8',
        'peopleNm': search_input,
    }
    url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json'
    r = requests.get(url, params=payload)
    rdata = r.json()['peopleListResult']['peopleList']

    return rdata


if __name__ == '__main__':
    """
    영화 검색 결과 반환
    """
    pprint(search_movie_people())

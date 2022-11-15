import requests
from pprint import pprint

API_KEY = '90948a33935bf9b9275c46d36a90412c'


def now_playing_movie_video_list():

    # 상영 중인 영화 목록 가져오기
    p_payload = {
        'api_key': API_KEY,
        'language': 'ko-KR',
        'region': 'KR',
        'page': 1,
        }
    url = 'https://api.themoviedb.org/3/movie/now_playing'
    r = requests.get(url, params=p_payload)
    rdata = r.json()['results']

    video_list = []

    for data in rdata:
        title = data['title']
        movie_id = str(data['id'])
        video_payload = {
            'api_key': API_KEY,
            'language': 'ko-KR',
        }
        video_url = 'https://api.themoviedb.org/3/movie/' + movie_id + '/videos'
        video_r = requests.get(video_url, params=video_payload)
        video_rdata = video_r.json()['results']
        if video_rdata:
            if str(type(video_rdata)) == "<class 'list'>":
                video_rdata = video_rdata[0]
            video_rdata['title'] = title
            video_list.append(video_rdata)

    return video_list




if __name__ == '__main__':
    """
    상영 중인 영화 목록 출력
    """
    pprint(now_playing_movie_video_list())


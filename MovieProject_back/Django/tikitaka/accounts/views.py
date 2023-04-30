from django.shortcuts import render, redirect

from django.conf import settings
from accounts.models import User
from allauth.socialaccount.models import SocialAccount
from dj_rest_auth.registration.views import SocialLoginView
# from allauth.socialaccount.providers.google import views as google_view
from allauth.socialaccount.providers.kakao import views as kakao_view
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from django.http import JsonResponse
import requests
from rest_framework import status
from json.decoder import JSONDecodeError
from movies.models import Genre, Movie, People
from movies.serializers import MovieNameSerializer, PosterSerializer
from community.models import Review
from community.serializers import UserReviewSerializer


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from accounts.models import User
from .serializers import UserShortSerializer, UserNameSerializer, UserSerializer, BookmarkSerializer
from django.db.models import Q



KAKAO_CALLBACK_URI = getattr(settings, 'KAKAO_CALLBACK_URI')
BASE_URL = 'http://localhost:8000/'


# 전체 유저 목록
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def all_user_list(request):
    users = User.objects.all()
    serializer = UserNameSerializer(users, many=True)
    lst = []
    for s in serializer.data:
        if s['username']:
            lst.append(s['username'])
    return Response(list(lst))


# 유저 검색
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def search_user(request):
    search_input = request.GET.get('search','')
    if search_input:
        users = User.objects.filter(
            first_name__icontains=search_input
        ).distinct()[:30]
        serializer = UserShortSerializer(users, many=True)
        return Response(serializer.data)
    else:
        return Response([])


# 닉네임으로 유저 반환
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_user(request):
    name = request.GET.get('name','')
    user = User.objects.get(username=name)
    serializer = UserSerializer(user)
    return Response(serializer.data)


# pk로 유저 반환
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def pk_user(request, user_id):
    user = User.objects.get(pk=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)



# 유저 북마크 반환
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def bookmark_list(request, user_id):
    user = User.objects.get(pk=user_id)
    serializer = BookmarkSerializer(user)
    return Response(serializer.data)









# 북마크 기반 영화 추천
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def recommend_bookmark(request, user_id):
    user = User.objects.get(pk=user_id)
    bookmarks = BookmarkSerializer(user).data['bookmarks']
    reviews = UserReviewSerializer(user).data['reviews']
    bookmark_lst = []
    for bookmark in bookmarks:
        bookmark_lst.append(bookmark['id'])
    
    review_lst = []
    for review in reviews:
        review_lst.append(review['id'])

    recommend_lst = []
    for bookmark in bookmarks:
        target = Movie.objects.get(pk=bookmark['id'])


        # 제목 기반
        title = target.title
        all_movie = Movie.objects.all()

        for movie in all_movie:
            cnt = 0
            for i in range(len(title)):
                if cnt == min(5, len(title)) or i >= len(movie.title) or len(recommend_lst)>2:
                    break
                if title[i] == movie.title[i]:
                    cnt += 1
                elif title[i] == movie.title[i] == ':':
                    if movie not in recommend_lst and movie.id not in bookmark_lst and movie.id not in review_lst and movie.id != target.id:
                        recommend_lst.append(movie)
                else:
                    break
            if cnt > 4 or cnt == len(title):
                if movie not in recommend_lst and movie.id not in bookmark_lst and movie.id not in review_lst and movie.id != target.id:
                    recommend_lst.append(movie)
        # 제작진 기반
        director = People.objects.get(id=target.director.id)
        d_lst = director.movie_set.all().order_by('-vote_count')
        flag = 0
        for dr in d_lst:
            if flag > 2:
                break 
            if dr not in recommend_lst and dr.id not in bookmark_lst and dr.id not in review_lst and dr.id != target.id:
                recommend_lst.append(dr)
                flag += 1
        # 장르 기반
        genres = target.genres.all()
        for genre in genres:
            g = Genre.objects.get(id=genre.id)
            g_lst = g.movies.all().order_by('-vote_count')[:10]
            for gr in g_lst:
                if gr not in recommend_lst and gr.id not in bookmark_lst and movie.id not in review_lst and gr.id != target.id:
                    recommend_lst.append(gr)
    serializer = PosterSerializer(recommend_lst, many=True).data
    # recommend_lst = list(set(list(serializer)))
    return Response(serializer)


# 유저 프로필 변경
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def edit_profile(request):
    user = User.objects.get(id=request.data.get('id'))
    if request.data.get('profile_img'):
        user.profile_img = request.data.get('profile_img')
    if request.data.get('description'):
        user.description = request.data.get('description')
    genre_id_list = request.data.get('genre_id_list')
    print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%', genre_id_list)
    genres = Genre.objects.all()
    if genre_id_list :
        for genre in genres:
            if genre.id in genre_id_list:
                if not genre.favorite_users.filter(id=user.id).exists():
                    genre.favorite_users.add(user)
            else:
                if genre.favorite_users.filter(id=user.id).exists():
                    genre.favorite_users.remove(user)
    user.save()
    return Response(status=status.HTTP_200_OK)



# @api_view(['POST'])
# @authentication_classes([])
# @permission_classes([])
# def follow(request, user_pk):
#     if request.user.is_authenticated:
#         User = get_user_model()
#         me = request.user
#         you = User.objects.get(pk=user_pk)
#         if me != you:
#             # 내가(request.user) 그 사람의 팔로워 목록에 있다면
#             # if me in you.followers.all():
#             if you.followers.filter(pk=me.pk).exists():
#                 # 언팔로우
#                 you.followers.remove(me)
#             else:
#                 # 팔로우
#                 you.followers.add(me)
#         return redirect('accounts:profile', you.username)
#     return redirect('accounts:login')

# 팔로우
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def follow(request, user_id):
    me = User.objects.get(pk=request.data['id'])
    you = User.objects.get(pk=user_id)
    if me != you:
        if you.follower.filter(pk=me.id).exists():
            you.follower.remove(me)
            is_followed = False
        else:
            you.follower.add(me)
            is_followed = True
    context = {
        'is_followed' : is_followed,
    }
    return JsonResponse(context)






# ============================================================= #
#                        카카오 로그인                          #
# ============================================================= #





def kakao_login(request):
    rest_api_key = getattr(settings, 'KAKAO_REST_API_KEY')
    return redirect(
        f"https://kauth.kakao.com/oauth/authorize?client_id={rest_api_key}&redirect_uri={KAKAO_CALLBACK_URI}&response_type=code"
    )


def kakao_callback(request):
    rest_api_key = getattr(settings, 'KAKAO_REST_API_KEY')
    code = request.GET.get("code")
    redirect_uri = KAKAO_CALLBACK_URI

    # Access Token Request

    token_req = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={rest_api_key}&redirect_uri={redirect_uri}&code={code}")
    token_req_json = token_req.json()
    error = token_req_json.get("error")
    if error is not None:
        raise JSONDecodeError(error)
    access_token = token_req_json.get("access_token")

    # Email Request

    profile_request = requests.get(
        "https://kapi.kakao.com/v2/user/me", headers={"Authorization": f"Bearer {access_token}"})
    profile_json = profile_request.json()
    kakao_account = profile_json.get('kakao_account')
    email = kakao_account.get('email')
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', email)

    # Signup or Signin Request

    try:
        user = User.objects.get(email=email)
        # 기존에 가입된 유저의 Provider가 kakao가 아니면 에러 발생, 맞으면 로그인
        # 다른 SNS로 가입된 유저
        social_user = SocialAccount.objects.get(user=user)
        if social_user is None:
            return JsonResponse({'err_msg': 'email exists but not social user'}, status=status.HTTP_400_BAD_REQUEST)
        # 기존에 Google로 가입된 유저
        if social_user.provider != 'kakao':
            return JsonResponse({'err_msg': 'no matching social type'}, status=status.HTTP_400_BAD_REQUEST)
        data = {'access_token': access_token, 'code': code}
        accept = requests.post(
            f"{BASE_URL}accounts/kakao/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signin'}, status=accept_status)
        accept_json = accept.json()
        # accept_json.pop('user', None)
        return JsonResponse(accept_json)
        
    # 기존에 가입된 유저가 없으면 새로 가입
    except User.DoesNotExist:
        data = {'access_token': access_token, 'code': code}
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@', data)
        accept = requests.post(
            f"{BASE_URL}accounts/kakao/login/finish/", data=data)
        accept_status = accept.status_code
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)
        # user의 pk, email, first name, last name과 Access Token, Refresh token 가져옴
        accept_json = accept.json()
        # accept_json.pop('user', None)
        return JsonResponse(accept_json)


class KakaoLogin(SocialLoginView):
    adapter_class = kakao_view.KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = KAKAO_CALLBACK_URI
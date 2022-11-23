from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.shortcuts import render, redirect
from .models import Review, Comment, Vote, Calendar
from .serializers import ReviewCreateSerializer, CommentCreateSerializer, VoteCreateSerializer, ReviewSerializer, CommentSerializer, VoteSerializer, LikeReviewSerializer, FeedSerializer, UserReviewSerializer, CalendarCreateSerializer, CalendarSerializer, UserCalendarSerializer, ReviewSerializerForLike
from movies.models import Movie, Backdrop
from movies.serializers import BackdropSerializer, MovieNameSerializer
# from .forms import ReviewForm, CommentForm
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework import status
from django.core import serializers
from rest_framework.decorators import authentication_classes
from rest_framework.decorators import permission_classes
from accounts.models import User
from django.db.models import Q





# def like(request, review_pk):
#     if request.user.is_authenticated:
#         review = Review.objects.get(pk=review_pk)
#         if review.like_users.filter(pk=request.user.pk).exists():
#             review.like_users.remove(request.user)
#             is_liked = False
#         else:
#             review.like_users.add(request.user)
#             is_liked = True
#         context = {
#             'is_liked' : is_liked,
#             'like_count' : review.like_users.count()
#         }
#         return JsonResponse(context)
#     return redirect('accounts:login')






# ================= CREATE ================= #

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def all_movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieNameSerializer(movies, many=True)
    lst = []
    for s in serializer.data:
        lst.append({
            'id': s['id'],
            'title': s['title']
        })
        if s['title'] != s['original_title']:
            lst.append({
                'id': s['id'],
                'title': s['original_title']
            })
    return Response(lst)



@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def get_backdrop(request):
    movie_id = request.GET.get('id','')
    movie = Movie.objects.get(id=movie_id)
    backdrops = Backdrop.objects.filter(movie_id=int(movie_id))
    serializer = BackdropSerializer(backdrops, many=True)
    data = dict()
    data['backdrops'] = serializer.data
    
    data['title'] = movie.title
    return Response(data)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_vote(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    vote = VoteCreateSerializer(data=request.data)
    if vote.is_valid(raise_exception=True):
        vote.save(movie=movie)
        return Response(vote.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_review(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    review = ReviewCreateSerializer(data=request.data)
    if review.is_valid(raise_exception=True):
        review = review.save(movie=movie)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_comment(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment = CommentCreateSerializer(data=request.data)
    if comment.is_valid(raise_exception=True):
        comment.save(review=review)
        return Response(comment.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def create_calendar(request):
    calendar = CalendarCreateSerializer(data=request.data)
    if calendar.is_valid(raise_exception=True):
        calendar.save()
    user = User.objects.get(id=request.data.get('user'))
    calendars = UserCalendarSerializer(user)
    data = calendars.data.get('calendar_set')
    return Response(data, status=status.HTTP_201_CREATED)


# ================= READ UPDATE DELETE ================= #

@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def review_list(request, username):
    user = User.objects.get(username=username)
    reviews = Review.objects.filter(user=user)
    serializer = ReviewSerializerForLike(reviews, many=True)
    return Response(serializer.data)




@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewCreateSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        username = review.user.username
        review.delete()
        return Response(username)



@api_view(['PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def vote_detail(request, vote_pk):
    vote = Vote.objects.get(pk=vote_pk)
    if request.method == 'PUT':
        serializer = VoteSerializer(vote, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        vote.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def delete_calendar(request):
    user = User.objects.get(id=request.data.get('user'))
    calendar = Calendar.objects.all().filter(
        Q(start=request.data.get('start')) &  Q(user=user)
        )
    calendar[0].delete()
    calendars = UserCalendarSerializer(user)
    data = calendars.data.get('calendar_set')
    return Response(data, status=status.HTTP_201_CREATED)


# =============== 북마크 ===================
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def bookmark(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    user = User.objects.get(pk=request.data['user'])
    if movie.bookmark_users.filter(id=user.id).exists():
        movie.bookmark_users.remove(user)
        is_bookmark = False
    else:
        movie.bookmark_users.add(user)
        is_bookmark = True
    context = {
        'is_bookmark' : is_bookmark,
    }
    return JsonResponse(context)


# =============== 좋아요 ===================
@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def like(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    user = User.objects.get(pk=request.data['id'])
    if review.like_users.filter(id=user.id).exists():
        review.like_users.remove(user)
        is_liked = False
    else:
        review.like_users.add(user)
        is_liked = True
    context = {
        'is_liked' : is_liked,
        'like_count' : review.like_users.count()
    }
    return JsonResponse(context)
# return redirect('accounts:login')


# 유저 좋아요한 리뷰 목록 반환
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def like_list(request, username):
    user = User.objects.get(username=username)
    serializer = LikeReviewSerializer(user)
    return Response(serializer.data)


# =========== 피드 출력 ==============
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def feed(request, user_id):
    user = User.objects.get(pk=user_id)
    review_me = UserReviewSerializer(user).data['reviews']
    if FeedSerializer(user).data.get('following'):
        review_following = FeedSerializer(user).data['following'][0]['reviews']
        feed = review_me + review_following
        feed.sort(key=lambda x:x['created_at'], reverse=True)
    else:
        feed = review_me
    return Response(feed)


# ============ 캘린더 출력 ============
@api_view(['GET'])
@authentication_classes([])
@permission_classes([])
def calendar(request, user_id):
    user = User.objects.get(pk=user_id)
    calendars = UserCalendarSerializer(user)
    calendars = calendars.data.get("calendar_set")
    return Response(calendars)
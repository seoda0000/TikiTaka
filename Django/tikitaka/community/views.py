from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.shortcuts import render, redirect
from .models import Review, Comment, Vote
from .serializers import ReviewCreateSerializer, CommentCreateSerializer, VoteCreateSerializer, ReviewSerializer, CommentSerializer, VoteSerializer
from movies.models import Movie, Backdrop
from movies.serializers import BackdropSerializer
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



# @login_required
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
def get_backdrop(request):
    movie_id = request.GET.get('id','')
    backdrops = Backdrop.objects.filter(movie_id=int(movie_id))
    serializer = BackdropSerializer(backdrops, many=True)
    return Response(serializer.data)


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


# ================= READ UPDATE DELETE ================= #


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([])
@permission_classes([])
def review_detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



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



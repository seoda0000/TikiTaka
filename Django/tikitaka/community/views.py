from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.shortcuts import render, redirect
from .models import Review, Comment, Vote
from .serializers import ReviewSerializer, ReviewCreateSerializer
from movies.models import Movie, Backdrop
# from .forms import ReviewForm, CommentForm
from django.http import JsonResponse
from rest_framework.response import Response
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework import status
from django.core import serializers


# Create your views here.

# def index(request):
#     reviews = Review.objects.all()
#     context = {
#         'reviews':reviews
#     }
#     return render(request, 'community/index.html', context)

# @login_required
# @require_http_methods(['GET', 'POST'])
# def create(request):
#     if request.user.is_authenticated:
#         if request.method == 'POST':
#             review_form = ReviewForm(request.POST)
#             if review_form.is_valid():
#                 review = review_form.save(commit=False)
#                 review.user = request.user
#                 review.save()
#             return redirect('community:detail', review.pk)
#         else:
#             review_form = ReviewForm()
#         context = {
#             'review_form': review_form
#         }
#         return render(request, 'community/create.html', context)

        
#     else:
#         return redirect('accounts:login')

# def detail(request, review_pk):
#     review = Review.objects.get(pk=review_pk)
#     comments = review.comment_set.all()
#     comment_form = CommentForm()
#     context = {
#         'review': review,
#         'comments':comments,
#         'comment_form': comment_form,
#     }
#     return render(request, 'community/detail.html', context)

# @login_required
# def comment_create(request, review_pk):
#     review = Review.objects.get(pk=review_pk)
#     comment_form = CommentForm(request.POST)
#     if comment_form.is_valid():
#         comment = comment_form.save(commit=False)
#         comment.review = review
#         comment.user = request.user
#         comment.save()
#     return redirect('community:detail', review_pk)

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






@api_view(['POST'])
def review_create(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    review = ReviewCreateSerializer(data=request.data)
    if review.is_valid(raise_exception=True):
        review = review.save(movie=movie)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    # elif request.method == 'POST':
    #     serializer = MovieSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)


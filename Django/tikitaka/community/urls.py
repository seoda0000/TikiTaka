from django.urls import path
from . import views

app_name = "community"
urlpatterns = [
    # path('reviews/', views.review_list),
    # path('reviews/<int:review_pk>/', views.review_detail),
    path('<int:movie_pk>/create_review/', views.create_review),
    path('<int:movie_pk>/create_vote/', views.create_vote),
    path('review/<int:review_pk>/create_comment/', views.create_comment),
    path('review/<int:review_pk>/', views.review_detail),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('vote/<int:vote_pk>/', views.vote_detail),
]

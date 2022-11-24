from django.urls import path
from . import views

app_name = "community"
urlpatterns = [
    # path('reviews/', views.review_list),
    # path('reviews/<int:review_pk>/', views.review_detail),
    path('<int:movie_pk>/create_review/', views.create_review),
    path('<int:movie_pk>/create_vote/', views.create_vote),
    path('<int:movie_pk>/bookmark/', views.bookmark),
    path('<int:movie_pk>/send_message/', views.send_message),
    path('review/<int:review_pk>/create_comment/', views.create_comment),
    path('review/<int:review_pk>/', views.review_detail),
    path('review/<int:review_pk>/like/', views.like),
    path('review/<str:username>/', views.review_list),
    path('like/<str:username>/', views.like_list),
    path('comment/<int:comment_pk>/', views.comment_detail),
    path('vote/<int:vote_pk>/', views.vote_detail),
    path('get_backdrop/', views.get_backdrop),
    path('all_movie_list/', views.all_movie_list),
    path('feed/<int:user_id>/', views.feed),
    path('calendar/create/', views.create_calendar),
    path('calendar/delete/', views.delete_calendar),
    path('calendar/list/<int:user_id>/', views.calendar),
    path('message/list/<int:user_id>/', views.message_list),
    path('message/new/<int:user_id>/', views.message_new),
    path('message/check/<int:user_id>/', views.message_check),
]

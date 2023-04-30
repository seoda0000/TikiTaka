from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('movie_detail/', views.movie_detail),
    path('movie_id/', views.movie_id),
    path('popular_movie/', views.popular_movie),
    path('top_rated_movie/', views.top_rated_movie),
    path('now_playing_movie/', views.now_playing_movie),
    path('now_playing_movie_video/', views.now_playing_movie_video),
    path('search_movie/', views.search_movie),
    path('search_movie_people/', views.search_movie_people),
    path('<int:movie_id>/recommend/', views.recommend_movie),

    # DB에서 사용하는 링크
    # path('get_countries/', views.get_countries),
    # path('get_genres/', views.get_genres),
    # path('get_providers/', views.get_providers),
    path('get_movies/', views.get_movies),
]

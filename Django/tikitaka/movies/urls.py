from django.urls import path
from . import views

app_name = "movies"
urlpatterns = [
    path('popular_movie/', views.popular_movie),
    path('top_rated_movie/', views.top_rated_movie),
    path('now_playing_movie/', views.now_playing_movie),
    path('now_playing_movie_video/', views.now_playing_movie_video),
    
]

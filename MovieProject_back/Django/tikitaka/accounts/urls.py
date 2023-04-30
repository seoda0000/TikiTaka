from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('all_user_list/', views.all_user_list),
    path('search_user/', views.search_user),
    path('get_user/', views.get_user),
    path('<int:user_id>/bookmarks/', views.bookmark_list),
    path('<int:user_id>/recommend/', views.recommend_bookmark),
    path('<int:user_id>/user/', views.pk_user),
    path('<int:user_id>/follow/', views.follow),
    path('edit_profile/', views.edit_profile),


    # 카카오 로그인
    path('kakao/login/', views.kakao_login, name='kakao_login'),
    path('kakao/callback/', views.kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),
    
]
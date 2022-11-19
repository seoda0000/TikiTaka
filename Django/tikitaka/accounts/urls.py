from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('search_user/', views.search_user),
    path('all_user_list/', views.all_user_list),


    # 카카오 로그인
    path('kakao/login/', views.kakao_login, name='kakao_login'),
    path('kakao/callback/', views.kakao_callback, name='kakao_callback'),
    path('kakao/login/finish/', views.KakaoLogin.as_view(), name='kakao_login_todjango'),
    
]
from django.urls import path

from user.views import views

urlpatterns = [
    path("/kakao", views.KakaoOauthView.as_view(), name="kakao_login"),
    path("/tokens/verify", views.TokenVerifyAPI.as_view(), name="token_verify"),
    path("/tokens/refresh", views.TokenRefreshAPI.as_view(), name="token_refresh"),
    path("/logout", views.SocialLogutAPI.as_view(), name="logout"),
]

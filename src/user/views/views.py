from typing import Dict

from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenVerifyView

from shared.api import BaseAPIView
from user.models.models import SocialUser
from user.models.platform_domain import PlatformNames
from user.services.auth_service import KakaoOauthService
from user.services.token_service import token_refresh


class KakaoOauthView(BaseAPIView):
    permission_classes = [
        AllowAny,
    ]
    oauth_service = KakaoOauthService()
    platform = PlatformNames.kakao

    def get(self, request: Request) -> Response:
        code: str = request.GET.get("code")
        access_token: str = self.oauth_service.get_access_token(code)

        user_profile_request: Dict[str, str | int] = self.oauth_service.get_user_profile(access_token)

        try:
            social_id: str = self.oauth_service.get_user_uuid(user_profile_request)
            user: SocialUser = SocialUser.objects.get(social_id=social_id, is_active=True)

            return self.oauth_service.social_login(user)

        except SocialUser.DoesNotExist:
            return self.oauth_service.register(self.platform, user_profile_request)

        except Exception as e:
            response_message = {"error": str(e)}
            return self.fail_response(message=response_message, status_code=status.HTTP_400_BAD_REQUEST)


class SocialLogutAPI(BaseAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    oauth_service = KakaoOauthService()

    def post(self, request: Request) -> Response:
        return self.oauth_service.social_logout()


class TokenVerifyAPI(TokenVerifyView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


class TokenRefreshAPI(BaseAPIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request) -> Response:
        return token_refresh(request)

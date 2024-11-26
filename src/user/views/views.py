from typing import Dict

from rest_framework import status
from rest_framework.permissions import AllowAny
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
            user: SocialUser = SocialUser.objects.get(social_id=social_id)

            return self.oauth_service.social_login(user)

        except SocialUser.DoesNotExist:
            return self.oauth_service.register(self.platform, user_profile_request)

        except Exception as e:
            response_message = {"error": str(e)}
            return Response(response_message, status=e.status_code or status.HTTP_400_BAD_REQUEST)


# class KakaoLoginAPI(SocialLoginServiceMixin):
#     platform = "kakao"
#     uuid_key = "id"
#
#     def get_username(self, user_profile: Dict[str, str | Dict]) -> str:
#         kakao_account = user_profile.get("properties")
#         uuid = self.get_user_uuid(user_profile)[:4]
#
#         if not kakao_account:
#             return f"Unkown{uuid}"
#
#         return kakao_account.get("nickname", f"Unkown{uuid}")


# class SocialLogutAPI(BaseAPIView, SocialOAuthService):
#     permission_classes = (IsAuthenticated,)
#
#     @extend_schema(
#         summary="소셜 로그아웃 API",
#         tags=["로그아웃"],
#         responses=OutputSerializer,
#     )
#     def post(self, request: Request) -> Response:
#         return self.social_logout()


class TokenVerifyAPI(TokenVerifyView):
    def post(self, request: Request, *args, **kwargs) -> Response:
        return super().post(request, *args, **kwargs)


class TokenRefreshAPI(BaseAPIView):
    permission_classes = (AllowAny,)

    def get(self, request: Request) -> Response:
        return token_refresh(request)

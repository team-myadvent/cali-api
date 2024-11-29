from typing import Optional

from django.conf import settings
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken, Token

from shared.mixin import APIViewResponseMixin


def token_refresh(request) -> Response:
    """
    request access tokens with refresh tokens
    """
    refresh_token: Optional[Token] = request.COOKIES.get("refresh_token", None)

    if not refresh_token:
        return APIViewResponseMixin.fail_response(message="refresh token is empty or missing")

    refresh = RefreshToken(refresh_token)
    access_token_lifetime = settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]
    response_data = {"access_token": str(refresh.access_token)}
    response: Response = APIViewResponseMixin.success_response(
        data=response_data, message="successfully refreshed token"
    )

    response.set_cookie("access_token", str(refresh.access_token), max_age=access_token_lifetime)

    return response

from rest_framework.exceptions import APIException


class InvalidAuthorizationCode(APIException):
    status_code = 400
    default_detail = "invalid authorization code"


class PlatformServerException(APIException):
    status_code = 400


class EmptyTokenException(APIException):
    status_code = 400
    default_detail = "token is empty or missing"


class EmptyKakaoAccount(APIException):
    status_code = 400
    default_detail = "kakao account response has empty"


class UserNotFound(APIException):
    status_code = 400
    default_detail = "Does not found user"

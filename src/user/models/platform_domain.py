from dataclasses import asdict, dataclass

from django.conf import settings


@dataclass
class Secret:
    client_id: str
    redirect_uri: str
    token_info_api: str

    def to_dict(self):
        return asdict(self)


@dataclass
class KakaoAuthDomain:
    info = Secret(
        client_id=settings.KAKAO_OAUTH2_CLIENT_ID,
        redirect_uri=settings.KAKAO_OAUTH2_REDIRECT_URI,
        token_info_api=settings.KAKAO_OAUTH2_TOKEN_INFO_API,
    )
    platform_url = settings.KAKAO_OAUTH2_PLATFROM_URL


@dataclass
class PlatformNames:
    kakao: str = "kakao"

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
        client_id=settings.ENV.str("KAKAO_CLIENT_ID", default=None),
        redirect_uri=settings.ENV.str("KAKAO_REDIRECT_URI", default=None),
        token_info_api=settings.ENV.str("KAKAO_TOKEN_INFO_API", default=None),
    )
    platform_url = settings.ENV.str("KAKAO_PLATFROM_URL", default=None)


@dataclass
class PlatformNames:
    kakao: str = "kakao"

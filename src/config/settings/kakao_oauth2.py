from config.env import env, ENVS_DIR


KAKAO_OAUTH2_CLIENT_ID = env.str("KAKAO_OAUTH2_CLIENT_ID", default="")
KAKAO_OAUTH2_REDIRECT_URI = env.str("KAKAO_REDIRECT_URI", default="")
KAKAO_OAUTH2_TOKEN_INFO_API = env.str("KAKAO_TOKEN_INFO_API", default="")
KAKAO_OAUTH2_PLATFROM_URL = env.str("KAKAO_PLATFROM_URL", default="")

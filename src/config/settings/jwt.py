from datetime import timedelta

from config.env import ENV


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "SIGNING_KEY": ENV.str("SIGNING_KEY", default=""),
    "USER_ID_FIELD": "social_id",
    "USER_ID_CLAIM": "user_id",
}

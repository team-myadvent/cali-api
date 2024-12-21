from config.env import env

FILE_MAX_SIZE = env.int("FILE_MAX_SIZE", default=10485760)


AWS_S3_ACCESS_KEY_ID = env.str("AWS_S3_ACCESS_KEY_ID", default="")
AWS_S3_SECRET_ACCESS_KEY = env.str("AWS_S3_SECRET_ACCESS_KEY", default="")
AWS_S3_REGION_NAME = env.str("AWS_S3_REGION_NAME", default="")
AWS_STORAGE_BUCKET_NAME = env.str("AWS_STORAGE_BUCKET_NAME", default="")
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_S3_URL = env.str("AWS_S3_URL", default="")
AWS_LAMBDA_FUNCTION_NAME = env.str("AWS_LAMBDA_FUNCTION_NAME", default="")
S3_IMAGE_URL = "default_{seq}.png"

USE_S3 = env.bool("USE_S3", default=False)

if USE_S3:
    AWS_LOCATION = "static"
    STATIC_URL = f"https://{AWS_S3_URL}/{AWS_LOCATION}/"

    AWS_LOCATION = "media"
    MEDIA_URL = f"https://{AWS_S3_URL}/{AWS_LOCATION}/"

    STORAGES = {
        "default": {
            "BACKEND": "storages.backends.s3.S3Storage",
        },
        "staticfiles": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"},
    }
    AWS_QUERYSTRING_AUTH = False
    S3_IMAGE_URL = "https://cali-bucket.s3.ap-northeast-2.amazonaws.com/media/default_calendar_img/default_{seq}.png"

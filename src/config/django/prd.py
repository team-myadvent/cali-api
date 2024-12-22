from .base import *  # noqa
from .base import env

DEBUG = env.ENV.bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = [env.str("ALLOWED_HOSTS", "*")]

DATABASES = {"default": env.ENV.db("DATABASE_URL")}

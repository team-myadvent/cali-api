from .base import *  # noqa
from .base import env

DEBUG = env.bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = [env.str("ALLOWED_HOSTS")]

DATABASES = {"default": env.db("DATABASE_URL")}

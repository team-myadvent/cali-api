from .base import *  # noqa

env.environ.Env.read_env(env.Path(env.ROOT_DIR, ".envs", ".dev", ".django"))

DEBUG = env.ENV.bool("DJANGO_DEBUG", True)

CSRF_TRUSTED_ORIGINS = ["http://localhost:8000", "http://127.0.0.1:8000"]

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS: True

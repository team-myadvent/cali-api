import environ

from django.conf import settings

from pathlib import Path

env = environ.Env()
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
ENVS_DIR = Path(ROOT_DIR, ".envs")
LOG_DIR = env.str("LOG_DIR", default=Path(ROOT_DIR, "logs"))

if settings.SETTINGS_MODULE.endswith("dev"):
    env.read_env(Path(ENVS_DIR, ".dev", ".django"))

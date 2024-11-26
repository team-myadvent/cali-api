import environ

from pathlib import Path

ENV = environ.Env()
ROOT_DIR = Path(__file__).resolve().parent.parent.parent
ENVS_DIR = Path(ROOT_DIR, "envs")
LOG_DIR = ENV.str("LOG_DIR", default=Path(ROOT_DIR, "logs"))

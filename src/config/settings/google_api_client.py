from config.env import env


DEVELOPER_KEY = env.str("DEVELOPER_KEY", default="")
YOUTUBE_API_SERVICE_NAME = env.str("YOUTUBE_API_SERVICE_NAME", default="")
YOUTUBE_API_VERSION = env.str("YOUTUBE_API_VERSION", default="")

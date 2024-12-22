from dataclasses import dataclass
from io import BytesIO
from typing import Optional

import requests
from PIL import Image


@dataclass
class YoutubeThumbnailImageSize:
    width: int
    height: int

    def is_invalid_image_size(self):
        return self.width == 120 and self.height == 90


def get_youtube_thumbnail_image_size(youtube_thumbnail_url: Optional[str]) -> YoutubeThumbnailImageSize:
    """
    유튜브 썸네일 이미지의 사이즈 추출
    :param youtube_thumbnail_url: 유튜브 썸네일에서 제공 하는 이미지 링크
    :return: Tuple[width, height]
    """

    if not youtube_thumbnail_url:
        raise ValueError("must be have youtube thumbnail url")

    res = requests.get(youtube_thumbnail_url)
    youtube_thumbnail_url_image = Image.open(BytesIO(res.content))
    return YoutubeThumbnailImageSize(*youtube_thumbnail_url_image.size)

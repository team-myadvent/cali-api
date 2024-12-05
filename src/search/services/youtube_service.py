from dataclasses import dataclass, asdict

from django.conf import settings
from googleapiclient.discovery import build

from search.exceptions import SearchResponseEmtpy

YOUTUBE = build(settings.YOUTUBE_API_SERVICE_NAME, settings.YOUTUBE_API_VERSION, developerKey=settings.DEVELOPER_KEY)


@dataclass
class YoutubeSearchResponse:
    videoId: str
    title: str
    url: str

    @classmethod
    def from_dict(cls, serach_response):
        video_id = serach_response["id"]["videoId"]
        title = serach_response["snippet"]["title"]
        url = f"https://www.youtube.com/watch?v={video_id}"

        return cls(video_id, title, url)

    def to_dict(self):
        return asdict(self)


class YotubueService:
    @staticmethod
    def get_search_response(query: str, max_results: int = 10) -> dict:
        return YOUTUBE.search().list(q=query, order="relevance", part="snippet", maxResults=max_results).execute()

    @staticmethod
    def get_video_info(search_response):
        result_json = {}
        idx = 0
        for item in search_response["items"]:
            if item["id"]["kind"] == "youtube#video":
                result_json[idx] = YoutubeSearchResponse.from_dict(item)
                idx += 1
        return result_json

    def search(self, query: str, max_results: int = 10):
        res = self.get_search_response(query, max_results)
        yotubue_search_response = self.get_video_info(res)

        if not yotubue_search_response:
            raise SearchResponseEmtpy()

        youtube_search_response_list = [video_info.to_dict() for video_info in yotubue_search_response.values()]
        return youtube_search_response_list

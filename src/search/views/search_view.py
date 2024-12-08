from rest_framework import status
from rest_framework.permissions import AllowAny

from search.services.youtube_crawling import get_youtube_search_results
from search.services.youtube_service import YotubueService
from shared.api import BaseAPIView


class YoutubeSearchAPI(BaseAPIView):
    permission_classes = [AllowAny]
    service = YotubueService()

    def get(self, request, *args, **kwargs):
        search_query = request.query_params.get("q")

        if not search_query:
            return self.fail_response(message="Empty search query")

        # search_response_list = self.service.search(search_query)
        search_response_list = get_youtube_search_results(search_query)
        return self.success_response(
            message="YouTube search results retrieved successfully",
            data=search_response_list,
            status_code=status.HTTP_200_OK,
        )

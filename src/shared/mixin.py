import logging

from rest_framework import status
from rest_framework.response import Response

from .constants import FAILURE, SUCCESS

logger = logging.getLogger("django")


class APIViewResponseMixin:
    """
    Mixin to customize the response format
    """

    @classmethod
    def success_response(cls, data=None, message=None, status_code=status.HTTP_200_OK):
        """
        Returns Success Response
        """
        response_data = {
            "status": SUCCESS,
            "status_code": status_code,
            "results": {
                "message": message,
                "data": data or None,
                # **(data or {"data": None})
            },
        }
        return Response(response_data, status=status_code)

    @classmethod
    def fail_response(cls, data=None, message=None, status_code=status.HTTP_400_BAD_REQUEST):
        """
        Returns Failure Response
        """

        if isinstance(data, dict) and "detail" in data:
            message = data["detail"]
            data = None

        response_data = {
            "status": FAILURE,
            "status_code": status_code,
            "results": {
                "message": message,
                "data": data,
            },
        }
        return Response(response_data, status=status_code)

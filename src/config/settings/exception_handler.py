import logging

from rest_framework import status
from rest_framework.views import exception_handler
from shared.messages import INTERNAL_SERVER_ERROR_MESSAGE
from shared.mixin import APIViewResponseMixin

logger = logging.getLogger("django")


def custom_exception_handler(exc, context):
    """
    Custom exception handler to handle and format exceptions globally.
    Args:
        exc (Exception): The exception raised.
        context (dict): Context information for the exception.
    Returns:
        Response: Customized response object.
    """
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now customize the response format.
    if response is not None:
        # Extract information from the original response
        status_code = response.status_code
        message = response.data.get("detail", INTERNAL_SERVER_ERROR_MESSAGE)
        if status_code == status.HTTP_500_INTERNAL_SERVER_ERROR:
            logger.exception(exc)

        return APIViewResponseMixin.fail_response(status_code=status_code, message=message, data=response.data)

    logger.exception(exc)
    # Utilize gettext_lazy for localization and translation in the response
    return APIViewResponseMixin.fail_response(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message=INTERNAL_SERVER_ERROR_MESSAGE, data=None
    )

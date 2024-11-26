from rest_framework.views import APIView

from .mixin import APIViewResponseMixin


class BaseAPIView(APIView, APIViewResponseMixin):
    """
    Create a base API view that combines APIView and APIViewResponseMixin
    Custom API View to handle all the common logic for all APIs
    """
